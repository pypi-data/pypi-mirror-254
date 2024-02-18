#!/usr/bin/env python
# -*- coding: utf-8 -*-
from mindspore.common.seed import _get_graph_seed
import mindspore as ms
from mindtorch.torch.tensor import cast_to_ms_tensor
import mindtorch.torch.nn.functional as ms_torch_nn_func
from mindtorch.torch.common._inner import _inplace_assign, _inplace_limit_pynative
from .module import Module

__all__ = ['Dropout', 'Dropout1d', 'Dropout2d', 'Dropout3d', 'AlphaDropout', 'FeatureAlphaDropout']


class _DropoutNd(Module):
    def __init__(self, p=0.5, inplace=False):
        super(_DropoutNd, self).__init__()
        if p < 0 or p > 1:
            raise ValueError("dropout probability has to be between 0 and 1, "
                             "but got {}".format(p))
        self.p = p
        self.inplace = inplace

    def extra_repr(self) -> str:
        return 'p={}, inplace={}'.format(self.p, self.inplace)


class Dropout(_DropoutNd):
    r"""During training, randomly zeroes some of the elements of the input
    tensor with probability :attr:`p` using samples from a Bernoulli
    distribution. Each channel will be zeroed out independently on every forward
    call.

    This has proven to be an effective technique for regularization and
    preventing the co-adaptation of neurons as described in the paper
    `Improving neural networks by preventing co-adaptation of feature
    detectors`_ .

    Furthermore, the outputs are scaled by a factor of :math:`\frac{1}{1-p}` during
    training. This means that during evaluation the module simply computes an
    identity function.

    Args:
        p: probability of an element to be zeroed. Default: 0.5
        inplace: If set to ``True``, will do this operation in-place. Default: ``False``

    Shape:
        - Input: :math:`(*)`. Input can be of any shape
        - Output: :math:`(*)`. Output is of the same shape as input

    Examples::

        >>> m = nn.Dropout(p=0.2)
        >>> input = mindtorch.torch.randn(20, 16)
        >>> output = m(input)

    .. _Improving neural networks by preventing co-adaptation of feature
        detectors: https://arxiv.org/abs/1207.0580
    """
    def __init__(self, p=0.5, inplace=False):
        _inplace_limit_pynative(inplace, "Dropout")
        super(Dropout, self).__init__(p, inplace)
        if p < 0 or p > 1:
            raise ValueError("dropout probability has to be between 0 and 1, "
                             "but got {}".format(p))
        self.keep_prob = 1.0 - self.p
        seed0, seed1 = _get_graph_seed(0, "dropout")
        self.seed0 = seed0
        self.seed1 = seed1
        self.dropout = ms.ops.Dropout(self.keep_prob, seed0, seed1)

    def forward(self, input):
        if not self.training or self.keep_prob == 1.0:
            return input

        input_ms = cast_to_ms_tensor(input)
        # ms.ops.dropout will cause the graph to be dynamic.
        output, _ = self.dropout(input_ms)
        return _inplace_assign(input, self.inplace, output)


class Dropout1d(_DropoutNd):
    def __init__(self, p=0.5, inplace=False):
        _inplace_limit_pynative(inplace, "Dropout1d")
        super(Dropout1d, self).__init__(p, inplace)

    def forward(self, input):
        return ms_torch_nn_func.dropout1d(input, self.p, self.training, self.inplace)


class Dropout2d(_DropoutNd):
    r"""Randomly zero out entire channels (a channel is a 2D feature map,
    e.g., the :math:`j`-th channel of the :math:`i`-th sample in the
    batched input is a 2D tensor :math:`\text{input}[i, j]`).
    Each channel will be zeroed out independently on every forward call with
    probability :attr:`p` using samples from a Bernoulli distribution.

    Usually the input comes from :class:`nn.Conv2d` modules.

    As described in the paper
    `Efficient Object Localization Using Convolutional Networks`_ ,
    if adjacent pixels within feature maps are strongly correlated
    (as is normally the case in early convolution layers) then i.i.d. dropout
    will not regularize the activations and will otherwise just result
    in an effective learning rate decrease.

    In this case, :func:`nn.Dropout2d` will help promote independence between
    feature maps and should be used instead.

    Args:
        p (float, optional): probability of an element to be zero-ed.
        inplace (bool, optional): If set to ``True``, will do this operation
            in-place

    Shape:
        - Input: :math:`(N, C, H, W)` or :math:`(C, H, W)`.
        - Output: :math:`(N, C, H, W)` or :math:`(C, H, W)` (same shape as input).

    Examples::

        >>> m = nn.Dropout2d(p=0.2)
        >>> input = mindtorch.randn(20, 16, 32, 32)
        >>> output = m(input)

    .. _Efficient Object Localization Using Convolutional Networks:
       https://arxiv.org/abs/1411.4280
    """
    def __init__(self, p=0.5, inplace=False):
        _inplace_limit_pynative(inplace, "Dropout2d")
        super(Dropout2d, self).__init__(p, inplace)

    def forward(self, input):
        return ms_torch_nn_func.dropout2d(input, self.p, self.training, self.inplace)


class Dropout3d(_DropoutNd):
    r"""Randomly zero out entire channels (a channel is a 3D feature map,
    e.g., the :math:`j`-th channel of the :math:`i`-th sample in the
    batched input is a 3D tensor :math:`\text{input}[i, j]`).
    Each channel will be zeroed out independently on every forward call with
    probability :attr:`p` using samples from a Bernoulli distribution.

    Usually the input comes from :class:`nn.Conv3d` modules.

    As described in the paper
    `Efficient Object Localization Using Convolutional Networks`_ ,
    if adjacent pixels within feature maps are strongly correlated
    (as is normally the case in early convolution layers) then i.i.d. dropout
    will not regularize the activations and will otherwise just result
    in an effective learning rate decrease.

    In this case, :func:`nn.Dropout3d` will help promote independence between
    feature maps and should be used instead.

    Args:
        p (float, optional): probability of an element to be zeroed.
        inplace (bool, optional): If set to ``True``, will do this operation
            in-place

    Shape:
        - Input: :math:`(N, C, D, H, W)` or :math:`(C, D, H, W)`.
        - Output: :math:`(N, C, D, H, W)` or :math:`(C, D, H, W)` (same shape as input).

    Examples::

        >>> m = nn.Dropout3d(p=0.2)
        >>> input = mindtorch.randn(20, 16, 4, 32, 32)
        >>> output = m(input)

    .. _Efficient Object Localization Using Convolutional Networks:
       https://arxiv.org/abs/1411.4280
    """

    def __init__(self, p=0.5, inplace=False):
        _inplace_limit_pynative(inplace, "Dropout3d")
        super(Dropout3d, self).__init__(p, inplace)

    def forward(self, input):
        return ms_torch_nn_func.dropout3d(input, self.p, self.training, self.inplace)


class AlphaDropout(_DropoutNd):
    def __init__(self, p=0.5, inplace=False):
        _inplace_limit_pynative(inplace, "AlphaDropout")
        super(AlphaDropout, self).__init__(p, inplace)

    def forward(self, input):
        return ms_torch_nn_func.alpha_dropout(input, self.p, self.training, self.inplace)

class FeatureAlphaDropout(_DropoutNd):
    def __init__(self, p=0.5, inplace=False):
        _inplace_limit_pynative(inplace, "FeatureAlphaDropout")
        super(FeatureAlphaDropout, self).__init__(p, inplace)

    def forward(self, input):
        return ms_torch_nn_func.feature_alpha_dropout(input, self.p, self.training, self.inplace)
