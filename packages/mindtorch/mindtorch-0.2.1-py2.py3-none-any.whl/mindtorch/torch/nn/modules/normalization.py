#!/usr/bin/env python
# -*- coding: utf-8 -*-

import mindspore as ms
import mindspore.ops.functional as F
import mindspore.ops.operations as P
from mindspore.ops._primitive_cache import _get_cache_prim

from mindtorch.torch.tensor import cast_to_adapter_tensor, cast_to_ms_tensor
from mindtorch.torch.nn.parameter import Parameter
from mindtorch.utils import unsupported_attr
from mindtorch.torch.nn import init
import mindtorch.torch.functional as torch_func
import mindtorch.torch.nn.functional as torch_nn_func
from .module import Module


__all__ = ['LayerNorm', 'GroupNorm', 'LocalResponseNorm']

class LayerNorm(Module):
    def __init__(self, normalized_shape, eps=1e-5, elementwise_affine=True,
                 device=None, dtype=None):
        unsupported_attr(device)
        unsupported_attr(dtype)
        if not isinstance(normalized_shape, (list, tuple, int)):
            raise TypeError("`normalized_shape` should be in type of `list`, `tuple`, `int`"
                         "but got {}".format(type(normalized_shape)))
        super(LayerNorm,self).__init__()
        self.eps = eps
        if isinstance(normalized_shape, int):
            normalized_shape = (normalized_shape,)

        self.normalized_shape = tuple(normalized_shape)
        self.elementwise_affine = elementwise_affine
        self.weight = Parameter(torch_func.empty(self.normalized_shape))
        self.bias = Parameter(torch_func.empty(self.normalized_shape))
        self.normalized_shape_rank = len(self.normalized_shape)

        if self.elementwise_affine:
            self.weight.requires_grad = True
            self.bias.requires_grad = True
        else:
            self.weight.requires_grad = False
            self.bias.requires_grad = False

        self.reset_parameters()

    def reset_parameters(self):
        init.ones_(self.weight)
        init.zeros_(self.bias)

    def forward(self, input):
        input_ms = cast_to_ms_tensor(input)
        begin_axis = ms.ops.rank(input_ms) - self.normalized_shape_rank
        layer_norm_ops = _get_cache_prim(ms.ops.LayerNorm)(begin_norm_axis=begin_axis,
                                                           begin_params_axis=begin_axis,
                                                           epsilon=float(self.eps))
        output_x, _, _ = layer_norm_ops(input_ms, self.weight, self.bias)
        return cast_to_adapter_tensor(output_x)

    def extra_repr(self):
        return "{normalized_shape}, eps={eps}, "\
            "elementwise_affine={elementwise_affine}".format(**self.__dict__)


class GroupNorm(Module):
    def __init__(self, num_groups, num_channels, eps=1e-5, affine=True,
                 device=None, dtype=None):

        unsupported_attr(device)
        unsupported_attr(dtype)
        super(GroupNorm, self).__init__()
        self.num_groups = num_groups
        self.num_channels = num_channels
        self.eps = eps
        self.affine = affine
        self.weight = Parameter(torch_func.empty(num_channels), requires_grad=self.affine)
        self.bias = Parameter(torch_func.empty(num_channels), requires_grad=self.affine)

        self.shape = F.shape
        self.size = F.size
        self.reshape = F.reshape
        self.reduce_mean = P.ReduceMean(keep_dims=True)
        self.square = F.square
        self.reduce_sum = P.ReduceSum(keep_dims=True)
        self.sqrt = P.Sqrt()

        self.reset_parameters()

    def reset_parameters(self):
        init.ones_(self.weight)
        init.zeros_(self.bias)

    def _cal_output(self, x):
        """calculate groupnorm output"""
        x_dtype = x.dtype
        # TODO: This interface has a significant accuracy error under float16.
        x = cast_to_adapter_tensor(x).astype(ms.float32)
        shape = self.shape(x)
        batch = shape[0]
        x = self.reshape(x, (batch, self.num_groups, -1))
        mean = self.reduce_mean(x, 2)
        tmp = self.size(x) // batch
        var = self.reduce_sum(self.square(x - mean), 2) / (tmp / self.num_groups)
        std = self.sqrt(var + self.eps)
        x = (x - mean) / std
        x = self.reshape(x, shape).astype(x_dtype)
        ndim = len(shape)
        param_shape = [1] * (ndim - 1)
        param_shape[0] = -1
        param_shape = tuple(param_shape)
        output = x * self.reshape(self.weight, param_shape) + self.reshape(self.bias, param_shape)
        output = cast_to_adapter_tensor(output)
        return output

    def forward(self, input):
        output = self._cal_output(input)
        return output

    def extra_repr(self):
        return '{num_groups}, {num_channels}, eps={eps}, ' \
            'affine={affine}'.format(**self.__dict__)


class LocalResponseNorm(Module):
    def __init__(self, size, alpha=1e-4, beta=0.75, k=1.):
        super(LocalResponseNorm, self).__init__()
        self.size = size
        self.alpha = alpha
        self.beta = beta
        self.k = k

    def forward(self, input):
        return torch_nn_func.local_response_norm(input, self.size, self.alpha, self.beta,
                                                 self.k)

    def extra_repr(self):
        return '{size}, alpha={alpha}, beta={beta}, k={k}'.format(**self.__dict__)
