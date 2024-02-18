#!/usr/bin/env python
# -*- coding: utf-8 -*-
import collections
# from functools import lru_cache
import mindspore as ms
from mindspore import context
from mindspore.ops.primitive import _primexpr


_GLOBAL_LRU_CACHE_SIZE = 4
_GLOBAL_LRU_CACHE_SIZE_NN = 256

INT32_MIN = -2147483648
INT32_MAX = 2147483647
INT64_MIN = -9223372036854775808
INT64_MAX = 9223372036854775807
FP64_MAX = 1.79869313e+308 
FP64_MIN = -1.79869313e+308
FP32_MAX = 3.4028235e+38
FP32_MIN = -3.4028235e+38

def unsupported_attr(attr):
    """
    To mark the attribute that is not currently supported.
    """
    return attr

@_primexpr
def pynative_mode_condition():
    return context.get_context("mode") == context.PYNATIVE_MODE

@_primexpr
def graph_mode_condition():
    return context.get_context("mode") == context.GRAPH_MODE

@_primexpr
def get_backend():
    return context.get_context("device_target")

@_primexpr
def is_under_gpu_context():
    return get_backend() == 'GPU'

@_primexpr
def is_under_ascend_context():
    return get_backend() == 'Ascend'

@_primexpr
def is_under_cpu_context():
    return get_backend() == 'CPU'

@_primexpr
def ascend_raise_implement_error(func):
    if is_under_ascend_context():
        raise NotImplementedError(func + " currently not support on Ascend")

@_primexpr
def set_name_tuple(name):
    return collections.namedtuple(name, 'values, indices')

@_primexpr
def set_multiple_name_tuple(name, tags):
    return collections.namedtuple(name, tags)

@_primexpr
def bitwise_adapter(input, other):
    if (not isinstance(input, ms.Tensor)) and (not isinstance(other, ms.Tensor)):
        raise ValueError("Expected at least one tensor argument in the inputs")
    elif not isinstance(other, ms.Tensor):
        other = ms.Tensor(other)
    elif not isinstance(input, ms.Tensor):
        input = ms.Tensor(input)
    output_dtype = ms.numpy.result_type(input, other)
    input = input.astype(ms.int32)
    other = other.astype(ms.int32)
    return input, other, output_dtype

_AscendGenernalConvertDict = {
    ms.float64: ms.float32,
    ms.int8: ms.float16,
    ms.int16: ms.float16,
    ms.int32: ms.float32,
    ms.int64: ms.float32,
    ms.uint8: ms.float16,
    ms.bool_: ms.float16,
    ms.double: ms.float32,
}

def _ascend_tensor_general_cast(input, conver_dicts={}):
    """
    Example:
        >>> import mindtorch.torch as torch
        >>> from mindtorch.utils import _ascend_tensor_general_cast
        >>> a = torch.tensor(2)
        >>> print(a.dtype)
        Int64
        >>> b = _ascend_tensor_general_cast(a)
        >>> print(b.dtype)
        Float32
        >>> c = _ascend_tensor_general_cast(a, conver_dicts={torch.int64: torch.int32})
        >>> print(b.dtype)
        Int32
    """
    value = conver_dicts.get(input.dtype)
    if value:
        return input.astype(value)

    _to_dtype = _AscendGenernalConvertDict.get(input.dtype)
    if _to_dtype:
        return input.astype(_to_dtype)
    return input


@_primexpr
# @lru_cache(_GLOBAL_LRU_CACHE_SIZE)
def _infer_size(shape, numel):
    if len(shape) == 1 and isinstance(shape[0], tuple):
        shape = shape[0]

    dim = None
    newsize = 1
    for i, d in enumerate(shape):
        if d == -1:
            if dim is not None:
                raise RuntimeError("only one dimension can be inferred")
            dim = i
        elif d >= 0:
            newsize *= d
        else:
            raise RuntimeError(f"invalid shape dimension {d}")

    if not (numel == newsize or (dim is not None and newsize > 0 and numel % newsize == 0)):
        raise RuntimeError(f"shape '{list(shape)}' is invalid for input of size {numel}")

    if dim is not None:
        if newsize == 0:
            raise RuntimeError(f"cannot reshape tensor fo 0 elements into shape {shape} because the "
                               "unspecified dimension size -1 can be any value and is ambiguous.")
        shape = list(shape)
        shape[dim] = numel // newsize
    return tuple(shape)


_PythonTypeDict = {
    int: ms.int64,
    float: ms.float64,
    bool: ms.bool_
}

@_primexpr
def _get_ms_type(dtype):
    _to_dtype = _PythonTypeDict.get(dtype)
    if _to_dtype:
        return _to_dtype
    return dtype

@_primexpr
def promote_type_lookup(type1, type2):
    u1 = ms.uint8
    u2 = ms.uint16
    u4 = ms.uint32
    u8 = ms.uint64
    i1 = ms.int8
    i2 = ms.int16
    i4 = ms.int32
    i8 = ms.int64
    f2 = ms.float16
    f4 = ms.float32
    f8 = ms.float64
    c4 = ms.complex64
    c8 = ms.complex128
    b1 = ms.bool_
    bf = ms.bfloat16

    _promoteTypesLookup = \
        [[b1, u1, u2, u4, u8, i1, i2, i4, i8, f2, f4, f8, c4, c8, bf], # b1
         [u1, u1, u2, u4, u8, i2, i2, i4, i8, f2, f4, f8, c4, c8, bf], # u1
         [u2, u2, u2, u4, u8, i1, i2, i4, i8, f2, f4, f8, c4, c8, bf], # u2
         [u4, u4, u4, u4, u8, i1, i2, i4, i8, f2, f4, f8, c4, c8, bf], # u4
         [u8, u8, u8, u8, u8, i1, i2, i4, i8, f2, f4, f8, c4, c8, bf], # u8
         [i1, i2, i1, i1, i1, i1, i2, i4, i8, f2, f4, f8, c4, c8, bf], # i1
         [i2, i2, i2, i2, i2, i2, i2, i4, i8, f2, f4, f8, c4, c8, bf], # i2
         [i4, i4, i4, i4, i4, i4, i4, i4, i8, f2, f4, f8, c4, c8, bf], # i4
         [i8, i8, i8, i8, i8, i8, i8, i8, i8, f2, f4, f8, c4, c8, bf], # i8
         [f2, f2, f2, f2, f2, f2, f2, f2, f2, f2, f4, f8, c4, c8, f4], # f2
         [f4, f4, f4, f4, f4, f4, f4, f4, f4, f4, f4, f8, c4, c8, f4], # f4
         [f8, f8, f8, f8, f8, f8, f8, f8, f8, f8, f8, f8, c8, c8, f8], # f8
         [c4, c4, c4, c4, c4, c4, c4, c4, c4, c4, c4, c8, c4, c8, c4], # c4
         [c8, c8, c8, c8, c8, c8, c8, c8, c8, c8, c8, c8, c8, c8, c8], # c8
         [bf, bf, bf, bf, bf, bf, bf, bf, bf, f4, f4, f8, c4, c8, bf]] # bf
        # b1  u1  u2  u4  u8  i1  i2  i4  i8  f2  f4  f8  c4  c8  bf

    _numpy_type_dict = {bool: ms.bool_,
                        int: ms.int64,
                        float: ms.float64,
                        complex: ms.complex128}

    numpy_dtype = (bool, int, float, complex)
    if type1 in numpy_dtype:
        type1 = _numpy_type_dict.get(type1)
    if type2 in numpy_dtype:
        type2 = _numpy_type_dict.get(type2)

    type1_index = _promoteTypesLookup[0].index(type1)
    type2_index = _promoteTypesLookup[0].index(type2)
    return _promoteTypesLookup[type1_index][type2_index]
