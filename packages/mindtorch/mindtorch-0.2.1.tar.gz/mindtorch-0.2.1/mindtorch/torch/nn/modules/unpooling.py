#!/usr/bin/env python
# -*- coding: utf-8 -*-
import mindtorch.torch.nn.functional as Adapter_F
from .module import Module

__all__ = ['MaxUnpool1d', 'MaxUnpool2d', 'MaxUnpool3d']


class _MaxUnpoolNd(Module):
    def __init__(self, kernel_size, stride=None, padding=0):
        super(_MaxUnpoolNd, self).__init__()
        self.kernel_size = kernel_size
        self.stride = stride if (stride is not None) else kernel_size
        self.padding = padding

    def extra_repr(self) -> str:
        return 'kernel_size={}, stride={}, padding={}'.format(
            self.kernel_size, self.stride, self.padding
        )

class MaxUnpool1d(_MaxUnpoolNd):
    def forward(self, input, indices, output_size = None):
        return Adapter_F.max_unpool1d(input, indices,
                                      self.kernel_size, self.stride, self.padding, output_size)

class MaxUnpool2d(_MaxUnpoolNd):
    def forward(self, input, indices, output_size = None):
        return Adapter_F.max_unpool2d(input, indices,
                                      self.kernel_size, self.stride, self.padding, output_size)

class MaxUnpool3d(_MaxUnpoolNd):
    def forward(self, input, indices, output_size = None):
        return Adapter_F.max_unpool3d(input, indices,
                                      self.kernel_size, self.stride, self.padding, output_size)
