#!/usr/bin/env python
# -*- coding: utf-8 -*-

import numpy as np
import mindspore as ms
from mindspore import dtype as mstype
from mindspore.ops.primitive import _primexpr
from mindspore._c_expression import typing
from mindtorch.torch.logging import warning

MS_Bool = typing.Bool
MS_Int = typing.Int
MS_UInt = typing.UInt
MS_Float = typing.Float
MS_BFloat = typing.BFloat
MS_Complex = typing.Complex

ms_dtype = mstype.Type

inf = float('inf')
nan = float('nan')


class TypeFunc():
    def __init__(self):
        self._is_complex = False
        self._is_floating_point = False
        self._is_signed = False

    @property
    def is_complex(self):
        return self._is_complex

    @property
    def is_floating_point(self):
        return self._is_floating_point

    @property
    def is_signed(self):
        return self._is_signed

    def __deepcopy__(self, memodict):
        return self


class Bool(TypeFunc, MS_Bool):
    def __new__(cls, *args, **kwargs):
        return MS_Bool.__new__(cls, *args, **kwargs)

    def __init__(self, *args, **kwargs):
        TypeFunc.__init__(self)
        MS_Bool.__init__(self, *args, **kwargs)

    def __str__(self):
        return "mindtorch." + MS_Bool.__str__(self).lower()


class Int(TypeFunc, MS_Int):
    def __new__(cls, *args, **kwargs):
        return MS_Int.__new__(cls, *args, **kwargs)

    def __init__(self, *args, **kwargs):
        TypeFunc.__init__(self)
        MS_Int.__init__(self, *args, **kwargs)
        self.nbits = args[0]
        self._is_signed = True

    def __str__(self):
        return "mindtorch." + MS_Int.__str__(self).lower()


class UInt(TypeFunc, MS_UInt):
    def __new__(cls, *args, **kwargs):
        return MS_UInt.__new__(cls, *args, **kwargs)

    def __init__(self, *args, **kwargs):
        TypeFunc.__init__(self)
        MS_UInt.__init__(self,*args, **kwargs)
        self.nbits = args[0]

    def __str__(self):
        return "mindtorch." + MS_UInt.__str__(self).lower()


class Float(TypeFunc, MS_Float):
    def __new__(cls, *args, **kwargs):
        return MS_Float.__new__(cls, *args, **kwargs)

    def __init__(self, *args, **kwargs):
        TypeFunc.__init__(self)
        MS_Float.__init__(self, *args, **kwargs)
        self.nbits = args[0]
        self._is_floating_point = True
        self._is_signed = True

    def __str__(self):
        return "mindtorch." + MS_Float.__str__(self).lower()


class BFloat(TypeFunc, MS_BFloat):
    def __new__(cls, *args, **kwargs):
        return MS_BFloat.__new__(cls, *args, **kwargs)

    def __init__(self, *args, **kwargs):
        TypeFunc.__init__(self)
        MS_BFloat.__init__(self, *args, **kwargs)
        self.nbits = args[0]
        self._is_floating_point = True
        self._is_signed = True

    def __str__(self):
        return "mindtorch." + MS_BFloat.__str__(self).lower()


class Complex(TypeFunc, MS_Complex):
    def __new__(cls, *args, **kwargs):
        return MS_Complex.__new__(cls, *args, **kwargs)

    def __init__(self, *args, **kwargs):
        TypeFunc.__init__(self)
        MS_Complex.__init__(self, *args, **kwargs)
        self.nbits = args[0]
        self._is_complex = True
        self._is_signed = True

    def __str__(self):
        return "mindtorch." + MS_Complex.__str__(self).lower()


bool = Bool()
int8 = Int(8)
int16 = Int(16)
int32 = Int(32)
int64 = Int(64)
short = int16
int = int32
long = int64
uint8 = UInt(8)
char = uint8
float16 = Float(16)
float32 = Float(32)
float64 = Float(64)
bfloat16 = BFloat(16)
half = float16
float = float32
double = float64
complex64 = Complex(64)
complex128 = Complex(128)
cfloat = complex64
cdouble = complex128


all_signed_type = (int8, int16, int32, int64, float16, float32, float64, bfloat16, complex64, complex128, )
all_int_type = (int8, int16, int32, int64, uint8, )
all_int_type_with_bool = all_int_type + (bool,)
all_float_type = (float16, float32, float64, bfloat16)
all_complex_type = (complex64, complex128, )
all_float_and_complex_type = (float16, float32, float64, bfloat16, complex64, complex128, )

_TypeDict = {float16: np.float16,
             float32: np.float32,
             float64: np.float64,
             int8: np.int8,
             int16: np.int16,
             int32: np.int32,
             int64: np.int64,
             uint8: np.uint8}

_msdtype2typeDict = {'Bool': bool,
                     'Int8': int8,
                     'Int16': int16,
                     'Int32': int32,
                     'Int64': int64,
                     'Uint8': uint8,
                     'Float16': float16,
                     'Float32': float32,
                     'Float64': float64,
                     'BFloat16': bfloat16,
                     'Complex64': complex64,
                     'Complex128': complex128}

@ms.jit_class
class iinfo:
    def __init__(self, dtype):
        if dtype in all_int_type:
            np_iinfo = np.iinfo(_TypeDict[dtype])
            self.bits = np_iinfo.bits
            self.max = np_iinfo.max
            self.min = np_iinfo.min
        else:
            raise ValueError("iinfo currently only supports torch.uint8/torch.int8/torch.int16/torch.int32/"
                             "torch.int64 as the input, but get a", dtype)

@ms.jit_class
class finfo:
    def __init__(self, dtype):
        if dtype in all_float_type and dtype != bfloat16:
            np_finfo = np.finfo(_TypeDict[dtype])
            self.bits = np_finfo.bits
            self.eps = np_finfo.eps.item()
            self.max = np_finfo.max.item()
            self.min = np_finfo.min.item()
            self.tiny = np_finfo.tiny.item()
            # smallest_normal for NumPy was added in 1.23.0
            if np.lib.NumpyVersion(np.__version__) >= '1.23.0':
                self.smallest_normal = np_finfo.smallest_normal.item()
            else:
                warning("If you want to obtain `smallest_normal` in finfo, " \
                        "NumPy version must be greater or equal 1.23.0.")
            self.resolution = np_finfo.resolution.item()
        else:
            raise ValueError("finfo currently only supports torch.float16/torch.float32/"
                             "torch.float64 as the input, but get a", dtype)


_dtype2typeDict = {
    'float32': 'FloatTensor',
    'float': 'FloatTensor',
    'float64': 'DoubleTensor',
    'double': 'DoubleTensor',
    'complex64': 'ComplexFloatTensor',
    'cfloat': 'ComplexFloatTensor',
    'complex128': 'ComplexDoubleTensor',
    'cdouble': 'ComplexDoubleTensor',
    'float16': 'HalfTensor',
    'half': 'HalfTensor',
    'bfloat16': 'BFloat16Tensor',
    'uint8': 'ByteTensor',
    'int8': 'CharTensor',
    'int16': 'ShortTensor',
    'short': 'ShortTensor',
    'int32': 'IntTensor',
    'int': 'IntTensor',
    'int64': 'LongTensor',
    'long': 'LongTensor',
    'bool': 'BoolTensor'
}

_type2dtypeDict = {
    'FloatTensor': float32,
    'DoubleTensor': float64,
    'ComplexFloatTensor': complex64,
    'ComplexDoubleTensor': complex128,
    'HalfTensor': float16,
    'BFloat16Tensor': bfloat16,
    'ByteTensor': uint8,
    'CharTensor' : int8,
    'ShortTensor': int16,
    'IntTensor': int32,
    'LongTensor': int64,
    'BoolTensor': bool
}

@_primexpr
def _get_type_from_dtype(dtype):
    str_dtype = str(dtype).split('.')[-1].lower()
    _type = _dtype2typeDict.get(str_dtype)
    return _type

@_primexpr
def _get_dtype_from_type(type):
    if hasattr(type, '__name__'):
        _type = type.__name__
    else:
        _type = str(type)
    str_dtype = _type.split('.')[-1]
    _dtype = _type2dtypeDict.get(str_dtype, 'None')
    if _dtype == 'None':
        _dtype = type
    return _dtype
