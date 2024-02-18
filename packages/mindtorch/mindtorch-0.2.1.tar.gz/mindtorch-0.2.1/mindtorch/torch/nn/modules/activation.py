#!/usr/bin/env python
# -*- coding: utf-8 -*-
import numpy as np
from mindspore.ops import operations as P
from mindspore.common import dtype as mstype
import mindspore as ms
from mindspore import nn
import mindspore._checkparam as validator

from mindtorch.torch.functional import empty
from mindtorch.torch.nn.parameter import Parameter
import mindtorch.torch.nn.functional as ms_torch_nn_func
from mindtorch.torch.tensor import Tensor, tensor, cast_to_ms_tensor, cast_to_adapter_tensor
from mindtorch.torch.logging import warning
from mindtorch.utils import unsupported_attr
from mindtorch.torch.common._inner import _inplace_assign, _inplace_limit_pynative
from mindtorch.torch._default_dtype import _dtype_or_default
from .module import Module
from .linear import Linear
from ..init import constant_, xavier_normal_, xavier_uniform_

__all__ = ['ReLU', 'Hardtanh', 'ReLU6', 'SiLU', 'Hardswish', 'LeakyReLU', 'Sigmoid', 'LogSigmoid', 'ELU', 'RReLU',
           'SELU', 'CELU', 'GELU', 'Mish', 'Softshrink', 'Tanh', 'Tanhshrink','Threshold', 'Softmax', 'LogSoftmax',
           'Softmin', 'Softsign', 'GLU', 'Hardshrink', 'MultiheadAttention', 'Hardsigmoid', 'PReLU', 'Softplus',
           'Softmax2d']


class ReLU(Module):
    r"""Applies the rectified linear unit function element-wise:

    :math:`\text{ReLU}(x) = (x)^+ = \max(0, x)`

    Args:
        inplace: can optionally do the operation in-place. Default: ``False``

    Shape:
        - Input: :math:`(*)`, where :math:`*` means any number of dimensions.
        - Output: :math:`(*)`, same shape as the input.

    .. image:: ../scripts/activation_images/ReLU.png

    Examples::

        >>> import mindtorch.torch as torch
        >>> import mindtorch.torch.nn as nn
        >>> m = nn.ReLU()
        >>> input = torch.randn(2)
        >>> output = m(input)
    """

    def __init__(self, inplace=False):
        super(ReLU, self).__init__()
        self.relu = P.ReLU()
        self.inplace = inplace
        _inplace_limit_pynative(inplace, "ReLU")

    def forward(self, input):
        input_ms = cast_to_ms_tensor(input)
        output = self.relu(input_ms)
        return _inplace_assign(input, self.inplace, output)

    def extra_repr(self):
        inplace_str = 'inplace=True' if self.inplace else ''
        return inplace_str


class Hardtanh(Module):
    def __init__(
        self,
        min_val=-1.,
        max_val=1.,
        inplace=False,
        min_value=None,
        max_value=None
    ):
        super(Hardtanh, self).__init__()
        _inplace_limit_pynative(inplace, "Hardtanh")
        if min_value is not None:
            warning("keyword argument min_value is deprecated and rename to min_val")
            min_val = min_value
        if max_value is not None:
            warning("keyword argument max_value is deprecated and rename to max_val")
            max_val = max_value

        self.min_val = min_val
        self.max_val = max_val
        self.inplace = inplace
        if self.max_val <= self.min_val:
            raise ValueError('`max_val` must be larger than `min_val` in `{}`, but get `max_val`:{} and '
                             '`min_val`:{}'.format(self.__class__.__name__, self.max_val, self.min_val))
        self.hardtanh = nn.Hardtanh(min_val, max_val)


    def forward(self, input):
        input_ms = cast_to_ms_tensor(input)
        output = self.hardtanh(input_ms)
        return _inplace_assign(input, self.inplace, output)

    def extra_repr(self):
        inplace_str = ', inplace=True' if self.inplace else ''
        return 'min_val={}, max_val={}{}'.format(
            self.min_val, self.max_val, inplace_str
        )


class ReLU6(Module):
    def __init__(self, inplace=False):
        super(ReLU6, self).__init__()
        self.inplace = inplace
        _inplace_limit_pynative(inplace, "ReLU6")

    def forward(self, input):
        input_ms = cast_to_ms_tensor(input)
        output = ms.ops.relu6(input_ms)
        return _inplace_assign(input, self.inplace, output)

    def extra_repr(self):
        inplace_str = 'inplace=True' if self.inplace else ''
        return inplace_str


class SiLU(Module):
    def __init__(self, inplace=False):
        super(SiLU, self).__init__()
        _inplace_limit_pynative(inplace, "SiLU")
        self.inplace = inplace

    def forward(self, input):
        input_ms = cast_to_ms_tensor(input)
        output = ms.ops.silu(input_ms)
        return _inplace_assign(input, self.inplace, output)

    def extra_repr(self):
        inplace_str = 'inplace=True' if self.inplace else ''
        return inplace_str


class Hardswish(Module):
    def __init__(self, inplace=False):
        super(Hardswish, self).__init__()
        _inplace_limit_pynative(inplace, "Hardswish")
        self.inplace = inplace
        self.hardswish = P.HSwish()

    def forward(self, input):
        input_ms = cast_to_ms_tensor(input)
        output = self.hardswish(input_ms)
        return _inplace_assign(input, self.inplace, output)


class LeakyReLU(Module):
    def __init__(self, negative_slope=1e-2, inplace=False):
        super(LeakyReLU, self).__init__()
        _inplace_limit_pynative(inplace, "LeakyReLU")
        self.negative_slope = negative_slope
        self.inplace = inplace

    def forward(self, input):
        input_ms = cast_to_ms_tensor(input)
        output = ms.ops.leaky_relu(input_ms, self.negative_slope)
        return _inplace_assign(input, self.inplace, output)

    def extra_repr(self):
        inplace_str = ', inplace=True' if self.inplace else ''
        return 'negative_slope={}{}'.format(self.negative_slope, inplace_str)


class Sigmoid(Module):
    def __init__(self):
        super(Sigmoid, self).__init__()
        self.sigmoid = P.Sigmoid()

    def forward(self, input):
        input_ms = cast_to_ms_tensor(input)
        output =  self.sigmoid(input_ms)
        return cast_to_adapter_tensor(output)


class LogSigmoid(Module):
    def __init__(self):
        super(LogSigmoid, self).__init__()
        self.logsigmoid = ms_torch_nn_func.logsigmoid

    def forward(self, input):
        return self.logsigmoid(input)


class ELU(Module):
    def __init__(self, alpha=1., inplace=False):
        super(ELU, self).__init__()
        _inplace_limit_pynative(inplace, "ELU")
        self.elu = ms_torch_nn_func.elu
        self.alpha = alpha
        self.inplace = inplace

    def forward(self, input):
        return self.elu(input, self.alpha, self.inplace)


class RReLU(Module):
    def __init__(
        self,
        lower=1./8,
        upper=1./3,
        inplace=False
    ):
        super(RReLU, self).__init__()
        _inplace_limit_pynative(inplace, "RReLU")
        self.lower = lower
        self.upper = upper
        self.inplace = inplace

    def forward(self, input):
        input_ms = cast_to_ms_tensor(input)
        out = ms.ops.rrelu(input_ms, self.lower, self.upper)
        return _inplace_assign(input, self.inplace, out)

    def extra_repr(self):
        inplace_str = ', inplace=True' if self.inplace else ''
        return 'lower={}, upper={}{}'.format(self.lower, self.upper, inplace_str)


class SELU(Module):
    def __init__(self, inplace=False):
        super(SELU, self).__init__()
        _inplace_limit_pynative(inplace, "SELU")
        self.inplace = inplace
        self.selu = P.SeLU()

    def forward(self, input):
        input_ms = cast_to_ms_tensor(input)
        out = self.selu(input_ms)
        return _inplace_assign(input, self.inplace, out)

    def extra_repr(self):
        inplace_str = 'inplace=True' if self.inplace else ''
        return inplace_str


class CELU(Module):
    def __init__(self, alpha=1., inplace=False):
        super(CELU, self).__init__()
        _inplace_limit_pynative(inplace, "CELU")
        self.alpha = alpha
        self.inplace = inplace
        self.celu = P.CeLU(alpha=self.alpha)

    def forward(self, input):
        input_ms = cast_to_ms_tensor(input)
        out = self.celu(input_ms)
        return _inplace_assign(input, self.inplace, out)

    def extra_repr(self):
        inplace_str = ', inplace=True' if self.inplace else ''
        return 'alpha={}{}'.format(self.alpha, inplace_str)


class GELU(Module):
    def __init__(self, approximate='none'):
        super(GELU, self).__init__()
        self.approximate = approximate

    def forward(self, input):
        input_ms = cast_to_ms_tensor(input)
        # TODO: The output of ms.ops.gelu will be converted to float32 when using default approximate.
        input_dtype = input_ms.dtype
        out = ms.ops.gelu(input_ms, self.approximate).astype(input_dtype)
        return cast_to_adapter_tensor(out)


class Mish(Module):
    def __init__(self, inplace=False):
        super(Mish, self).__init__()
        _inplace_limit_pynative(inplace, "Mish")
        self.inplace = inplace
        self.mish = P.Mish()

    def forward(self, input):
        input_ms = cast_to_ms_tensor(input)
        out = self.mish(input_ms)
        return _inplace_assign(input, self.inplace, out)

    def extra_repr(self):
        inplace_str = 'inplace=True' if self.inplace else ''
        return inplace_str


class Softshrink(Module):
    def __init__(self, lambd=0.5):
        super(Softshrink, self).__init__()
        self.lambd = float(lambd)

    def forward(self, input):
        input_ms = cast_to_ms_tensor(input)
        softshrink = P.SoftShrink(lambd=self.lambd)
        out = softshrink(input_ms)
        return cast_to_adapter_tensor(out)

    def extra_repr(self):
        return str(self.lambd)


class Tanh(Module):
    def forward(self,input):
        return ms_torch_nn_func.tanh(input)


class Tanhshrink(Module):
    def forward(self,input):
        return ms_torch_nn_func.tanhshrink(input)


class Threshold(Module):
    def __init__(self, threshold, value, inplace=False):
        super(Threshold, self).__init__()
        _inplace_limit_pynative(inplace, "Threshold")
        self.threshold = threshold
        self.value = value
        self.inplace = inplace

    def forward(self, input):
        return ms_torch_nn_func.threshold(input, self.threshold, self.value, self.inplace)

    def extra_repr(self):
        inplace_str = ', inplace=True' if self.inplace else ''
        return 'threshold={}, value={}{}'.format(self.threshold, self.value, inplace_str)


class Softmax(Module):
    def __init__(self, dim=None):
        super(Softmax, self).__init__()
        self.dim = dim

    def forward(self, input):
        # TODO: not support fp64 on Ascend
        return ms_torch_nn_func.softmax(input, self.dim)

    def extra_repr(self):
        return 'dim={dim}'.format(dim=self.dim)

class LogSoftmax(Module):
    def __init__(self, dim=None):
        super(LogSoftmax, self).__init__()
        self.dim = dim

    def forward(self, input):
        return ms_torch_nn_func.log_softmax(input, self.dim)

    def extra_repr(self):
        return 'dim={dim}'.format(dim=self.dim)

class Softmin(Module):
    def __init__(self, dim=None):
        super(Softmin, self).__init__()
        self.dim = dim

    def forward(self, input):
        # TODO: not support fp64 on Ascend
        return ms_torch_nn_func.softmin(input, self.dim)

    def extra_repr(self):
        return 'dim={dim}'.format(dim=self.dim)

class Softsign(Module):
    def __init__(self):
        super(Softsign, self).__init__()

    def forward(self, input):
        # TODO: not support fp64 on Ascend
        return ms_torch_nn_func.softsign(input)


class GLU(Module):
    def __init__(self, dim=-1):
        super(GLU, self).__init__()
        self.glu = ms_torch_nn_func.glu
        self.dim = dim

    def forward(self, input):
        return self.glu(input, self.dim)

    def extra_repr(self):
        return 'dim={dim}'.format(dim=self.dim)


class Hardshrink(Module):
    def __init__(self, lambd=0.5):
        super(Hardshrink, self).__init__()
        self.lambd = lambd

    def forward(self, input):
        return ms_torch_nn_func.hardshrink(input, self.lambd)

    def extra_repr(self):
        return '{}'.format(self.lambd)


class Hardsigmoid(Module):
    def __init__(self, inplace=False):
        super(Hardsigmoid, self).__init__()
        _inplace_limit_pynative(inplace, "Hardsigmoid")
        self.inplace = inplace

    def forward(self, input):
        return ms_torch_nn_func.hardsigmoid(input, self.inplace)


class MultiheadAttention(Module):
    def __init__(self, embed_dim, num_heads, dropout=0., bias=True, add_bias_kv=False, add_zero_attn=False,
                 kdim=None, vdim=None, batch_first=False, device=None, dtype=None):
        unsupported_attr(device)
        super(MultiheadAttention, self).__init__()
        self.embed_dim = embed_dim
        self.kdim = kdim if kdim is not None else embed_dim
        self.vdim = vdim if vdim is not None else embed_dim
        self._qkv_same_embed_dim = self.kdim == embed_dim and self.vdim == embed_dim

        self.num_heads = num_heads
        self.dropout = dropout
        self.batch_first = batch_first
        self.head_dim = embed_dim // num_heads
        if self.head_dim * num_heads != self.embed_dim:
            raise ValueError("The init argument 'embed_dim' must be divisible by 'num_heads'.")

        if self._qkv_same_embed_dim is False:
            self.q_proj_weight = Parameter(empty((embed_dim, embed_dim), dtype=dtype))
            self.k_proj_weight = Parameter(empty((embed_dim, self.kdim), dtype=dtype))
            self.v_proj_weight = Parameter(empty((embed_dim, self.vdim), dtype=dtype))
            self.in_proj_weight = None
        else:
            self.in_proj_weight = Parameter(empty((3 * embed_dim, embed_dim), dtype=dtype))
            self.q_proj_weight = None
            self.k_proj_weight = None
            self.v_proj_weight = None

        if bias:
            self.in_proj_bias = Parameter(empty(3 * embed_dim, dtype=dtype))
        else:
            self.in_proj_bias = None
        self.out_proj = Linear(embed_dim, embed_dim, bias=bias, dtype=dtype)

        if add_bias_kv:
            self.bias_k = Parameter(empty((1, 1, embed_dim), dtype=dtype))
            self.bias_v = Parameter(empty((1, 1, embed_dim), dtype=dtype))
        else:
            self.bias_k = self.bias_v = None

        self.add_zero_attn = add_zero_attn
        self.k_is_v = False
        self.q_is_k = False

        self._reset_parameters()

    def _reset_parameters(self):
        if self._qkv_same_embed_dim:
            xavier_uniform_(self.in_proj_weight)
        else:
            xavier_uniform_(self.q_proj_weight)
            xavier_uniform_(self.k_proj_weight)
            xavier_uniform_(self.v_proj_weight)

        if self.in_proj_bias is not None:
            constant_(self.in_proj_bias, 0.)
            constant_(self.out_proj.bias, 0.)
        if self.bias_k is not None:
            xavier_normal_(self.bias_k)
        if self.bias_v is not None:
            xavier_normal_(self.bias_v)

    def __call__(self, *args, **kwargs):
        query = kwargs.get('query', None)
        if query is None:
            query = args[0]
        key = kwargs.get('key', None)
        if key is None:
            key = args[1]
        value = kwargs.get('value', None)
        if value is None:
            value = args[2]
        self.k_is_v = key is value
        self.q_is_k = query is key
        return super().__call__(*args, **kwargs)

    def __setstate__(self, state):
        # Support loading old MultiheadAttention checkpoints generated by v1.1.0
        if '_qkv_same_embed_dim' not in state[1]:
            state[1]['_qkv_same_embed_dim'] = True

        super(MultiheadAttention, self).__setstate__(state)

    def forward(self, query, key, value, key_padding_mask=None, need_weights=True, attn_mask=None,
                average_attn_weights=True):
        query = cast_to_ms_tensor(query)
        key = cast_to_ms_tensor(key)
        value = cast_to_ms_tensor(value)
        key_padding_mask = cast_to_ms_tensor(key_padding_mask)
        attn_mask = cast_to_ms_tensor(attn_mask)

        is_batched = query.dim() == 3
        if key_padding_mask is not None:
            if key_padding_mask.dtype != ms.bool_ and not ms.ops.is_floating_point(key_padding_mask):
                raise ValueError("only bool and floating types of key_padding_mask are supported")
        if self.batch_first and is_batched:
            # k_is_v and q_is_k preprocess in __call__ since Graph mode do not support `is`
            if self.k_is_v:
                if self.q_is_k:
                    query = key = value = query.swapaxes(1, 0)
                else:
                    query, key = [x.swapaxes(1, 0) for x in (query, key)]
                    value = key
            else:
                query, key, value = [x.swapaxes(1, 0) for x in (query, key, value)]

        if not self._qkv_same_embed_dim:
            # TODO: older ver of torch doesn't have is_causal arg
            attn_output, attn_output_weights = ms_torch_nn_func.multi_head_attention_forward(
                query, key, value, self.embed_dim, self.num_heads,
                self.in_proj_weight, self.in_proj_bias,
                self.bias_k, self.bias_v, self.add_zero_attn,
                self.dropout, self.out_proj.weight, self.out_proj.bias,
                training=self.training,
                key_padding_mask=key_padding_mask,
                attn_mask=attn_mask, use_separate_proj_weight=True,
                q_proj_weight=self.q_proj_weight, k_proj_weight=self.k_proj_weight,
                v_proj_weight=self.v_proj_weight, average_attn_weights=average_attn_weights,
                k_is_v=self.k_is_v, q_is_k=self.q_is_k)
        else:
            attn_output, attn_output_weights = ms_torch_nn_func.multi_head_attention_forward(
                query, key, value, self.embed_dim, self.num_heads,
                self.in_proj_weight, self.in_proj_bias,
                self.bias_k, self.bias_v, self.add_zero_attn,
                self.dropout, self.out_proj.weight, self.out_proj.bias,
                training=self.training,
                key_padding_mask=key_padding_mask,
                attn_mask=attn_mask, average_attn_weights=average_attn_weights,
                k_is_v=self.k_is_v, q_is_k=self.q_is_k)
        if self.batch_first and is_batched:
            attn_output = attn_output.swapaxes(1, 0)
        if need_weights:
            return cast_to_adapter_tensor(attn_output), cast_to_adapter_tensor(attn_output_weights)
        return (cast_to_adapter_tensor(attn_output),)

class PReLU(Module):
    def __init__(self, num_parameters=1, init=0.25, device=None, dtype=None):
        super(PReLU, self).__init__()
        unsupported_attr(device)
        validator.check_positive_int(num_parameters, 'num_parameters', self.cls_name)
        dtype = _dtype_or_default(dtype)
        w = init
        if isinstance(w, (float, np.float32)):
            tmp = np.empty((num_parameters,), dtype=np.float32)
            tmp.fill(w)
            w = tensor(tmp, dtype=dtype)
        elif isinstance(w, list):
            if len(w) != num_parameters:
                raise ValueError(f"For '{self.cls_name}', the length of 'init' must be equal to the 'num_parameters'"
                                 f"when the 'init' is a list, but got the length of 'num_parameters': {len(w)}, "
                                 f"the 'num_parameters': {num_parameters}.")

            for i in w:
                if not isinstance(i, (float, np.float32)):
                    raise ValueError(f"For '{self.cls_name}', all elements in 'init' must be "
                                     f"float when the 'init' is a list, but got {i}.")
            w = tensor(w, dtype=dtype)
        elif isinstance(w, Tensor):
            if w.dtype not in (mstype.float16, mstype.float32):
                raise ValueError(f"For '{self.cls_name}', the dtype of 'init' must be float16 or "
                                 f"float32 when the 'init' is a tensor, but got {w.dtype}.")
            if len(w.shape) != 1 or w.shape[0] != num_parameters:
                raise ValueError(f"For '{self.cls_name}', the dimension of 'init' must be 1, and the elements number "
                                 f"should be equal to the 'num_parameters' when the 'init' is a tensor, "
                                 f"but got 'init' shape {w.shape}, the 'num_parameters' {num_parameters}.")
        else:
            raise TypeError(f"For '{self.cls_name}', the 'init' only supported float, list and tensor, "
                            f"but got {type(w).__name__}.")

        self.weight = Parameter(w)
        self.num_parameters = num_parameters

    def forward(self, input):
        return ms_torch_nn_func.prelu(input, self.weight)

    def extra_repr(self) -> str:
        return 'num_parameters={}'.format(self.num_parameters)


class Softplus(Module):
    def __init__(self, beta=1, threshold=20):
        super(Softplus, self).__init__()
        self.beta = beta
        self.threshold = threshold

    def forward(self, input):
        # TODO: not support fp64 on Ascend
        return ms_torch_nn_func.softplus(input, self.beta, self.threshold)

    def extra_repr(self):
        return 'beta={}, threshold={}'.format(self.beta, self.threshold)


class Softmax2d(Module):
    def __init__(self):
        super(Softmax2d, self).__init__()

    def forward(self, input):
        if input.dim() not in (3, 4):
            raise RuntimeError("Softmax2d requires a 3D or 4D tensor as input")
        # TODO: not support fp64 on Ascend
        return ms_torch_nn_func.softmax(input, -3)
