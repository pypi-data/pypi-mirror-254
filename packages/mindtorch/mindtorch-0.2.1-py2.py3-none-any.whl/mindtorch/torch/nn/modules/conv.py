#!/usr/bin/env python
# -*- coding: utf-8 -*-
import math
# from functools import lru_cache

import mindspore as ms
from mindspore.ops.primitive import _primexpr

from mindtorch.torch.nn.parameter import Parameter
from mindtorch.torch.nn import init
from mindtorch.torch.functional import empty
from mindtorch.utils import unsupported_attr
from mindtorch.torch.tensor import cast_to_ms_tensor, cast_to_adapter_tensor
from mindtorch.torch.nn.functional import conv2d, conv_transpose3d, conv1d, conv3d, \
                                            _deconv_output_length, _process_conv_transpose1d_const
from .utils import _triple, _pair, _single, _reverse_repeat_tuple
from .module import Module

__all__ = ['Conv1d', 'Conv2d', 'Conv3d',
           'ConvTranspose1d', 'ConvTranspose2d', 'ConvTranspose3d']


class _ConvNd(Module):
    def __init__(self,
                 in_channels,
                 out_channels,
                 kernel_size,
                 stride,
                 padding,
                 dilation,
                 transposed,
                 output_padding,
                 groups,
                 bias,
                 padding_mode,
                 device=None,
                 dtype=None,
                 ):
        """Initialize _Conv."""
        unsupported_attr(device)
        unsupported_attr(dtype)

        super(_ConvNd, self).__init__()
        self.in_channels = in_channels
        self.out_channels = out_channels
        self.kernel_size = kernel_size
        self.stride = stride
        self.padding = padding
        self.dilation = dilation
        self.transposed = transposed
        self.output_padding = output_padding
        self.groups = groups
        self.padding_mode = padding_mode
        # MS add
        self.has_bias = bias
        if in_channels % groups != 0:
            raise ValueError('in_channels must be divisible by groups')
        if out_channels % groups != 0:
            raise ValueError('out_channels must be divisible by groups')
        valid_padding_strings = {'same', 'valid'}
        if isinstance(padding, str):
            if padding not in valid_padding_strings:
                raise ValueError(
                    "Invalid padding string {!r}, should be one of {}".format(
                        padding, valid_padding_strings))

            if padding == 'same' and any(s != 1 for s in stride):
                raise ValueError("padding='same' is not supported for strided convolutions")

        if isinstance(self.padding, str):
            self._reversed_padding_repeated_twice = [0, 0] * len(kernel_size)
            if padding == 'same':
                for d, k, i in zip(dilation, kernel_size,
                                   range(len(kernel_size) - 1, -1, -1)):
                    total_padding = d * (k - 1)
                    left_pad = total_padding // 2
                    self._reversed_padding_repeated_twice[2 * i] = left_pad
                    self._reversed_padding_repeated_twice[2 * i + 1] = (
                        total_padding - left_pad)
        else:
            self._reversed_padding_repeated_twice = _reverse_repeat_tuple(self.padding, 2)

        if transposed:
            self.weight = Parameter(empty((in_channels, out_channels // groups, *kernel_size)))
        else:
            self.weight = Parameter(empty((out_channels, in_channels // groups, *kernel_size)))
        if bias:
            self.bias = Parameter(empty(out_channels))
        else:
            self.bias = None
        self.reset_parameters()

    def reset_parameters(self):
        init.kaiming_uniform_(self.weight, a=math.sqrt(5))
        if self.bias is not None:
            fan_in, _ = init._calculate_fan_in_and_fan_out(self.weight)
            if fan_in != 0:
                bound = 1 / math.sqrt(fan_in)
                init.uniform_(self.bias, -bound, bound)

    def extra_repr(self):
        s = 'input_channels={}, output_channels={}, kernel_size={}, ' \
            'stride={}, padding={}, dilation={}, ' \
            'group={}, has_bias={}'.format(self.in_channels,
                                           self.out_channels,
                                           self.kernel_size,
                                           self.stride,
                                           self.padding,
                                           self.dilation,
                                           self.groups,
                                           self.has_bias)
        return s


class Conv1d(_ConvNd):
    r"""
        1D convolution layer.

        Calculates the 1D convolution on the input tensor which is typically of shape :math:`(N, C_{in}, L_{in})`,
        where :math:`N` is batch size, :math:`C_{in}` is a number of channels and :math:`L_{in}` is a length of
        sequence. For the tensor of each batch, its shape is :math:`(C_{in}, L_{in})`, the formula is defined as:

        Supported Platforms:
            ``Ascend`` ``GPU`` ``CPU``

        Examples:
            >>> net = nn.Conv1d(120, 240, 4, has_bias=False, weight_init='normal')
            >>> x = Tensor(np.ones([1, 120, 640]), mindspore.float32)
            >>> output = net(x).shape
            >>> print(output)
            (1, 240, 640)
        """

    def __init__(
        self,
        in_channels,
        out_channels,
        kernel_size,
        stride=1,
        padding=0,
        dilation=1,
        groups=1,
        bias=True,
        padding_mode='zeros',
        device=None,
        dtype=None
    ):
        factory_kwargs = {'device': device, 'dtype': dtype}
        kernel_size_ = _single(kernel_size)
        stride_ = _single(stride)
        padding_ = padding if isinstance(padding, str) else _single(padding)
        dilation_ = _single(dilation)
        super(Conv1d, self).__init__(in_channels, out_channels, kernel_size_, stride_, padding_, dilation_,
            False, _single(0), groups, bias, padding_mode, **factory_kwargs)

    def _conv_forward(self, input, padding):
        ndim = input.ndim
        if ndim == 2:
            input = input.expand_dims(0)
            output = conv1d(input, self.weight, self.bias, self.stride, padding, self.dilation, self.groups)
            output = output.squeeze(0)
        else:
            output = conv1d(input, self.weight, self.bias, self.stride, padding, self.dilation, self.groups)
        return output

    def forward(self, input):
        x = cast_to_ms_tensor(input)

        if self.padding_mode == 'zeros':
            return self._conv_forward(x, self.padding)

        x = ms.ops.pad(x, self._reversed_padding_repeated_twice, self.padding_mode)
        return self._conv_forward(x, 0)

class Conv2d(_ConvNd):
    def __init__(self,
                 in_channels,
                 out_channels,
                 kernel_size,
                 stride=1,
                 padding=0,
                 dilation=1,
                 groups=1,
                 bias=True,
                 padding_mode='zeros',
                 device=None,
                 dtype=None):
        """Initialize Conv2d."""
        factory_kwargs = {'device': device, 'dtype': dtype}
        kernel_size_ = _pair(kernel_size)
        stride_ = _pair(stride)
        padding_ = padding if isinstance(padding, str) else _pair(padding)
        dilation_ = _pair(dilation)
        super(Conv2d, self).__init__(in_channels, out_channels, kernel_size_, stride_, padding_, dilation_,
            False, _pair(0), groups, bias, padding_mode, **factory_kwargs)

    def _conv_forward(self, x, padding):
        ndim = x.ndim
        if ndim == 3:
            x = x.expand_dims(0)
            # Under pynative-mode, self.stride, etc can be changed at any time.
            # However, under graph-mode, the graph will be generated at first time running and can not
            # be altered anymore. After that, self.stride, etc are not supported to be changed dynamically.
            output = conv2d(x, self.weight, self.bias, self.stride, padding, self.dilation, self.groups)
            output = output.squeeze(0)
        else:
            output = conv2d(x, self.weight, self.bias, self.stride, padding, self.dilation, self.groups)
        return output

    def forward(self, input):
        x = cast_to_ms_tensor(input)

        if self.padding_mode == 'zeros':
            return self._conv_forward(x, self.padding)

        x = ms.ops.pad(x, self._reversed_padding_repeated_twice, self.padding_mode)
        return self._conv_forward(x, 0)


class Conv3d(_ConvNd):
    r"""
    3D convolution layer.

    Calculates the 3D convolution on the input tensor which is typically of shape

    Supported Platforms:
        ``Ascend`` ``GPU`` ``CPU``

    Examples:
        >>> x = Tensor(np.ones([16, 3, 10, 32, 32]), mindspore.float32)
        >>> conv3d = nn.Conv3d(in_channels=3, out_channels=32, kernel_size=(4, 3, 3))
        >>> output = conv3d(x)
        >>> print(output.shape)
        (16, 32, 10, 32, 32)
    """
    def __init__(
        self,
        in_channels,
        out_channels,
        kernel_size,
        stride=1,
        padding=0,
        dilation=1,
        groups=1,
        bias=True,
        padding_mode='zeros',
        device=None,
        dtype=None
    ):
        factory_kwargs = {'device': device, 'dtype': dtype}

        kernel_size_ = _triple(kernel_size)
        stride_ = _triple(stride)
        padding_ = padding if isinstance(padding, str) else _triple(padding)
        dilation_ = _triple(dilation)

        super(Conv3d, self).__init__(in_channels, out_channels, kernel_size_, stride_, padding_, dilation_,
            False, _triple(0), groups, bias, padding_mode, **factory_kwargs)

        if padding_mode == 'reflect':
            raise ValueError("Pad mode '{}' is not currently supported.".format(padding_mode))

    def _conv_forward(self, input, padding):
        ndim = input.ndim
        if ndim == 4:
            input = input.expand_dims(0)
            output = conv3d(input, self.weight, self.bias, self.stride, padding, self.dilation, self.groups)
            output = output.squeeze(0)
        else:
            output = conv3d(input, self.weight, self.bias, self.stride, padding, self.dilation, self.groups)
        return output

    def forward(self, input):
        x = cast_to_ms_tensor(input)

        if self.padding_mode == 'zeros':
            return self._conv_forward(x, self.padding)

        x = ms.ops.pad(x, self._reversed_padding_repeated_twice, self.padding_mode)
        return self._conv_forward(x, 0)


@_primexpr
# @lru_cache(_GLOBAL_LRU_CACHE_SIZE_NN)
def _output_padding(output_padding, input_ndim, input_shape, output_size,
                    stride, padding, kernel_size,
                    num_spatial_dims, dilation=None):
    if output_size is None:
        ret = _single(output_padding)
    else:
        has_batch_dim = input_ndim == num_spatial_dims + 2
        num_non_spatial_dims = 2 if has_batch_dim else 1
        if len(output_size) == num_non_spatial_dims + num_spatial_dims:
            output_size = output_size[num_non_spatial_dims:]
        if len(output_size) != num_spatial_dims:
            raise ValueError(
                f"ConvTranspose{num_spatial_dims}D: for {input.dim()}D input, "
                f"output_size must have {num_spatial_dims} "
                f"or {num_non_spatial_dims + num_spatial_dims} elements (got {len(output_size)})")

        min_sizes = []
        max_sizes = []
        for d in range(num_spatial_dims):
            dim_size = ((input_shape[d + num_non_spatial_dims] - 1) * stride[d] -
                        2 * padding[d] +
                        (dilation[d] if dilation is not None else 1) * (kernel_size[d] - 1) + 1)
            min_sizes.append(dim_size)
            max_sizes.append(min_sizes[d] + stride[d] - 1)

        for i in range(len(output_size)):
            size = output_size[i]
            min_size = min_sizes[i]
            max_size = max_sizes[i]
            if size < min_size or size > max_size:
                raise ValueError((
                    "requested an output size of {}, but valid sizes range "
                    "from {} to {} (for an input of {})").format(
                        output_size, min_sizes, max_sizes, input_shape[2:]))

        res = []
        for d in range(num_spatial_dims):
            res.append(output_size[d] - min_sizes[d])

        ret = tuple(res)
    return ret

class _ConvTransposeNd(_ConvNd):
    def __init__(self, in_channels, out_channels, kernel_size, stride,
                 padding, dilation, transposed, output_padding,
                 groups, bias, padding_mode, device=None, dtype=None):
        if padding_mode != 'zeros':
            raise ValueError('Only "zeros" padding mode is supported for {}'.format(self.__class__.__name__))

        factory_kwargs = {'device': device, 'dtype': dtype}
        super().__init__(
            in_channels, out_channels, kernel_size, stride,
            padding, dilation, transposed, output_padding,
            groups, bias, padding_mode, **factory_kwargs)

class ConvTranspose1d(_ConvTransposeNd):
    r"""
    1D transposed convolution layer.

    Calculates a 1D transposed convolution, which can be regarded as Conv1d for the gradient of the input.
    It also called deconvolution (although it is not an actual deconvolution).
    Supported Platforms:
        ``Ascend`` ``GPU`` ``CPU``

    Examples:
        >>> net = nn.ConvTranspose1d(3, 64, 4, has_bias=False)
        >>> x = Tensor(np.ones([1, 3, 50]), mindspore.float32)
        >>> output = net(x).shape
        >>> print(output)
        (1, 64, 53)
    """
    def __init__(
        self,
        in_channels,
        out_channels,
        kernel_size,
        stride=1,
        padding=0,
        output_padding=0,
        groups=1,
        bias=True,
        dilation=1,
        padding_mode='zeros',
        device=None,
        dtype=None,
    ):
        if output_padding > 0:
            raise ValueError("output_padding '{}' is not currently supported.".format(output_padding))

        factory_kwargs = {'device': device, 'dtype': dtype}
        kernel_size = _single(kernel_size)
        stride = _single(stride)
        padding = _single(padding)
        dilation = _single(dilation)
        output_padding = _single(output_padding)
        super().__init__(
            in_channels, out_channels, kernel_size, stride, padding, dilation,
            True, output_padding, groups, bias, padding_mode, **factory_kwargs)

        if stride[0] != 1 and padding[0] == (kernel_size[0] - 1) // 2 and output_padding[0] == stride[0] - 1:
            _pad_mode = 'same'
            _padding = 0
            raise Warning("pad_mode = same is some thing wrong, please switch to others")
        elif padding[0] == 0 and output_padding[0] == 0:
            _pad_mode = 'valid'
            _padding = 0
        else:
            _pad_mode = 'pad'
            _padding = self.padding

        _kernel_size, _stride, _dilation, _padding = \
            _process_conv_transpose1d_const(self.kernel_size, self.stride, self.dilation, _padding)

        self._ms_pad_mode = _pad_mode
        self._ms_kernel_size = _kernel_size
        self._ms_stride = _stride
        self._ms_dilation = _dilation
        self._ms_padding = _padding

        self._conv_transpose2d = ms.ops.Conv2DBackpropInput(out_channel=self.in_channels,
                                                            kernel_size=_kernel_size,
                                                            mode=1,
                                                            pad_mode=_pad_mode,
                                                            pad=_padding,
                                                            stride=_stride,
                                                            dilation=_dilation,
                                                            group=groups)
        self._bias_add = ms.ops.BiasAdd()
        self._expand_dims = ms.ops.ExpandDims()
        self._squeeze_0 = ms.ops.Squeeze(0)
        self._squeeze_2 = ms.ops.Squeeze(2)
        self._shape = ms.ops.Shape()

    def forward(self, input, output_size=None):
        # TODO: to support `output_size`
        if output_size is not None:
            raise ValueError("output_size '{}' is not currently supported.".format(output_size))

        x = cast_to_ms_tensor(input)
        ndim = x.ndim
        _weight = self._expand_dims(self.weight, 2)
        if ndim == 2:
            x = self._expand_dims(x, 0)
            x = self._expand_dims(x, 2)
            n, _, h, w = self._shape(x)

            h_out = _deconv_output_length(self._ms_pad_mode, h, self._ms_kernel_size[0], self._ms_stride[0],
                                          self._ms_dilation[0], self._ms_padding[0] + self._ms_padding[1])
            w_out = _deconv_output_length(self._ms_pad_mode, w, self._ms_kernel_size[1], self._ms_stride[1],
                                          self._ms_dilation[1], self._ms_padding[2] + self._ms_padding[3])
            output = self._conv_transpose2d(x, _weight, (n, self.out_channels, h_out, w_out))
            if self.bias is not None:
                output = self._bias_add(output, self.bias)
            output = self._squeeze_2(output)
            output = self._squeeze_0(output)
        else:
            x = self._expand_dims(x, 2)
            n, _, h, w = self._shape(x)

            h_out = _deconv_output_length(self._ms_pad_mode, h, self._ms_kernel_size[0], self._ms_stride[0],
                                          self._ms_dilation[0], self._ms_padding[0] + self._ms_padding[1])
            w_out = _deconv_output_length(self._ms_pad_mode, w, self._ms_kernel_size[1], self._ms_stride[1],
                                          self._ms_dilation[1], self._ms_padding[2] + self._ms_padding[3])
            output = self._conv_transpose2d(x, _weight, (n, self.out_channels, h_out, w_out))
            if self.bias is not None:
                output = self._bias_add(output, self.bias)
            output = self._squeeze_2(output)
        return cast_to_adapter_tensor(output)


class ConvTranspose2d(_ConvTransposeNd):
    r"""
    2D transposed convolution layer.

    Calculates a 2D transposed convolution, which can be regarded as Conv2d for the gradient of the input.
    It also called deconvolution (although it is not an actual deconvolution).

    Supported Platforms:
        ``Ascend`` ``GPU`` ``CPU``

    Examples:
        >>> net = nn.ConvTranspose2d(3, 64, 4, has_bias=False)
        >>> x = Tensor(np.ones([1, 3, 16, 50]), mindspore.float32)
        >>> output = net(x).shape
        >>> print(output)
        (1, 64, 19, 53)
        """

    def __init__(
        self,
        in_channels,
        out_channels,
        kernel_size,
        stride=1,
        padding=0,
        output_padding=0,
        groups=1,
        bias=True,
        dilation=1,
        padding_mode='zeros',
        device=None,
        dtype=None
    ):
        factory_kwargs = {'device': device, 'dtype': dtype}
        kernel_size = _pair(kernel_size)
        stride = _pair(stride)
        padding = _pair(padding)
        dilation = _pair(dilation)
        output_padding = _pair(output_padding)
        if output_padding != (0, 0):
            raise ValueError("output_padding '{}' is not currently supported.".format(output_padding))
        super().__init__(
            in_channels, out_channels, kernel_size, stride, padding, dilation,
            True, output_padding, groups, bias, padding_mode, **factory_kwargs)

        if padding == (0, 0):
            _pad_mode = 'valid'
        else:
            _pad_mode = 'pad'

        self._ms_padding = (padding[0], padding[0], padding[1], padding[1])
        self._ms_pad_mode = _pad_mode
        self._conv_transpose2d = ms.ops.Conv2DTranspose(out_channel=self.in_channels,
                                                        kernel_size=self.kernel_size,
                                                        mode=1,
                                                        pad_mode=self._ms_pad_mode,
                                                        pad=self._ms_padding,
                                                        stride=self.stride,
                                                        dilation=self.dilation,
                                                        group=groups)
        self._bias_add = ms.ops.BiasAdd()
        self._expand_dims = ms.ops.ExpandDims()
        self._squeeze_0 = ms.ops.Squeeze(0)
        self._shape = ms.ops.Shape()

    def forward(self, input, output_size=None):
        # TODO: To support output_size after ms.ops.Conv2DTranspose support `out_padding`
        if output_size is not None:
            raise ValueError("output_size '{}' is not currently supported.".format(output_size))

        x = cast_to_ms_tensor(input)
        ndim = x.ndim
        if ndim == 3:
            x = self._expand_dims(x, 0)
            n, _, h, w = self._shape(x)
            h_out = _deconv_output_length(self._ms_pad_mode, h, self.kernel_size[0], self.stride[0],
                                          self.dilation[0], self._ms_padding[0] + self._ms_padding[1])
            w_out = _deconv_output_length(self._ms_pad_mode, w, self.kernel_size[1], self.stride[1],
                                          self.dilation[1], self._ms_padding[2] + self._ms_padding[3])
            output = self._conv_transpose2d(x, self.weight, (n, self.out_channels, h_out, w_out))
            if self.bias is not None:
                output = self._bias_add(output, self.bias)
            output = self._squeeze_0(output)
        else:
            n, _, h, w = self._shape(x)
            h_out = _deconv_output_length(self._ms_pad_mode, h, self.kernel_size[0], self.stride[0],
                                          self.dilation[0], self._ms_padding[0] + self._ms_padding[1])
            w_out = _deconv_output_length(self._ms_pad_mode, w, self.kernel_size[1], self.stride[1],
                                          self.dilation[1], self._ms_padding[2] + self._ms_padding[3])
            output = self._conv_transpose2d(x, self.weight, (n, self.out_channels, h_out, w_out))
            if self.bias is not None:
                output = self._bias_add(output, self.bias)
        return cast_to_adapter_tensor(output)


class ConvTranspose3d(_ConvTransposeNd):
    r"""
       3D transposed convolution layer.

       Calculates a 3D transposed convolution, which can be regarded as Conv3d for the gradient of the input.
       It also called deconvolution (although it is not an actual deconvolution).

       Examples:
           >>> x = Tensor(np.ones([32, 16, 10, 32, 32]), mindspore.float32)
           >>> conv3d_transpose = nn.ConvTranspose3d(in_channels=16, out_channels=3, kernel_size=(4, 6, 2),
           ...                                       pad_mode='pad')
           >>> output = conv3d_transpose(x)
           >>> print(output.shape)
           (32, 3, 13, 37, 33)
       """

    def __init__(
        self,
        in_channels,
        out_channels,
        kernel_size,
        stride = 1,
        padding = 0,
        output_padding = 0,
        groups = 1,
        bias = True,
        dilation = 1,
        padding_mode = 'zeros',
        device=None,
        dtype=None
    ):
        factory_kwargs = {'device': device, 'dtype': dtype}

        _kernel_size = _triple(kernel_size)
        _stride = _triple(stride)
        _padding = _triple(padding)
        _dilation = _triple(dilation)
        output_padding = _triple(output_padding)

        super(ConvTranspose3d, self).__init__(in_channels, out_channels, _kernel_size, _stride, _padding, _dilation,
                                              True, output_padding, groups, bias, padding_mode, **factory_kwargs)

    def forward(self, input, output_size = None):
        if self.padding_mode != 'zeros':
            raise ValueError('Only `zeros` padding mode is supported for ConvTranspose3d')

        ndim = input.ndim
        input_shape = input.size()
        num_spatial_dims = 3

        if output_size is not None:
            output_size = tuple(output_size)

        _out_padding = _output_padding(self.output_padding, ndim, input_shape, output_size,
                                       self.stride, self.padding, self.kernel_size, num_spatial_dims,
                                       self.dilation)

        if ndim == 4:
            input = input.unsqueeze(0)
            output = conv_transpose3d(input, self.weight, self.bias, self.stride,
                                      self.padding, _out_padding, self.groups, self.dilation)
            output = output.squeeze(0)
        else:
            output = conv_transpose3d(input, self.weight, self.bias, self.stride,
                                      self.padding, _out_padding, self.groups, self.dilation)
        return cast_to_adapter_tensor(output)


class _ConvTransposeMixin(_ConvTransposeNd):
    def __init__(self, *args, **kwargs):
        unsupported_attr(args)
        unsupported_attr(kwargs)
        raise NotImplementedError("`_ConvTransposeMixin` is not implemented now.")
