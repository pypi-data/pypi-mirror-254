#!/usr/bin/env python
# -*- coding: utf-8 -*-
import mindtorch.torch.nn.functional as Adapter_F
from mindtorch.torch.nn.modules.utils import _pair, _triple
from .module import Module

__all__ = ['MaxPool1d', 'MaxPool2d', 'MaxPool3d',
           'AvgPool1d', 'AvgPool2d', 'AvgPool3d',
           'AdaptiveAvgPool1d', 'AdaptiveAvgPool2d', 'AdaptiveAvgPool3d',
           'AdaptiveMaxPool1d', 'AdaptiveMaxPool2d', 'AdaptiveMaxPool3d',
           'LPPool1d', 'LPPool2d', 'FractionalMaxPool2d', 'FractionalMaxPool3d']

class _MaxPoolNd(Module):
    def __init__(self, kernel_size, stride=None, padding=0, dilation=1, return_indices=False, ceil_mode=False):
        super(_MaxPoolNd, self).__init__()
        self.kernel_size = kernel_size
        self.stride = stride if (stride is not None) else kernel_size
        self.padding = padding
        self.dilation = dilation
        self.return_indices = return_indices
        self.ceil_mode = ceil_mode

    def extra_repr(self):
        return 'kernel_size={kernel_size}, stride={stride}, padding={padding}' \
            ', dilation={dilation}, ceil_mode={ceil_mode}'.format(**self.__dict__)


class MaxPool1d(_MaxPoolNd):
    def forward(self, input):
        return Adapter_F.max_pool1d(input, self.kernel_size, self.stride, self.padding, self.dilation,
                                    self.ceil_mode, self.return_indices)


class MaxPool2d(_MaxPoolNd):
    def forward(self, input):
        return Adapter_F.max_pool2d(input, self.kernel_size, self.stride, self.padding, self.dilation,
                                    self.ceil_mode, self.return_indices)


class MaxPool3d(_MaxPoolNd):
    def forward(self, input):
        return Adapter_F.max_pool3d(input, self.kernel_size, self.stride, self.padding, self.dilation,
                                    self.ceil_mode, self.return_indices)


class _AvgPoolNd(Module):
    def __init__(self, kernel_size, stride=None, padding=0, ceil_mode=False, count_include_pad=True,
                 divisor_override = None):
        super(_AvgPoolNd, self).__init__()
        self.kernel_size = kernel_size
        self.stride = stride if (stride is not None) else kernel_size
        self.padding = padding
        self.ceil_mode = ceil_mode
        self.count_include_pad = count_include_pad
        self.divisor_override = divisor_override

    def extra_repr(self):
        return 'kernel_size={}, stride={}, padding={}'.format(
            self.kernel_size, self.stride, self.padding
        )


class AvgPool1d(_AvgPoolNd):
    def __init__(self, kernel_size, stride=None, padding=0, ceil_mode=False, count_include_pad=True):
        super(AvgPool1d, self).__init__(kernel_size, stride, padding, ceil_mode, count_include_pad)

    def forward(self, input):
        return Adapter_F.avg_pool1d(input, kernel_size=self.kernel_size, stride=self.stride, padding=self.padding,
                                    ceil_mode=self.ceil_mode, count_include_pad=self.count_include_pad)


class AvgPool2d(_AvgPoolNd):
    def forward(self, input):
        return Adapter_F.avg_pool2d(input, kernel_size=self.kernel_size, stride=self.stride, padding=self.padding,
                                    ceil_mode=self.ceil_mode, count_include_pad=self.count_include_pad,
                                    divisor_override=self.divisor_override)


class AvgPool3d(_AvgPoolNd):
    def forward(self, input):
        return Adapter_F.avg_pool3d(input, kernel_size=self.kernel_size, stride=self.stride, padding=self.padding,
                                    ceil_mode=self.ceil_mode, count_include_pad=self.count_include_pad,
                                    divisor_override=self.divisor_override)


class _AdaptiveAvgPoolNd(Module):
    def __init__(self, output_size):
        super(_AdaptiveAvgPoolNd, self).__init__()
        self.output_size = output_size

    def extra_repr(self):
        return 'output_size={}'.format(self.output_size)


class AdaptiveAvgPool1d(_AdaptiveAvgPoolNd):
    def forward(self, input):
        return Adapter_F.adaptive_avg_pool1d(input, self.output_size)


class AdaptiveAvgPool2d(_AdaptiveAvgPoolNd):
    def forward(self, input):
        return Adapter_F.adaptive_avg_pool2d(input, self.output_size)


class AdaptiveAvgPool3d(_AdaptiveAvgPoolNd):
    def forward(self, input):
        return Adapter_F.adaptive_avg_pool3d(input, self.output_size)


class _AdaptiveMaxPoolNd(Module):
    def __init__(self, output_size, return_indices=False):
        super(_AdaptiveMaxPoolNd, self).__init__()
        self.output_size = output_size
        self.return_indices = return_indices

    def extra_repr(self) -> str:
        return 'output_size={}'.format(self.output_size)


class AdaptiveMaxPool1d(_AdaptiveMaxPoolNd):
    def forward(self, input):
        return Adapter_F.adaptive_max_pool1d(input, self.output_size, self.return_indices)


class AdaptiveMaxPool2d(_AdaptiveMaxPoolNd):
    def forward(self, input):
        return Adapter_F.adaptive_max_pool2d(input, self.output_size, self.return_indices)


class AdaptiveMaxPool3d(_AdaptiveMaxPoolNd):
    def forward(self, input):
        outputs = Adapter_F.adaptive_max_pool3d(input, self.output_size, self.return_indices)
        return outputs


class _LPPoolNd(Module):
    def __init__(self, norm_type, kernel_size, stride=None, ceil_mode=False):
        super(_LPPoolNd, self).__init__()
        self.norm_type = norm_type
        self.kernel_size = kernel_size
        self.stride = stride if (stride is not None) else kernel_size
        self.ceil_mode = ceil_mode

    def extra_repr(self):
        return 'norm_type={norm_type}, kernel_size={kernel_size}, stride={stride}, ' \
            'ceil_mode={ceil_mode}'.format(**self.__dict__)


class LPPool1d(_LPPoolNd):
    def forward(self, input):
        return Adapter_F.lp_pool1d(input, self.norm_type, self.kernel_size, self.stride, self.ceil_mode)


class LPPool2d(_LPPoolNd):
    def forward(self, input):
        return Adapter_F.lp_pool2d(input, self.norm_type, self.kernel_size, self.stride, self.ceil_mode)


class FractionalMaxPool2d(Module):
    def __init__(self, kernel_size, output_size=None, output_ratio=None, return_indices=False,
                 _random_samples=None):
        super(FractionalMaxPool2d, self).__init__()
        self.kernel_size = kernel_size
        self.return_indices = return_indices
        self.output_size = _pair(output_size) if output_size is not None else None
        self.output_ratio = _pair(output_ratio) if output_ratio is not None else None
        self._random_samples = _random_samples
        if output_size is None and output_ratio is None:
            raise ValueError("FractionalMaxPool2d requires specifying either "
                             "an output size, or a pooling ratio")
        if output_size is not None and output_ratio is not None:
            raise ValueError("only one of output_size and output_ratio may be specified")
        if self.output_ratio is not None:
            if not (0 < self.output_ratio[0] < 1 and 0 < self.output_ratio[1] < 1):
                raise ValueError("output_ratio must be between 0 and 1 (got {})".format(output_ratio))
    def forward(self, input):
        return Adapter_F.fractional_max_pool2d(input, self.kernel_size, self.output_size, self.output_ratio,
                                               self.return_indices, self._random_samples)

class FractionalMaxPool3d(Module):
    def __init__(self, kernel_size, output_size=None, output_ratio=None, return_indices=False,
                 _random_samples=None):
        super(FractionalMaxPool3d, self).__init__()
        self.kernel_size = kernel_size
        self.return_indices = return_indices
        self.output_size = _triple(output_size) if output_size is not None else None
        self.output_ratio = _triple(output_ratio) if output_ratio is not None else None
        self._random_samples = _random_samples
        if output_size is None and output_ratio is None:
            raise ValueError("FractionalMaxPool3d requires specifying either "
                             "an output size, or a pooling ratio")
        if output_size is not None and output_ratio is not None:
            raise ValueError("only one of output_size and output_ratio may be specified")
        if self.output_ratio is not None:
            if not (0 < self.output_ratio[0] < 1 and 0 < self.output_ratio[1] < 1 and 0 < self.output_ratio[2] < 1):
                raise ValueError("output_ratio must be between 0 and 1 (got {})".format(output_ratio))
    def forward(self, input):
        return Adapter_F.fractional_max_pool3d(input, self.kernel_size, self.output_size, self.output_ratio,
                                                   self.return_indices, self._random_samples)
