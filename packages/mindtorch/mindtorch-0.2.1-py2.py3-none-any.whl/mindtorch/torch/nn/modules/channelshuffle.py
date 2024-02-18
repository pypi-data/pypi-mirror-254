#!/usr/bin/env python
# -*- coding: utf-8 -*-

import mindspore as ms
from mindspore.ops.primitive import _primexpr
from mindtorch.torch.tensor import cast_to_ms_tensor, cast_to_adapter_tensor
from .module import Module

__all__ = ['ChannelShuffle']


class ChannelShuffle(Module):
    def __init__(self, groups):
        super(ChannelShuffle, self).__init__()
        if not isinstance(groups, int):
            raise TypeError("For ChannelShuffle, the param `groups` must be int, but got {}.".format(type(groups)))
        if groups < 1:
            raise ValueError(f"For ChannelShuffle, the param `groups` must be larger than 0, but got {groups}.")

        self.groups = groups
        self.reshape = ms.ops.Reshape()
        self.transpose = ms.ops.Transpose()

    @staticmethod
    @_primexpr
    def _check_input_dim(shape, channels, groups, cls_name):
        """check input dim"""
        dim = len(shape)
        if dim < 3:
            raise ValueError(f"For {cls_name}, the in_shape must have more than 2 dims, but got {dim}.")

        if channels % groups != 0:
            raise ValueError(f"For {cls_name}, number of channels must be divisible by groups, "
                             f"but got {channels} channels and {groups} groups.")

    def forward(self, input):
        x = cast_to_ms_tensor(input)
        x_shape = x.shape
        n, c = x_shape[0], x_shape[1]
        self._check_input_dim(x_shape, c, self.groups, self.cls_name)
        out = self.reshape(x, (n, self.groups, c // self.groups, -1))
        out = self.transpose(out, (0, 2, 1, 3))
        out = self.reshape(out, x_shape)
        return cast_to_adapter_tensor(out)

    def extra_repr(self):
        return 'groups={}'.format(self.groups)
