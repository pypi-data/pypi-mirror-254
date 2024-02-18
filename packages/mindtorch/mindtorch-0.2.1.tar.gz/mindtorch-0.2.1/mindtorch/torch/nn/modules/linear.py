#!/usr/bin/env python
# -*- coding: utf-8 -*-

import math
import mindspore.ops as P
from mindtorch.torch.nn import init
from mindtorch.torch.nn.functional import linear
from mindtorch.torch.functional import empty
from mindtorch.torch.nn.parameter import Parameter
from mindtorch.utils import unsupported_attr
from mindtorch.torch.tensor import cast_to_ms_tensor, cast_to_adapter_tensor
from .module import Module

__all__ = ['Linear', 'Identity', 'Bilinear']


class Linear(Module):
    r"""Applies a linear transformation to the incoming data: :math:`y = xA^T + b`

    Args:
        in_features: size of each input sample
        out_features: size of each output sample
        bias: If set to ``False``, the layer will not learn an additive bias.
            Default: ``True``

    Shape:
        - Input: :math:`(*, H_{in})` where :math:`*` means any number of
          dimensions including none and :math:`H_{in} = \text{in\_features}`.
        - Output: :math:`(*, H_{out})` where all but the last dimension
          are the same shape as the input and :math:`H_{out} = \text{out\_features}`.

    Attributes:
        weight: the learnable weights of the module of shape
            :math:`(\text{out\_features}, \text{in\_features})`. The values are
            initialized from :math:`\mathcal{U}(-\sqrt{k}, \sqrt{k})`, where
            :math:`k = \frac{1}{\text{in\_features}}`
        bias:   the learnable bias of the module of shape :math:`(\text{out\_features})`.
                If :attr:`bias` is ``True``, the values are initialized from
                :math:`\mathcal{U}(-\sqrt{k}, \sqrt{k})` where
                :math:`k = \frac{1}{\text{in\_features}}`

    Examples::

        >>> import mindtorch.torch as torch
        >>> import mindtorch.torch.nn as nn
        >>> m = nn.Linear(20, 30)
        >>> input = torch.randn(128, 20)
        >>> output = m(input)
        >>> print(output.size())
        torch.Size([128, 30])
    """
    def __init__(self, in_features, out_features, bias=True, device=None, dtype=None):
        super(Linear, self).__init__()
        self.in_features = in_features
        self.out_features = out_features
        self.has_bias = False
        self.bias = None
        self.weight = Parameter(empty((self.out_features, self.in_features), dtype=dtype, device=device),
                                requires_grad=True)
        if bias:
            self.bias = Parameter(empty(self.out_features, dtype=dtype, device=device), requires_grad=True)
            self.has_bias = True
        self.reset_parameters()

    def reset_parameters(self):
        # Setting a=sqrt(5) in kaiming_uniform is the same as initializing with
        # uniform(-1/sqrt(in_features), 1/sqrt(in_features)).
        init.kaiming_uniform_(self.weight, a=math.sqrt(5))
        if self.has_bias:
            fan_in, _ = init._calculate_fan_in_and_fan_out(self.weight)
            bound = 1 / math.sqrt(fan_in) if fan_in > 0 else 0
            init.uniform_(self.bias, -bound, bound)

    def forward(self, input):
        return linear(input, self.weight, self.bias)

    def extra_repr(self):
        return 'in_features={}, out_features={}, bias={}'.format(
            self.in_features, self.out_features, self.has_bias is not None
        )


class Identity(Module):
    def __init__(self, *args, **kwargs):
        super(Identity, self).__init__()
        unsupported_attr(args)
        unsupported_attr(kwargs)

    def forward(self, input):
        return input


class Bilinear(Module):
    def __init__(self, in1_features, in2_features, out_features, bias=True, device=None, dtype=None):
        super(Bilinear, self).__init__()
        self.in1_features = in1_features
        self.in2_features = in2_features
        self.out_features = out_features
        self.matmul = P.MatMul()
        self.mul = P.Mul()
        self.tile = P.Tile()
        self.reducesum = P.ReduceSum()

        self.has_bias = False
        self.weight = Parameter(empty((self.out_features, self.in1_features, self.in2_features),
                                      dtype=dtype, device=device), requires_grad=True)
        if bias:
            self.bias_add = P.BiasAdd()
            self.bias = Parameter(empty(self.out_features, dtype=dtype, device=device), requires_grad=True)
            self.has_bias = True
        self.reset_parameters()

    def reset_parameters(self):
        bound = 1 / math.sqrt(self.weight.shape[1])
        init.uniform_(self.weight, -bound, bound)
        if self.has_bias:
            init.uniform_(self.bias, -bound, bound)

    def forward(self, input1, input2):
        input1 = cast_to_ms_tensor(input1)
        input2 = cast_to_ms_tensor(input2)
        input1_shape = input1.shape
        input2_shape = input2.shape
        if len(input1_shape) != 2:
            input1 = input1.reshape((-1, input1_shape[-1]))
        x = self.matmul(input1, self.weight.permute(1, 0, 2).reshape(self.weight.shape[1], -1))
        if len(input2_shape) != 2:
            input2 = input2.reshape((-1, input2_shape[-1]))
        x = self.mul(x, self.tile(input2, (1, self.out_features)))
        x = x.reshape(x.shape[0], self.out_features, -1)
        x = self.reducesum(x, -1)
        if self.has_bias:
            x = self.bias_add(x, self.bias)
        x = x.reshape(*input1_shape[:-1], -1)
        return cast_to_adapter_tensor(x)

    def extra_repr(self):
        return 'in1_features={}, in2_features={}, out_features={}, bias={}'.format(
            self.in1_features, self.in2_features, self.out_features, self.has_bias is not None
        )
