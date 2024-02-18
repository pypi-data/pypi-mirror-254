#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Register MindTorch Tensor/Parameter to MindSpore, it should be executed at the top of all.
from mindtorch.torch._register import *
from mindtorch.torch.types import *
from mindtorch.torch._C import *
from mindtorch.torch.common import *
from mindtorch.torch.tensor import *
from mindtorch.torch.tensor_type import *
from mindtorch.torch import nn
from mindtorch.torch import optim
from mindtorch.torch.functional import *
from mindtorch.torch.utils import data
from mindtorch.torch._ref import *
from mindtorch.torch import cuda
import mindtorch.torch.backends.cuda
import mindtorch.torch.backends.mps
import mindtorch.torch.backends.cudnn
import mindtorch.torch.backends.mkl
import mindtorch.torch.backends.mkldnn
import mindtorch.torch.backends.openmp
from mindtorch.torch.conflict_functional import *
import mindtorch.torch.fft as fft
from mindtorch.torch import autograd
from mindtorch.torch.autograd import (
    no_grad, enable_grad, set_grad_enabled, is_grad_enabled, inference_mode, is_inference_mode_enabled)
from mindtorch.torch.random import *
from mindtorch.torch.storage import *
from mindtorch.torch.serialization import *
import mindtorch.torch.linalg as linalg
from mindtorch.torch.common.dtype import ms_dtype as dtype
import mindtorch.torch.amp as amp
import mindtorch.torch.cpu as cpu
import mindtorch.torch.library as library
from mindtorch.torch import hub
from mindtorch.torch.logging import debug, info, warning, error, critical
from mindtorch.torch.torch_version import __version__
from mindtorch.torch import jit
from mindtorch.torch import fx
from mindtorch.torch._export_func_to_root import _export_func_to_root
from mindtorch.torch.storage import _StorageBase, _TypedStorage, _LegacyStorage, _UntypedStorage, DoubleStorage, \
    FloatStorage, LongStorage, IntStorage, ShortStorage, CharStorage, ByteStorage, HalfStorage, \
    BoolStorage, BFloat16Storage, ComplexFloatStorage, ComplexDoubleStorage
from mindtorch.torch._default_dtype import set_default_dtype, get_default_dtype, set_default_tensor_type


def _assert(condition, message):
    assert condition, message

def is_tensor(obj):
    r"""Returns True if `obj` is a mindtorch.torch tensor.

    Note that this function is simply doing ``isinstance(obj, Tensor)``.
    Using that ``isinstance`` check is better for typechecking with mypy,
    and more explicit - so it's recommended to use that instead of
    ``is_tensor``.
    """
    return isinstance(obj, Tensor)

def is_floating_point(obj):
    if not is_tensor(obj):
        raise TypeError("is_floating_point(): argument 'input' (position 1) must be Tensor, not {}.".format(type(obj)))

    return obj.is_floating_point()

class Size(tuple):
    def __new__(cls, shape):
        if isinstance(shape, Tensor):
            _shape = shape.tolist()
        else:
            _shape = shape
        if not isinstance(_shape, (tuple, list)):
            raise TypeError("{} object is not supportted.".format(type(shape)))

        return tuple.__new__(Size, _shape)
strided = False

def is_storage(obj):
    return type(obj) in _storage_classes

_storage_classes = {
    _UntypedStorage, DoubleStorage, FloatStorage, LongStorage, IntStorage,
    ShortStorage, CharStorage, ByteStorage, HalfStorage, BoolStorage,
    BFloat16Storage, ComplexFloatStorage, ComplexDoubleStorage, _TypedStorage,
    # TODO:The quantized dtype is not supported
    # QUInt8Storage, QInt8Storage, QInt32Storage, , QUInt4x2Storage, QUInt2x4Storage,
}

# export tensor.xxx and nn.functional.xxx to the current directory
_export_func_to_root()
