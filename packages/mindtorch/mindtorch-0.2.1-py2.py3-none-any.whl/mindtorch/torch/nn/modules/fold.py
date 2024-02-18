#!/usr/bin/env python
# -*- coding: utf-8 -*-

from mindtorch.torch.nn.functional import fold, unfold
from .module import Module

__all__ = ['Fold', 'Unfold']

class Fold(Module):
    #TODO: do not support on Ascend
    def __init__(self, output_size, kernel_size, dilation=1, padding=0, stride=1):
        super(Fold, self).__init__()
        self.output_size = output_size
        self.kernel_size = kernel_size
        self.dilation = dilation
        self.padding = padding
        self.stride = stride

    def forward(self, input):
        return fold(input, self.output_size, self.kernel_size, self.dilation, self.padding, self.stride)

    def extra_repr(self):
        return 'output_size={output_size}, kernel_size={kernel_size}, ' \
            'dilation={dilation}, padding={padding}, stride={stride}'.format(
                **self.__dict__
            )


class Unfold(Module):
    def __init__(self, kernel_size, dilation=1, padding=0, stride=1):
        super(Unfold, self).__init__()
        self.kernel_size = kernel_size
        self.dilation = dilation
        self.padding = padding
        self.stride = stride

    def forward(self, input):
        return unfold(input, self.kernel_size, self.dilation, self.padding, self.stride)

    def extra_repr(self):
        return 'kernel_size={kernel_size}, dilation={dilation}, padding={padding},' \
               ' stride={stride}'.format(**self.__dict__)
