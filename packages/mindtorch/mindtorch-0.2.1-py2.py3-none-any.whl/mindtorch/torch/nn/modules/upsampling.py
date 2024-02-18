#!/usr/bin/env python
# -*- coding: utf-8 -*-
from mindtorch.torch.nn import functional as adapter_F

from .module import Module

__all__ = ['Upsample', 'UpsamplingNearest2d', 'UpsamplingBilinear2d']


class Upsample(Module):
    r"""Upsamples a given multi-channel 1D (temporal), 2D (spatial) or 3D (volumetric) data.

    The input data is assumed to be of the form
    `minibatch x channels x [optional depth] x [optional height] x width`.
    Hence, for spatial inputs, we expect a 4D Tensor and for volumetric inputs, we expect a 5D Tensor.

    The algorithms available for upsampling are nearest neighbor and linear,
    bilinear, bicubic and trilinear for 3D, 4D and 5D input Tensor,
    respectively.

    One can either give a :attr:`scale_factor` or the target output :attr:`size` to
    calculate the output size. (You cannot give both, as it is ambiguous)

    Args:
        size (int or Tuple[int] or Tuple[int, int] or Tuple[int, int, int], optional):
            output spatial sizes
        scale_factor (float or Tuple[float] or Tuple[float, float] or Tuple[float, float, float], optional):
            multiplier for spatial size. Has to match input size if it is a tuple.
        mode (str, optional): the upsampling algorithm: one of ``'nearest'``,
            ``'linear'``, ``'bilinear'``, ``'bicubic'`` and ``'trilinear'``.
            Default: ``'nearest'``
        align_corners (bool, optional): if ``True``, the corner pixels of the input
            and output tensors are aligned, and thus preserving the values at
            those pixels. This only has effect when :attr:`mode` is
            ``'linear'``, ``'bilinear'``, or ``'trilinear'``. Default: ``False``


    """

    def __init__(self, size=None, scale_factor=None, mode='nearest', align_corners=None, recompute_scale_factor=None):
        super(Upsample, self).__init__()
        self.name = type(self).__name__
        self.size = size
        if isinstance(scale_factor, tuple):
            self.scale_factor = tuple(float(factor) for factor in scale_factor)
        else:
            self.scale_factor = float(scale_factor) if scale_factor else None
        self.mode = mode
        self.align_corners = align_corners
        self.recompute_scale_factor = recompute_scale_factor

    def forward(self, input):
        return adapter_F.interpolate(input, size=self.size, scale_factor=self.scale_factor,
                                     mode=self.mode, align_corners=self.align_corners,
                                     recompute_scale_factor=self.recompute_scale_factor)

    def extra_repr(self) -> str:
        if self.scale_factor is not None:
            info = 'scale_factor=' + str(self.scale_factor)
        else:
            info = 'size=' + str(self.size)
        info += ', mode=' + self.mode
        return info


class UpsamplingNearest2d(Upsample):
    def __init__(self, size=None, scale_factor=None):
        super(UpsamplingNearest2d, self).__init__(size, scale_factor, mode='nearest')

    def forward(self, input):
        return adapter_F.upsample_nearest(input, self.size, self.scale_factor)


class UpsamplingBilinear2d(Upsample):
    def __init__(self, size=None, scale_factor=None):
        super(UpsamplingBilinear2d, self).__init__(size, scale_factor, mode='bilinear')

    def forward(self, input):
        return adapter_F.upsample_bilinear(input, self.size, self.scale_factor)
