# Copyright (c) 2011 The University of Sydney

from __future__ import print_function
import copy
import functools
import itertools
import numpy as np
import os
import sys
import warnings
if sys.version_info.major < 3: from itertools import izip
else: izip = zip # todo! watch performance! it's reported python3 zip is some 30% slower than izip
from ..util import warning
from ..io import readlines_unbuffered
from ..numpy import merge_arrays, types_of_dtype, structured_dtype
from . import time as csv_time
from .struct import struct

DEFAULT_PRECISION = 12
NUMPY_VERSION_MAJOR_, NUMPY_VERSION_MINOR_, NUMPY_VERSION_PATCH_ = ( int( _ ) for _ in np.__version__.split( '.' ) )

def custom_formatwarning(msg, *args): return __name__ + " warning: " + str(msg) + '\n'

class stream(object):
    """
    see github.com/acfr/comma/wiki/python-csv-module for details
    """
    buffer_size_in_bytes = 65536

    def __init__(self,
                 s,
                 fields='',
                 format='',
                 binary=None,
                 delimiter=',',
                 precision=DEFAULT_PRECISION,
                 flush=False,
                 source=sys.stdin,
                 target=sys.stdout,
                 tied=None,
                 full_xpath=True,
                 verbose=False,
                 default_values=None):
        self.struct = self._struct(s)
        self.delimiter = delimiter
        self.precision = precision
        self.flush = flush
        self.source = source
        self.target = target
        #if np.__version__ >= '1.16.0' and target == sys.stdout: self.stdout = os.fdopen( sys.stdout.fileno(), "wb" )
        self.tied = tied
        self.full_xpath = full_xpath
        self.verbose = verbose
        self.fields = self._fields(fields)
        self._check_fields()
        self.format = self._format(binary, format)
        self.binary = self.format != ''
        self._check_consistency_with_tied()
        self.input_dtype = self._input_dtype()
        self.size = self._default_buffer_size()
        if not self.binary:
            unrolled_types = types_of_dtype(self.input_dtype, unroll=True)
            self.ascii_converters = csv_time.ascii_converters(unrolled_types)
            num_utypes = len(unrolled_types)
            self.usecols = tuple(range(num_utypes))
            self.filling_values = None if num_utypes == 1 else ('',) * num_utypes
        self.missing_fields = self._missing_fields()
        self.missing_dtype = self._missing_dtype()
        self.complete_fields = self.fields + self.missing_fields
        self.complete_dtype = self._complete_dtype()
        self.default_values = self._default_values(default_values)
        self.missing_values = self._missing_values()
        self.data_extraction_fields = self._data_extraction_fields()
        self.struct_and_extraction_fields = list( zip( self.struct.flat_dtype.names, self.data_extraction_fields ) )
        #self.write_dtype = self._write_dtype()
        #self.unrolled_write_dtype = structured_dtype( ','.join( types_of_dtype( self.write_dtype, unroll=True ) ) )
        #print( "self.write_dtype.descr = %s" % str(self.write_dtype.descr), file = sys.stderr )
        #print( "self.unrolled_write_dtype = %s" % str(self.unrolled_write_dtype), file = sys.stderr )
        self._input_array = None
        self._ascii_buffer = None
        self._strings = functools.partial(map, self.numpy_scalar_to_string)

    def iter(self, size=None):
        """
        a generator that calls read() repeatedly until there is no data in the stream

        size has the same meaning as in read()
        """
        while True:
            s = self.read(size)
            if s is None: break
            yield s

    def __iter__(self): return self.iter()

    def read(self, size=None):
        """
        read the specified number of records from stream, extract data,
        put it into appropriate numpy array with the dtype defined by struct, and return it

        if size is None, default size is used
        if size is negative, all records from source are read
        if no records have been read, return None
        """
        if size is None: size = self.size
        self._input_array = copy.deepcopy( self._read( size ) ) if sys.version_info.major > 2 else self._read( size ) # todo! watch performance in python3!
        if self._input_array.size == 0: return
        return self._struct_array(self._input_array, self.missing_values)

    def _genfromtxt( self ): # quick and dirty due to the ugliness of the change in numpy 1.14; see doc of encoding parameter in https://docs.scipy.org/doc/numpy-1.14.0/reference/generated/numpy.genfromtxt.html
        if NUMPY_VERSION_MAJOR_ > 1 or NUMPY_VERSION_MINOR_ >= 14: # quick and dirty, since ubuntu 18.04 python3-numpy still install numpy 1.13; remove once move on with the version since it's waste of cpu cycles
            return np.genfromtxt( self._ascii_buffer
                                , dtype = self.input_dtype
                                , delimiter = self.delimiter
                                , converters = self.ascii_converters
                                , usecols = self.usecols
                                , filling_values = self.filling_values
                                , comments = None
                                , encoding = None )
        else:
            # https://github.com/numpy/numpy/issues/10511 genfromtxt issue in numpy 1.13.x
            from io import BytesIO
            return np.genfromtxt( BytesIO( bytes( '\n'.join( self._ascii_buffer ).encode( 'utf-8' ) ) ) if NUMPY_VERSION_MAJOR_ == 1 and NUMPY_VERSION_MINOR_ == 13 else self._ascii_buffer
                                , dtype = self.input_dtype
                                , delimiter = self.delimiter
                                , converters = self.ascii_converters
                                , usecols = self.usecols
                                , filling_values = self.filling_values
                                , comments = None )
        
    def read_from_line(self, line):
        self._ascii_buffer = line
        self._input_array = np.atleast_1d( self._genfromtxt() )
        if self._input_array.size == 0: return
        return self._struct_array(self._input_array, self.missing_values)

    def _read(self, size):
        if self.binary:
            if sys.version_info.major > 2: #if np.__version__ >= '1.16.0': # sigh...
                if self.source == sys.stdin:
                    b = sys.stdin.buffer.read( ( size * self.input_dtype.itemsize ) if size >= 0 else -1 ) # b = sys.stdin.buffer.read( self.input_dtype.itemsize * ( size if size >= 0 else self.size ) )
                    # todo! test on streams where bytes come with irregular delays!
                    if len(b) % self.input_dtype.itemsize != 0: raise ValueError( "expected records of size {}, got {} bytes, which is not divisible by record size".format( self.input_dtype.itemsize, len( b ) ) )
                    return np.frombuffer( b, dtype = self.input_dtype, count = len( b ) // self.input_dtype.itemsize )
                else:
                    return np.fromfile( self.source, dtype = self.input_dtype, count = -1 if size < 0 else size ) # this line may not be covered by regression test
            else:
                if size < 0 and self.source == sys.stdin:
                    return np.fromstring(self.source.read(), dtype=self.input_dtype)
                else:
                    count = -1 if size < 0 else size
                    return np.fromfile(self.source, dtype=self.input_dtype, count=count)
        else:
            with warnings.catch_warnings():
                warnings.simplefilter('ignore')
                self._ascii_buffer = readlines_unbuffered(size, self.source)
                return np.atleast_1d( self._genfromtxt() )

    def _struct_array(self, input_array, missing_values):
        if not self.data_extraction_fields:
            return input_array.copy().view(self.struct)
        flat_struct_array = np.empty(input_array.size, dtype=self.struct.flat_dtype)
        for sf, ef in self.struct_and_extraction_fields:
            if sf in self.missing_fields:
                flat_struct_array[sf] = missing_values[ef]
            else:
                flat_struct_array[sf] = input_array[ef]
        return flat_struct_array.view(self.struct)

    def _missing_values(self):
        if not self.missing_dtype:
            return
        missing = np.zeros(1, dtype=self.missing_dtype)
        if self.default_values:
            dtype_name_of = dict(zip(self.missing_fields, self.missing_dtype.names))
            for field, value in self.default_values.items():
                name = dtype_name_of[field]
                if self.missing_dtype[name] == csv_time.DTYPE:
                    try: missing[name] = csv_time.to_numpy(value)
                    except TypeError: missing[name] = value
                else:
                    missing[name] = value
        return missing[0]

    def numpy_scalar_to_string(self, scalar): return numpy_scalar_to_string(scalar, precision=self.precision)

    def write(self, s):
        """
        serialize the given numpy array of dtype defined by struct and write the result to
        the target
        """
        if s.dtype != self.struct.dtype:
            msg = "expected {}, got {}".format(repr(self.struct.dtype), repr(s.dtype))
            raise TypeError(msg)
        if s.shape != (s.size,):
            msg = "expected shape=({},), got {}".format(s.size, s.shape)
            raise ValueError(msg)
        if self.tied and s.size != self.tied._input_array.size:
            tied_size = self.tied._input_array.size
            msg = "size {} not equal to tied size {}".format(s.size, tied_size)
            raise ValueError(msg)
        if self.binary:
            if sys.version_info.major > 2 and self.target == sys.stdout: # sigh...
                #self.stdout.write( self._tie_binary(self.tied._input_array, s).tobytes() if self.tied else s.tobytes() )
                sys.stdout.buffer.write( self._tie_binary(self.tied._input_array, s).tobytes() if self.tied else s.tobytes() )
            else:
                if self.tied: self._tie_binary(self.tied._input_array, s).tofile(self.target)
                else: s.tofile(self.target)
        else:
            unrolled_array = s.view(self.struct.unrolled_flat_dtype)
            #unrolled_array = s.view( self.unrolled_write_dtype )
            if self.tied: lines = self._tie_ascii(self.tied._ascii_buffer, unrolled_array)
            else: lines = (self._toline(scalars) for scalars in unrolled_array)
            for line in lines: print( line, file = self.target )
        self.target.flush()

    def _tie_binary(self, tied_array, array): return merge_arrays(tied_array, array)

    if sys.version_info.major < 3: # python3, sigh... don't ask
        def _tie_ascii(self, tied_buffer, unrolled_array):
            for tied_line, scalars in izip(tied_buffer, unrolled_array): yield self.delimiter.join([tied_line] + self._strings(scalars))
    else:
        def _tie_ascii(self, tied_buffer, unrolled_array):
            for tied_line, scalars in izip(tied_buffer, unrolled_array): yield self.delimiter.join([tied_line] + list(self._strings(scalars)))

    def _toline(self, scalars): return self.delimiter.join(self._strings(scalars))

    def dump(self, mask=None):
        """
        dump the data in the stream buffer to the output
        """
        if mask is None: self._dump()
        else: self._dump_with_mask(mask)

    def _dump(self):
        if self.binary:
            if sys.version_info.major > 2 and self.target == sys.stdout: # sigh...
                sys.stdout.buffer.write( self._input_array.tobytes() )
            else:
                self._input_array.tofile( self.target )
        else:
            for line in self._ascii_buffer: print( line, file = self.target )
        self.target.flush()

    def _dump_with_mask(self, mask):
        if mask.dtype != bool:
            msg = "expected mask type to be {}, got {}" \
                .format(repr(np.dtype(bool)), repr(mask.dtype))
            raise TypeError(msg)
        if mask.shape != (mask.size,):
            msg = "expected mask shape=({},), got {}".format(mask.size, mask.shape)
            raise ValueError(msg)
        if mask.size != self._input_array.size:
            data_size = self._input_array.size
            msg = "mask size {} not equal to data size {}".format(mask.size, data_size)
            raise ValueError(msg)
        if self.binary:
            if sys.version_info.major > 2 and self.target == sys.stdout: # sigh...
                sys.stdout.buffer.write( self._input_array[mask].tobytes() )
            else:
                self._input_array[mask].tofile(self.target)
        else:
            for line, allowed in izip(self._ascii_buffer, mask):
                if allowed: print( line, file = self.target )
        self.target.flush()

    def _warn(self, msg, verbose=True):
        if verbose:
            if sys.version_info.major < 3: # sigh, something is broken at least in python3.7; dumb it down for now
                with warning(custom_formatwarning) as warn: warn(msg)
            else:
                print( 'stream.py: warning:', msg, file=sys.stderr )

    def _struct(self, s):
        if not isinstance(s, struct):
            msg = "expected '{}', got '{}'".format(repr(struct), repr(s))
            raise TypeError(msg)
        return s

    def _fields(self, fields):
        if fields == '':
            return self.struct.fields
        if self.full_xpath:
            return self.struct.expand_shorthand(fields)
        if '/' in fields:
            msg = "expected fields without '/', got '{}'".format(fields)
            raise ValueError(msg)
        ambiguous_leaves = self.struct.ambiguous_leaves.intersection(fields.split(','))
        if ambiguous_leaves:
            msg = "fields '{}' are ambiguous in '{}', use full xpath" \
                .format(','.join(ambiguous_leaves), fields)
            raise ValueError(msg)
        xpath = self.struct.xpath_of_leaf.get
        return tuple(xpath(name) or name for name in fields.split(','))

    def _format(self, binary, format):
        if isinstance(binary, str): # if isinstance(binary, basestring):
            if self.verbose and binary and format and binary != format:
                msg = "ignoring '{}' and using '{}' since binary keyword has priority" \
                    .format(format, binary)
                self._warn(msg)
            return binary
        if binary is True and not format:
            if not set(self.struct.fields).issuperset(self.fields):
                msg = "failed to infer type of every field in '{}', specify format" \
                    .format(','.join(self.fields))
                raise ValueError(msg)
            type_of = self.struct.type_of_field.get
            return ','.join(type_of(field) for field in self.fields)
        if binary is False:
            return ''
        return format

    def _check_fields(self):
        fields_in_struct = set(self.fields).intersection(self.struct.fields)
        if not fields_in_struct:
            msg = "fields '{}' do not match any of expected fields '{}'" \
                .format(','.join(self.fields), ','.join(self.struct.fields))
            raise ValueError(msg)
        duplicates = tuple(field for field in self.struct.fields
                           if field in self.fields and self.fields.count(field) > 1)
        if duplicates:
            msg = "fields '{}' have duplicates in '{}'" \
                "".format(','.join(duplicates), ','.join(self.fields))
            raise ValueError(msg)

    def _check_consistency_with_tied(self):
        if not self.tied: return
        if not isinstance(self.tied, stream):
            msg = "expected tied stream of type '{}', got '{}'".format(str(stream), repr(self.tied))
            raise TypeError(msg)
        if self.tied.binary != self.binary:
            msg = "expected tied stream to be {}, got {}" \
                "".format("binary" if self.binary else "ascii",
                          "binary" if self.tied.binary else "ascii")
            raise ValueError(msg)
        if not self.binary and self.tied.delimiter != self.delimiter:
            msg = "expected tied stream to have the same delimiter '{}', got '{}'".format(self.delimiter, self.tied.delimiter)
            raise ValueError(msg)

    def _input_dtype(self):
        if self.binary:
            input_dtype = structured_dtype(self.format)
            if len(self.fields) != len(input_dtype.names):
                msg = "expected same number of fields and format types, got '{}' and '{}'".format(','.join(self.fields), self.format)
                raise ValueError(msg)
        else:
            type_of = self.struct.type_of_field.get
            types = [type_of(name) or 'S' for name in self.fields]
            input_dtype = structured_dtype(','.join(types))
        return input_dtype

    def _default_buffer_size(self):
        if self.tied: return self.tied.size
        elif self.flush: return 1
        return max( 1, stream.buffer_size_in_bytes // self.input_dtype.itemsize ) # todo? too arbitrary for ascii?

    def _missing_fields(self):
        missing_fields = [field for field in self.struct.fields if field not in self.fields]
        if not missing_fields: return ()
        if self.verbose:
            msg = "expected fields '{}' are not found in supplied fields '{}'".format(','.join(missing_fields), ','.join(self.fields))
            self._warn(msg)
        return tuple(missing_fields)

    def _missing_dtype(self):
        if not self.missing_fields: return
        n = len(self.input_dtype.names)
        missing_names = ['f{}'.format(n + i) for i in range(len(self.missing_fields))] # missing_names = ['f{}'.format(n + i) for i in xrange(len(self.missing_fields))]
        type_of = self.struct.type_of_field.get
        missing_types = [type_of(name) for name in self.missing_fields]
        return np.dtype(list(zip(missing_names, missing_types)))

    def _complete_dtype(self):
        if self.missing_dtype: return np.dtype(self.input_dtype.descr + self.missing_dtype.descr)
        else: return self.input_dtype

    def _default_values(self, default_values):
        if not (self.missing_fields and default_values): return
        if self.full_xpath:
            default_fields_ = default_values.keys()
            default_values_ = default_values.copy()
        else:
            leaves = default_values.keys()
            xpath_of = self.struct.xpath_of_leaf.get
            default_fields_ = tuple(xpath_of(leaf) or leaf for leaf in leaves)
            default_values_ = dict(zip(default_fields_, default_values.values()))
        default_fields_in_stream = set(default_fields_).intersection(self.fields)
        unknown_default_fields = set(default_fields_).difference(self.struct.fields)
        if default_fields_in_stream:
            if self.verbose:
                msg = "default values for fields in stream are ignored: '{}'" \
                    "".format(','.join(default_fields_in_stream))
                self._warn(msg)
        if unknown_default_fields:
            if self.verbose:
                msg = "found default values for fields not in struct: '{}'" \
                    "".format(','.join(unknown_default_fields))
                self._warn(msg)
        for field in default_fields_in_stream.union(unknown_default_fields):
            del default_values_[field]
        return default_values_

    def _data_extraction_fields(self):
        if self.fields == self.struct.fields: return ()
        index_of = self.complete_fields.index
        return tuple('f{}'.format(index_of(field)) for field in self.struct.fields)

    def _write_dtype(self):
        names = []
        formats = []
        offsets = []
        for name in self.fields:
            try:
                flat_dtype = self.struct.flat_dtype.fields[name]
                names.append( name )
                formats.append( flat_dtype[0] )
                offsets.append( flat_dtype[1] )
            except KeyError:
                pass
        itemsize = self.struct.flat_dtype.itemsize
        return np.dtype( dict( names=names, formats=formats, offsets=offsets, itemsize=itemsize ) )


def numpy_scalar_to_string(scalar, precision=DEFAULT_PRECISION):
    """
    convert numpy scalar to a string suitable to comma csv stream

    >>> from comma.csv import numpy_scalar_to_string
    >>> numpy_scalar_to_string(np.int32(-123))
    '-123'
    >>> numpy_scalar_to_string(np.float64(-12.3499), precision=4)
    '-12.35'
    >>> numpy_scalar_to_string(np.float64(0.1234567890123456))
    '0.123456789012'
    >>> numpy_scalar_to_string(np.string_('abc'))
    'abc'
    >>> numpy_scalar_to_string(np.datetime64('2015-01-02T12:34:56', 'us'))
    '20150102T123456'
    >>> numpy_scalar_to_string(np.datetime64('2015-01-02T12:34:56.000000', 'us'))
    '20150102T123456'
    >>> numpy_scalar_to_string(np.datetime64('2015-01-02T12:34:56.123456', 'us'))
    '20150102T123456.123456'
    >>> numpy_scalar_to_string(np.timedelta64(-123, 's'))
    '-123'
    """    
    if scalar.dtype.char in np.typecodes['AllInteger']: return str(scalar)
    elif scalar.dtype.char in np.typecodes['Float']: return "{scalar:.{precision}g}".format(scalar=scalar, precision=precision)
    elif scalar.dtype.char in np.typecodes['Datetime']: return csv_time.from_numpy(scalar)
    elif scalar.dtype.char in 'Sa': return scalar.decode('UTF-8') # quick and dirty, python3, sigh...
    elif scalar.dtype.char in 'U': return str(scalar) # quick and dirty, python3, sigh...
    elif scalar.dtype.char in '?': return str( int( scalar ) ) #elif scalar.dtype.char in '?': return str( map( int, scalar ) )
    msg = "converting {} to string is not implemented".format(repr(scalar.dtype))
    raise NotImplementedError(msg)
