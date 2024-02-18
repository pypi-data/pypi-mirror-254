#!/usr/bin/env python
import mindspore as ms
from mindspore.ops.primitive import _primexpr
from mindtorch.torch.common.dtype import all_float_type, float32, _get_dtype_from_type

__all__ = ['set_default_dtype', 'get_default_dtype', 'set_default_tensor_type']


@ms.jit_class
class TypeHelperBase:
    # global dtype
    _float_dtype = float32

    @classmethod
    def set_default_dtype(cls, dtype):
        cls._float_dtype = dtype

    @classmethod
    def get_default_dtype(cls):
        return cls._float_dtype


# TODO: unsupport float32->complex64, float64->complex128
def set_default_dtype(d):
    if d not in all_float_type:
        raise TypeError("set default dtype only supports [float16, float32, float64, bfloat16] "
                ", but received ", d)

    TypeHelperBase.set_default_dtype(d)


@_primexpr
def get_default_dtype():
    return TypeHelperBase.get_default_dtype()


def set_default_tensor_type(d):
    dtype = _get_dtype_from_type(d)
    set_default_dtype(dtype)


@_primexpr
def _not_default_fp32_dtype():
    if TypeHelperBase.get_default_dtype() == float32:
        return False
    return True


def _dtype_or_default(dtype):
    if dtype is None:
        return get_default_dtype()
    return dtype
