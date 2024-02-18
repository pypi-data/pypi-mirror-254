#!/usr/bin/env python
# -*- coding: utf-8 -*-
import abc
import numbers
import operator
# from functools import reduce, lru_cache
from copy import deepcopy
from functools import reduce
import numpy as np
import mindspore as ms
from mindspore import Tensor as ms_Tensor
from mindspore.scipy.ops import SolveTriangular
from mindspore.common import dtype as mstype
import mindspore.ops as P
from mindspore.ops.primitive import _primexpr
from mindspore.ops._primitive_cache import _get_cache_prim
from mindspore.ops.operations import _inner_ops as inner
from mindspore.common.initializer import Zero
from mindspore._c_expression import Tensor as Tensor_
from mindspore.common._stub_tensor import StubTensor

from mindtorch.utils import unsupported_attr, is_under_gpu_context, get_backend, is_under_ascend_context, _infer_size, \
    _ascend_tensor_general_cast, is_under_cpu_context, pynative_mode_condition, set_multiple_name_tuple, \
    set_name_tuple, graph_mode_condition, bitwise_adapter, FP64_MAX, FP64_MIN, FP32_MAX, FP32_MIN, promote_type_lookup
import mindtorch.torch.common.dtype as msdapter_dtype
from mindtorch.torch.common.dtype import all_int_type_with_bool, finfo, iinfo, all_int_type, _get_type_from_dtype, \
    _get_dtype_from_type, all_float_and_complex_type, all_complex_type, _msdtype2typeDict
from mindtorch.torch.types import device as device_class
from mindtorch.torch.storage import _TypedStorage, _UntypedStorage
from mindtorch.torch.logging import warning
import mindtorch.torch._register_numpy_primitive  as numpy_cell
from mindtorch.torch._default_dtype import _not_default_fp32_dtype, get_default_dtype


_dtypeDict = {
    'float16': mstype.float16,
    'float32': mstype.float32,
    'float64': mstype.float64,
    'int8': mstype.int8,
    'int16': mstype.int16,
    'int32': mstype.int32,
    'int64': mstype.int64,
    'uint8': mstype.uint8,
    'bool': mstype.bool_,
    'complex64': mstype.complex64,
    'complex128': mstype.complex128,
    'long': mstype.int64,
    'half': mstype.float16,
    'int': mstype.int32,
    'double': mstype.float64,
    'float': mstype.float32,
    'char': mstype.int8,
    'byte': mstype.uint8,
    'short': mstype.int16,
    'bfloat16': mstype.bfloat16
}

kMaxInt8 = 2 ** 7 - 1
kMaxInt16 = 2 ** 15 - 1
kMaxInt32 = 2 ** 31 - 1
kMaxInt64 = 2 ** 63 - 1
kMaxUint8 = 2 ** 8 - 1
kMaxUint16 = 2 ** 16 - 1
kMaxUint32 = 2 ** 32 - 1
kMaxUint64 = 2 ** 64 - 1
kMantissaFloat16 = 2 ** 11
kMantissaFloat32 = 2 ** 24
kMantissaFloat64 = 2 ** 53


@_primexpr
# @lru_cache(_GLOBAL_LRU_CACHE_SIZE)
def _get_unflatten_size(input_shape, dim, sizes):
    input_rank = len(input_shape)
    if not isinstance(sizes, (tuple, list)):
        raise TypeError(f"Type of `sizes` should be `Tuple` or `List`, but got {type(sizes)}")

    if len(sizes) == 0:
        raise ValueError("`sizes` must be non-empty")

    if isinstance(dim, str):
        raise TypeError("Until Now, `dim` not support type of str in `unflatten`")

    _dim = dim
    if _dim < 0:
        _dim += input_rank

    if _dim < 0 or _dim >= input_rank:
        raise ValueError("`dim` should be in range [{}, {}), but got {}".format(-input_rank, input_rank, dim))

    _sizes_mul = reduce(operator.mul, list(sizes))
    if -1 not in sizes and _sizes_mul != input_shape[_dim]:
        raise ValueError(f"unflatten: Provided `sizes` {sizes} don't multiply up to the"
            f"size of dim {dim} ({input_shape[_dim]}) in the input tensor")

    out_shape = input_shape[:_dim] + tuple(sizes) + input_shape[_dim + 1:]
    return out_shape


@_primexpr
# @lru_cache(_GLOBAL_LRU_CACHE_SIZE)
def _get_slice_scatter_const(x_shape, dim, start, end, step):
    x_rank = len(x_shape)
    dim = dim if dim >= 0 else dim + x_rank
    start = start if start else 0
    end = end if end else x_shape[dim]
    index = list(range(start, end, step))
    return x_rank, index, dim


@_primexpr
# @lru_cache(_GLOBAL_LRU_CACHE_SIZE)
def _get_select_out_shape(input_shape, dim):
    shape = [input_shape[i] for i in range(len(input_shape)) if i != dim]
    return tuple(shape)


@_primexpr
# @lru_cache(_GLOBAL_LRU_CACHE_SIZE)
def _get_unfold_indices(input_shape, dimension, size, step):
    if dimension < 0:
        dimension += len(input_shape)
    indices = []
    for i in range(0, input_shape[dimension] - size + 1, step):
        indices.append(list(range(i, i + size)))

    return indices, dimension

@_primexpr
def _check_int_size(size, op_name, arg_name='size'):
    # Check whether 'arg_name' is an integer or a tensor with Int type, or a tuple/list composed of them,
    # while converting them uniformly to integer.
    if isinstance(size, Tensor) and size.dtype in all_int_type:
        size = int(size)
    elif isinstance(size, (tuple, list)):
        size_ = ()
        for item in size:
            if isinstance(item, int):
                size_ = size_ + (item,)
            elif isinstance(item, Tensor) and item.dtype in all_int_type:
                size_ = size_ + (int(item),)
            else:
                raise ValueError(f"For '{op_name}', the component of '{arg_name}' must be of type int, " \
                                 f"but got {type(item)}.")
        size = size_
    elif size and not isinstance(size, int):
        raise ValueError(f"For '{op_name}', the '{arg_name}' must be of type int, but got {type(size)}.")
    return size


def custom_matmul(input, other):
    # TODO: ms.ops.matmul not support int-dtype inpself.dtypeut on GPU, only support float16/float32 dtype input.
    input_dtype = input.dtype
    other_dtype = other.dtype
    if input_dtype != other_dtype:
        RuntimeError("For matmul, expected scalar type {}, but found {}.".format(input_dtype, other_dtype))

    if is_under_gpu_context() and input_dtype not in (ms.float32, ms.float16):
        input = input.astype(ms.float32)
        other = other.astype(ms.float32)

    ndim1_orig = ms.ops.rank(input)
    ndim2_orig = ms.ops.rank(other)
    if ndim1_orig == ndim2_orig:
        if ndim1_orig == 2:
            _matmul = _get_cache_prim(P.MatMul)(False, False)
            return _matmul(input, other).astype(input_dtype)

    return ms.ops.matmul(input, other).astype(input_dtype)

@_primexpr
def _get_diagonal_scatter_index(input_shape, offset, dim1, dim2):
    ndim = len(input_shape)
    _flag = 0
    if offset > 0 or (offset == 0 and input_shape[dim2] - offset < input_shape[dim1]):
        _flag = 1
        _arange_size = min(input_shape[dim1], input_shape[dim2] - offset)
    else:
        _arange_size = input_shape[dim1]

    index_shape = list(input_shape)
    index_shape[dim2] = 1
    if _flag == 1:
        index_shape[dim1] = _arange_size
    index_shape = tuple(index_shape)

    index = np.arange(_arange_size)
    index = index + offset
    index = np.expand_dims(index, -1)
    for _ in range(0, dim1):
        index = np.expand_dims(index, 0)
    for i in range(dim1 + 1, dim2):
        index = np.expand_dims(index, i)
    for _ in range(dim1 + 2, ndim):
        index = np.expand_dims(index, -1)
    index = np.broadcast_to(index, index_shape)
    return index

@_primexpr
def _norm_get_const(p, dim, ndim):
    if p not in [None, 'fro', 'nuc', float('inf'), float('-inf'), 0, 1, -1, 2, -2]:
        raise NotImplementedError("'Tensor.norm' and 'torch.norm' not support `p` beside "
                                 f"'fro', 'nuc', float('inf'), float('-inf'), 0, 1, -1, 2, -2., but got p={p}.")

    _matrix_norm = False
    if p in (0, 1, -1, -2):
        if dim is None:
            if ndim > 1:
                _matrix_norm = True
        elif isinstance(dim, (tuple, list)):
            if len(dim) != 1:
                _matrix_norm = True
    if _matrix_norm:
        raise NotImplementedError("For 'Tensor.norm' and 'torch.norm', when p in [0, 1, -1, -2], "
                                  "only support vector-norm. "
                                  "If need matrix-norm, please use torch.linalg.norm instead.")
    if p in ('fro', 2):
        if dim is None or isinstance(dim, int):
            p = None
        elif isinstance(dim, (list, tuple)) and len(dim) == 1:
            p = None
    return p

@_primexpr
def _gather_no_need_padding(input_shape, index_shape, dim):
    input_shape_list = list(input_shape)
    index_shape_list = list(index_shape)
    input_shape_list.pop(dim)
    index_shape_list.pop(dim)
    return input_shape_list == index_shape_list


@_primexpr
def _gather_get_padding_pattern(input_shape, index_shape, dim):
    padding_pattern = ()
    for i in range(len(input_shape)):
        if i == dim:
            padding_pattern = (0, 0) + padding_pattern
        else:
            padding_pattern = (0, input_shape[i] - index_shape[i]) + padding_pattern
    return padding_pattern

class _TensorMeta(type(ms_Tensor), abc.ABCMeta):
    """
    Meta class for Tensor. Used internally.
    """

class Tensor(StubTensor, metaclass=_TensorMeta):
    def __init__(self, *data, dtype=None, inner=False, cast_tensor=False):
        if cast_tensor:
            if len(data) != 1:
                raise RuntimeError("Tensor init data lenght is not 1 when cast_tensor=True")
            input_data = data[0]
            if isinstance(input_data, StubTensor):
                super(Tensor, self).__init__(stub=input_data.stub, tensor=input_data.tensor)
            elif isinstance(input_data, Tensor_):
                super(Tensor, self).__init__(tensor=input_data)
            else:
                raise ValueError(f"Tensor init data type is invaild: {type(input_data)}")
            self.adapter_flag = True
            return

        if dtype is not None:
            dtype = _dtypeDict[str(dtype).split('.')[-1].lower()]

        if inner is True:
            init_tensor = ms_Tensor(*data, dtype=dtype)
        else:
            _input_data, _shape = self._process_data(data)
            if _shape:
                if dtype is None:
                    dtype = get_default_dtype()
                init_func = Zero()
                init_func.__enable_zero_dim__ = True
                init_tensor = ms_Tensor(shape=_shape, dtype=dtype, init=init_func)
                init_tensor.init_data()
            else:
                if dtype is None:
                    if not isinstance(_input_data, (ms.Tensor, Tensor_, _TypedStorage)):
                        dtype = get_default_dtype()
                init_tensor = ms_Tensor(input_data=_input_data, dtype=dtype)
        super(Tensor, self).__init__(tensor=init_tensor)
        self.adapter_flag = True


    def _process_data(self, data):
        _shape = None
        _input_data = None
        if len(data) == 1:
            if isinstance(data[0], int):
                _shape = data
            elif isinstance(data[0], (np.ndarray, ms.Tensor, list, Tensor_)):
                _input_data = data[0]
            elif isinstance(data[0], tuple):
                if len(data[0]) == 1:
                    _shape = data[0]
                else:
                    _input_data = data[0]
            elif isinstance(data[0], _TypedStorage):
                _input_data=data[0]._storage.inner_data
            else:
                raise TypeError(f"For Tensor, data must be a sequence, got {type(data[0])}")
        elif len(data) > 1:
            _shape = list(data)
            for i, s in enumerate(data):
                if isinstance(s, int):
                    continue
                if isinstance(s, Tensor):
                    if s.dtype not in all_int_type_with_bool:
                        raise TypeError("For Tensor input shape, "
                                        f"elements should be int type but got {s.dtype} at pos {i + 1}")
                    _shape[i] = int(s)
                else:
                    raise TypeError("For Tensor, elements of shape must be int or Tensor.")
        else:
            _input_data = ()
        return _input_data, _shape

    def __format__(self, format_spec):
        if self.dim() == 0 and isinstance(self, Tensor):
            return self.item().__format__(format_spec)
        return object.__format__(self, format_spec)

    @classmethod
    def __subclasshook__(cls, param):
        """
        Parameter will be instance of Tensor
        """
        if cls is Tensor:
            if any("param_info" in s.__dict__ for s in param.__mro__):
                return True
        return NotImplemented

    def __deepcopy__(self, memodict):
        tensor_ms = cast_to_ms_tensor(self)
        return Tensor(ms.Tensor.__deepcopy__(tensor_ms, memodict))

    def __neg__(self):
        tensor_ms = cast_to_ms_tensor(self)
        out = tensor_ms.__neg__()
        return cast_to_adapter_tensor(out)

    def __invert__(self):
        tensor_ms = cast_to_ms_tensor(self)
        if tensor_ms.dtype != ms.bool_:
            out = - 1 - tensor_ms
        else:
            out = tensor_ms.__invert__()
        return cast_to_adapter_tensor(out)

    def __round__(self):
        tensor_ms = cast_to_ms_tensor(self)
        out = tensor_ms.__round__()
        return cast_to_adapter_tensor(out)

    def __pos__(self):
        tensor_ms = cast_to_ms_tensor(self)
        out = tensor_ms.__pos__()
        return cast_to_adapter_tensor(out)

    def __abs__(self):
        tensor_ms = cast_to_ms_tensor(self)
        out = tensor_ms.__abs__()
        return cast_to_adapter_tensor(out)

    def __add__(self, other):
        tensor_ms = cast_to_ms_tensor(self)
        other_ms = cast_to_ms_tensor(other)
        # TODO: mindspore __add__ do not support logical_or with two bool dtype tensors.
        out = tensor_ms.__add__(other_ms)
        return cast_to_adapter_tensor(out)

    def __and__(self, other):
        tensor_ms = cast_to_ms_tensor(self)
        other_ms = cast_to_ms_tensor(other)
        input_dtype = tensor_ms.dtype
        if input_dtype == mstype.bool_:
            # avoid BitwiseAnd op has not corresponding bprop.
            tensor_ms = tensor_ms.astype(mstype.int8)
            out = tensor_ms.mul(other_ms)
            out = out.astype(mstype.bool_)
        else:
            out = tensor_ms.__and__(other_ms)
        return cast_to_adapter_tensor(out)

    def __xor__(self, other):
        tensor_ms = cast_to_ms_tensor(self)
        other_ms = cast_to_ms_tensor(other)
        out = tensor_ms.__xor__(other_ms)
        return cast_to_adapter_tensor(out)

    def __or__(self, other):
        tensor_ms = cast_to_ms_tensor(self)
        other_ms = cast_to_ms_tensor(other)
        input_dtype = tensor_ms.dtype
        if input_dtype == mstype.bool_:
            # avoid BitwiseOr op has not corresponding bprop.
            tensor_ms = tensor_ms.astype(mstype.int8)
            out = tensor_ms.add(other_ms)
            out = out.astype(mstype.bool_)
        else:
            out = tensor_ms.__or__(other_ms)
        return cast_to_adapter_tensor(out)

    def __radd__(self, other):
        return self.__add__(other)

    def __iadd__(self, other):
        return self.__add__(other)

    def __sub__(self, other):
        tensor_ms = cast_to_ms_tensor(self)
        other_ms = cast_to_ms_tensor(other)
        out = tensor_ms.__sub__(other_ms)
        return cast_to_adapter_tensor(out)

    def __rsub__(self, other):
        tensor_ms = cast_to_ms_tensor(self)
        other_ms = cast_to_ms_tensor(other)
        out = tensor_ms.__rsub__(other_ms)
        return cast_to_adapter_tensor(out)

    def __isub__(self, other):
        tensor_ms = cast_to_ms_tensor(self)
        other_ms = cast_to_ms_tensor(other)
        out = tensor_ms.__isub__(other_ms)
        return cast_to_adapter_tensor(out)

    def __mul__(self, other):
        # TODO: In mindspore tensor.__mul__, float tensor can not mul with complex tensor
        tensor_ms = cast_to_ms_tensor(self)
        other_ms = cast_to_ms_tensor(other)
        out = tensor_ms.__mul__(other_ms)
        return cast_to_adapter_tensor(out)

    def __rmul__(self, other):
        return self.__mul__(other)

    def __imul__(self, other):
        return self.__mul__(other)

    def __truediv__(self, other):
        tensor_ms = cast_to_ms_tensor(self)
        other_ms = cast_to_ms_tensor(other)
        tensor_type = tensor_ms.dtype
        if 'Int' in str(tensor_type):
            tensor_ms = ms.ops.cast(tensor_ms, mstype.float32)
        out = tensor_ms.__truediv__(other_ms)
        return cast_to_adapter_tensor(out)

    def __rtruediv__(self, other):
        tensor_ms = cast_to_ms_tensor(self)
        other_ms = cast_to_ms_tensor(other)
        tensor_type = tensor_ms.dtype
        if 'Int' in str(tensor_type):
            tensor_ms = ms.ops.cast(tensor_ms, mstype.float32)
        out = tensor_ms.__rtruediv__(other_ms)
        return cast_to_adapter_tensor(out)

    def __mod__(self, other):
        tensor_ms = cast_to_ms_tensor(self)
        other_ms = cast_to_ms_tensor(other)
        out = tensor_ms.__mod__(other_ms)
        return cast_to_adapter_tensor(out)

    def __rmod__(self, other):
        tensor_ms = cast_to_ms_tensor(self)
        other_ms = cast_to_ms_tensor(other)
        out = tensor_ms.__rmod__(other_ms)
        return cast_to_adapter_tensor(out)

    def __imod__(self, other):
        tensor_ms = cast_to_ms_tensor(self)
        other_ms = cast_to_ms_tensor(other)
        out = tensor_ms.__imod__(other_ms)
        return cast_to_adapter_tensor(out)

    def __pow__(self, other):
        tensor_ms = cast_to_ms_tensor(self)
        other_ms = cast_to_ms_tensor(other)
        out = tensor_ms.__pow__(other_ms)
        return cast_to_adapter_tensor(out)

    def __rpow__(self, other):
        tensor_ms = cast_to_ms_tensor(self)
        other_ms = cast_to_ms_tensor(other)
        out = tensor_ms.__rpow__(other_ms)
        return cast_to_adapter_tensor(out)

    def __floordiv__(self, other):
        tensor_ms = cast_to_ms_tensor(self)
        other_ms = cast_to_ms_tensor(other)
        out = tensor_ms.__floordiv__(other_ms)
        return cast_to_adapter_tensor(out)

    def __rfloordiv__(self, other):
        tensor_ms = cast_to_ms_tensor(self)
        other_ms = cast_to_ms_tensor(other)
        out = tensor_ms.__rfloordiv__(other_ms)
        return cast_to_adapter_tensor(out)

    def __ifloordiv__(self, other):
        tensor_ms = cast_to_ms_tensor(self)
        other_ms = cast_to_ms_tensor(other)
        out = tensor_ms.__ifloordiv__(other_ms)
        return cast_to_adapter_tensor(out)

    def __lt__(self, other):
        tensor_ms = cast_to_ms_tensor(self)
        other_ms = cast_to_ms_tensor(other)
        out = tensor_ms.__lt__(other_ms)
        return cast_to_adapter_tensor(out)

    def __le__(self, other):
        tensor_ms = cast_to_ms_tensor(self)
        other_ms = cast_to_ms_tensor(other)
        out = tensor_ms.__le__(other_ms)
        return cast_to_adapter_tensor(out)

    def __gt__(self, other):
        tensor_ms = cast_to_ms_tensor(self)
        other_ms = cast_to_ms_tensor(other)
        out = tensor_ms.__gt__(other_ms)
        return cast_to_adapter_tensor(out)

    def __ge__(self, other):
        tensor_ms = cast_to_ms_tensor(self)
        other_ms = cast_to_ms_tensor(other)
        out = tensor_ms.__ge__(other_ms)
        return cast_to_adapter_tensor(out)

    def __eq__(self, other):
        tensor_ms = cast_to_ms_tensor(self)
        other_ms = cast_to_ms_tensor(other)
        out = tensor_ms.__eq__(other_ms)
        return cast_to_adapter_tensor(out)

    def __matmul__(self, other):
        tensor_ms = cast_to_ms_tensor(self)
        other_ms = cast_to_ms_tensor(other)
        out = tensor_ms.__matmul__(other_ms)
        return cast_to_adapter_tensor(out)

    def __rmatmul__(self, other):
        tensor_ms = cast_to_ms_tensor(self)
        other_ms = cast_to_ms_tensor(other)
        out = tensor_ms.__rmatmul__(other_ms)
        return cast_to_adapter_tensor(out)

    def __hash__(self):
        return hash(id(self))

    def __ne__(self, other):
        tensor_ms = cast_to_ms_tensor(self)
        other_ms = cast_to_ms_tensor(other)
        out = tensor_ms.__ne__(other_ms)
        return cast_to_adapter_tensor(out)

    # __setitem__ no need to overload
    def __getitem__(self, index):
        # TODO: not support complex Tensor and False bool index getitem
        def _getitem_handler(tensor_ms, index):
            if isinstance(index, bool):
                if index:
                    return tensor_ms.expand_dims(0)
                else:
                    index = ms.Tensor(False)
                    out = ms.ops.masked_select(tensor_ms, index)
                    return out
            if isinstance(index, tuple) and isinstance(index[0], bool):
                if False in index:
                    index = ms.Tensor(False)
                    out = ms.ops.masked_select(tensor_ms, index)
                    return out
                else:
                    return tensor_ms.expand_dims(0)
            return tensor_ms.__getitem__(index)

        tensor_ms = cast_to_ms_tensor(self)
        out_ms = _getitem_handler(tensor_ms, index)
        out = cast_to_adapter_tensor(out_ms)
        if out_ms is not tensor_ms:
            out.parent_tensor_ = tensor_ms
            out.index_of_parent_ = index
        return out

    def __getstate__(self):
        pickled = {"input_data": self.asnumpy(), "dtype": self.dtype}
        return pickled

    def __setstate__(self, state):
        Tensor.__init__(self, state["input_data"], dtype=state["dtype"], inner=True)

    def storage(self):
        if graph_mode_condition():
            warning('Currently, `tensor.storage()` is not supported in graph mode. '
                    'Please replace `Storage` related interfaces with the equivalent interface.')
        _storage = _UntypedStorage(inner_data=self)
        return _TypedStorage(wrap_storage=_storage, dtype=self.dtype)

    def storage_type(self):
        return self.storage()._get_legacy_storage_class()

    def storage_offset(self):
        # TODO: output of x[3:].storage_offset() is 3, which depends on the slice supporting inplace operations.
        return 0

    @property
    def dtype(self):
        x = cast_to_ms_tensor(self)
        dtype = x.dtype
        return _msdtype2typeDict.get(str(dtype), dtype)

    def fill_adapter(self, val):
        val = cast_to_ms_tensor(val)
        output = ms.ops.fill(self.dtype, self.shape, val)
        return cast_to_adapter_tensor(output)

    def fill_(self, val):
        output = self.fill_adapter(val)
        return _tensor_inplace_assign(self, output, "fill_", "fill_adapter")

    def normal_adapter(self, mean=0, std=1, *, generator=None):
        if generator is not None:
            raise ValueError("`generator` can not be supportted.")
        output = ms.ops.normal(self.shape, mean, std).astype(self.dtype)
        return cast_to_adapter_tensor(output)

    def normal_(self, mean=0, std=1, *, generator=None):
        output = self.normal_adapter(mean, std, generator=generator)
        return _tensor_inplace_assign(self, output, "normal_", "normal_adapter")

    def size(self, dim=None):
        """
        tensor.size() has the same function as tensor.size() in PyTorch,
        but different from the tensor.size in MindSpore.
        """
        if dim is None:
            return self.shape
        return self.shape[dim]

    def uniform_adapter(self, from_alias=0, to=1):  #TODO: from_alias->from
        from_alias = ms.Tensor(from_alias, ms.float32)
        to = ms.Tensor(to, ms.float32)
        output = ms.ops.uniform(self.shape, from_alias, to).astype(self.dtype)
        return cast_to_adapter_tensor(output)

    def uniform_(self, from_alias=0, to=1):
        output = self.uniform_adapter(from_alias, to)
        return _tensor_inplace_assign(self, output, "uniform_", "uniform_adapter")

    def random_adapter(self, from_alias=0, to=None, *, generator=None):  #TODO: from_alias->from
        unsupported_attr(generator)
        if generator:
            raise NotImplementedError("generator is not supported.")

        self_dtype = self.dtype

        if not to:
            if self_dtype == ms.float64:
                return self.uniform_adapter(from_alias, kMantissaFloat64)
            elif self_dtype == ms.float32:
                return self.uniform_adapter(from_alias, kMantissaFloat32)
            elif self_dtype == ms.float16:
                return self.uniform_adapter(from_alias, kMantissaFloat16)
            elif self_dtype == ms.uint8:
                return self.uniform_adapter(from_alias, kMaxUint8)
            elif self_dtype == ms.int64:
                return self.uniform_adapter(from_alias, kMaxInt64)
            elif self_dtype == ms.int32:
                return self.uniform_adapter(from_alias, kMaxInt32)
            elif self_dtype == ms.int16:
                return self.uniform_adapter(from_alias, kMaxInt16)
            elif self_dtype == ms.int8:
                return self.uniform_adapter(from_alias, kMaxInt8)
        to = to - 1 if to > 1 else to
        return self.uniform_adapter(from_alias, to)

    def random_(self, from_alias=0, to=None, *, generator=None):  #TODO: from_alias->from
        output = self.random_adapter(from_alias, to, generator=generator)
        return _tensor_inplace_assign(self, output, "random_", "random_adapter")

    def zero_adapter(self):
        output = ms.ops.fill(self.dtype, self.shape, 0.0)
        return cast_to_adapter_tensor(output)

    def zero_(self):
        output = self.zero_adapter()
        return _tensor_inplace_assign(self, output, "zero_", "zero_adapter")

    #TODO: adapter needs to support both positional and keywords input size to be consistent with pytorch
    #positional_size represents the positional arguments of size, size represents the keywords arguments input
    def new_zeros(self, *positional_size, size=None, dtype=None, device=None, requires_grad=False):
        unsupported_attr(device)
        unsupported_attr(requires_grad)

        if not dtype:
            dtype = self.dtype
        if size is None:
            if isinstance(positional_size[0], (tuple, list)):
                size = positional_size[0]
            else:
                size = positional_size
        if isinstance(size[0], tuple):
            size = size[0]

        output = ms.ops.fill(dtype, size, 0.0)
        return cast_to_adapter_tensor(output)

    def new_full(self, size, fill_value, *, dtype=None, device=None, requires_grad=False,
                 layout=None, pin_memory=False):
        unsupported_attr(device)
        unsupported_attr(requires_grad)
        unsupported_attr(layout)
        if layout:
            raise NotImplementedError("layout is not supported.")
        unsupported_attr(pin_memory)
        if pin_memory is True:
            raise NotImplementedError("pin_memory is not supported to True.")

        if not dtype:
            dtype = self.dtype

        size = _check_int_size(size, "new_full")
        output = ms.ops.fill(dtype, size, fill_value)
        return cast_to_adapter_tensor(output)

    def add(self, other, *, alpha=1):
        # TODO: ms.ops.add when add both bool Tensor, return int tensor instead of bool tensor.
        input_ms = cast_to_ms_tensor(self)
        other = cast_to_ms_tensor(other)
        output = ms.ops.add(input_ms, other*alpha)
        return cast_to_adapter_tensor(output)

    def add_(self, other, *, alpha=1):
        output = self.add(other, alpha=alpha)
        return _tensor_inplace_assign(self, output, "add_", "add")

    def erfinv(self):
        input_ms = cast_to_ms_tensor(self)
        output = ms.ops.erfinv(input_ms)
        return cast_to_adapter_tensor(output)

    def erfinv_(self):
        output = self.erfinv()
        return _tensor_inplace_assign(self, output, "erfinv_", "erfinv")

    def permute(self, *dims):
        ms_input = cast_to_ms_tensor(self)
        output = ms_input.transpose(*dims)
        return cast_to_adapter_tensor(output)

    def contiguous(self, memory_format=None):
        #TODO
        unsupported_attr(memory_format)
        return self

    def new_tensor(self, data, *, dtype=None, device=None, requires_grad=False, layout=None, pin_memory=False):
        unsupported_attr(layout)
        unsupported_attr(pin_memory)
        if not dtype:
            dtype = self.dtype

        if isinstance(data, Tensor):
            raise ValueError("To copy construct from a tensor, it is recommended to use sourceTensor.clone().detach() "
                             "or sourceTensor.clone().detach().requires_grad_(True), "
                             "rather than tensor.new_tensor(sourceTensor).")
        return tensor(data, dtype, device, requires_grad)

    def copy_adapter(self, src, non_blocking=False):
        unsupported_attr(non_blocking)
        input_ms = cast_to_ms_tensor(src)
        if len(self.shape) > 0 and input_ms != self.shape:
            output = ms.ops.broadcast_to(input_ms, self.shape)
        else:
            output = input_ms
        output = output.astype(self.dtype)
        return cast_to_adapter_tensor(output)

    def copy_(self, src, non_blocking=False):
        unsupported_attr(non_blocking)
        input_ms = cast_to_ms_tensor(src)
        if len(self.shape) > 0 and input_ms != self.shape:
            output = ms.ops.broadcast_to(input_ms, self.shape)
        else:
            output = input_ms
        output = output.astype(self.dtype)
        return _tensor_inplace_assign(self, output, "copy_", "copy_adapter")

    def expand(self, *size):
        # TODO: to use ms.ops.expand after it support on gpu. And ms.ops.expand support too few data type now
        input_ms = cast_to_ms_tensor(self)
        if isinstance(size[0], (list, tuple)):
            size = size[0]
        if isinstance(size, list):
            size = tuple(size)
        out = ms.ops.broadcast_to(input_ms, size)
        return cast_to_adapter_tensor(out)

    def sigmoid(self):
        input_ms = cast_to_ms_tensor(self)
        # TODO: ms.ops.sigmoid not support float64 on Ascend
        if is_under_ascend_context() and input_ms.dtype == ms.float64:
            input_ms = input_ms.astype(ms.float32)
            output = ms.ops.sigmoid(input_ms)
            output = output.astype(ms.float64)
        else:
            output = ms.ops.sigmoid(input_ms)
        return cast_to_adapter_tensor(output)

    def sigmoid_(self):
        output = self.sigmoid()
        return _tensor_inplace_assign(self, output, "sigmoid_", "sigmoid")

    def float(self, memory_format=None):
        if memory_format:
            raise NotImplementedError("memory_format is not supported.")
        input_ms = cast_to_ms_tensor(self)
        return cast_to_adapter_tensor(input_ms.float())

    def flip(self, dims):
        input_ms = cast_to_ms_tensor(self)
        if not isinstance(dims, (list, tuple)):
            dims = (dims,)
        output = input_ms.flip(dims)
        return cast_to_adapter_tensor(output)

    def sign(self):
        input_ms = cast_to_ms_tensor(self)
        output = ms.ops.sign(input_ms)
        return cast_to_adapter_tensor(output)

    def sign_(self):
        output = self.sign()
        return _tensor_inplace_assign(self, output, "sign_", "sign")

    def signbit(self):
        input_ms = cast_to_ms_tensor(self)
        output = ms.ops.signbit(input_ms)
        return cast_to_adapter_tensor(output)

    def svd(self, some=True, compute_uv=True):
        input_ms = cast_to_ms_tensor(self)
        if is_under_ascend_context():
            full_matrices = not some
            svd_op = numpy_cell.NumpySvd('svd')
            output = svd_op(input_ms, full_matrices, compute_uv)
        else:
            output = ms.ops.svd(input_ms, not some, compute_uv)
        if compute_uv:
            s, u, v = output
        else:
            if some:
                s = output
                row = input_ms.shape[0]
                col = input_ms.shape[1]
                u = ms.ops.zeros((row, row), input_ms.dtype)
                v = ms.ops.zeros((col, col), input_ms.dtype)
        output = (u, s, v)
        return cast_to_adapter_tensor(output)

    def swapaxes(self, axis0, axis1):
        if self.nelement() == 0:
            out_shape = list(self.shape)
            out_shape[axis0], out_shape[axis1] = out_shape[axis1], out_shape[axis0]
            return self.reshape(tuple(out_shape))
        input_ms = cast_to_ms_tensor(self)
        output = input_ms.swapaxes(axis0, axis1)
        return cast_to_adapter_tensor(output)

    def swapdims(self, dim0, dim1):
        input_ms = cast_to_ms_tensor(self)
        output = ms.ops.swapdims(input_ms, dim0, dim1)
        return cast_to_adapter_tensor(output)

    def subtract(self, other, *, alpha=1):
        input_ms = cast_to_ms_tensor(self)
        other = cast_to_ms_tensor(other)
        output = ms.ops.subtract(input_ms, other, alpha=alpha)
        return cast_to_adapter_tensor(output)

    def subtract_(self, other, *, alpha=1):
        output = self.subtract(other, alpha=alpha)
        return _tensor_inplace_assign(self, output, "subtract_", "subtract")

    def trace(self):
        input_ms = cast_to_ms_tensor(self)
        output = input_ms.trace()
        return cast_to_adapter_tensor(output)

    def ceil(self):
        input_ms = cast_to_ms_tensor(self)
        output = ms.ops.ceil(input_ms)
        return cast_to_adapter_tensor(output)

    def ceil_(self):
        output = self.ceil()
        return _tensor_inplace_assign(self, output, "ceil_", "ceil")

    def conj(self):
        input_ms = cast_to_ms_tensor(self)
        output = input_ms.conj()
        output = cast_to_adapter_tensor(output)
        output.conj_bit = True
        return output

    def is_conj(self):
        if not hasattr(self, "conj_bit"):
            return False
        else:
            return self.conj_bit

    def resolve_conj(self):
        output = deepcopy(self)
        output.conj_bit = False
        return output

    def ger(self, vec2):
        input_ms = cast_to_ms_tensor(self)
        vec2 = cast_to_ms_tensor(vec2)
        if input_ms.dtype != vec2.dtype:
            raise TypeError("For torch.ger(), input_ms and vec2 dtype must be the same")
        if not input_ms.is_floating_point():
            _out_dtype = input_ms.dtype
            input_ms = input_ms.astype(ms.float32)
            vec2 = vec2.astype(ms.float32)
            output = ms.ops.ger(input_ms, vec2)
            output = output.astype(_out_dtype)
        else:
            output = ms.ops.ger(input_ms, vec2)
        return cast_to_adapter_tensor(output)

    def movedim(self, source, destination):
        input_ms = cast_to_ms_tensor(self)
        output = ms.ops.movedim(input_ms, source, destination)
        return cast_to_adapter_tensor(output)

    def moveaxis(self, source, destination):
        input_ms = cast_to_ms_tensor(self)
        output = ms.ops.moveaxis(input_ms, source, destination)
        return cast_to_adapter_tensor(output)

    def mul(self, value):
        input_ms = cast_to_ms_tensor(self)
        ms_value = cast_to_ms_tensor(value)
        output = ms.ops.mul(input_ms, ms_value)
        return cast_to_adapter_tensor(output)

    def mul_(self, value):
        output = self.mul(value)
        return _tensor_inplace_assign(self, output, "mul_", "mul")

    @property
    def device(self):
        # Tensor.device and tensor.to(device) do not actually have effect in adapter
        # because mindspore do not control a single tensor to a certain deivce
        # So here for performance, return class device with target and id.
        return device_class(get_backend(), 0)

    def div(self, value, *, rounding_mode=None) :
        input_ms = cast_to_ms_tensor(self)
        value = cast_to_ms_tensor(value)
        # TODO: ms.ops.div to support real div when rounding_mode is None and input are all int type
        if rounding_mode is None:
            if input_ms.dtype in all_int_type:
                input_ms = ms.ops.cast(input_ms, mstype.float32)
        output = ms.ops.div(input_ms, value, rounding_mode=rounding_mode)
        return cast_to_adapter_tensor(output)

    def div_(self, value, *, rounding_mode=None):
        output = self.div(value, rounding_mode=rounding_mode)
        return _tensor_inplace_assign(self, output, "div_", "div")

    def cpu(self):
        #TODO
        return self

    # To achieve the polymorphism Tensor.min(Tensor input, Tensor other, *, Tensor out)
    # other=None is used to represent the keywords param input
    def min(self, dim=None, keepdim=False, other=None):
        input_ms = cast_to_ms_tensor(self)
        type = input_ms.dtype
        if other is not None:
            other = cast_to_ms_tensor(other)
            output = ms.ops.minimum(input_ms, other).astype(type)
            return cast_to_adapter_tensor(output)
        if isinstance(dim, Tensor):
            other = cast_to_ms_tensor(dim)
            output = ms.ops.minimum(input_ms, other).astype(type)
            return cast_to_adapter_tensor(output)
        if dim is None:
            output = input_ms.min(axis=dim, keepdims=keepdim).astype(type)
            return cast_to_adapter_tensor(output)
        value, indice = ms.ops.min(input_ms, dim, keepdim)
        value = value.astype(type)
        indice = indice.astype(ms.int64)
        if pynative_mode_condition():
            point = set_name_tuple('min')
            rlt = point(cast_to_adapter_tensor(value), cast_to_adapter_tensor(indice))
            return rlt
        return cast_to_adapter_tensor(value), cast_to_adapter_tensor(indice)

    # To achieve the polymorphism Tensor.max(Tensor input, Tensor other, *, Tensor out)
    # other=None is used to represent the keywords param input
    def max(self, dim=None, keepdim=False, other=None):
        input_ms = cast_to_ms_tensor(self)
        type = input_ms.dtype
        if other is not None:
            other = cast_to_ms_tensor(other)
            output = ms.ops.maximum(input_ms, other).astype(type)
            return cast_to_adapter_tensor(output)
        if isinstance(dim, Tensor):
            other = cast_to_ms_tensor(dim)
            output = ms.ops.maximum(input_ms, other).astype(type)
            return cast_to_adapter_tensor(output)
        if dim is None:
            output = input_ms.max(axis=dim, keepdims=keepdim).astype(type)
            return cast_to_adapter_tensor(output)
        value, indice = ms.ops.max(input_ms, dim, keepdim)
        value = value.astype(type)
        indice = indice.astype(ms.int64)
        if pynative_mode_condition():
            point = set_name_tuple('max')
            rlt = point(cast_to_adapter_tensor(value), cast_to_adapter_tensor(indice))
            return rlt
        return cast_to_adapter_tensor(value), cast_to_adapter_tensor(indice)


    def numel(self):
        input_ms = cast_to_ms_tensor(self)
        return P.size(input_ms)

    def detach(self):
        input_ms = cast_to_ms_tensor(self)
        output = ms.ops.stop_gradient(input_ms)
        return cast_to_adapter_tensor(output)

    def detach_(self):
        return _tensor_inplace_assign(self, self.detach(), "detach_", "detach")

    def sum(self, dim=None, keepdim=False, dtype=None):
        input_ms = cast_to_ms_tensor(self)
        # TODO: mindspore tensor.sum can not automatically promote dtype yet, will cause overflow.
        if dtype is not None:
            input_ms = input_ms.astype(dtype) if dtype != mstype.bool_ else \
                input_ms.astype(mstype.bool_).astype(mstype.int64)
        elif input_ms.dtype in msdapter_dtype.all_int_type_with_bool:
            dtype = mstype.int64
            input_ms = input_ms.astype(dtype)

        if isinstance(dim, list):
            dim = tuple(dim)
        res = input_ms.sum(dim, dtype, keepdim)
        if dtype is not None and dtype == mstype.bool_:
            res = res.astype(mstype.bool_)
        return cast_to_adapter_tensor(res)

    def sum_to_size(self, *size):
        input_ms = cast_to_ms_tensor(self)
        output = input_ms.sum_to_size(*size)
        return cast_to_adapter_tensor(output)

    def mean(self, dim=None, keepdim=False, dtype=None, axis=None):
        if dim is None:
            dim = axis

        input_ms = cast_to_adapter_tensor(self)
        if dtype:
            input_ms = self.astype(dtype)

        output = ms.ops.mean(input_ms, dim, keepdim)
        return cast_to_adapter_tensor(output)

    def prod(self, dim=None, keepdim=False, dtype=None):
        input_ms = cast_to_adapter_tensor(self)
        if dtype:
            input_ms = self.astype(dtype)

        #TODO: ms.ops.prod not support bool type on Ascend, CPU&GPU return type is bool
        if input_ms.dtype == ms.bool_:
            output = ms.ops.prod(input_ms.astype(ms.int8), dim, keepdim)
            output = output.astype(ms.int64)
        else:
            output = ms.ops.prod(input_ms, dim, keepdim)
        return cast_to_adapter_tensor(output)

    def split(self, split_size, dim=0):
        tensor = cast_to_ms_tensor(self)
        output = ms.ops.split(tensor, split_size, dim)
        return cast_to_adapter_tensor(output)

    def numpy(self):
        return self.asnumpy()

    def view(self, *shape):
        return self.reshape(*shape)

    def view_as(self, other):
        return self.view(other.shape)

    def ndimension(self):
        return len(self.shape)

    def pow(self, exponent):
        power = cast_to_ms_tensor(exponent)
        input_ms = cast_to_ms_tensor(self)
        output = input_ms.pow(power)
        return cast_to_adapter_tensor(output)

    def pow_(self, exponent):
        output = self.pow(exponent)
        return _tensor_inplace_assign(self, output, "pow_", "pow")

    def rad2deg(self):
        input_ms = cast_to_ms_tensor(self)
        if not input_ms.is_floating_point():
            input_ms = input_ms.astype(ms.float32)
        output = ms.ops.rad2deg(input_ms)
        return cast_to_adapter_tensor(output)

    @property
    def real(self):
        input_ms = cast_to_ms_tensor(self)
        output = ms.ops.real(input_ms)
        return cast_to_adapter_tensor(output)

    def reciprocal(self):
        input_ms = cast_to_ms_tensor(self)
        output = ms.ops.reciprocal(input_ms)
        #TODO: GPU has problem handling boundary value
        if is_under_gpu_context():
            output_dtype = output.dtype
            if output_dtype == ms.float32:
                output = ms.ops.where((output <= FP32_MIN) | (output >= FP32_MAX), float('inf'), output)
            if output_dtype == ms.float64:
                output = ms.ops.where((output <= FP64_MIN) | (output >= FP64_MAX), float('inf'), output)
        return cast_to_adapter_tensor(output)

    def reciprocal_(self):
        output = self.reciprocal()
        return _tensor_inplace_assign(self, output, "reciprocal_", "reciprocal")

    def remainder(self, other):
        input_ms = cast_to_ms_tensor(self)
        other = cast_to_ms_tensor(other)
        output = ms.ops.remainder(input_ms, other)
        return cast_to_adapter_tensor(output)

    def remainder_(self, other):
        output = self.remainder(other)
        return _tensor_inplace_assign(self, output, "remainder_", "remainder")

    def repeat(self, *sizes):
        input_x = cast_to_ms_tensor(self)
        if isinstance(sizes[0], list):
            sizes = tuple(*sizes)
        elif isinstance(sizes[0], tuple):
            sizes = sizes[0]
        output = ms.ops.tile(input_x, sizes)
        return cast_to_adapter_tensor(output)

    def repeat_interleave(self, repeats, dim=None, *, output_size=None):
        unsupported_attr(output_size)

        if isinstance(repeats, Tensor):
            new_repeats = []
            for index in repeats:
                new_repeats.append(int(index))
            repeats = new_repeats
        input_ms = cast_to_ms_tensor(self)
        output = input_ms.repeat(repeats, dim)
        return cast_to_adapter_tensor(output)

    def reshape(self, *shape):
        if not shape:
            raise ValueError("The shape variable should not be empty")
        if isinstance(shape[0], (tuple, list)):
            shape = shape[0]
        if isinstance(shape, list):
            shape = tuple(shape)

        input_size = self.shape
        if not ms.ops.is_sequence_value_unknown(input_size) and input_size[0] == 0:  # only support first element is 0
            numel = ms.ops.size(self)
            shape = _infer_size(shape, numel)
            # TODO: ms.ops.zeros() currently has problem handling input shape including 0
            output = _get_cache_prim(ms.ops.Zeros)()(shape, self.dtype)
        else:
            input_ms = cast_to_ms_tensor(self)
            output = ms.ops.reshape(input_ms, shape)
        return cast_to_adapter_tensor(output)

    def reshape_as(self, other):
        return self.reshape(other.shape)

    def arcsinh(self):
        return self.asinh()

    def arcsinh_(self):
        output = self.asinh()
        return _tensor_inplace_assign(self, output, "arcsinh_", "arcsinh")

    def arctanh(self):
        return self.atanh()

    def arctanh_(self):
        output = self.atanh()
        return _tensor_inplace_assign(self, output, "arctanh_", "arctanh")

    def det(self):
        input_ms = cast_to_ms_tensor(self)
        output = ms.ops.det(input_ms)
        return cast_to_adapter_tensor(output)

    def negative(self):
        input_ms = cast_to_ms_tensor(self)
        return cast_to_adapter_tensor(input_ms.negative())

    def negative_(self):
        output = self.negative()
        return _tensor_inplace_assign(self, output, "negative_", "negative")

    def abs(self):
        input_ms = cast_to_ms_tensor(self)
        if input_ms.dtype in [mstype.complex64, mstype.complex128]:
            output = _get_cache_prim(ms.ops.ComplexAbs)()(input_ms)
        else:
            output = input_ms.abs()
        return cast_to_adapter_tensor(output)

    def abs_(self):
        output = self.abs()
        return _tensor_inplace_assign(self, output, "abs_", "abs")

    @property
    def ndim(self):
        return len(self.shape)

    def amax(self, dim=None, keepdim=False):
        input_ms = cast_to_ms_tensor(self)
        if dim is not None:
            return cast_to_adapter_tensor(input_ms.amax(axis=dim, keepdims=keepdim))
        return cast_to_adapter_tensor(input_ms.amax(keepdims=keepdim))

    def amin(self, dim=None, keepdim=False):
        input_ms = cast_to_ms_tensor(self)
        if dim is not None:
            return cast_to_adapter_tensor(input_ms.amin(axis=dim, keepdims=keepdim))
        return cast_to_adapter_tensor(input_ms.amin(keepdims=keepdim))

    def as_strided(self, size, stride, storage_offset=None):
        warning("not support output as a view.")
        input_ms = cast_to_ms_tensor(self)
        if len(size) != len(stride):
            raise RuntimeError("mismatch in length of strides and shape.")
        index = np.arange(0, size[0]*stride[0], stride[0])
        for i in range(1, len(size)):
            tmp = np.arange(0, size[i]*stride[i], stride[i])
            index = np.expand_dims(index, -1)
            index = index + tmp
        if storage_offset is not None:
            index = index + storage_offset
        if index.size == 0:
            input_indices = ms.numpy.empty(index.shape, dtype=mstype.int32)
        else:
            input_indices = ms.Tensor(index)
        out = ms.ops.gather(input_ms.reshape(-1), input_indices, 0)
        return cast_to_adapter_tensor(out)

    def bmm(self, batch2):
        input_ms = cast_to_ms_tensor(self)
        return cast_to_adapter_tensor(input_ms.bmm(batch2))

    def clamp(self, min=None, max=None):
        input_ms = cast_to_ms_tensor(self)
        if is_under_ascend_context() and input_ms.dtype == ms.float64:
            input_ms = input_ms.astype(ms.float32)
            output = ms.ops.clamp(input_ms, min, max)
            output = output.astype(ms.float64)
        else:
            output = ms.ops.clamp(input_ms, min, max)
        return cast_to_adapter_tensor(output)

    def clamp_(self, min=None, max=None):
        output = self.clamp(min, max)
        return _tensor_inplace_assign(self, output, "clamp_", "clamp")

    def dim(self):
        return len(self.shape)

    def expand_as(self, other):
        input_ms = cast_to_ms_tensor(self)
        other_ms = cast_to_ms_tensor(other)
        output = input_ms.expand_as(other_ms)
        return cast_to_adapter_tensor(output)

    def item(self):
        input_ms = cast_to_ms_tensor(self)
        if input_ms.size > 1:
            raise ValueError("only one element tensors can be converted to Python scalars")
        output = input_ms.asnumpy().reshape(-1).tolist()
        return output[0]

    def log(self):
        input_ms = cast_to_ms_tensor(self)
        output = input_ms.log()
        return cast_to_adapter_tensor(output)

    def log_(self):
        output = self.log()
        return _tensor_inplace_assign(self, output, "log_", "log")

    def log2(self):
        input_ms = cast_to_ms_tensor(self)
        output = ms.ops.log2(input_ms)
        return cast_to_adapter_tensor(output)

    def log2_(self):
        output = self.log2()
        return _tensor_inplace_assign(self, output, "log2_", "log2")

    # TODO: currently not support return qr as second result
    def lstsq(self, A):
        input_ms = cast_to_ms_tensor(self)
        A = cast_to_ms_tensor(A)
        if is_under_cpu_context():
            output = ms.ops.lstsq(A, input_ms)
            qr = ms.ops.zeros(A.shape, A.dtype)
        else:
            #TODO: ms.ops.lstsq not support GPU and Ascend, use numpy func
            lstsq_op = numpy_cell.NumpyLstsq('lstsq')
            output, qr = lstsq_op(input_ms, A)
        return cast_to_adapter_tensor((output, qr))

    def matmul(self, tensor2):
        input_ms = cast_to_ms_tensor(self)
        tensor2_ms = cast_to_ms_tensor(tensor2)
        # TODO: repalce with output = ms.ops.matmul(input_ms, tensor2_ms)
        output = custom_matmul(input_ms, tensor2_ms)
        return cast_to_adapter_tensor(output)

    def squeeze(self, dim=None):
        input_ms = cast_to_ms_tensor(self)
        if dim is not None:
            if input_ms.shape[dim] != 1:
                output = input_ms
            else:
                output = ms.ops.squeeze(input_ms, dim)
        else:
            output = ms.ops.squeeze(input_ms)
        return cast_to_adapter_tensor(output)

    def squeeze_(self, dim=None):
        output = self.squeeze(dim)
        return _tensor_inplace_assign(self, output, "squeeze_", "squeeze")

    def stride(self, dim=None):
        input_ms = cast_to_ms_tensor(self)
        bytelen = input_ms.itemsize
        output = list(input_ms.strides)
        for i in range(len(output)):
            output[i] = output[i]//bytelen
        output = tuple(output)
        if dim is not None:
            output = output[dim]
        return output

    def sub(self, other, *, alpha=1):
        input_ms = cast_to_ms_tensor(self)
        input_other = cast_to_ms_tensor(other)
        if alpha != 1:
            if isinstance(input_other, ms.Tensor) and input_other.dtype in all_complex_type:
                # ms.ops.mul only support tensor input when dtype is complex type.
                input_other = input_other * ms.ops.scalar_to_tensor(alpha, input_other.dtype)
            else:
                input_other = input_other * alpha
        output = ms.ops.sub(input_ms, input_other)
        return cast_to_adapter_tensor(output)

    def sub_(self, other, *, alpha=1):
        output = self.sub(other, alpha=alpha)
        return _tensor_inplace_assign(self, output, "sub_", "sub")

    def is_floating_point(self):
        input_ms = cast_to_ms_tensor(self)
        return input_ms.is_floating_point()

    def unbind(self, dim=0):
        input_ms = cast_to_ms_tensor(self)
        return cast_to_adapter_tensor(input_ms.unbind(dim))

    def unsqueeze(self, dim):
        input_ms = cast_to_ms_tensor(self)
        return cast_to_adapter_tensor(input_ms.unsqueeze(dim))

    def unsqueeze_(self, dim):
        output = self.unsqueeze(dim)
        return _tensor_inplace_assign(self, output, "unsqueeze_", "unsqueeze")

    def is_signed(self):
        input_ms = cast_to_ms_tensor(self)
        return input_ms.is_signed()

    def transpose(self, dim0, dim1):
        input_ms = cast_to_ms_tensor(self)
        # The functions of ms.ops.swapaxes are consistent with torch.transpose
        output = ms.ops.swapaxes(input_ms, dim0, dim1)
        return cast_to_adapter_tensor(output)

    def transpose_(self, dim0, dim1):
        output = self.transpose(dim0, dim1)
        return _tensor_inplace_assign(self, output, "transpose_", "transpose")

    def floor(self):
        input_ms = cast_to_ms_tensor(self)
        output = input_ms.floor()
        return cast_to_adapter_tensor(output)

    def floor_(self):
        output = self.floor()
        return _tensor_inplace_assign(self, output, "floor_", "floor")

    def isfinite(self):
        input_ms = cast_to_ms_tensor(self)
        output = ms.ops.isfinite(input_ms)
        return cast_to_adapter_tensor(output)

    def isnan(self):
        input_ms = cast_to_ms_tensor(self)
        return cast_to_adapter_tensor(input_ms.isnan())

    def is_contiguous(self, memory_format=None):
        unsupported_attr(memory_format)
        warning("is_contiguous is always True in Tensor.")
        return True

    def is_pinned(self):
        warning("is_pinned is always False in Tensor.")
        return False

    def is_set_to(self, tensor):
        return id(self.tensor) == id(tensor.tensor)

    def is_shared(self):
        warning("is_shared is always False in Tensor.")
        return False

    @property
    def is_sparse(self):
        warning("is_sparse is always False in Tensor.")
        return False

    def pin_memory(self):
        warning("Currently, pin_memory is not effective.")
        return self

    def clone(self):
        input_ms = cast_to_ms_tensor(self)
        return cast_to_adapter_tensor(input_ms.copy())

    def to(self, *args, **kwargs):
        # TODO:
        # Note that this API requires the user to ensure the correctness of the input currently,
        # and only the function of modifying dtype is available.

        if len(args) == 0 and len(kwargs) == 0:
            raise ValueError("Tensor.to is missing inputs, please check.")
        input_ms = cast_to_ms_tensor(self)

        if "dtype" in kwargs:
            set_dtype = kwargs.get("dtype")
            return cast_to_adapter_tensor(input_ms.astype(set_dtype))
        elif "other" in kwargs:
            set_dtype = kwargs.get("other").dtype
            return cast_to_adapter_tensor(input_ms.astype(set_dtype))
        elif "device" in kwargs:
            return self

        if len(args) == 0:
            return self

        if args[0] in _dtypeDict.values():
            return cast_to_adapter_tensor(input_ms.astype(args[0]))
        elif isinstance(args[0], Tensor):
            set_dtype = args[0].dtype
            return cast_to_adapter_tensor(input_ms.astype(set_dtype))
        elif args[0] and not isinstance(args[0], (str, device_class, int)):
            raise ValueError("The inputs of Tensor.to is abnormal, please check.")

        if len(args) > 1 and args[1] in _dtypeDict.values():
            return cast_to_adapter_tensor(input_ms.astype(args[1]))
        return self

    def sort(self, dim=-1, descending=False):
        input_ms = cast_to_ms_tensor(self)
        input_type = input_ms.dtype
        if 'Int' in str(input_type):
            input_ms = input_ms.astype(ms.float32)
            sort_tensor, sort_index = ms.ops.sort(input_ms, dim, descending)
            sort_tensor = sort_tensor.astype(input_type)
            sort_index = sort_index.astype(ms.int64)
            return cast_to_adapter_tensor((sort_tensor, sort_index))
        else:
            output = ms.ops.sort(input_ms, dim, descending)
        return cast_to_adapter_tensor(output)

    def msort(self):
        input_ms = cast_to_ms_tensor(self)
        input_type = input_ms.dtype
        if input_type in msdapter_dtype.all_int_type:
            input_ms = input_ms.astype(ms.float32)
            output= ms.ops.msort(input_ms)
            output = output.astype(input_type)
        else:
            output = ms.ops.msort(input_ms)
        return cast_to_adapter_tensor(output)

    def argsort(self, dim=-1, descending=False):
        input_ms = cast_to_ms_tensor(self)
        if input_ms.dtype in msdapter_dtype.all_int_type:
            input_ms = input_ms.astype(ms.float32)
            output = ms.ops.argsort(input_ms, dim, descending)
            output = output.astype(ms.int64)
        else:
            output = ms.ops.argsort(input_ms, dim, descending)
        return cast_to_adapter_tensor(output)

    def sqrt(self):
        input_ms = cast_to_ms_tensor(self)
        return cast_to_adapter_tensor(ms.ops.sqrt(input_ms))

    def sqrt_(self):
        output = self.sqrt()
        return _tensor_inplace_assign(self, output, "sqrt_", "sqrt")

    def rsqrt(self):
        input_ms = cast_to_ms_tensor(self)
        if input_ms.dtype in all_int_type_with_bool:
            input_ms = input_ms.astype(ms.float32)
        output = ms.ops.rsqrt(input_ms)
        return cast_to_adapter_tensor(output)

    def rsqrt_(self):
        output = self.rsqrt()
        return _tensor_inplace_assign(self, output, "rsqrt_", "rsqrt")

    def resize(self, *size, memory_format=None):
        unsupported_attr(memory_format)
        input_ms = cast_to_ms_tensor(self)
        input_size = input_ms.shape
        if len(input_size) == 1 and input_size[0] == 0:
            if isinstance(size[0], (tuple, list)):
                size = size[0]
            out = ms.ops.zeros(size, self.dtype)
        elif len(size) > 0 and isinstance(size[0], tuple):
            out = input_ms.resize(size[0])
        else:
            out = input_ms.resize(size)
        return cast_to_adapter_tensor(out)

    def resize_(self, *size, memory_format=None):
        output = self.resize(*size, memory_format=memory_format)
        return _tensor_inplace_assign(self, output, "resize_", "resize")

    def resize_as(self, tensor, memory_format=None):
        unsupported_attr(memory_format)
        if not isinstance(tensor, Tensor):
            raise TypeError("resize_as(): argument 'tensor' must be Tensor.")
        input_ms = cast_to_ms_tensor(self)
        size = tensor.shape
        input_size = input_ms.shape
        if len(input_size) == 1 and input_size[0] == 0:
            out = ms.ops.zeros(size, self.dtype)
        else:
            out = input_ms.resize(size)
        return cast_to_adapter_tensor(out)

    def resize_as_(self, tensor, memory_format=None):
        output = self.resize_as(tensor, memory_format)
        return _tensor_inplace_assign(self, output, "resize_as_", "resize_as")

    def index_fill(self, dim, index, value):
        input_ms = cast_to_ms_tensor(self)
        index = cast_to_ms_tensor(index)
        index = ms.ops.cast(index, mstype.int32)
        out = input_ms.index_fill(dim, index, value)
        return cast_to_adapter_tensor(out)

    def index_fill_(self, dim, index, value):
        output = self.index_fill(dim, index, value)
        return _tensor_inplace_assign(self, output, "index_fill_", "index_fill")

    def index_select(self, dim, index):
        _input_params = cast_to_ms_tensor(self)
        _input_indices = cast_to_ms_tensor(index)

        output = ms.ops.gather(_input_params, _input_indices, dim)
        return cast_to_adapter_tensor(output)

    @property
    def data(self):
        return self.detach()

    @data.setter
    def data(self, data):
        ms_data = cast_to_ms_tensor(data)
        self.assign_value(ms_data)

    def new(self, *size):
        if len(size) > 0 and isinstance(size[0], tuple):
            size = size[0]
        _dtype = self.dtype
        return Tensor(*size, dtype=_dtype)

    def cuda(self, device=None, non_blocking=False, memory_format=None):
        unsupported_attr(device)
        unsupported_attr(non_blocking)
        unsupported_attr(memory_format)
        if not is_under_gpu_context():
            backend = get_backend()
            warning_msg = f"MsAdater.pytorch.Tensor.cuda() didn't work because it is under {backend} context."
            warning(warning_msg)
        return self

    def is_cuda(self):
        return is_under_gpu_context()

    def le(self, other):
        input_ms = cast_to_ms_tensor(self)
        if isinstance(other, Tensor):
            other = cast_to_ms_tensor(other)
        out = ms.ops.le(input_ms, other)
        return cast_to_adapter_tensor(out)

    def le_(self, other):
        output = self.le(other)
        return _tensor_inplace_assign(self, output, "le_", "le")

    def t(self):
        input_ms = cast_to_ms_tensor(self)
        output = ms.ops.t(input_ms)
        return cast_to_adapter_tensor(output)

    def t_(self):
        output = self.t()
        return _tensor_inplace_assign(self, output, "t_", "t")

    @property
    def T(self):
        input_ms = cast_to_ms_tensor(self)
        if input_ms.ndim <= 2:
            warning_msg = ("The use of Tensor.T() on tensors of dimension other than 2 to reverse "
                           "their shape is deprecated and it will throw an error in a future release. ")
            warning(warning_msg)
        output = input_ms.transpose()
        return cast_to_adapter_tensor(output)

    @property
    def H(self):
        # TODO: torch is view of origin Tensor, but adapter create a new tensor
        if not self.ndim == 2:
            raise ValueError(f"tensor.H is only supported on matrices (2-D tensors). Got {self.ndim}-D tensor.")

        if self.is_complex():
            return self.transpose(0, 1).conj()
        else:
            return self.transpose(0, 1)

    @property
    def is_quantized(self):
        warning("tensor.is_quantized only suppport set to False now. So It is always False.")
        return False

    @is_quantized.setter
    def is_quantized(self, flag):
        raise AttributeError("attribute 'is_quantized' of 'torch.Tensor' objects is not writable.")

    @property
    def requires_grad(self):
        warning("tensor.requires_grad only suppport set to True now. So It is always True.")
        return True

    @requires_grad.setter
    def requires_grad(self, flag):
        if not isinstance(flag, bool):
            raise RuntimeError("requires_grad must be a bool")
        if flag is False:
            raise NotImplementedError("tensor.requires_grad can not set to False yet. "
                                      "If tensor is not leaf Tensor, can try tensor.detach() instead. "
                                      "If tensor is leaf Tensor, can replaces tensor with Parameter, because "
                                      "Parameter.requires_grad work with mindspore autograd mechanism, "
                                      "when it set to False, the gradient return by ms.grad"
                                      "(https://www.mindspore.cn/docs/zh-CN/r2.0/"
                                      "api_python/mindspore/mindspore.grad.html) "
                                      "or ms.value_and_grad"
                                      "(https://www.mindspore.cn/docs/zh-CN/r2.0/"
                                      "api_python/mindspore/mindspore.value_and_grad.html)"
                                      " is zero. ")

    def requires_grad_(self, requires_grad=True):
        if requires_grad is False:
            warning("requires_grad is always True in Tensor.")
        return self

    def nonzero(self,  *, out=None, as_tuple=False):
        if out is not None:
            warning("Do not support parameter 'out'.")
        input_ms = cast_to_ms_tensor(self)
        output = None
        if as_tuple:
            if input_ms.ndim == 1:
                res = ms.ops.nonzero(input_ms)
                output = (cast_to_adapter_tensor(res.flatten()),)
            elif input_ms.ndim > 1:
                output = []
                res = ms.ops.nonzero(input_ms)
                res = res.transpose(1, 0)
                res = ms.ops.split(res, input_ms.ndim, axis=0)
                for cur in res:
                    output.append(cast_to_adapter_tensor(cur))
                output = tuple(output)
            elif input_ms.ndim == 0:
                raise ValueError("Do not support input ndim == 0.")
            return output
        return cast_to_adapter_tensor(ms.ops.nonzero(input_ms))

    def bool(self, memory_format=None):
        unsupported_attr(memory_format)
        input_ms = cast_to_ms_tensor(self)
        output = input_ms.bool()
        return cast_to_adapter_tensor(output)

    def eq(self, other):
        input_ms = cast_to_ms_tensor(self)
        other_ms = cast_to_ms_tensor(other)
        output = input_ms.equal(other_ms)
        return cast_to_adapter_tensor(output)

    def eq_(self, other):
        output = self.eq(other)
        return _tensor_inplace_assign(self, output, "eq_", "eq")

    def std(self, dim=None, unbiased=True, keepdim=False):
        #TODO: not support complex input
        input_ms = cast_to_ms_tensor(self)
        _dim = dim if dim is not None else ()
        _ddof = 1 if unbiased else 0
        output = input_ms.std(_dim, _ddof, keepdim)
        return cast_to_adapter_tensor(output)

    def exp(self):
        input_ms = cast_to_ms_tensor(self)
        output = input_ms.exp()
        return cast_to_adapter_tensor(output)

    def exp_(self):
        output = self.exp()
        return _tensor_inplace_assign(self, output, "exp_", "exp")

    def masked_fill(self, mask, value):
        input_ms = cast_to_ms_tensor(self)
        output = input_ms.masked_fill(mask.bool(), value)
        return cast_to_adapter_tensor(output)

    def masked_fill_(self, mask, value):
        output = self.masked_fill(mask, value)
        return _tensor_inplace_assign(self, output, "masked_fill_", "masked_fill")

    def tolist(self):
        return self.numpy().tolist()

    def bernoulli(self, *, generator=None):
        return self._bernoulli_adapter(self, generator=generator)

    def bernoulli_(self, p=0.5, *, generator=None):
        output = self._bernoulli_adapter(p, generator=generator)
        return _tensor_inplace_assign(self, output, "bernoulli_", "_bernoulli_adapter")

    def _bernoulli_adapter(self, p=0.5, *, generator=None):
        if generator:
            raise NotImplementedError("generator is not supported.")
        input_ms = cast_to_ms_tensor(self)

        bernoulli_seed = ms.get_seed()
        if not bernoulli_seed:
            bernoulli_seed = -1
        if not isinstance(p, (Tensor, float)):
            p = float(p)
        #TODO: Ascend currently not support ops.bernoulli, use numpy.random.binomial
        if is_under_ascend_context():
            if isinstance(p, ms.Tensor):
                p = p.numpy()
            # on Ascend, use numpy binomial to do forward computation
            # here it doesn't need to consider the backward
            # because torch.bernoulli return zero grad, and mindspore return zero grad here as well.
            np_output = np.random.binomial(1, p, size=input_ms.shape)
            output = ms.Tensor.from_numpy(np_output).to(dtype=input_ms.dtype)
            return cast_to_adapter_tensor(output)
        else:
            p = cast_to_ms_tensor(p)
            return cast_to_adapter_tensor(input_ms.bernoulli(p, bernoulli_seed))

    def round(self, decimals=0):
        input_ms = cast_to_ms_tensor(self)
        # TODO: after ms.ops.round() support `decimals`, change code below.
        if decimals == 0:
            output = ms.ops.round(input_ms)
        else:
            p = 10 ** decimals
            input_ms = input_ms * p
            output = ms.ops.round(input_ms) / p
        return cast_to_adapter_tensor(output)

    def round_(self, decimals=0):
        output = self.round(decimals)
        return _tensor_inplace_assign(self, output, "round_", "round")

    def long(self, memory_format=None):
        unsupported_attr(memory_format)
        if memory_format:
            raise NotImplementedError("memory_format is not supported.")
        input_ms = cast_to_ms_tensor(self)
        return cast_to_adapter_tensor(input_ms.astype(_dtypeDict["long"]))

    def half(self, memory_format=None):
        unsupported_attr(memory_format)
        if memory_format:
            raise NotImplementedError("memory_format is not supported.")
        input_ms = cast_to_ms_tensor(self)
        return cast_to_adapter_tensor(input_ms.astype(_dtypeDict["half"]))

    def int(self, memory_format=None):
        unsupported_attr(memory_format)
        if memory_format:
            raise NotImplementedError("memory_format is not supported.")
        input_ms = cast_to_ms_tensor(self)
        return cast_to_adapter_tensor(input_ms.int())

    def double(self, memory_format=None):
        unsupported_attr(memory_format)
        if memory_format:
            raise NotImplementedError("memory_format is not supported.")
        input_ms = cast_to_ms_tensor(self)
        return cast_to_adapter_tensor(input_ms.astype(_dtypeDict["double"]))

    def char(self, memory_format=None):
        unsupported_attr(memory_format)
        if memory_format:
            raise NotImplementedError("memory_format is not supported.")
        input_ms = cast_to_ms_tensor(self)
        return cast_to_adapter_tensor(input_ms.astype(_dtypeDict["char"]))

    def byte(self, memory_format=None):
        unsupported_attr(memory_format)
        if memory_format:
            raise NotImplementedError("memory_format is not supported.")
        input_ms = cast_to_ms_tensor(self)
        return cast_to_adapter_tensor(input_ms.astype(_dtypeDict["byte"]))

    def short(self, memory_format=None):
        unsupported_attr(memory_format)
        if memory_format:
            raise NotImplementedError("memory_format is not supported.")
        input_ms = cast_to_ms_tensor(self)
        return cast_to_adapter_tensor(input_ms.astype(_dtypeDict["short"]))


    def chunk(self, chunks, dim=0):
        input_ms = cast_to_ms_tensor(self)
        output = ms.ops.chunk(input_ms, chunks, dim)
        return cast_to_adapter_tensor(output)

    def flatten(self, start_dim=0, end_dim=-1):
        input_ms = cast_to_ms_tensor(self)
        output = ms.ops.flatten(input_ms, order='C', start_dim=start_dim, end_dim=end_dim)
        return cast_to_adapter_tensor(output)

    def unflatten(self, dim, sizes):
        input_ms = cast_to_ms_tensor(self)
        out_shape = _get_unflatten_size(input_ms.shape, dim, sizes)
        out = ms.ops.reshape(input_ms, out_shape)
        return cast_to_adapter_tensor(out)

    def sin(self):
        input_ms = cast_to_ms_tensor(self)
        return cast_to_adapter_tensor(ms.ops.sin(input_ms))

    def sin_(self):
        output = self.sin()
        return _tensor_inplace_assign(self, output, "sin_", "sin")

    def ge(self, other):
        input_ms = cast_to_ms_tensor(self)
        other = cast_to_ms_tensor(other)
        output = input_ms.ge(other)
        return cast_to_adapter_tensor(output)

    def ge_(self, other):
        output = self.ge(other)
        return _tensor_inplace_assign(self, output, "ge_", "ge")

    def cumsum(self, dim, dtype=None):
        input_ms = cast_to_ms_tensor(self)
        if dtype is not None:
            input_ms = input_ms.astype(dtype)
        elif input_ms.dtype in msdapter_dtype.all_int_type_with_bool:
            # TODO: ms.cumsum only support int32 on Ascend
            dtype = mstype.int32 if is_under_ascend_context() else mstype.int64
            input_ms = input_ms.astype(dtype)

        res = ms.ops.cumsum(input_ms, dim, dtype)
        return cast_to_adapter_tensor(res)

    def cumsum_(self, dim, dtype=None):
        output = self.cumsum(dim, dtype)
        return _tensor_inplace_assign(self, output, "cumsum_", "cumsum")

    def absolute(self):
        return self.abs()

    def absolute_(self):
        output = self.abs()
        return _tensor_inplace_assign(self, output, "absolute_", "absolute")

    def acos(self):
        input_ms = cast_to_ms_tensor(self)
        if input_ms.dtype in all_int_type:
            input_ms = input_ms.astype(mstype.float32)
        output = ms.ops.acos(input_ms)
        return cast_to_adapter_tensor(output)

    def acos_(self):
        output = self.acos()
        return _tensor_inplace_assign(self, output, "acos_", "acos")

    def arccos(self):
        return self.acos()

    def arccos_(self):
        output = self.acos()
        return _tensor_inplace_assign(self, output, "arccos_", "arccos")

    def asinh(self):
        input_ms = cast_to_ms_tensor(self)
        if input_ms.dtype in all_int_type:
            input_ms = input_ms.astype(mstype.float32)
        output = ms.ops.asinh(input_ms)
        return cast_to_adapter_tensor(output)

    def asinh_(self):
        output = self.asinh()
        return _tensor_inplace_assign(self, output, "asinh_", "asinh")

    def atanh(self):
        input_ms = cast_to_ms_tensor(self)
        if input_ms.dtype in all_int_type:
            input_ms = input_ms.astype(mstype.float32)
        output = ms.ops.atanh(input_ms)
        return cast_to_adapter_tensor(output)

    def atanh_(self):
        output = self.atanh()
        return _tensor_inplace_assign(self, output, "atanh_", "atanh")

    def addcdiv(self, tensor1, tensor2, *, value=1):
        input_ms = cast_to_ms_tensor(self)
        tensor1 = cast_to_ms_tensor(tensor1)
        tensor2 = cast_to_ms_tensor(tensor2)
        if is_under_ascend_context():
            value = ms.Tensor(value).astype(input_ms.dtype)
        output = ms.ops.addcdiv(input_ms, tensor1, tensor2, value)
        return cast_to_adapter_tensor(output)

    def addcdiv_(self, tensor1, tensor2, *, value=1):
        output = self.addcdiv(tensor1, tensor2, value=value)
        return _tensor_inplace_assign(self, output, "addcdiv_", "addcdiv")

    def gather(self, dim, index):
        input_ms = cast_to_ms_tensor(self)
        index = cast_to_ms_tensor(index)
        input_shape = input_ms.shape
        index_shape = index.shape
        if _gather_no_need_padding(input_shape, index_shape, dim):
            output = ms.ops.gather_elements(input_ms, dim, index)
        else:
            padding_pattern = _gather_get_padding_pattern(input_shape, index_shape, dim)
            padded_index = ms.ops.pad(index, padding_pattern)
            output = ms.ops.gather_elements(input_ms, dim, padded_index)
            index_mask = ms.ops.pad(ms.ops.ones(index_shape), padding_pattern).astype(ms.bool_)
            output = output[index_mask].reshape(index_shape)
        return cast_to_adapter_tensor(output)

    def fmod(self, divisor):
        x = cast_to_ms_tensor(self)
        other = cast_to_ms_tensor(divisor)
        output = ms.ops.fmod(x, other)
        return cast_to_adapter_tensor(output)

    def fmod_(self, divisor):
        output = self.fmod(divisor)
        return _tensor_inplace_assign(self, output, "fmod_", "fmod")

    def lt(self, other):
        input_ms = cast_to_ms_tensor(self)
        other = cast_to_ms_tensor(other)
        output = ms.ops.less(input_ms, other)
        return cast_to_adapter_tensor(output)

    def lt_(self, other):
        output = self.lt(other)
        return _tensor_inplace_assign(self, output, "lt_", "lt")

    def less(self, other):
        return self.lt(other)

    def less_(self, other):
        output = self.lt(other)
        return _tensor_inplace_assign(self, output, "less_", "less")

    def less_equal(self, other):
        input_ms = cast_to_ms_tensor(self)
        other = cast_to_ms_tensor(other)
        output = ms.ops.less_equal(input_ms, other)
        return cast_to_adapter_tensor(output)

    def less_equal_(self, other):
        output = self.less_equal(other)
        return _tensor_inplace_assign(self, output, "less_equal_", "less_equal")

    def ne(self, other):
        input_ms = cast_to_ms_tensor(self)
        other = cast_to_ms_tensor(other)
        output = ms.ops.ne(input_ms, other)
        return cast_to_adapter_tensor(output)

    def ne_(self, other):
        output = self.ne(other)
        return _tensor_inplace_assign(self, output, "ne_", "ne")

    def not_equal(self, other):
        return self.ne(other)

    def not_equal_(self, other):
        output = self.ne(other)
        return _tensor_inplace_assign(self, output, "not_equal_", "not_equal")

    def equal(self, other):
        if not isinstance(other, Tensor):
            raise ValueError("`other` must be Tensor")
        x = cast_to_ms_tensor(self)
        y = cast_to_ms_tensor(other)

        if x.dtype != y.dtype:
            return False
        if x.shape == y.shape:
            size = x.size
            output = ms.ops.equal(x, y)
            output = output.sum()
            if output == size:
                return True
        return False

    def greater(self, other):
        input_ms = cast_to_ms_tensor(self)
        other = cast_to_ms_tensor(other)
        output = ms.ops.greater(input_ms, other)
        return cast_to_adapter_tensor(output)

    def greater_(self, other):
        output = self.greater(other)
        return _tensor_inplace_assign(self, output, "greater_", "greater")

    def gt(self, other):
        input_ms = cast_to_ms_tensor(self)
        other = cast_to_ms_tensor(other)
        output = ms.ops.gt(input_ms, other)
        return cast_to_adapter_tensor(output)

    def gt_(self, other):
        output = self.greater(other)
        return _tensor_inplace_assign(self, output, "gt_", "gt")

    def greater_equal(self, other):
        x = cast_to_ms_tensor(self)
        y = cast_to_ms_tensor(other)
        output = ms.ops.greater_equal(x, y)
        return cast_to_adapter_tensor(output)

    def greater_equal_(self, other):
        output = self.greater_equal(other)
        return _tensor_inplace_assign(self, output, "greater_equal_", "greater_equal")

    def argmin(self, dim=None, keepdim=False):
        input_ms = cast_to_ms_tensor(self)
        output = ms.ops.argmin(input_ms, axis=dim, keepdims=keepdim)
        return cast_to_adapter_tensor(output)

    def argmax(self, dim=None, keepdim=False, axis=None):
        if dim is None:
            dim = axis
        input_ms = cast_to_ms_tensor(self)
        output = ms.ops.argmax(input_ms, dim, keepdim)
        return cast_to_adapter_tensor(output)

    def type(self, dtype=None, non_blocking=False, **kwargs):
        unsupported_attr(non_blocking)
        unsupported_attr(kwargs)
        if dtype is None:
            return _get_type_from_dtype(self.dtype)

        _dtype =  _get_dtype_from_type(dtype)
        if _dtype == self.dtype:
            return self
        x = cast_to_ms_tensor(self)
        output = x.astype(_dtype)
        return cast_to_adapter_tensor(output)

    def type_as(self, tensor):
        x = cast_to_ms_tensor(self)
        output = x.astype(tensor.dtype)
        return cast_to_adapter_tensor(output)

    def get_device(self):
        return -1

    def baddbmm(self, batch1, batch2, *, beta=1, alpha=1):
        x = cast_to_ms_tensor(self)
        batch1 = cast_to_ms_tensor(batch1)
        batch2 = cast_to_ms_tensor(batch2)
        output = ms.ops.baddbmm(x, batch1, batch2, beta, alpha)
        return cast_to_adapter_tensor(output)

    def baddbmm_(self, batch1, batch2, *, beta=1, alpha=1):
        output = self.baddbmm(batch1, batch2, beta=beta, alpha=alpha)
        return _tensor_inplace_assign(self, output, "baddbmm_", "baddbmm")

    def topk(self, k, dim=None, largest=True, sorted=True):
        input_x = cast_to_ms_tensor(self)
        if k == 0:
            value, indice = (ms.ops.zeros((0,), dtype=input_x.dtype), ms.ops.zeros((0,), dtype=ms.int32))
        else:
            value, indice = ms.ops.topk(input_x, k, dim, largest, sorted)
        if pynative_mode_condition():
            point = set_name_tuple('topk')
            rlt = point(cast_to_adapter_tensor(value), cast_to_adapter_tensor(indice))
            return rlt
        return cast_to_adapter_tensor((value, indice))

    def maximum(self, other):
        x = cast_to_ms_tensor(self)
        y = cast_to_ms_tensor(other)
        #TODO: NAN is different
        output = ms.ops.maximum(x, y)
        return cast_to_adapter_tensor(output)

    def minimum(self, other):
        x = cast_to_ms_tensor(self)
        y = cast_to_ms_tensor(other)
        #TODO: NAN is different
        output = ms.ops.minimum(x, y)
        return cast_to_adapter_tensor(output)

    def fmax(self, other):
        if is_under_ascend_context() or is_under_gpu_context():
            fmax_op = numpy_cell.NumpyFmax('fmax')
            output = fmax_op(self, other)
        else:
            x = cast_to_ms_tensor(self)
            y = cast_to_ms_tensor(other)
            # TODO: ms.ops.fmax only support CPU now
            output = ms.ops.fmax(x, y)
        return cast_to_adapter_tensor(output)

    def fmin(self, other):
        fmin_op = numpy_cell.NumpyFmin('fmin')
        output = fmin_op(self, other)
        return cast_to_adapter_tensor(output)

    def multiply(self, value):
        x = cast_to_ms_tensor(self)
        y = cast_to_ms_tensor(value)
        output = ms.ops.mul(x, y)
        return cast_to_adapter_tensor(output)

    def multiply_(self, value):
        output = self.multiply(value)
        return _tensor_inplace_assign(self, output, "multiply_", "multiply")

    def neg(self):
        x = cast_to_ms_tensor(self)
        output = ms.ops.neg(x)
        return cast_to_adapter_tensor(output)

    def neg_(self):
        output = self.neg()
        return _tensor_inplace_assign(self, output, "neg_", "neg")

    def ravel(self):
        x = cast_to_ms_tensor(self)
        output = x.ravel()
        return cast_to_adapter_tensor(output)

    def select(self, dim, index):
        input_ms = cast_to_ms_tensor(self)
        _input_indices = ms.Tensor(index)
        output = ms.ops.gather(input_ms, _input_indices, dim)
        output_shape = _get_select_out_shape(input_ms.shape, dim)
        output = output.reshape(output_shape)
        return cast_to_adapter_tensor(output)

    def square(self):
        x = cast_to_ms_tensor(self)
        output = ms.ops.square(x)
        return cast_to_adapter_tensor(output)

    def square_(self):
        output = self.square()
        return _tensor_inplace_assign(self, output, "square_", "square")

    def broadcast_to(self, shape):
        input_ms = cast_to_ms_tensor(self)
        if isinstance(shape, list):
            shape = tuple(shape)
        output = ms.ops.broadcast_to(input_ms, shape)
        return cast_to_adapter_tensor(output)

    def divide(self, value, *, rounding_mode=None) :
        output = self.div(value, rounding_mode=rounding_mode)
        return cast_to_adapter_tensor(output)

    def divide_(self, value, *, rounding_mode=None) :
        output = self.div(value, rounding_mode=rounding_mode)
        return _tensor_inplace_assign(self, output, "divide_", "divide")

    def unique(self, sorted=True, return_inverse=False, return_counts=False, dim=None):
        unsupported_attr(dim)
        unsupported_attr(return_counts)
        input_ms = cast_to_ms_tensor(self)
        data_type = input_ms.dtype
        if sorted and return_inverse:
            raise ValueError("Don't support sorted=True and return_inverse=True.")

        res, idx = ms.ops.unique(input_ms)
        if sorted:
            res = ms.ops.cast(res, ms.float32)
            res, _ = ms.ops.sort(res)
            res = ms.ops.cast(res, data_type)
        if return_inverse:
            res = cast_to_adapter_tensor(res)
            idx = cast_to_adapter_tensor(idx)
            return (res, idx)
        else:
            res = cast_to_adapter_tensor(res)
            return res

    def mm(self, mat2):
        input_ms = cast_to_ms_tensor(self)
        input2 = cast_to_ms_tensor(mat2)
        input_type = input_ms.dtype
        if input_type in all_int_type and is_under_gpu_context():
            input_ms = input_ms.astype(mstype.float32)
            input2 = input2.astype(mstype.float32)
            # TODO: repalce with output = ms.ops.matmul(input_ms, input2)
            output = custom_matmul(input_ms, input2)
            output = ms.ops.cast(output, input_type)
        else:
            # TODO: repalce with output = ms.ops.matmul(input_ms, input2)
            output = custom_matmul(input_ms, input2)
        return cast_to_adapter_tensor(output)

    def logsumexp(self, dim, keepdim=False):
        ms_input = cast_to_ms_tensor(self)
        if ms_input.dtype != mstype.float32:
            ms_input = ms_input.astype(mstype.float32)
        output = ms.ops.logsumexp(ms_input, dim, keepdim)
        return cast_to_adapter_tensor(output)

    def addmv(self, mat, vec, *, beta=1, alpha=1):
        input_ms = cast_to_ms_tensor(self)
        mat = cast_to_ms_tensor(mat)
        vec = cast_to_ms_tensor(vec)
        output = ms.ops.addmv(input_ms, mat, vec, beta=beta, alpha=alpha)
        return cast_to_adapter_tensor(output)

    def addmv_(self, mat, vec, *, beta=1, alpha=1):
        output = self.addmv(mat, vec, beta=beta, alpha=alpha)
        return _tensor_inplace_assign(self, output, "addmv_", "addmv")

    def dot(self, other):
        input_ms = cast_to_ms_tensor(self)
        other = cast_to_ms_tensor(other)
        #TODO: ms.ops.tensor_dot only supports float16/float32
        input_dtype = input_ms.dtype
        if input_dtype in (mstype.float32, mstype.float16):
            output = ms.ops.tensor_dot(input_ms, other, 1)
        else:
            input_ms = input_ms.astype(ms.float32)
            other = other.astype(ms.float32)
            output = ms.ops.tensor_dot(input_ms, other, 1)
            output = output.astype(input_dtype)
        return cast_to_adapter_tensor(output)

    def inverse(self):
        input_ms = cast_to_ms_tensor(self)
        if self.dtype in msdapter_dtype.all_int_type:
            input_ms = input_ms.astype(mstype.float32)
        output = ms.ops.inverse(input_ms)
        return cast_to_adapter_tensor(output)

    def asin(self):
        input_ms = cast_to_ms_tensor(self)
        if self.dtype in msdapter_dtype.all_int_type:
            input_ms = input_ms.astype(mstype.float32)
        output = ms.ops.asin(input_ms)
        return cast_to_adapter_tensor(output)

    def asin_(self):
        output = self.asin()
        return _tensor_inplace_assign(self, output, "asin_", "asin")

    def atan(self):
        input_ms = cast_to_ms_tensor(self)
        if input_ms.dtype in all_int_type:
            input_ms = input_ms.astype(mstype.float32)
        output = ms.ops.atan(input_ms)
        return cast_to_adapter_tensor(output)

    def atan_(self):
        output = self.atan()
        return _tensor_inplace_assign(self, output, "atan_", "atan")

    def atan2(self, other):
        input_ms = cast_to_ms_tensor(self)
        other = cast_to_ms_tensor(other)
        if input_ms.dtype in all_int_type:
            input_ms = input_ms.astype(mstype.float32)
            other = other.astype(mstype.float32)
        output = ms.ops.atan2(input_ms, other)
        return cast_to_adapter_tensor(output)

    def atan2_(self, other):
        output = self.atan2(other)
        return _tensor_inplace_assign(self, output, "atan2_", "atan2")


    def count_nonzero(self, dim=None):
        input_ms = cast_to_ms_tensor(self)
        if dim is None:
            dim = ()
        output = ms.ops.count_nonzero(input_ms, dim)
        return cast_to_adapter_tensor(output)

    def scatter(self, dim, index, src, reduce=None):
        if not reduce:
            reduce = 'none'
        else:
            # TODO: to supported 'multiply'
            if reduce not in ('none', 'add'):
                raise ValueError("For tensor.scatter or scatter_, `reduce` only support 'none', "
                                 f"'add', but got '{reduce}'.")

            # TODO: add not supported on Ascend yet
            if reduce == 'add' and is_under_ascend_context():
                raise NotImplementedError("For tensor.scatter or scatter_, `reduce` == 'add' not supported on Ascend")

        input_ms, index, src = cast_to_ms_tensor((self, index, src))

        if isinstance(src, numbers.Number):
            src = ms.ops.scalar_to_tensor(src, dtype=input_ms.dtype)
            src = ms.ops.broadcast_to(src, index.shape)
        elif isinstance(src, ms.Tensor):
            src_shape = src.shape
            index_shape = index.shape
            if src_shape != index_shape:
                # TODO
                raise NotImplementedError("For scatter, not support src.shape != index.shape yet")
        else:
            raise TypeError(f"For scatter, `src` must be number or tensor, but got {type(src)}")

        if is_under_ascend_context():
            input_dtype = input_ms.dtype
            input_ms = _ascend_tensor_general_cast(input_ms)
            src = _ascend_tensor_general_cast(src)
            output = ms.ops.tensor_scatter_elements(input_ms, index, src, dim, reduce)
            output = output.astype(input_dtype)
        else:
            output = ms.ops.tensor_scatter_elements(input_ms, index, src, dim, reduce)

        return cast_to_adapter_tensor(output)

    def scatter_(self, dim, index, src, reduce=None):
        output = self.scatter(dim, index, src, reduce)
        return _tensor_inplace_assign(self, output, "scatter_", "scatter")

    def acosh(self):
        input_ms = cast_to_ms_tensor(self)
        if input_ms.dtype in all_int_type:
            input_ms = input_ms.astype(mstype.float32)
        output = ms.ops.acosh(input_ms)
        return cast_to_adapter_tensor(output)

    def acosh_(self):
        output = self.acosh()
        return _tensor_inplace_assign(self, output, "acosh_", "acosh")

    def new_ones(self, *size, dtype=None, device=None, requires_grad=False, layout=None, pin_memory=False):
        unsupported_attr(device)
        unsupported_attr(requires_grad)
        unsupported_attr(layout)
        unsupported_attr(pin_memory)

        if dtype is None:
            dtype = self.dtype

        if isinstance(size[0], (tuple, list)):
            output = ms.ops.ones(*size, dtype=dtype)
        else:
            output = ms.ops.ones(size, dtype=dtype)

        return cast_to_adapter_tensor(output)

    def new_empty(self, *size, dtype=None, layout=None,
                  device=None, requires_grad=False, pin_memory=False,
                  memory_format=None):
        unsupported_attr(layout)
        unsupported_attr(device)
        unsupported_attr(requires_grad)
        unsupported_attr(pin_memory)
        unsupported_attr(memory_format)
        if dtype is None:
            dtype = self.dtype

        _size = size
        if isinstance(size[0], (tuple, list)):
            _size = size[0]
        output = ms.numpy.empty(_size, dtype)
        return cast_to_adapter_tensor(output)

    def addcmul(self, tensor1, tensor2, *, value=1):
        #Todo: use ms.ops.addcmul after it has been fixed
        input_ms = cast_to_ms_tensor(self)
        tensor1 = cast_to_ms_tensor(tensor1)
        tensor2 = cast_to_ms_tensor(tensor2)
        if is_under_ascend_context():
            value = ms.Tensor(value).astype(input_ms.dtype)
        output = ms.ops.addcmul(input_ms, tensor1, tensor2, value)
        return cast_to_adapter_tensor(output)

    def addcmul_(self, tensor1, tensor2, *, value=1):
        output = self.addcmul(tensor1, tensor2, value=value)
        return _tensor_inplace_assign(self, output, "addcmul_", "addcmul")

    def arccosh(self):
        return self.acosh()

    def arccosh_(self):
        output = self.acosh()
        return _tensor_inplace_assign(self, output, "arccosh_", "arccosh")

    def arcsin(self):
        return self.asin()

    def arcsin_(self):
        output = self.asin()
        return _tensor_inplace_assign(self, output, "arcsin_", "arcsin")

    def arctan(self):
        return self.atan()

    def arctan_(self):
        output = self.atan()
        return _tensor_inplace_assign(self, output, "arctan_", "arctan")

    def arctan2(self, other):
        input_ms = cast_to_ms_tensor(self)
        other = cast_to_ms_tensor(other)
        if input_ms.dtype in all_int_type:
            input_ms = input_ms.astype(mstype.float32)
        if other.dtype in all_int_type:
            other = other.astype(mstype.float32)
        output = ms.ops.atan2(input_ms, other)
        return cast_to_adapter_tensor(output)

    def arctan2_(self, other):
        output = self.arctan2(other)
        return _tensor_inplace_assign(self, output, "arctan2_", "arctan2")

    def bitwise_not(self):
        input_ms = cast_to_ms_tensor(self)
        type = input_ms.dtype
        if str(type) != 'Bool':
            output = 0 - input_ms - 1
        else:
            output = 1 - input_ms
            output = output.astype(ms.bool_)
        return cast_to_adapter_tensor(output)

    def bitwise_not_(self):
        output = self.bitwise_not(self)
        return _tensor_inplace_assign(self, output, "bitwise_not_", "bitwise_not")

    def bitwise_and(self, other):
        input_ms = cast_to_ms_tensor(self)
        other = cast_to_ms_tensor(other)
        #TODO: currently bitwise operations on Ascend not support bool type
        if is_under_ascend_context():
            input_ms, other, output_dtype = bitwise_adapter(input_ms, other)
            output = ms.ops.bitwise_and(input_ms, other)
            output = output.astype(output_dtype)
        else:
            output = ms.ops.bitwise_and(input_ms, other)
        return cast_to_adapter_tensor(output)

    def bitwise_and_(self, other):
        output = self.bitwise_and(other)
        return _tensor_inplace_assign(self, output, "bitwise_and_", "bitwise_and")

    def bitwise_or(self, other):
        input_ms = cast_to_ms_tensor(self)
        other = cast_to_ms_tensor(other)
        #TODO: currently bitwise operations on Ascend not support bool type
        if is_under_ascend_context():
            input_ms, other, output_dtype = bitwise_adapter(input_ms, other)
            output = ms.ops.bitwise_or(input_ms, other)
            output = output.astype(output_dtype)
        else:
            output = ms.ops.bitwise_or(input_ms, other)
        return cast_to_adapter_tensor(output)

    def bitwise_or_(self, other):
        output = self.bitwise_or(other)
        return _tensor_inplace_assign(self, output, "bitwise_or_", "bitwise_or")

    def bitwise_xor(self, other):
        input_ms = cast_to_ms_tensor(self)
        other = cast_to_ms_tensor(other)
        #TODO: currently bitwise operations on Ascend not support bool type
        if is_under_ascend_context():
            input_ms, other, output_dtype = bitwise_adapter(input_ms, other)
            output = ms.ops.bitwise_xor(input_ms, other)
            output = output.astype(output_dtype)
        else:
            output = ms.ops.bitwise_xor(input_ms, other)
        return cast_to_adapter_tensor(output)

    def bitwise_xor_(self, other):
        output = self.bitwise_xor(other)
        return _tensor_inplace_assign(self, output, "bitwise_xor_", "bitwise_xor")

    def addbmm(self, batch1, batch2, *, beta=1, alpha=1):
        _input, _batch1, _batch2 = cast_to_ms_tensor((self, batch1, batch2))
        output = ms.ops.addbmm(_input, _batch1, _batch2, beta=beta, alpha=alpha)
        return cast_to_adapter_tensor(output)

    def addbmm_(self, batch1, batch2, *, beta=1, alpha=1):
        output = self.addbmm(batch1, batch2, beta=beta, alpha=alpha)
        return _tensor_inplace_assign(self, output, "addbmm_", "addbmm")

    def addmm(self, mat1, mat2, *, beta=1, alpha=1):
        _input, _mat1, _mat2 = cast_to_ms_tensor((self, mat1, mat2))
        output = ms.ops.addmm(_input, _mat1, _mat2, beta=beta, alpha=alpha)
        return cast_to_adapter_tensor(output)

    def addmm_(self, mat1, mat2, *, beta=1, alpha=1):
        output = self.addmm(mat1, mat2, beta=beta, alpha=alpha)
        return _tensor_inplace_assign(self, output, "addmm_", "addmm")

    def addr(self, vec1, vec2, *, beta=1, alpha=1):
        _input, _vec1, _vec2 = cast_to_ms_tensor((self, vec1, vec2))
        output = ms.ops.addr(_input, _vec1, _vec2, beta=beta, alpha=alpha)
        return cast_to_adapter_tensor(output)

    def addr_(self, vec1, vec2, *, beta=1, alpha=1):
        output = self.addr(vec1, vec2, beta=beta, alpha=alpha)
        return _tensor_inplace_assign(self, output, "addr_", "addr")

    def all(self, dim=(), keepdim=False):
        input_ms = cast_to_ms_tensor(self)
        # tensor.all only support bool dtype
        output = ms.ops.all(input_ms, axis=dim, keep_dims=keepdim)
        return cast_to_adapter_tensor(output)

    def isclose(self, other, rtol=1e-05, atol=1e-08, equal_nan=False):
        _input, _other = cast_to_ms_tensor((self, other))
        output = ms.ops.isclose(_input, _other, rtol=rtol, atol=atol, equal_nan=equal_nan)
        return cast_to_adapter_tensor(output)

    def allclose(self, other, rtol=1e-05, atol=1e-08, equal_nan=False):
        output = self.isclose(other, rtol=rtol, atol=atol, equal_nan=equal_nan)
        output = output.all()
        return output.item()

    def cholesky(self, upper=False):
        input_ms = cast_to_ms_tensor(self)
        output = input_ms.cholesky(upper)
        return cast_to_adapter_tensor(output)

    def cholesky_inverse(self, upper=False):
        input_ms = cast_to_ms_tensor(self)
        # TODO: ms.tensor.cholesky_inverse not support GPU.
        output = input_ms.cholesky_inverse(upper)
        return cast_to_adapter_tensor(output)

    def cholesky_solve(self, input2, upper=False):
        input_ms = cast_to_ms_tensor(self)
        input2 = cast_to_ms_tensor(input2)
        output = ms.ops.cholesky_solve(input_ms, input2, upper)
        return cast_to_adapter_tensor(output)

    def nelement(self):
        input_ms = cast_to_ms_tensor(self)
        output = input_ms.nelement()
        return output

    def aminmax(self, *, dim=None, keepdim=False):
        _input = cast_to_ms_tensor(self)
        _min = _input.min(axis=dim, keepdims=keepdim)
        _max = _input.max(axis=dim, keepdims=keepdim)
        return cast_to_adapter_tensor((_min, _max))

    def any(self, dim=(), keepdim=False):
        input_ms = cast_to_ms_tensor(self)
        if input_ms.dtype != ms.bool_:
            input_ms = input_ms.astype(ms.bool_)
        output = input_ms.any(axis=dim, keep_dims=keepdim)
        return cast_to_adapter_tensor(output)

    def bincount(self, weights=None, minlength=0):
        input_ms = cast_to_ms_tensor(self)
        type = 'int64'
        if input_ms.dtype == ms.uint8:
            input_ms = input_ms.astype(ms.int16)
        if weights is not None:
            weights = cast_to_ms_tensor(weights)
            type = weights.dtype
        output = ms.ops.bincount(input_ms, weights, minlength).astype(type)
        return cast_to_adapter_tensor(output)

    def bitwise_left_shift(self, other):
        input_ms = cast_to_ms_tensor(self)
        other = cast_to_ms_tensor(other)
        output = ms.ops.bitwise_left_shift(input_ms, other)
        return cast_to_adapter_tensor(output)

    def bitwise_left_shift_(self, other):
        output = self.bitwise_left_shift(other)
        return _tensor_inplace_assign(self, output, "bitwise_left_shift_", "bitwise_left_shift")

    def bitwise_right_shift(self, other):
        input_ms = cast_to_ms_tensor(self)
        other = cast_to_ms_tensor(other)
        output = ms.ops.bitwise_right_shift(input_ms, other)
        return cast_to_adapter_tensor(output)

    def bitwise_right_shift_(self, other):
        output = self.bitwise_right_shift(other)
        return _tensor_inplace_assign(self, output, "bitwise_right_shift_", "bitwise_right_shift")

    def clip(self, min=None, max=None):
        input_ms = cast_to_ms_tensor(self)
        output = input_ms.clip(min, max)
        return cast_to_adapter_tensor(output)

    def clip_(self, min=None, max=None):
        output = self.clip(min=min, max=max)
        return _tensor_inplace_assign(self, output, "clip_", "clip")

    def copysign(self, other):
        input_ms = cast_to_ms_tensor(self)
        input_type = input_ms.dtype
        is_num = True
        # for graph
        other_type = None
        if isinstance(other, Tensor):
            is_num = False
            other = cast_to_ms_tensor(other)
            other_type = other.dtype
            #TODO: currently the prim[Tile] has problem broadcasting
            if input_ms.ndim < other.ndim:
                input_ms = ms.ops.broadcast_to(input_ms, other.shape)
            if other.ndim < input_ms.ndim:
                other = ms.ops.broadcast_to(other, input_ms.shape)
        output = ms.ops.copysign(input_ms, other)
        if 'Int' in str(input_type):
            if is_num or 'Int' in str(other_type):
                output = output.astype(ms.float32)
            else:
                output = output.astype(other_type)
        elif is_num or 'Int' in str(other_type):
            output = output.astype(input_type)
        else:
            type1 = input_type if input_ms.itemsize > other.itemsize else other_type
            output = output.astype(type1)
        return cast_to_adapter_tensor(output)

    def copysign_(self, other):
        output = self.copysign(other)
        return _tensor_inplace_assign(self, output, "copysign_", "copysign")

    def cos(self):
        input_ms = cast_to_ms_tensor(self)
        output = ms.ops.cos(input_ms)
        return cast_to_adapter_tensor(output)

    def cos_(self):
        output = self.cos()
        return _tensor_inplace_assign(self, output, "cos_", "cos")

    def cosh(self):
        input_ms = cast_to_ms_tensor(self)
        output = ms.ops.cosh(input_ms)
        return cast_to_adapter_tensor(output)

    def cosh_(self):
        output = self.cosh()
        return _tensor_inplace_assign(self, output, "cosh_", "cosh")

    def cummax(self, dim):
        input_ms = cast_to_ms_tensor(self)
        output = ms.ops.cummax(input_ms, axis=dim)
        return cast_to_adapter_tensor(output)

    def cummin(self, dim):
        input_ms = cast_to_ms_tensor(self)
        output = ms.ops.cummin(input_ms, dim)
        # the output dtype in ms.ops.cummin is different with ms.ops.cummax
        output[1] = output[1].astype(ms.common.dtype.int64)
        return cast_to_adapter_tensor(output)

    def cumprod(self, dim, *, dtype=None):
        input_ms = cast_to_ms_tensor(self)
        output = ms.ops.cumprod(input_ms, dim, dtype=dtype)
        return cast_to_adapter_tensor(output)

    def cumprod_(self, dim, *, dtype=None):
        output = self.cumprod(dim, dtype=dtype)
        return _tensor_inplace_assign(self, output, "cumprod_", "cumprod")

    def deg2rad(self):
        input_ms = cast_to_ms_tensor(self)
        if input_ms.dtype not in (ms.float16, ms.float32, ms.float64):
            input_ms = input_ms.astype(ms.float32)
        output = ms.ops.deg2rad(input_ms)
        return cast_to_adapter_tensor(output)

    def diag(self, diagonal=0):
        # TODO
        # May be use mindspore.ops.diag instead. Nowadays, this operator do not support CPU.
        # ms.numpy.diag has bug on ascend, use ms.ops.diag for diagonal=None and 1D input
        input_ms = cast_to_ms_tensor(self)
        if is_under_ascend_context() and input_ms.ndim == 1 and diagonal == 0:
            output = ms.ops.diag(input_ms)
        else:
            output =  ms.numpy.diag(input_ms, diagonal)
        return cast_to_adapter_tensor(output)

    def diagflat(self, offset=0):
        input_ms = cast_to_ms_tensor(self)
        output = ms.ops.diagflat(input_ms, offset)
        return cast_to_adapter_tensor(output)

    def diagonal(self, offset=0, dim1=0, dim2=1):
        input_ms = cast_to_ms_tensor(self)
        #TODO float64 not support if offset != 0
        if offset != 0:
            input_ms = input_ms.astype(mstype.float32)
        output = ms.ops.diagonal(input_ms, offset, dim1, dim2)
        return cast_to_adapter_tensor(output)

    def is_complex(self):
        input_ms = cast_to_ms_tensor(self)
        return input_ms.is_complex()

    def isinf(self):
        input_ms = cast_to_ms_tensor(self)
        output = ms.ops.isinf(input_ms)
        return cast_to_adapter_tensor(output)

    def isneginf(self):
        input_ms = cast_to_ms_tensor(self)
        output = ms.ops.isneginf(input_ms)
        return cast_to_adapter_tensor(output)

    def isposinf(self):
        input_ms = cast_to_ms_tensor(self)
        output = ms.ops.isposinf(input_ms)
        return cast_to_adapter_tensor(output)

    def isreal(self):
        input_ms = cast_to_ms_tensor(self)
        output = ms.ops.isreal(input_ms)
        return cast_to_adapter_tensor(output)

    def var(self, dim=None, unbiased=True, keepdim=False):
        #2.0  Tensor.var(dim=None, *, correction=1, keepdim=False)
        #1.12 Tensor.var(dim, unbiased=True, keepdim=False)
        #1.12 Tensor.var(unbiased=True)
        if dim is not None and isinstance(dim, bool):
            raise TypeError("var() received an invalid combination of arguments: got (dim=bool)," +
                            "but expected one of: (tuple of ints dim, bool unbiased, bool keepdim)")
        input_ms = cast_to_ms_tensor(self)
        #ms.ops.var unsupport ddof=0/1 on GPU
        ddof = 1 if unbiased is True else 0
        output = input_ms.var(axis=dim, ddof=ddof, keepdims=keepdim)
        return cast_to_adapter_tensor(output)

    def diff(self, n=1, dim=-1, prepend=None, append=None):
        input_ms = cast_to_ms_tensor(self)
        #TODO: ms.ops.diff only support n=1
        if n == 1:
            output = ms.ops.diff(input_ms, n, dim, prepend, append)
        else:
            output = ms.numpy.diff(input_ms, n, dim, prepend, append)
        return cast_to_adapter_tensor(output)

    def digamma(self):
        # TODO: When input dtype is float64, result may be inaccurate
        input_ms = cast_to_ms_tensor(self)
        output = ms.ops.digamma(input_ms)
        return cast_to_adapter_tensor(output)

    def digamma_(self):
        output = self.digamma()
        return _tensor_inplace_assign(self, output, "digamma_", "digamma")

    #TODO: eig currently not support on GPU
    def eig(self):
        if is_under_gpu_context():
            raise NotImplementedError("for adapter, eig not supported on GPU")
        input_ms = cast_to_ms_tensor(self)
        output = ms.ops.eig(input_ms)
        return cast_to_adapter_tensor(output)

    def dist(self, other, p=2):
        _input = cast_to_ms_tensor(self)
        _other = cast_to_ms_tensor(other)

        _input_dtype = _input.dtype
        _other_dtype = _other.dtype
        if _input_dtype in (ms.float16, ms.float32) and _other_dtype != ms.float64:
            if _other_dtype == ms.float32:
                _input = _input.astype(_other_dtype)
            else:
                _other = _other.astype(_input_dtype)
            output = ms.ops.dist(_input, _other, p=p)
        elif _input_dtype == ms.float64 or _other_dtype == ms.float64:
            _input = _input.astype(ms.float32)
            _other = _other.astype(ms.float32)
            output = ms.ops.dist(_input, _other, p=p)
            output = output.astype(ms.float64)
        else:
            raise ValueError(f"For torch.dist, input should be floating Tensor, but got {_input_dtype}.")

        return cast_to_adapter_tensor(output)

    def dsplit(self, indices_or_sections):
        input_ms = cast_to_ms_tensor(self)
        output = ms.ops.dsplit(input_ms, indices_or_sections)
        return cast_to_adapter_tensor(output)

    def erf(self):
        input_ms = cast_to_ms_tensor(self)
        output = ms.ops.erf(input_ms)
        return cast_to_adapter_tensor(output)

    def erf_(self):
        output = self.erf()
        return _tensor_inplace_assign(self, output, "erf_", "erf")

    def erfc(self):
        input_ms = cast_to_ms_tensor(self)
        output = ms.ops.erfc(input_ms)
        return cast_to_adapter_tensor(output)

    def erfc_(self):
        output = self.erfc()
        return _tensor_inplace_assign(self, output, "erfc_", "erfc")

    def expm1(self):
        input_ms = cast_to_ms_tensor(self)
        output = ms.ops.expm1(input_ms)
        return cast_to_adapter_tensor(output)

    def expm1_(self):
        output = self.expm1()
        return _tensor_inplace_assign(self, output, "expm1_", "expm1")

    def trunc(self):
        input_ms = cast_to_ms_tensor(self)
        output = ms.ops.trunc(input_ms)
        return cast_to_adapter_tensor(output)

    def trunc_(self):
        output = self.trunc()
        return _tensor_inplace_assign(self, output, "trunc_", "trunc")

    def fix(self):
        return self.trunc()

    def fix_(self):
        output = self.fix()
        return _tensor_inplace_assign(self, output, "fix_", "fix")

    def fliplr(self):
        input_ms = cast_to_ms_tensor(self)
        output = ms.ops.fliplr(input_ms)
        return cast_to_adapter_tensor(output)

    def float_power(self, exponent):
        # TODO: not support complex input and exponent now
        input_ms = cast_to_ms_tensor(self)
        output = ms.ops.float_power(input_ms, exponent)
        return cast_to_adapter_tensor(output)

    def float_power_(self, exponent):
        output = self.float_power(exponent)
        return _tensor_inplace_assign(self, output, "float_power_", "float_power")

    def narrow(self, dimension, start, length):
        input_ms = cast_to_ms_tensor(self)

        def _get_tensor_data(x):
            if isinstance(x, Tensor):
                if x.ndim != 0:
                    raise ValueError("it must be an 0-dim integral Tensor.")
                return int(x)
            return x

        dimension = _get_tensor_data(dimension)
        start = _get_tensor_data(start)
        length = _get_tensor_data(length)
        output = ms.ops.narrow(input_ms, dimension, start, length)
        return cast_to_adapter_tensor(output)

    def narrow_copy(self, dimension, start, length):
        input_ms = cast_to_ms_tensor(self)
        output = ms.ops.narrow(input_ms, dimension, start, length)
        return cast_to_adapter_tensor(output)

    def norm(self, p='fro', dim=None, keepdim=False, dtype=None):
        # TODO: ms.ops.norm benchmarking torch.linalg.norm. some matrix-norm result not right.
        # `p` can not support value beside ['fro', 'nuc', inf, -inf, 0, 1, -1, 2, -2]
        warning("`torch.norm` or `tensor.norm` is deprecated, please use `linalg.vector_norm()` "
                "or `linalg.matrix_norm()` instead.")
        p = _norm_get_const(p, dim, len(self.shape))
        input_ms = cast_to_ms_tensor(self)
        output = ms.ops.norm(input_ms, ord=p, dim=dim, keepdim=keepdim)
        if dtype:
            output = output.astype(dtype)
        return cast_to_adapter_tensor(output)

    def xlogy(self, other):
        input_ms = cast_to_ms_tensor(self)
        other = cast_to_ms_tensor(other)
        # TODO: To support more datatype on Ascend
        output = ms.ops.xlogy(input_ms, other)
        if is_under_gpu_context() or is_under_ascend_context():
            if isinstance(input_ms, ms.Tensor) and isinstance(other, ms.Tensor):
                mask = ms.ops.isnan(other)
                output = ms.ops.where(mask, ms.Tensor(float('nan')).astype(output.dtype), output)
            elif not isinstance(input_ms, ms.Tensor):
                output = ms.ops.where((other < 0), ms.Tensor(float('nan')).astype(output.dtype), output)
        return cast_to_adapter_tensor(output)

    def xlogy_(self, other):
        output = self.xlogy(other)
        return _tensor_inplace_assign(self, output, "xlogy_", "xlogy")

    def vsplit(self, indices_or_sections):
        input_ms = cast_to_ms_tensor(self)
        output = ms.ops.vsplit(input_ms, indices_or_sections)
        return cast_to_adapter_tensor(output)

    def vdot(self, other):
        if not isinstance(other, Tensor):
            raise TypeError(f"For Tensor.vdot, other must be tensor, but got {type(other)}")
        if self.dtype != other.dtype:
            raise RuntimeError(f"For Tensor.vdot, expected both vectors to have same dtype, but found {self.dtype}"
                               f" and {other.dtype}")
        if self.ndim != 1 or other.ndim != 1:
            raise RuntimeError(f"For Tensor.vdot, 1D tensors expected, but got {self.ndim}D and {other.ndim}D tensors")
        input_ms = cast_to_ms_tensor(self)
        other = cast_to_ms_tensor(other)
        if input_ms.is_complex():
            input_ms = ms.ops.conj(input_ms)
        if (is_under_gpu_context() and (input_ms.dtype in all_int_type)) or \
            (is_under_ascend_context() and (input_ms.dtype in (ms.float64,) + all_int_type)):
            warning("For vdot, input_ms with int64 type has risk of being truncated.")
            input_dtype = input_ms.dtype
            input_ms = input_ms.astype(ms.float32)
            other = other.astype(ms.float32)
            output = ms.ops.inner(input_ms, other).astype(input_dtype)
        else:
            output = ms.ops.inner(input_ms, other)
        return cast_to_adapter_tensor(output)

    def where(self, condition, y):
        x = cast_to_ms_tensor(self)
        y = cast_to_ms_tensor(y)
        output = ms.ops.where(condition, x, y)
        return cast_to_adapter_tensor(output)

    def true_divide(self, divisor):
        input_ms = cast_to_ms_tensor(self)
        other = cast_to_ms_tensor(divisor)
        if not input_ms.is_floating_point():
            if isinstance(other, ms.Tensor):
                if not other.is_floating_point():
                    input_ms = input_ms.astype(ms.float32)

            elif not isinstance(other, float):
                input_ms = input_ms.astype(ms.float32)

        output = ms.ops.true_divide(input_ms, other)
        return cast_to_adapter_tensor(output)

    def true_divide_(self, divisor):
        output = self.true_divide(divisor)
        return _tensor_inplace_assign(self, output, "true_divide_", "true_divide")

    def triu(self, diagonal=0):
        input_ms = cast_to_ms_tensor(self)
        # TODO: To use ms.ops.triu after it supported on Ascend
        output = ms.numpy.triu(input_ms, diagonal)
        return cast_to_adapter_tensor(output)

    def triu_(self, diagonal=0):
        output = self.triu(diagonal)
        return _tensor_inplace_assign(self, output, "triu_", "triu")

    def tril(self, diagonal=0):
        input_ms = cast_to_ms_tensor(self)
        output = ms.ops.tril(input_ms, diagonal)
        return cast_to_adapter_tensor(output)

    def tril_(self, diagonal=0):
        output = self.tril(diagonal)
        return _tensor_inplace_assign(self, output, "tril_", "tril")

    def nanmean(self, dim=None, keepdim=False, *, dtype=None):
        input_ms = cast_to_ms_tensor(self)
        output = ms.ops.nanmean(input_ms, dim, keepdim, dtype=dtype)
        return cast_to_adapter_tensor(output)

    def nansum(self, dim=None, keepdim=False, dtype=None):
        input_ms = cast_to_ms_tensor(self)
        output = ms.ops.nansum(input_ms, dim, keepdim, dtype=dtype)
        return cast_to_adapter_tensor(output)

    def heaviside(self, values):
        input_ms = cast_to_ms_tensor(self)
        return cast_to_adapter_tensor(input_ms.heaviside(values))

    def flipud(self):
        input_ms = cast_to_ms_tensor(self)
        output = ms.ops.flipud(input_ms)
        return cast_to_adapter_tensor(output)

    def tile(self, *reps):
        # TODO: ms.ops.tile to support the len of `multiples` to be less than input.ndim.
        if isinstance(reps[0], (tuple, list)):
            reps = tuple(reps[0])
        new_reps = (1,) * (self.ndim - len(reps)) + reps
        reps = new_reps

        input_ms = cast_to_ms_tensor(self)
        if is_under_gpu_context and input_ms.dtype == ms.uint8:
            input_ms = input_ms.astype(ms.float32)
            output = ms.ops.tile(input_ms, reps).astype(ms.uint8)
        else:
            output = ms.ops.tile(input_ms, reps)
        return cast_to_adapter_tensor(output)

    def unique_consecutive(self, return_inverse=False, return_counts=False, dim=None):
        input_ms = cast_to_ms_tensor(self)
        output = ms.ops.unique_consecutive(input_ms, return_idx=return_inverse, return_counts=return_counts, axis=dim)
        return cast_to_adapter_tensor(output)

    def tanh(self):
        input_ms = cast_to_ms_tensor(self)
        input_dtype = input_ms.dtype
        if input_dtype not in all_float_and_complex_type:
            input_ms = input_ms.astype(ms.float32)
        output = ms.ops.tanh(input_ms)
        return cast_to_adapter_tensor(output)

    def tanh_(self):
        output = self.tanh()
        return _tensor_inplace_assign(self, output, "tanh_", "tanh")

    def tan(self):
        input_ms = cast_to_ms_tensor(self)
        if not input_ms.is_floating_point():
            input_ms = input_ms.astype(ms.float32)
        output = ms.ops.tan(input_ms)
        return cast_to_adapter_tensor(output)

    def tan_(self):
        output = self.tan()
        return _tensor_inplace_assign(self, output, "tan_", "tan")

    def tensor_split(self, indices_or_sections, dim=0):
        input_ms = cast_to_ms_tensor(self)
        output = ms.ops.tensor_split(input_ms, indices_or_sections, axis=dim)
        return cast_to_adapter_tensor(output)

    def take(self, index):
        input_ms = cast_to_ms_tensor(self)
        index = cast_to_ms_tensor(index)
        output = input_ms.take(index)
        return cast_to_adapter_tensor(output)

    def take_along_dim(self, indices, dim=None):
        input_ms = cast_to_ms_tensor(self)
        indices = cast_to_ms_tensor(indices)

        if not dim:
            input_ms = input_ms.reshape(-1)
            dim = 0

        output = ms.ops.gather_d(input_ms, dim, indices)
        return cast_to_adapter_tensor(output)

    def sinc(self):
        input_ms = cast_to_ms_tensor(self)
        output = ms.ops.sinc(input_ms)
        return cast_to_adapter_tensor(output)

    def sinc_(self):
        output = self.sinc()
        return _tensor_inplace_assign(self, output, "sinc_", "sinc")

    def sinh(self):
        input_ms = cast_to_ms_tensor(self)
        output = ms.ops.sinh(input_ms)
        return cast_to_adapter_tensor(output)

    def sinh_(self):
        output = self.sinh()
        return _tensor_inplace_assign(self, output, "sinh_", "sinh")


    def hardshrink(self, lambd=0.5):
        # support only float16 and float32
        input_ms = cast_to_ms_tensor(self)
        output = ms.ops.hardshrink(input_ms, lambd)
        return cast_to_adapter_tensor(output)

    def hsplit(self, split_size_or_sections):
        input_ms = cast_to_ms_tensor(self)
        output = ms.ops.hsplit(input_ms, split_size_or_sections)
        return cast_to_adapter_tensor(output)

    def hypot(self, other):
        input_ms = cast_to_ms_tensor(self)
        other_ms = cast_to_ms_tensor(other)
        output = ms.ops.hypot(input_ms, other_ms)
        return cast_to_adapter_tensor(output)

    def hypot_(self, other):
        output = self.hypot(other)
        return _tensor_inplace_assign(self, output, "hypot_", "hypot")

    def log10(self):
        input_ms = cast_to_ms_tensor(self)
        output = ms.ops.log10(input_ms)
        return cast_to_adapter_tensor(output)

    def log10_(self):
        output = self.log10()
        return _tensor_inplace_assign(self, output, "log10_", "log10")

    def log1p(self):
        input_ms = cast_to_ms_tensor(self)
        output = ms.ops.log1p(input_ms)
        return cast_to_adapter_tensor(output)

    def log1p_(self):
        output = self.log1p()
        return _tensor_inplace_assign(self, output, "log1p_", "log1p")

    def logaddexp(self, other):
        input_ms = cast_to_ms_tensor(self)
        other_ms = cast_to_ms_tensor(other)
        output = ms.ops.logaddexp(input_ms, other_ms)
        return cast_to_adapter_tensor(output)

    def logdet(self):
        input_ms = cast_to_ms_tensor(self)
        output = ms.ops.logdet(input_ms)
        return cast_to_adapter_tensor(output)

    def logical_not(self):
        input_ms = cast_to_ms_tensor(self).astype(ms.bool_)
        output = ms.ops.logical_not(input_ms)
        return cast_to_adapter_tensor(output)

    def logical_not_(self):
        output = self.logical_not().astype(self.dtype)
        return _tensor_inplace_assign(self, output, "logical_not_", "logical_not")

    def logical_or(self, other):
        input_ms = cast_to_ms_tensor(self).astype(ms.bool_)
        if isinstance(other, Tensor):
            other_ms = cast_to_ms_tensor(other).astype(ms.bool_)
        output = ms.ops.logical_or(input_ms, other_ms)
        return cast_to_adapter_tensor(output)

    def logical_or_(self, other):
        output = self.logical_or(other).astype(self.dtype)
        return _tensor_inplace_assign(self, output, "logical_or_", "logical_or")

    def logical_xor(self, other):
        if isinstance(self, Tensor):
            input_ms = cast_to_ms_tensor(self).astype(ms.bool_)
        if isinstance(other, Tensor):
            other = cast_to_ms_tensor(other).astype(ms.bool_)

        # TODO: ms.ops.logical_xor to supported GPU
        if is_under_gpu_context():
            output = ms.numpy.logical_xor(input_ms, other)
        else:
            output = ms.ops.logical_xor(input_ms, other)
        return cast_to_adapter_tensor(output)

    def logical_xor_(self, other):
        output = self.logical_xor(other).astype(self.dtype)
        return _tensor_inplace_assign(self, output, "logical_xor_", "logical_xor")

    def adjoint(self):
        input_ms = cast_to_ms_tensor(self)
        output = ms.ops.adjoint(input_ms)
        return cast_to_adapter_tensor(output)

    def lerp(self, end, weight):
        input_ms = cast_to_ms_tensor(self)
        end_ms = cast_to_ms_tensor(end)
        if isinstance(weight, Tensor):
            weight = cast_to_ms_tensor(weight)
        elif not isinstance(weight, float):
            weight = float(weight)
        output = ms.ops.lerp(input_ms, end_ms, weight)
        return cast_to_adapter_tensor(output)

    def lerp_(self, end, weight):
        output = self.lerp(end, weight)
        return _tensor_inplace_assign(self, output, "lerp_", "lerp")

    def lu(self, *, pivot=True, get_infos=False):
        if get_infos:
            output1, info = _lu_factor_ex(self, pivot=pivot)
            output = output1 + (info,)
        else:
            output = _lu_factor(self, pivot=pivot)
        return cast_to_adapter_tensor(output)

    def lu_solve(self, LU_data, LU_pivots):
        input_ms = cast_to_ms_tensor(self)
        LU_data = cast_to_ms_tensor(LU_data)
        LU_pivots = cast_to_ms_tensor(LU_pivots)
        output = ms.ops.lu_solve(input_ms, LU_data, LU_pivots)
        return cast_to_adapter_tensor(output)

    def masked_select(self, mask):
        mask_ms = cast_to_ms_tensor(mask)
        mask_dtype = mask.dtype
        if mask_dtype not in (ms.bool_, ms.uint8):
            raise RuntimeError("masked_select: expected BoolTensor or ByteTensor for mask")
        input_ms = cast_to_ms_tensor(self)
        if mask_dtype == ms.uint8:
            warning("masked_select received a mask with dtype torch.uint8, this behavior is now deprecated, " \
                    "please use a mask with dtype torch.bool instead")
            mask_ms = mask_ms.astype(ms.bool_)
        output = ms.ops.masked_select(input_ms, mask_ms)
        return cast_to_adapter_tensor(output)

    def angle(self):
        input_ms = cast_to_ms_tensor(self)
        output = ms.ops.angle(input_ms)
        return cast_to_adapter_tensor(output)

    def element_size(self):
        return self.numpy().itemsize

    def argwhere(self):
        input_ms = cast_to_ms_tensor(self)
        output = ms.ops.argwhere(input_ms)
        return cast_to_adapter_tensor(output)

    def cauchy_(self, median=0, sigma=1, *, generator=None):
        if generator:
            raise NotImplementedError("For tensor.cauchy, generator has not been supported.")

        input_ms = cast_to_ms_tensor(self)
        _shape = input_ms.shape
        output = _get_cache_prim(ms.ops.Cauchy)(list(_shape), sigma=float(sigma), median=float(median))()

        return _tensor_inplace_assign(self, output, "cauchy_", "cauchy")

    def conj_physical(self):
        input_ms = cast_to_ms_tensor(self)
        if ms.ops.is_complex(input_ms):
            output = ms.ops.conj(input_ms)
        else:
            output = input_ms
        return cast_to_adapter_tensor(output)

    def conj_physical_(self):
        output = self.conj_physical()
        return _tensor_inplace_assign(self, output, "conj_physical_", "conj_physical")

    def positive(self):
        input_ms = cast_to_ms_tensor(self)
        output = ms.ops.positive(input_ms)
        return cast_to_adapter_tensor(output)

    def outer(self, vec2):
        input_ms = cast_to_ms_tensor(self)
        vec2 = cast_to_ms_tensor(vec2)
        output = ms.ops.outer(input_ms, vec2)
        return cast_to_adapter_tensor(output)

    def sgn(self):
        input_ms = cast_to_ms_tensor(self)
        if 'Bool' in str(input_ms.dtype) or 'Int' in str(input_ms.dtype):
            type = input_ms.dtype
            input_ms = input_ms.astype(ms.float32)
            output = ms.ops.sgn(input_ms).astype(type)
        else:
            output = ms.ops.sgn(input_ms)
        return cast_to_adapter_tensor(output)

    def sgn_(self):
        output = self.sgn()
        return _tensor_inplace_assign(self, output, "sgn_", "sgn")

    def logical_and(self, other):
        input_ms = cast_to_ms_tensor(self).astype(ms.bool_)
        if isinstance(other, Tensor):
            other = cast_to_ms_tensor(other).astype(mstype.bool_)
        output = ms.ops.logical_and(input_ms, other)
        return cast_to_adapter_tensor(output)

    def logical_and_(self, other):
        output = self.logical_and(other).astype(self.dtype)
        return _tensor_inplace_assign(self, output, "logical_and_", "logical_and")

    def igamma(self, other):
        input_ms = cast_to_ms_tensor(self)
        other_ms = cast_to_ms_tensor(other)
        # TODO: after ms.ops.igamma support float16, delete code below
        input_ms, other_ms, flag = _gamma_type(input_ms, other_ms)
        output = ms.ops.igamma(input_ms, other_ms)
        if flag:
            output = output.astype(ms.float16)
        return cast_to_adapter_tensor(output)

    def igammac(self, other):
        input_ms = cast_to_ms_tensor(self)
        other_ms = cast_to_ms_tensor(other)
        # TODO: after ms.ops.igammac support float16, delete code below
        input_ms, other_ms, flag = _gamma_type(input_ms, other_ms)
        output = ms.ops.igammac(input_ms, other_ms)
        if flag:
            output = output.astype(ms.float16)
        return cast_to_adapter_tensor(output)

    def lcm(self, other):
        input_ms = cast_to_ms_tensor(self)
        other_ms = cast_to_ms_tensor(other)
        output = ms.ops.lcm(input_ms, other_ms)
        return cast_to_adapter_tensor(output)

    def lcm_(self, other):
        output = self.lcm(other)
        return _tensor_inplace_assign(self, output, "lcm_", "lcm")

    def inner(self, other):
        input_ms = cast_to_ms_tensor(self)
        other_ms = cast_to_ms_tensor(other)
        if is_under_gpu_context() and input_ms.dtype in all_int_type:
            input_type = input_ms.dtype
            other_type = other_ms.dtype
            input_ms = input_ms.astype(mstype.float32)
            other_ms = other_ms.astype(mstype.float32)
            output = ms.ops.inner(input_ms, other_ms)
            output = ms.ops.cast(output, promote_type_lookup(input_type, other_type))
        else:
            output = ms.ops.inner(input_ms, other_ms)
        return cast_to_adapter_tensor(output)

    def roll(self, shifts, dims=None):
        input_ms  = cast_to_ms_tensor(self)
        # TODO: support roll on CPU and Ascend platform. Currently use numpy func
        # TODO: on Ascend, ms.ops.roll can only accept shifts with single number.
        if not is_under_gpu_context():
            output = ms.numpy.roll(input_ms, shifts, dims)
        else:
            output = ms.ops.roll(input_ms, shifts, dims)
        return cast_to_adapter_tensor(output)

    def unfold(self, dimension, size, step):
        # TODO: mindspore do not have related interface, ms.ops.unfold is not the same as this interface
        input_ms = cast_to_ms_tensor(self)
        _indices, _dimension = _get_unfold_indices(input_ms.shape, dimension, size, step)
        indices = ms.Tensor(_indices).astype(ms.int32)
        output = ms.ops.gather(input_ms, indices, axis=_dimension)
        output = ms.ops.moveaxis(output, _dimension + 1, -1)
        return cast_to_adapter_tensor(output)

    def slogdet(self):
        input_ms = cast_to_ms_tensor(self)
        sign, output = ms.ops.slogdet(input_ms)
        return cast_to_adapter_tensor((sign, output))

    def slice_scatter(self, src, dim=0, start=None, end=None, step=1):
        # TODO: ms.ops.slice_scatter not support
        x = cast_to_ms_tensor(self)
        src = cast_to_ms_tensor(src)
        x_shape = x.shape
        x_rank, index, dim = _get_slice_scatter_const(x_shape, dim, start, end, step)

        src_shape = src.shape
        index_tensor = ms.Tensor(index)
        for _ in range(dim):
            src = src.expand_dims(0)
            index_tensor = index_tensor.expand_dims(0)

        if dim == x_rank - 1:
            src = src.broadcast_to(x.shape[0:dim] + src_shape)
        else:
            for _ in range(len(src_shape)):
                index_tensor = index_tensor.expand_dims(-1)
            src = src.broadcast_to(x.shape[0:dim] + (len(index),)+ src_shape)

        index_tensor = index_tensor.broadcast_to(src.shape)
        output = ms.ops.tensor_scatter_elements(x, axis=dim, indices=index_tensor, updates=src)
        return cast_to_adapter_tensor(output)

    def select_scatter(self, src, dim, index):
        return self.slice_scatter(src, dim, start=index, end=index + 1)

    def igamma_(self, other):
        flag32 = False
        flag16 = False
        if self.dtype == ms.float32:
            flag32 = True
        if self.dtype == ms.float16:
            flag16 = True
        output = self.igamma(other)
        if flag32:
            output = output.astype(ms.float32)
        if flag16:
            output = output.astype(ms.float16)
        return _tensor_inplace_assign(self, output, "igamma_", "igamma")

    def igammac_(self, other):
        flag32 = False
        flag16 = False
        if self.dtype == ms.float32:
            flag32 = True
        if self.dtype == ms.float16:
            flag16 = True
        output = self.igammac(other)
        if flag32:
            output = output.astype(ms.float32)
        if flag16:
            output = output.astype(ms.float16)
        return _tensor_inplace_assign(self, output, "igammac_", "igammac")

    def lgamma(self):
        # TODO: ms.ops.lgamma to support ascend
        input_ms = cast_to_ms_tensor(self)
        output = ms.ops.lgamma(input_ms)
        return cast_to_adapter_tensor(output)

    def lgamma_(self):
        # TODO: ms.ops.lgamma to support ascend
        output = self.lgamma()
        return _tensor_inplace_assign(self, output, "lgamma_", "lgamma")

    def multinomial(self, num_sample, replacement=False, seed=None):
        input_ms = cast_to_ms_tensor(self)
        if replacement and input_ms.ndim == 1:
            input_ms = input_ms.unsqueeze(0)
            output = ms.ops.multinomial(input_ms, num_sample, replacement, seed)
            output = output.squeeze(0)
        else:
            output = ms.ops.multinomial(input_ms, num_sample, replacement, seed)
        output = output.astype(ms.int64)
        return cast_to_adapter_tensor(output)

    def cov(self, *, correction=1, fweights=None, aweights=None):
        # TODO: ms.ops.cov to support float64 and complex input
        input_ms = cast_to_ms_tensor(self)
        if fweights is not None:
            fweights = cast_to_ms_tensor(fweights)
        if aweights is not None:
            aweights = cast_to_ms_tensor(aweights)
        output = ms.ops.cov(input_ms, correction=correction, fweights=fweights, aweights=aweights)
        return cast_to_adapter_tensor(output)

    def rot90(self, k, dims):
        input_ms = cast_to_ms_tensor(self)
        output = ms.ops.rot90(input_ms, k, dims)
        return cast_to_adapter_tensor(output)

    def median(self, dim=None, keepdim=False):
        input_ms = cast_to_ms_tensor(self)
        if dim is None:
            # ms.ops.median can not compute the median value along all dimentions
            # only ms.ops.Median(global_median=True) can do that.
            # so can not replace ms.ops.Median to ms.ops.median
            output, _ = _get_cache_prim(ms.ops.Median)(True)(input_ms)
            return cast_to_adapter_tensor(output)
        else:
            # TODO: On GPU, ms.ops.median the return indices may be wrong.
            value, indices = ms.ops.median(input_ms, dim, keepdim)
            if pynative_mode_condition():
                point = set_name_tuple('median')
                rlt = point(cast_to_adapter_tensor(value), cast_to_adapter_tensor(indices))
                return rlt
            return cast_to_adapter_tensor(value), cast_to_adapter_tensor(indices)

    def frac(self):
        input_ms = cast_to_ms_tensor(self)
        output = ms.ops.frac(input_ms)
        return cast_to_adapter_tensor(output)

    def frac_(self):
        output = self.frac()
        return _tensor_inplace_assign(self, output, "frac_", "frac")

    def gcd(self, other):
        input_ms = cast_to_ms_tensor(self)
        other_ms = cast_to_ms_tensor(other)
        output = ms.ops.gcd(input_ms, other_ms)
        return cast_to_adapter_tensor(output)

    def gcd_(self, other):
        output = self.gcd(other)
        return _tensor_inplace_assign(self, output, "gcd_", "gcd")

    @property
    def imag(self):
        input_ms = cast_to_ms_tensor(self)
        output = ms.ops.imag(input_ms)
        output = cast_to_adapter_tensor(output)
        output.neg_bit = True
        return output

    def ldexp(self, other):
        input_ms = cast_to_ms_tensor(self)
        other_ms = cast_to_ms_tensor(other)
        output = ms.ops.ldexp(input_ms, other_ms)
        return cast_to_adapter_tensor(output)

    def ldexp_(self, other):
        output = self.ldexp(other)
        return _tensor_inplace_assign(self, output, "ldexp_", "ldexp")

    def cross(self, other, dim=None):
        #TODO: when dim=None, ops.dim on Ascend has bug to be fix.
        input_ms = cast_to_ms_tensor(self)
        other = cast_to_ms_tensor(other)
        # TODO: after ms.ops.cross support GPU, remove code below
        if is_under_gpu_context():
            if dim is None:
                dim = -65530
            _op = _get_cache_prim(ms.ops.Cross)(dim=dim)
            _op.set_device("CPU")
            output = _op(input_ms, other)
        else:
            output = ms.ops.cross(input_ms, other, dim)
        return cast_to_adapter_tensor(output)

    def fill_diagonal_(self, fill_value, wrap=False):
        input_ms = cast_to_ms_tensor(self)
        # ms.ops.FillDiagonal need `fill_value` to be float type
        _op = _get_cache_prim(ms.ops.FillDiagonal)(float(fill_value), wrap)
        # ms.ops.FillDiagonal is not a in-place op
        output = _op(input_ms)
        return _tensor_inplace_assign(self, output, "fill_diagonal_", "fill_diagonal")

    def mv(self, vec):
        input_ms = cast_to_ms_tensor(self)
        vec_ms = cast_to_ms_tensor(vec)
        output = ms.ops.mv(input_ms, vec_ms)
        return cast_to_adapter_tensor(output)

    def histc(self, bins=100, min=0, max=0):
        input_ms = cast_to_ms_tensor(self)
        input_dtype = input_ms.dtype
        #TODO: currently not support histc on GPU
        if is_under_gpu_context():
            if max == min:
                max, _ = ms.ops.max(input_ms)
                min, _ = ms.ops.min(input_ms)
            output, _ = ms.numpy.histogram(input_ms, bins, (min, max))
        else:
            if input_dtype not in (ms.float16, ms.float32, ms.int32):
                input_ms = input_ms.astype(ms.float32)
            output = ms.ops.histc(input_ms, bins, min, max)
        return cast_to_adapter_tensor(output.astype(input_dtype))

    def histogram(self, bins, *, range=None, weight=None, density=False):
        input_ms = cast_to_ms_tensor(self)
        _bins = cast_to_ms_tensor(bins)
        if weight is not None:
            weight = cast_to_ms_tensor(weight)
        # TODO: ms.ops.histogram is not support now.
        output = ms.numpy.histogram(input_ms, _bins, range, weight, density)
        return cast_to_adapter_tensor(output)

    def geqrf(self):
        # TODO: On Ascend, ms.ops.geqrf do not support input.ndim > 2.
        input_ms = cast_to_ms_tensor(self)
        output = ms.ops.geqrf(input_ms)
        return cast_to_adapter_tensor(output)

    def logaddexp2(self, other):
        input_ms = cast_to_ms_tensor(self)
        other = cast_to_ms_tensor(other)
        output = ms.ops.logaddexp2(input_ms, other)
        return cast_to_adapter_tensor(output)

    def floor_divide(self, value):
        # ms.ops.floor_divide doesn't round the quotient towards 0
        # same behavior as torch version lower than 1.13
        input_ms = cast_to_ms_tensor(self)
        value = cast_to_ms_tensor(value)
        output = ms.ops.div(input_ms, value, rounding_mode='trunc')
        return cast_to_adapter_tensor(output)

    def floor_divide_(self, value):
        output = self.floor_divide(value)
        return _tensor_inplace_assign(self, output, "floor_divide_", "floor_divide")

    def renorm(self, p, dim, maxnorm):
        input_ms = cast_to_ms_tensor(self)
        output = ms.ops.renorm(input_ms, int(p), dim, float(maxnorm))
        return cast_to_adapter_tensor(output)

    def renorm_(self, p, dim, maxnorm):
        output = self.renorm(p, dim, maxnorm)
        return _tensor_inplace_assign(self, output, "renorm_", "renorm")

    def mvlgamma(self, p):
        input_ms = cast_to_ms_tensor(self)
        output = ms.ops.mvlgamma(input_ms, p)
        return cast_to_adapter_tensor(output)

    def mvlgamma_(self, p):
        output = self.mvlgamma(p)
        return _tensor_inplace_assign(self, output, "mvlgamma_", "mvlgamma")

    def orgqr(self, input2):
        input_ms = cast_to_ms_tensor(self)
        input2 = cast_to_ms_tensor(input2)
        output = ms.ops.orgqr(input_ms, input2)
        return cast_to_adapter_tensor(output)

    def qr(self, some=True):
        input_ms = cast_to_ms_tensor(self)
        if some:
            mode = "reduced"
        else:
            mode = "complete"
        output = ms.ops.qr(input_ms, mode)
        return cast_to_adapter_tensor(output)

    def i0(self):
        input_ms = cast_to_ms_tensor(self)
        # TODO：ms.ops.bessel_i0 to support on Ascend
        if is_under_ascend_context():
            i0_op = numpy_cell.NumpyI0('i0')
            output = i0_op(input_ms)
        else:
            if input_ms.dtype in msdapter_dtype.all_int_type:
                input_ms = input_ms.astype(ms.float32)
            output = ms.ops.bessel_i0(input_ms)
        return cast_to_adapter_tensor(output)

    def i0_(self):
        output = self.i0()
        return _tensor_inplace_assign(self, output, "i0_", "i0")

    def nextafter(self, other):
        input_ms = cast_to_ms_tensor(self)
        other = cast_to_ms_tensor(other)
        output = ms.ops.nextafter(input_ms, other)
        return cast_to_adapter_tensor(output)

    def nextafter_(self, other):
        output = self.nextafter(other)
        return _tensor_inplace_assign(self, output, "nextafter_", "nextafter")

    def logit(self, eps=None):
        input_ms = cast_to_ms_tensor(self)
        output = ms.ops.logit(input_ms, eps)
        return cast_to_adapter_tensor(output)

    def logit_(self, eps=None):
        output = self.logit(eps=eps)
        return _tensor_inplace_assign(self, output, "logit_", "logit")

    def matrix_power(self, n):
        input_ms = cast_to_ms_tensor(self)
        input_type = input_ms.dtype
        if input_type not in (ms.float32, ms.float16):
            input_ms = input_ms.astype(ms.float32)
        if not is_under_gpu_context():
            output = ms.ops.matrix_power(input_ms, n)
        else:
            #TODO: used ops func on GPU
            output = ms.numpy.matrix_power(input_ms, n)
        if input_type not in (ms.float32, ms.float16):
            output = output.astype(input_type)
        return cast_to_adapter_tensor(output)

    def index_add(self, dim, index, source, *, alpha=1):
        # TODO: to support input of more than 2-D & dim >= 1, to support GRAPH mode
        if self.dtype != source.dtype:
            raise RuntimeError(f"index_add(): self ({self.dtype}) and source ({source.dtype}) "
                               f"must have the same scalar type")
        input_ms = cast_to_ms_tensor(self)
        source = cast_to_ms_tensor(source)
        index = cast_to_ms_tensor(index).astype(mstype.int32)
        # ms.Tensor.index_add is an in-place operation, so we need to deepcopy input first
        input_copy = ms.ops.deepcopy(input_ms)
        source = source * alpha
        if input_copy.dtype == mstype.int64:
            # ms.ops.index_add takes only Parameter input, so we use ms.Tensor.index_add here
            output = input_copy.int().index_add(dim, index, source.int()).astype(mstype.int64)
        else:
            output = input_copy.index_add(dim, index, source)
        return cast_to_adapter_tensor(output)


    def index_add_(self, dim, index, source, *, alpha=1):
        # TODO: to support input of more than 2-D & dim >= 1, to support GRAPH mode
        output = self.index_add(dim, index, source, alpha=alpha)
        return _tensor_inplace_assign(self, output, "index_add_", "index_add")

    def scatter_add(self, dim, index, src):
        # TODO: support src and index of different shape
        # ms.ops.scatter_add has more restrictions on the shape of inputs
        input_ms = cast_to_ms_tensor(self)
        index = cast_to_ms_tensor(index)
        src = cast_to_ms_tensor(src)
        # TODO: ascend does not support tensor_scatter_elements
        if is_under_ascend_context():
            if dim > 0:
                nd_idx, nd_input, nd_src = self._get_scatter_ndim_input(input_ms, index, src, dim)
                output = ms.ops.scatter_nd_add(nd_input, nd_idx, nd_src).squeeze(-1)
            else:
                output = ms.ops.scatter_add(input_ms, index, src)
        else:
            output = ms.ops.tensor_scatter_elements(input_ms, index, src, axis=dim, reduction="add")
        return cast_to_adapter_tensor(output)

    def scatter_add_(self, dim, index, src):
        output = self.scatter_add(dim, index, src)
        return _tensor_inplace_assign(self, output, "scatter_add_", "scatter_add")

    def index_copy(self, dim, index, tensor2):
        # TODO: to support input of more than 2-D & dim >= 1, to support GRAPH mode
        # TODO: replace with ms.ops.index_copy
        if self.dtype != tensor2.dtype:
            raise RuntimeError(f"index_add(): self ({self.dtype}) and source ({tensor2.dtype}) "
                               f"must have the same scalar type")
        input_ms = cast_to_ms_tensor(self)
        source = cast_to_ms_tensor(tensor2)
        index = cast_to_ms_tensor(index).astype(mstype.int32)

        if self.dtype == mstype.int64:
            input_ms = input_ms.astype(mstype.int32)
            source = source.astype(mstype.int32)
        select = ms.ops.index_select(input_ms, dim, index)
        # ms.Tensor.index_add is an in-place operation, so we need to deepcopy input first
        input_copy = ms.ops.deepcopy(input_ms)
        # ms.ops.index_add supports only Parameter input so we use ms.Tensor.index_add here
        output0 = input_copy.index_add(dim, index, select, alpha=-1)
        output = output0.index_add(dim, index, source)
        if self.dtype == mstype.int64:
            output = output.astype(mstype.int64)
        return cast_to_adapter_tensor(output)

    def index_copy_(self, dim, index, tensor):
        # TODO: to support input of more than 2-D & dim >= 1, to support GRAPH mode
        output = self.index_copy(dim, index, tensor)
        return _tensor_inplace_assign(self, output, "index_copy_", "index_copy")

    def diag_embed(self, offset=0, dim1=-2, dim2=-1):
        input_ms = cast_to_ms_tensor(self)
        output = ms.ops.diag_embed(input_ms, offset=offset, dim1=dim1, dim2=dim2)
        return cast_to_adapter_tensor(output)

    def is_neg(self):
        if not hasattr(self, "neg_bit"):
            return False
        else:
            return self.neg_bit

    def resolve_neg(self):
        output = deepcopy(self)
        output.neg_bit = False
        return output

    #TODO: pinv currently not support on Ascend
    def pinverse(self, rcond=1e-15):
        if is_under_ascend_context():
            raise NotImplementedError("pinverse currently not supported on Ascend")
        input_ms = cast_to_ms_tensor(self)
        output = ms.ops.pinv(input_ms, rtol=rcond)
        return cast_to_adapter_tensor(output)

    #TODO: need to use ops func
    def symeig(self, eigenvectors=False, upper=True):
        symeig_op = numpy_cell.NumpyEigh('symeig')
        if eigenvectors:
            values, vectors = symeig_op(self, lower=not upper, eigvals_only=False)
        else:
            values =  symeig_op(self, lower=not upper, eigvals_only=True)
            vectors = ms.Tensor([])
        output = (values, vectors)
        if pynative_mode_condition():
            symeig_namedtuple = set_multiple_name_tuple('symeig', 'eigenvalues, eigenvectors')
            if values.dtype in (ms.complex64, ms.complex128):
                values = values.real()
            output = symeig_namedtuple(cast_to_adapter_tensor(values), cast_to_adapter_tensor(vectors))
            return output
        return cast_to_adapter_tensor(output)

    def nan_to_num(self, nan=0.0, posinf=None, neginf=None):
        # TODO: ms.ops.nan_to_num to support float64 input
        input_ms = cast_to_ms_tensor(self)
        #TODO: 2.1 not support neginf/posinf int input
        if neginf is not None:
            neginf = float(neginf)
        if posinf is not None:
            posinf = float(posinf)
        input_dtype = input_ms.dtype
        if is_under_gpu_context() or input_dtype == mstype.float64:
            output = input_ms.masked_fill(input_ms.isnan(), nan)
            if input_ms.dtype in all_int_type:
                input_dtype = input_ms.dtype
                if posinf is None:
                    posinf = iinfo(input_ms.dtype).max
                if neginf is None:
                    neginf = iinfo(input_ms.dtype).min
                output = output.astype(ms.float32)
                output = output.masked_fill(output.isneginf(), neginf)
                output = output.masked_fill(output.isposinf(), posinf).astype(input_dtype)
            else:
                if posinf is None:
                    posinf = finfo(input_ms.dtype).max
                if neginf is None:
                    neginf = finfo(input_ms.dtype).min
                output = output.masked_fill(output.isneginf(), neginf)
                output = output.masked_fill(output.isposinf(), posinf)
        elif input_dtype in all_int_type:
            input_ms = input_ms.astype(ms.float32)
            output = ms.ops.nan_to_num(input_ms, nan=nan, posinf=posinf, neginf=neginf)
            output = output.astype(input_dtype)
        else:
            output = ms.ops.nan_to_num(input_ms, nan=nan, posinf=posinf, neginf=neginf)
        return cast_to_adapter_tensor(output)

    def nan_to_num_(self, nan=0.0, posinf=None, neginf=None):
        # TODO: ms.ops.nan_to_num to support float64 input
        output = self.nan_to_num(nan=nan, posinf=posinf, neginf=neginf)
        return _tensor_inplace_assign(self, output, "nan_to_num_", "nan_to_num")

    def put_(self, index, source, accumulate=False):
        # TODO: does not support GRAPH MODE
        # ScatterUpdate takes only Parameter object as input
        # but Parameter object can't be created in construct func in graph mode
        input_ms = cast_to_ms_tensor(self)
        index = cast_to_ms_tensor(index)
        source = cast_to_ms_tensor(source)
        input_shape = self.shape
        input_type = self.dtype
        input_ms = input_ms.flatten()
        index = index.flatten()
        source = source.flatten()

        if is_under_ascend_context() and input_ms.dtype in msdapter_dtype.all_int_type:
            input_ms = input_ms.astype(ms.float32)
            source = source.astype(ms.float32)

        # behavior is undefined when accumulate=False and index contain duplicate elements, same as torch
        if accumulate is False:
            output = ms.ops.scatter_update(input_ms, index, source).reshape(input_shape).astype(input_type)
        else:
            # IndexAdd supports only Float16 Float32 Float64 Int16 Int32 Int8 UInt8 input and Int32 index
            index = index.astype(mstype.int32)
            output = ms.ops.index_add(input_ms.astype(mstype.float32), index, source, 0) \
                .reshape(input_shape).astype(input_type)
        output = cast_to_adapter_tensor(output)

        self.assign_value(output)
        return self

    def polygamma(self, n):
        n = ms.Tensor(n)
        input_ms = cast_to_ms_tensor(self)
        output = ms.ops.polygamma(n, input_ms)
        return cast_to_adapter_tensor(output)

    def polygamma_(self, n):
        output = self.polygamma(n)
        return _tensor_inplace_assign(self, output, "polygamma_", "polygamma")

    def index_put(self, indices, values, accumulate=False):
        input_ms = cast_to_ms_tensor(self)
        indices = cast_to_ms_tensor(indices)
        values = cast_to_ms_tensor(values)
        for index in indices:
            if index.numel() == 0:
                return cast_to_adapter_tensor(input_ms)
        # TODO: ms.ops.index_put does not support values input with rank>1
        idx = ms.ops.dstack(indices)[0]
        if accumulate is False:
            op = ms.ops.ScatterNdUpdate()
        else:
            op = ms.ops.ScatterNdAdd()
        output = op(input_ms, idx, values)
        return cast_to_adapter_tensor(output)

    def index_put_(self, indices, values, accumulate=False):
        output = self.index_put(indices, values, accumulate=accumulate)
        return _tensor_inplace_assign(self, output, "index_put_", "index_put")

    def logcumsumexp(self, dim):
        input_ms = cast_to_ms_tensor(self)
        output = input_ms.logcumsumexp(dim)
        return cast_to_adapter_tensor(output)


    #TODO: currently mindspore doe not support kthvalue
    def kthvalue(self, k, dim=None, keepdim=False):
        input_ms = cast_to_ms_tensor(self)
        input_type = input_ms.dtype
        type_trans = False
        if input_type not in (ms.float16, ms.float32, ms.int32):
            type_trans = True
            input_ms = input_ms.astype(ms.float32)
        values, indices = ms.ops.topk(input_ms, k, dim, largest=False, sorted=True)
        if dim is None:
            dim = values.ndim-1
        values=ms.ops.index_select(values, dim, ms.Tensor([k-1]))
        indices=ms.ops.index_select(indices, dim, ms.Tensor([k-1]))
        values = values.squeeze()
        indices = indices.squeeze()
        if keepdim:
            values = values.unsqueeze(dim)
            indices = indices.unsqueeze(dim)
        if type_trans:
            values = values.astype(input_type)
        indices = indices.astype(ms.int64)
        if pynative_mode_condition():
            point = set_name_tuple('kthvalue')
            rlt = point(cast_to_adapter_tensor(values), cast_to_adapter_tensor(indices))
            return rlt
        return cast_to_adapter_tensor(values), cast_to_adapter_tensor(indices)

    def _get_scatter_ndim_input(self, input, index, src, dim):
        index_stk = ()
        for i in range(len(index.shape)):
            new_shape=(index.shape[i],) + (1,) * (len(index.shape) - 1 - i)
            if i == dim:
                index_stk = index_stk + (index.float(),)
            else:
                index_stk = index_stk + \
                (ms.ops.arange(0, index.shape[i]).float().reshape(new_shape).broadcast_to(index.shape),)
        nd_idx = ms.ops.stack(index_stk, -1).long()
        nd_input = input.unsqueeze(-1)
        nd_src = src[..., :index.shape[-2], :index.shape[-1]].unsqueeze(-1)
        return nd_idx, nd_input, nd_src

    def scatter_reduce(self, dim, index, src, reduce, *, include_self=True):
        # TODO: to support reduce='mean'
        if reduce == 'mean':
            raise NotImplementedError("scatter_reduce currently doesn't support reduce=='mean'")

        input = self
        input_min = -float('inf')
        input_max = float('inf')

        input_ms = cast_to_ms_tensor(input)
        index = cast_to_ms_tensor(index)
        src = cast_to_ms_tensor(src)

        if dim > 0:
            nd_idx, nd_input, nd_src = self._get_scatter_ndim_input(input_ms, index, src, dim)

        if reduce == 'sum':
            if include_self is False:
                input_ms = input_ms.scatter(dim, index, ms.ops.zeros_like(index, dtype=input_ms.dtype))
            if dim > 0:
                output = ms.ops.scatter_nd_add(nd_input, nd_idx, nd_src).squeeze(-1)
            else:
                output = ms.ops.scatter_add(input_ms, index, src)
        elif reduce == 'prod':
            if include_self is False:
                input_ms = input_ms.scatter(dim, index, ms.ops.ones_like(index, dtype=input_ms.dtype))
            if dim > 0:
                # TODO: ms.ops.scatter_nd_mul to support Ascend
                output = ms.ops.scatter_nd_mul(nd_input, nd_idx, nd_src).squeeze(-1)
            else:
                output = ms.ops.scatter_mul(input_ms, index, src)
        elif reduce == 'amax':
            if include_self is False:
                input_ms = input_ms.scatter(dim, index, ms.ops.full_like(index, input_min, dtype=input_ms.dtype))
            if dim > 0:
                output = ms.ops.scatter_nd_max(nd_input, nd_idx, nd_src).squeeze(-1)
            else:
                output = ms.ops.scatter_max(input_ms, index, src)
        elif reduce == 'amin':
            if include_self is False:
                input_ms = input_ms.scatter(dim, index, ms.ops.full_like(index, input_max, dtype=input_ms.dtype))
            if dim > 0:
                output = ms.ops.scatter_nd_min(nd_input, nd_idx, nd_src).squeeze(-1)
            else:
                output = ms.ops.scatter_min(input_ms, index, src)
        else:
            raise NotImplementedError("for adapter, 'reduce' argument must be either 'sum', 'prod', 'mean', 'amax' or "
                                      f"'amin', but got '{reduce}'")
        return cast_to_adapter_tensor(output)

    def scatter_reduce_(self, dim, index, src, reduce, *, include_self=True):
        output = self.scatter_reduce(dim, index, src, reduce, include_self=include_self)
        return _tensor_inplace_assign(self, output, "scatter_reduce_", "scatter_reduce")


    def exponential_(self, lambd=1., *, generator=None):
        if generator is not None:
            raise ValueError("`generator` can not be supported.")
        output = np.random.exponential(scale=lambd, size=self.shape)
        output = ms.Tensor(output).astype(self.dtype)
        return _tensor_inplace_assign(self, output, "exponential_", "exponential")

    def index_reduce(self, dim, index, source, reduce, *, include_self=True):
        if self.dtype in msdapter_dtype.all_int_type:
            input_max = iinfo(self.dtype).max
            input_min = iinfo(self.dtype).min
        elif self.dtype in msdapter_dtype.all_float_type:
            input_max = finfo(self.dtype).max
            input_min = finfo(self.dtype).min

        input_ms = cast_to_ms_tensor(self)
        idx = cast_to_ms_tensor(index)
        src = cast_to_ms_tensor(source)
        if dim > 0:
            input_ms = input_ms.swapaxes(0, dim)
            src = src.swapaxes(0, dim)
        if reduce == "prod":
            if include_self is False:
                input_ms = ms.ops.scatter_update(ms.Parameter(input_ms), idx,
                                              ms.ops.ones_like(src, dtype=src.dtype))
            output = ms.ops.scatter_mul(ms.Parameter(input_ms), idx, src)
        elif reduce == "amax":
            if include_self is False:
                input_ms = ms.ops.scatter_update(ms.Parameter(input_ms), idx,
                                              ms.ops.full_like(src, input_min, dtype=src.dtype))
            output = ms.ops.scatter_max(ms.Parameter(input_ms), idx, src)
        elif reduce == "amin":
            if include_self is False:
                input_ms = ms.ops.scatter_update(ms.Parameter(input_ms), idx,
                                              ms.ops.full_like(src, input_max, dtype=src.dtype))
            output = ms.ops.scatter_min(ms.Parameter(input_ms), idx, src)
        elif reduce == "mean":
            raise NotImplementedError("scatter_reduce currently doesn't support reduce=='mean'")
        else:
            raise NotImplementedError("for adapter, 'reduce' argument must be either 'prod', 'mean', 'amax' or "
                                      f"'amin', but got '{reduce}'")
        if dim > 0:
            output = output.swapaxes(0, dim)
        return cast_to_adapter_tensor(output)

    def index_reduce_(self, dim, index, source, reduce, *, include_self=True):
        output = self.index_reduce(dim, index, source, reduce, include_self=include_self)
        return _tensor_inplace_assign(self, output, "index_reduce_", "index_reduce")

    # tensor.log_softmax is not displayed on the official website
    def log_softmax(self, dim=None, _stacklevel=3, dtype=None):
        unsupported_attr(_stacklevel) # `_stacklevel` in torch is deprecated
        if dim is None:
            dim = -1

        input_ms = cast_to_ms_tensor(self)
        if dtype is not None:
            input_ms = input_ms.astype(dtype)

        out = ms.ops.log_softmax(input_ms, dim)
        return cast_to_adapter_tensor(out)

    def masked_scatter(self, mask, tensor):
        # TODO: ms.ops.masked_scatter does not support input to be broadcasted to the shape of mask
        input_ms = cast_to_ms_tensor(self)
        mask = cast_to_ms_tensor(mask).bool()
        tensor = cast_to_ms_tensor(tensor)
        output = input_ms.masked_scatter(mask, tensor)
        return cast_to_adapter_tensor(output)

    def masked_scatter_(self, mask, tensor):
        output = self.masked_scatter(mask, tensor)
        return _tensor_inplace_assign(self, output, "masked_scatter_", "masked_scatter")

    def corrcoef(self):
        input_ms = cast_to_ms_tensor(self)
        if len(input_ms.shape) > 2:
            raise ValueError("corrcoef(): expected input to have two or fewer dimensions")
        # TODO: ms.ops.cov does not support complex input
        output = input_ms.cov()
        if len(output.shape) == 0:
            return cast_to_adapter_tensor(ms.ops.ones_like(output))
        # normalize covariance
        d = ms.numpy.diag(output)
        # Clip real and imaginary parts to [-1, 1].
        if input_ms.dtype == ms.complex64:
            real_op = _get_cache_prim(ms.ops.Real)()
            imag_op = _get_cache_prim(ms.ops.Imag)()
            complex_op = _get_cache_prim(ms.ops.Complex)()
            d_real = real_op(d)
            stddev = ms.ops.sqrt(d_real)
            output /= ms.ops.expand_dims(stddev, -1)
            output /= ms.ops.expand_dims(stddev, 0)
            output_real = real_op(output)
            output_imag = imag_op(output)
            output_real = ms.ops.clip_by_value(output_real, -1, 1)
            output_imag = ms.ops.clip_by_value(output_imag, -1, 1)
            output = complex_op(output_real, output_imag)
        else:
            stddev = ms.ops.sqrt(d)
            output /= ms.ops.expand_dims(stddev, -1)
            output /= ms.ops.expand_dims(stddev, 0)
            output = ms.ops.clip_by_value(output, -1, 1)
        return cast_to_adapter_tensor(output)

    def geometric_(self, p, *, generator=None):
        if generator is not None:
            raise ValueError("`generator` can not be supported.")
        output = np.random.geometric(p=p, size=self.shape)
        output = ms.Tensor(output).astype(self.dtype)
        return _tensor_inplace_assign(self, output, "geometric_", "geometric")

    def log_normal_(self, mean=1, std=2, *, generator=None):
        if generator is not None:
            raise ValueError("`generator` can not be supported.")
        input_ms = cast_to_ms_tensor(self)
        normal_op = _get_cache_prim(ms.ops.LogNormalReverse)(mean=mean, std=std)
        output = normal_op(input_ms)
        return _tensor_inplace_assign(self, output, "log_normal_", "log_normal")

    def map_(self, tensor, callable):
        input_ms = cast_to_ms_tensor(self)
        tensor_ms = cast_to_ms_tensor(tensor)
        output = callable(input_ms, tensor_ms)
        return _tensor_inplace_assign(self, output, "map_", "map")

    def apply_(self, fn):
        # This function should not be used in code sections that require high performance
        if not callable(fn):
            raise TypeError(f"for tensor.apply_(fn), fn must be callable, but got {type(fn).__name__}.")
        for i, elem in enumerate(self):
            self[i] = fn(elem)
        return self

    def diagonal_scatter(self, src, offset=0, dim1=0, dim2=1):
        input_ms = cast_to_ms_tensor(self)
        src_ms = cast_to_ms_tensor(src)

        input_shape = input_ms.shape

        index_np = _get_diagonal_scatter_index(input_shape, offset, dim1, dim2)
        index = ms.Tensor.from_numpy(index_np)

        if offset < 0:
            src_len = src_ms.shape[-1]
            tmp = ms.ops.zeros(src_ms.shape[:-1], src_ms.dtype)
            tmp = tmp.expand_dims(-1)
            for _ in range(src_len, input_shape[dim1]):
                src_ms = ms.ops.cat([tmp, src_ms], -1)

        src_ms = src_ms.moveaxis(-1, dim1)
        src_ms = src_ms.expand_dims(dim2)

        output = ms.ops.tensor_scatter_elements(input_ms, index, src_ms, axis=dim2)
        return cast_to_adapter_tensor(output)

    # tensor.softmax is not displayed on the official website
    def softmax(self, dim, dtype=None):
        input_ms = cast_to_ms_tensor(self)
        if dtype is not None:
            input_ms = input_ms.astype(dtype)
        output = ms.ops.softmax(input_ms, dim)
        return cast_to_adapter_tensor(output)

    def nanmedian(self, dim=None, keepdim=False):
        input_ms = cast_to_ms_tensor(self)
        if dim is None:
            # ms.ops.median can not compute the median value along all dimentions
            # only ms.ops.Median(global_median=True) can do that.
            # so can not replace ms.ops.Median to ms.ops.median
            output, _ = _get_cache_prim(ms.ops.Median)(global_median=True, ignore_nan=True)(input_ms)
            return cast_to_adapter_tensor(output)
        else:
            # TODO: On GPU, ms.ops.median the return indices may be wrong.
            nanmedian_ = _get_cache_prim(ms.ops.Median)(global_median=False, axis=dim, keep_dims=keepdim,
                                                        ignore_nan=True)
            value, indices = nanmedian_(input_ms)
            if pynative_mode_condition():
                point = set_name_tuple('nanmedian')
                rlt = point(cast_to_adapter_tensor(value), cast_to_adapter_tensor(indices))
                return rlt
            return cast_to_adapter_tensor(value), cast_to_adapter_tensor(indices)

    def backward(self, gradient=None, retain_graph=None, create_graph=False, inputs=None):
        unsupported_attr(gradient)
        unsupported_attr(retain_graph)
        unsupported_attr(create_graph)
        unsupported_attr(inputs)
        raise NotImplementedError(
            "tensor.backward() not support yet. please use "
            "mindspore.value_and_grad"
            "(https://www.mindspore.cn/docs/zh-CN/r2.0/api_python/mindspore/mindspore.value_and_grad.html) "
            "or mindspore.grad"
            "(https://www.mindspore.cn/docs/zh-CN/r2.0/api_python/mindspore/mindspore.grad.html) "
            "to compute gradient and send the gradient to the optimizer. "
            "please refer to mobilenet_v2 example: "
            "https://openi.pcl.ac.cn/OpenI/MindTorchModelZoo/src/branch/master/official/cv/"
            "mobilenet_v2/mobilenet_v2_adapter.py")

    @property
    def grad(self):
        raise NotImplementedError(
            "tensor.grad not support yet. pleause use "
            "mindspore.value_and_grad"
            "(https://www.mindspore.cn/docs/zh-CN/r2.0/api_python/mindspore/mindspore.value_and_grad.html) "
            "or mindspore.grad"
            "(https://www.mindspore.cn/docs/zh-CN/r2.0/api_python/mindspore/mindspore.grad.html) "
            "to get the gradient. And take out the corresponding element as grad."
        )

    def frexp(self):
        # TODO: to use ms.ops.frexp
        input_ms = cast_to_ms_tensor(self)
        if input_ms.dtype == ms.float16:
            input_ms = input_ms.astype(ms.float32)
            sign = ms.ops.sign(input_ms)
            input_ms = ms.ops.abs(input_ms)
            exp = ms.ops.floor(ms.ops.log2(input_ms)) + 1
            mantissa = (input_ms * sign / (2 ** exp)).astype(ms.float16)
        else:
            sign = ms.ops.sign(input_ms)
            input_ms = ms.ops.abs(input_ms)
            exp = ms.ops.floor(ms.ops.log2(input_ms)) + 1
            mantissa = input_ms * sign / (2 ** exp)
        output = (mantissa, exp.astype(ms.int32))
        return cast_to_adapter_tensor(output)

    def ormqr(self, tau, other, left=True, transpose=False):
        if not is_under_gpu_context():
            raise NotImplementedError("ormqr currently not supported on CPU nor Ascend")
        else:
            input_ms = cast_to_ms_tensor(self)
            tau = cast_to_ms_tensor(tau)
            other = cast_to_ms_tensor(other)
            output = ms.ops.ormqr(input_ms, tau, other, left, transpose)
            return cast_to_adapter_tensor(output)

    def triangular_solve(self, A, upper=True, transpose=False, unitriangular=False):
        if is_under_ascend_context():
            raise NotImplementedError("triangular_solve currently not supported on Ascend")
        B = cast_to_ms_tensor(self)
        A = cast_to_ms_tensor(A)
        trans = 'T' if transpose else 'N'
        solve_op = _get_cache_prim(SolveTriangular)(lower=(not upper), unit_diagonal=unitriangular, trans=trans)
        output = solve_op(A, B)
        if pynative_mode_condition():
            triangular_solve_namedtuple = set_multiple_name_tuple('triangular_solve', 'solution, cloned_coefficient')
            output = triangular_solve_namedtuple(cast_to_adapter_tensor(output), cast_to_adapter_tensor(A))
            return output
        return cast_to_adapter_tensor(output), cast_to_adapter_tensor(A)

    def relu(self):
        input_ms = cast_to_ms_tensor(self)
        output = ms.ops.relu(input_ms)
        return cast_to_adapter_tensor(output)

    def bfloat16(self, memory_format=None):
        if memory_format:
            raise NotImplementedError("memory_format is not supported.")
        x = cast_to_ms_tensor(self)
        output = x.astype(ms.bfloat16)
        return cast_to_adapter_tensor(output)

    def cfloat(self, memory_format=None):
        if memory_format:
            raise NotImplementedError("memory_format is not supported.")
        x = cast_to_ms_tensor(self)
        output = x.astype(ms.complex64)
        return cast_to_adapter_tensor(output)

    def cdouble(self, memory_format=None):
        if memory_format:
            raise NotImplementedError("memory_format is not supported.")
        x = cast_to_ms_tensor(self)
        output = x.astype(ms.complex128)
        return cast_to_adapter_tensor(output)


class _TypeTensor(Tensor):
    def __init__(self, *input_data, dtype_name):
        super(_TypeTensor, self).__init__(*input_data, dtype=dtype_name, inner=False)


class BoolTensor(_TypeTensor):
    def __init__(self, *input_data):
        super(BoolTensor, self).__init__(*input_data, dtype_name='bool')


class ByteTensor(_TypeTensor):
    def __init__(self, *input_data):
        super(ByteTensor, self).__init__(*input_data, dtype_name='uint8')


class CharTensor(_TypeTensor):
    def __init__(self, *input_data):
        super(CharTensor, self).__init__(*input_data, dtype_name='int8')


class ShortTensor(_TypeTensor):
    def __init__(self, *input_data):
        super(ShortTensor, self).__init__(*input_data, dtype_name='int16')


class IntTensor(_TypeTensor):
    def __init__(self, *input_data):
        super(IntTensor, self).__init__(*input_data, dtype_name='int32')


class HalfTensor(_TypeTensor):
    def __init__(self, *input_data):
        super(HalfTensor, self).__init__(*input_data, dtype_name='float16')


class FloatTensor(_TypeTensor):
    def __init__(self, *input_data):
        super(FloatTensor, self).__init__(*input_data, dtype_name='float32')


class DoubleTensor(_TypeTensor):
    def __init__(self, *input_data):
        super(DoubleTensor, self).__init__(*input_data, dtype_name='float64')


class LongTensor(_TypeTensor):
    def __init__(self, *input_data):
        super(LongTensor, self).__init__(*input_data, dtype_name='int64')

class BFloat16Tensor(_TypeTensor):
    def __init__(self, *input_data):
        super(BFloat16Tensor, self).__init__(*input_data, dtype_name='bfloat16')


_np_fp_types = (np.float16, np.float32, np.float64)

def _get_default_dtype_by_data(data):
    if isinstance(data, np.ndarray):
        origin_dtype = data.dtype
    elif isinstance(data, (tuple, list)):
        origin_dtype = np.array(data).dtype
    elif isinstance(data, float):
        input_data = np.array(data)
        origin_dtype = input_data.dtype
    else:
        return None

    if origin_dtype in _np_fp_types:
        default_dtype = get_default_dtype()
        return default_dtype
    return None

def tensor(data, dtype=None, device=None, requires_grad=True):
    unsupported_attr(device)
    if requires_grad is False:
        msg = ("In MindTorch, Tensor's `requires_grad` is always 'True', can not be set to 'False'. ")
        warning(msg)

    if dtype is None and _not_default_fp32_dtype():
        dtype = _get_default_dtype_by_data(data)

    return Tensor(data, dtype=dtype, inner=True)

def cast_to_ms_tensor(inputs):
    """
    Cast MindTorch.Tensor to MindSpore.Tensor before call mindspore API.
    """
    def _cast(inputs):
        if isinstance(inputs, Tensor):
            inputs = inner.convert_to_ms_tensor(inputs)
        elif isinstance(inputs, tuple):
            inputs_tuple = ()
            for value in inputs:
                inputs_tuple += (_cast(value), )
            inputs = inputs_tuple
        elif isinstance(inputs, list):
            inputs_list = []
            for value in inputs:
                inputs_list.append(_cast(value))
            inputs = inputs_list
        elif isinstance(inputs, dict):
            for key, value in inputs.items():
                inputs[key] = _cast(value)
        return inputs

    inputs = _cast(inputs)
    return inputs


def cast_to_adapter_tensor(outputs):
    """
    Cast MindSpore.Tensor to MindTorch.Tensor after call mindspore API.
    """
    def _cast(outputs):
        if isinstance(outputs, ms.Tensor):
            outputs = inner.convert_to_adapter_tensor(outputs)
        elif isinstance(outputs, tuple):
            outputs_tuple = ()
            for value in outputs:
                outputs_tuple += (_cast(value), )
            outputs = outputs_tuple
        elif isinstance(outputs, list):
            outputs_list = []
            for value in outputs:
                outputs_list.append(_cast(value))
            outputs = outputs_list
        elif isinstance(outputs, dict):
            for key, value in outputs.items():
                outputs[key] = _cast(value)
        return outputs

    outputs = _cast(outputs)
    return outputs


def _tensor_inplace_assign(input, output, op_name, replace_op):
    # if pynative_mode_condition():  # TODO: ms_function
    #     input.assign_value(output)
    #     return input

    # TODO: tensor api will be used in init data, but it can not be used in graph.
    if graph_mode_condition():
        raise RuntimeError('`Tensor.{a}` is an in-place operation and "x.{a}()" is not supported to use '
                           'in MindSpore static graph mode. Please use "x = x.{b}()" or other API '
                           'instead.'.format(a=op_name, b=replace_op))

    warning('`Tensor.{a}` is an in-place operation and "x.{a}()" is not encouraged to use in MindSpore. ' \
            'Please use "x = x.{b}()" or other API instead.'.format(a=op_name, b=replace_op))
    unsupported_attr(op_name)
    unsupported_attr(replace_op)
    # Pass `cast_to_ms_tensor(output)` for performance, add it back when needed.
    input.assign_value(output)
    return input

def _gamma_type(input_ms, other_ms):
    input_type = input_ms.dtype
    other_type = other_ms.dtype
    float_flag = False
    if input_type == ms.float64 or other_type == ms.float64:
        input_ms = input_ms.astype(ms.float64)
        other_ms = other_ms.astype(ms.float64)
    else:
        if input_type == ms.float16 and other_type == ms.float16:
            float_flag = True
        input_ms = input_ms.astype(ms.float32)
        other_ms = other_ms.astype(ms.float32)
    return input_ms, other_ms, float_flag

def _lu_factor(A, *, pivot=True):
    #TODO: Mindspore does not support pivot=False condition
    if not pivot:
        raise NotImplementedError("lu currently not supported pivot=False")
    inner_lu_factor_op = numpy_cell.NumpyLUFactor('lu')
    output = inner_lu_factor_op(A)
    return output

def _lu_factor_ex(A, *, pivot=True):
    #TODO: Mindspore does not support pivot=False condition
    if not pivot:
        raise NotImplementedError("lu currently not supported pivot=False")
    inner_lu_factor_op = numpy_cell.NumpyLUFactor('lu')
    output = inner_lu_factor_op(A)
    info = 0
    return output, info
