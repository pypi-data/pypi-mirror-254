#!/usr/bin/env python
# -*- coding: utf-8 -*-
import collections
from itertools import repeat
# from functools import lru_cache
import mindspore as ms
from mindspore.ops.primitive import _primexpr
# from mindtorch.utils import unsupported_attr,_GLOBAL_LRU_CACHE_SIZE, _GLOBAL_LRU_CACHE_SIZE_NN


def _ntuple(n, name="parse"):
    def parse(x):
        if isinstance(x, (list, tuple)) and len(x) == 1:
            x = x[0]
        if isinstance(x, collections.abc.Iterable):
            return tuple(x)
        return tuple(repeat(x, n))

    parse.__name__ = name
    return parse


_single = _ntuple(1, "_single")
_pair = _ntuple(2, "_pair")
_triple = _ntuple(3, "_triple")
_quadruple = _ntuple(4, "_quadruple")
_sextuple = _ntuple(6, "_sextuple")

def _reverse_repeat_tuple(t, n):
    r"""Reverse the order of `t` and repeat each element for `n` times.

    This can be used to translate padding arg used by Conv and Pooling modules
    to the ones used by `F.pad`.

    Only support paddding like (padH, padW), not support ((padW0, padW1), (padH0, padH1))
    Example:
        network-type padding: (padH, padW)
        function-pad-type padding:  (padW, padW, padH, padH)
    """
    return tuple(x for x in reversed(t) for _ in range(n))


def _repeat_tuple(t, n):
    r"""Reverse the order of `t` and repeat each element for `n` times.

    This can be used to translate padding arg used by Conv and Pooling modules
    to the ones used by `F.pad`.

    Only support paddding like (padH, padW), not support ((padW0, padW1), (padH0, padH1))
    Example:
        network-type padding: (padH, padW)
        function-pad-type padding:  (padH, padH, padW, padW)
    """
    return tuple(x for x in t for _ in range(n))


@_primexpr
# @lru_cache(_GLOBAL_LRU_CACHE_SIZE)
def _is_zero_paddings(padding):
    if isinstance(padding, int):
        if padding == 0:
            return True
    elif isinstance(padding, (tuple, list)):
        if not any(padding):
            return True
    return False

@_primexpr
# @lru_cache(_GLOBAL_LRU_CACHE_SIZE_NN)
def _expand_padding_for_padv1(network_padding, x_ndim):
    r"""
    use for to get expand padding for ms.ops.Pad.
    `network_padding` must be type of iterable.

    Example:
        x_ndim = 4

        network_padding: (padW, padH)
        padding_for_padv1: ((0, 0), (0, 0), (padW, padW), (padH, padH))

        network_padding: ((padW0, padW1), (padH0, padH1))
        padding_for_padv1: ((0, 0), (0, 0), (padW0, padW1), (padH0, padH1))
    """
    _pad = []

    for p in network_padding:
        _pad.append(_pair(p))
    for _ in range(len(_pad), x_ndim):
        _pad.insert(0, (0, 0))

    return tuple(_pad)


@_primexpr
# @lru_cache(_GLOBAL_LRU_CACHE_SIZE_NN)
def _reverse_padding(network_padding):
    r"""
    Reverse padding from network-type padding to functional.pad type padding.

    Example:
        network-type padding: (padH, padW)
        function-pad-type padding:  (padW, padW, padH, padH)

        network-type padding: ((padH0, padH1), (padW0, padW1))
        function-pad-type padding: (padW0, padW1, padH0, padH1)
    """
    _pad = ()
    for p in reversed(network_padding):
        _pad += _pair(p)
    return _pad


def _do_pad(input, network_padding, *, mode='constant', value=None):
    _pad = _reverse_padding(network_padding)
    return ms.ops.pad(input, _pad, mode, value)
