#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Functional interface"""
from typing import Iterable
# from functools import lru_cache
import numpy as np
import mindspore as ms
from mindspore.ops.primitive import _primexpr
from mindspore.ops._primitive_cache import _get_cache_prim
from mindspore.ops.function.math_func import _expand, _check_same_type
from mindspore.ops.operations.nn_ops import PromptFlashAttention

# from mindtorch.utils import unsupported_attr, is_under_ascend_context, _GLOBAL_LRU_CACHE_SIZE_NN
from mindtorch.utils import unsupported_attr, is_under_ascend_context, is_under_gpu_context, graph_mode_condition
from mindtorch.torch.tensor import Tensor, cast_to_ms_tensor, cast_to_adapter_tensor, _check_int_size
from mindtorch.torch.common._inner import _inplace_assign_pynative, _nn_functional_inplace_assign
from mindtorch.torch.common.dtype import all_int_type, all_float_and_complex_type
from mindtorch.torch.nn.modules.utils import _do_pad, _pair, _quadruple, _repeat_tuple, _single, _sextuple
from mindtorch.torch.common import pi
from mindtorch.torch.nn.modules.module import Module, Parameter
from mindtorch.torch.logging import warning

all = [
    'smooth_l1_loss',
    'log_softmax',
    'logsigmoid',
    'elu',
    'elu_',
    'relu',
    'relu_',
    'upsample',
    'rrelu',
    'rrelu_',
    'selu',
    'celu',
    'gelu',
    'mish',
    'softshrink',
    'hardtanh',
    'hardtanh_',
    'hardswish',
    'relu6',
    'leaky_relu',
    'softmax',
    'softmin',
    'softsign',
    'tanh',
    'tanhshrink',
    'glu',
    'softplus',
    'sigmoid',
    'hardsigmoid',
    'silu',
    'gumbel_softmax',
    'threshold',
    'threshold_',
    'hardshrink',

    'conv1d',
    'conv2d',
    'conv3d',

    'normalize',
    'local_response_norm',

    'l1_loss',
    'cross_entropy',
    'ctc_loss',
    'gaussian_nll_loss',
    'hinge_embedding_loss',
    'margin_ranking_loss',
    'multilabel_margin_loss',
    'multilabel_soft_margin_loss',
    'nll_loss',
    'kl_div',
    'binary_cross_entropy',
    'binary_cross_entropy_with_logits',
    'upsample_nearest',
    'poisson_nll_loss',
    'triplet_margin_with_distance_loss',

    'pairwise_distance',
    'cosine_similarity',
    'pdist',

    'dropout1d',
    'dropout2d',
    'dropout3d',
    'dropout',
    'alpha_dropout',
    'feature_alpha_dropout'
    'huber_loss',
    'soft_margin_loss',
    'cosine_embedding_loss',

    'pixel_shuffle',
    'pixel_unshuffle',
    'one_hot',

    'embedding',
    'max_pool2d',

    'fold',
    'unfold',

    'multi_head_attention_forward',
    'scaled_dot_product_attention',

    'prompt_flash_attention'
]


def adaptive_avg_pool1d(input, output_size):
    input_ms = cast_to_ms_tensor(input)
    input_ms = input_ms.expand_dims(-1)
    if isinstance(output_size, int):
        output_size = (output_size, 1)
    else:
        output_size = output_size + (1,)
    output = ms.ops.adaptive_avg_pool2d(input_ms, output_size)
    output = output.squeeze(-1)
    return cast_to_adapter_tensor(output)

def adaptive_avg_pool2d(input, output_size):
    input_ms = cast_to_ms_tensor(input)
    output = ms.ops.adaptive_avg_pool2d(input_ms, output_size)
    return cast_to_adapter_tensor(output)

def adaptive_avg_pool3d(input, output_size):
    input_ms = cast_to_ms_tensor(input)
    output = ms.ops.adaptive_avg_pool3d(input_ms, output_size)
    return cast_to_adapter_tensor(output)

def adaptive_max_pool1d(input, output_size, return_indices=False):
    # There is bug in ms.ops.adaptive_max_pool2d when return_indices==True on Ascend.
    if return_indices and is_under_ascend_context():
        raise NotImplementedError('adaptive_max_pool1d doesn\'t  support return_indices on Ascend now.')

    input_ms = cast_to_ms_tensor(input)
    input_shpae = input_ms.shape
    ndim = input_ms.ndim
    input_type = input_ms.dtype
    if is_under_ascend_context():
        input_ms = input_ms.astype(ms.float16)

    if isinstance(output_size, int):
        output_size = (output_size, 1)
    else:
        output_size = output_size + (1,)

    # TODO: On ascend, adaptive_max_pool2d not support 3D input yet. After supported, delete code below
    min_ndim = 2
    max_ndim = 3
    if is_under_ascend_context() and ndim == min_ndim:
        input_ms = input_ms.reshape((1,) + input_shpae + (1,))
        out = ms.ops.adaptive_max_pool2d(input_ms, output_size, return_indices)
        if return_indices:
            output, argmax = out
            return cast_to_adapter_tensor((output.reshape(output.shape[max_ndim - ndim:max_ndim]).astype(input_type),
                                           argmax.reshape(argmax.shape[max_ndim - ndim:max_ndim])))
        return cast_to_adapter_tensor(out.reshape(out.shape[max_ndim - ndim:max_ndim]).astype(input_type))

    input_ms = input_ms.expand_dims(-1)
    output = ms.ops.adaptive_max_pool2d(input_ms, output_size, return_indices)

    if is_under_ascend_context():
        # There is bug in ms.ops.adaptive_max_pool2d when return_indices==True on Ascend.
        # if return_indices:
        #     output = (output[0].squeeze(-1).astype(input_type), output[1].squeeze(-1))
        # else:
        #     output = output.squeeze(-1).astype(input_type)
        output = output.squeeze(-1).astype(input_type)
    elif return_indices:
        output = (output[0].squeeze(-1), output[1].squeeze(-1))
    else:
        output = output.squeeze(-1)
    return cast_to_adapter_tensor(output)

def adaptive_max_pool2d(input, output_size, return_indices=False):
    input_ms = cast_to_ms_tensor(input)
    input_type = input_ms.dtype
    if is_under_ascend_context():
        input_ms = input_ms.astype(ms.float16)
        output = ms.ops.adaptive_max_pool2d(input_ms, output_size, return_indices)
        if input_type != ms.float16:
            if not return_indices:
                output = output.astype(input_type)
            else:
                output = list(output)
                output[0] = output[0].astype(input_type)
                output = tuple(output)
        return cast_to_adapter_tensor(output)

    output = ms.ops.adaptive_max_pool2d(input_ms, output_size, return_indices)
    return cast_to_adapter_tensor(output)

@_primexpr
# @lru_cache(_GLOBAL_LRU_CACHE_SIZE_NN)
def _get_adaptive_max_pool3d_output_size(input_shape, output_size):
    output_shape = input_shape[-3:]
    if output_size is None:
        return output_shape
    if not isinstance(output_size, Iterable):
        output_size = [output_size, ] * 3
    output_size_list = list(output_size)
    for i, ele in enumerate(output_size_list):
        if ele is None:
            output_size_list[i] = output_shape[i]
    return tuple(output_size_list)

@_primexpr
# @lru_cache(_GLOBAL_LRU_CACHE_SIZE_NN)
def _get_adaptive_max_pool3d_stride(input_shape, output_size):
    out_d, out_h, out_w = output_size
    _, _, d, h, w = input_shape
    stride_d = d // out_d
    kernel_d = d - (out_d - 1) * stride_d
    stride_h = h // out_h
    kernel_h = h - (out_h - 1) * stride_h
    stride_w = w // out_w
    kernel_w = w - (out_w - 1) * stride_w

    return kernel_d, kernel_h, kernel_w, stride_d, stride_h, stride_w

def adaptive_max_pool3d(input, output_size, return_indices=False):
    input_ms = cast_to_ms_tensor(input)
    input_shape = ms.ops.shape(input_ms)
    _output_size = _get_adaptive_max_pool3d_output_size(input_shape, output_size)
    if is_under_ascend_context():
        ndim = input_ms.ndim
        if ndim == 4:
            input_ms = input_ms.expand_dims(0)
        input_shape = input_ms.shape
        # TODO: Ascend not support ms.ops.adaptive_max_pool3d, use MaxPool3D instead
        # MaxPool3D result is not the same as adaptive_max_pool3d, but the shape.
        # Implement below do not affect the converge of trainning.
        kernel_d, kernel_h, kernel_w, stride_d, stride_h, stride_w = \
            _get_adaptive_max_pool3d_stride(input_shape, _output_size)

        output = ms.ops.max_pool3d(input_ms, kernel_size=(kernel_d, kernel_h, kernel_w),
                                   stride=(stride_d, stride_h, stride_w), return_indices=return_indices)
        if ndim == 4:
            if return_indices:
                output = (output[0].squeeze(0), output[1].squeeze(0))
            else:
                output = output.squeeze(0)

        return cast_to_adapter_tensor(output)

    output = ms.ops.adaptive_max_pool3d(input_ms, _output_size, return_indices)
    if return_indices:
        output = (output[0], output[1].astype(ms.int64))
    return cast_to_adapter_tensor(output)

def pad(input, pad, mode="constant", value=None):
    # TODO: ms.ops.pad under 'reflect' do not support 3d padding
    # TODO: pad---function name and input name is same will raise error on Graph mode.
    input_ms = cast_to_ms_tensor(input)
    pad = _check_int_size(pad, "pad", "pad")
    output = ms.ops.pad(input_ms, pad, mode, value)
    return cast_to_adapter_tensor(output)

@_primexpr
def _get_softmax_default_dim(ndim, func_name):
    warning(f"Implicit dimension choice for {func_name} has been deprecated. " \
            f"Change the call to include dim=X as an argument")
    if ndim in (0, 1, 3):
        return 0
    else:
        return 1

def log_softmax(input, dim=None, _stacklevel=3, dtype=None):
    unsupported_attr(_stacklevel)
    # MS dim default is -1
    if dim is None:
        dim = _get_softmax_default_dim(input.dim(), "log_softmax")
    input_ms = cast_to_ms_tensor(input)
    if dtype is not None:
        input_ms = ms.ops.cast(input_ms, dtype)
    out = ms.ops.log_softmax(input_ms, dim)
    return cast_to_adapter_tensor(out)

def logsigmoid(input):
    input_ms = cast_to_ms_tensor(input)
    # TODO: the code of ms.ops.logsigmoid don't have better performance than the code below
    sigmoid_op = _get_cache_prim(ms.ops.Sigmoid)()
    sigmoid_out= sigmoid_op(input_ms)
    ret = ms.ops.log(sigmoid_out)
    return cast_to_adapter_tensor(ret)

def elu(input, alpha=1.0, inplace=False):
    input_ms = cast_to_ms_tensor(input)
    if alpha == 1.0:
        # TODO: ms.ops.elu only support `alpha` == 1.0
        out = ms.ops.elu(input_ms, alpha)
    else:
        cond = ms.ops.gt(input_ms, 0)
        out = alpha * (ms.ops.exp(input_ms) - 1)
        out = ms.ops.select(cond, input_ms, out)
    return _inplace_assign_pynative(input, inplace, out, "elu")

def elu_(input, alpha=1.0):
    output = elu(input, alpha)
    return _nn_functional_inplace_assign(input, output, 'elu_', 'elu')

def rrelu(input, lower=0.125, upper=0.3333333333333333, training=False, inplace=False):
    if training:
        raise ValueError("training '{}' is not currently supported.".format(training))

    input_ms = cast_to_ms_tensor(input)
    out = ms.ops.rrelu(input_ms, lower=lower, upper=upper)
    return _inplace_assign_pynative(input, inplace, out, "rrelu")

def rrelu_(input, lower=0.125, upper=0.3333333333333333, training=False):
    output = rrelu(input, lower, upper, training)
    return _nn_functional_inplace_assign(input, output, 'rrelu_', 'rrelu')

def selu(input, inplace=False):
    if inplace and graph_mode_condition():
        raise ValueError("nn.selu(): inplace=True is not currently supported in GRAPH mode.")
    input_ms = cast_to_ms_tensor(input)
    out = ms.ops.selu(input_ms)
    return _inplace_assign_pynative(input, inplace, out, "selu")

def celu(input, alpha=1.0, inplace=False):
    if inplace and graph_mode_condition():
        raise ValueError("nn.celu(): inplace=True is not currently supported in GRAPH mode.")
    input_ms = cast_to_ms_tensor(input)
    out = ms.ops.celu(input_ms, float(alpha))
    return _inplace_assign_pynative(input, inplace, out, "celu")

def celu_(input, alpha=1.0):
    output = celu(input, alpha)
    return _nn_functional_inplace_assign(input, output, 'celu_', 'celu')

def gelu(input, approximate='none'):
    input_x = cast_to_ms_tensor(input)
    # TODO: The output of ms.ops.gelu will be converted to float32 when using default approximate.
    input_dtype = input_x.dtype
    out = ms.ops.gelu(input_x, approximate).astype(input_dtype)
    return cast_to_adapter_tensor(out)

def mish(input, inplace=False):
    input_ms = cast_to_ms_tensor(input)
    out = ms.ops.mish(input_ms)
    return _inplace_assign_pynative(input, inplace, out, "mish")

def softshrink(input, lambd=0.5):
    # TODO: to support fp64 input
    input_ms = cast_to_ms_tensor(input)
    out = ms.ops.softshrink(input_ms, float(lambd))
    return cast_to_adapter_tensor(out)


def relu(input, inplace=False):
    input_ms = cast_to_ms_tensor(input)
    out = ms.ops.relu(input_ms)
    return _inplace_assign_pynative(input, inplace, out, "relu")

def relu_(input):
    output = relu(input)
    return _nn_functional_inplace_assign(input, output, 'relu_', 'relu')

def hardtanh(input, min_val=-1.0, max_val=1.0, inplace=False):
    input_ms = cast_to_ms_tensor(input)
    out = ms.ops.hardtanh(input_ms, min_val, max_val)
    return _inplace_assign_pynative(input, inplace, out, "hardtanh")

def hardtanh_(input, min_val=-1.0, max_val=1.0):
    output = hardtanh(input, min_val, max_val)
    return _nn_functional_inplace_assign(input, output, 'hardtanh_', 'hardtanh')


def hardswish(input, inplace=False):
    input_ms = cast_to_ms_tensor(input)
    out = ms.ops.hardswish(input_ms)
    return _inplace_assign_pynative(input, inplace, out, "hardswish")


def relu6(input, inplace=False):
    input_ms = cast_to_ms_tensor(input)
    out = ms.ops.relu6(input_ms)
    return _inplace_assign_pynative(input, inplace, out, "relu6")


def leaky_relu(input, negative_slope=0.01, inplace=False):
    input_ms = cast_to_ms_tensor(input)
    out = ms.ops.leaky_relu(input_ms, negative_slope)
    return _inplace_assign_pynative(input, inplace, out, "leaky_relu")

def leaky_relu_(input, negative_slope=0.01):
    output = leaky_relu(input, negative_slope)
    return _nn_functional_inplace_assign(input, output, 'leaky_relu_', 'leaky_relu')

def upsample(input, size=None, scale_factor=None, mode='nearest',
        align_corners=False):

    if size is None and scale_factor is None:
        raise ValueError("either size or scale_factor should be defined")

    if size is not None and scale_factor is not None:
        raise ValueError("only one of size or scale_factor should be defined")

    def linear_func(input):
        _size =_upsample_common_process_size(size, scale_factor, input.shape)

        input_ms = cast_to_ms_tensor(input)
        out = ms.ops.interpolate(input_ms, scale_factor=None, size=_size,
                                 align_corners=align_corners, mode=mode)

        return cast_to_adapter_tensor(out)

    def bllinear_func(input):
        return upsample_bilinear(input, size=size, scale_factor=scale_factor, align_corners=align_corners)

    def resize_nearest_neighbor_func(input):
        return upsample_nearest(input, size=size, scale_factor=scale_factor)

    mode_func = {'linear': linear_func,
                 'bilinear': bllinear_func,
                 'nearest': resize_nearest_neighbor_func}

    if mode not in mode_func:
        raise ValueError("Until now, `mode` beside 'linear', 'bilinear', 'nearest' are not supported")

    func = mode_func[mode]

    out = func(input)
    return out

def softmax(input, dim=None, _stacklevel=3, dtype=None):
    # TODO: not support fp64 on Ascend
    unsupported_attr(_stacklevel)
    if dim is None:
        dim = _get_softmax_default_dim(input.dim(), "softmax")
    input_ms = cast_to_ms_tensor(input)
    out = ms.ops.softmax(input_ms, dim, dtype=dtype)
    return cast_to_adapter_tensor(out)


def softmin(input, dim=None, _stacklevel=3, dtype=None):
    # TODO: not support fp64 on Ascend
    unsupported_attr(_stacklevel)
    if dim is None:
        dim = _get_softmax_default_dim(input.dim(), "softmin")
    input_ms = cast_to_ms_tensor(input)
    out = ms.ops.softmin(input_ms, dim, dtype=dtype)
    return cast_to_adapter_tensor(out)


def softsign(input):
    # TODO: not support fp64 on Ascend
    input_ms = cast_to_ms_tensor(input)
    if not input_ms.is_floating_point():
        input_ms = input_ms.astype(ms.float32)
    output =  ms.ops.functional.softsign(input_ms)
    return cast_to_adapter_tensor(output)


def tanh(input):
    input_ms = cast_to_ms_tensor(input)
    input_dtype = input_ms.dtype
    if input_dtype not in all_float_and_complex_type:
        input_ms = input_ms.astype(ms.float32)
    output = ms.ops.tanh(input_ms)
    return cast_to_adapter_tensor(output)


def tanhshrink(input):
    input_ms = cast_to_ms_tensor(input)
    input_dtype = input_ms.dtype
    if input_dtype not in all_float_and_complex_type:
        input_ms = input_ms.astype(ms.float32)
    output = ms.ops.tanhshrink(input_ms)
    return cast_to_adapter_tensor(output)


def glu(input, dim=-1):
    if not is_under_gpu_context():
        input_ms = cast_to_ms_tensor(input)
        out = ms.ops.glu(input_ms, axis=dim)
        return cast_to_adapter_tensor(out)

    if input.dim() == 0:
        raise RuntimeError("glu does not support scalars because halving size must be even")
    if input.shape[dim] % 2 == 1:
        raise RuntimeError("Halving dimension must be even, but dimension {} is size {}".format(dim,input.shape[dim]))
    halflen = input.shape[dim]//2
    input_ms = cast_to_ms_tensor(input)
    data_a = input_ms.narrow(axis=dim, start=0, length=halflen)
    data_b = input_ms.narrow(axis=dim, start=halflen, length=halflen)

    sigmoid_data_b = ms.ops.sigmoid(data_b)
    out = ms.ops.mul(data_a, sigmoid_data_b)
    return cast_to_adapter_tensor(out)


def normalize(input, p=2.0, dim=1, eps=1e-12, out=None):
    #the type of 'p' in ms.ops.functional.norm should be 'int'
    input_ms = cast_to_ms_tensor(input)
    input_p = ms.ops.pow(abs(input_ms), p)
    input_p_sum = input_p.sum(axis = dim, keepdims=True)

    norm = ms.ops.pow(input_p_sum, 1.0/p)
    min_value = ms.Tensor(eps, ms.float32)
    denom = ms.ops.clip_by_value(norm, min_value)
    denom = denom.expand_as(input_ms)
    output = ms.ops.functional.div(input_ms, denom)

    if out is not None:
        ms.ops.assign(out, output)
        return out
    return cast_to_adapter_tensor(output)


def softplus(input, beta=1, threshold=20):
    input_ms = cast_to_ms_tensor(input)
    ret = ms.ops.softplus(input_ms, beta, threshold)
    return cast_to_adapter_tensor(ret)


def sigmoid(input):
    input_ms = cast_to_ms_tensor(input)
    if is_under_ascend_context() and input_ms.dtype == ms.float64:
        input_ms = input_ms.astype(ms.float32)
        out = ms.ops.sigmoid(input_ms)
        out = out.astype(ms.float64)
    else:
        out = ms.ops.sigmoid(input_ms)
    return cast_to_adapter_tensor(out)


def hardsigmoid(input, inplace=False):
    input_ms = cast_to_ms_tensor(input)
    out = ms.ops.hardsigmoid(input_ms)
    return _inplace_assign_pynative(input, inplace, out, "hardsigmoid")


def silu(input, inplace=False):
    input_ms = cast_to_ms_tensor(input)
    out = ms.ops.silu(input_ms)
    return _inplace_assign_pynative(input, inplace, out, "silu")


def gumbel_softmax(logits, tau=1.0, hard=False, eps=1e-10, dim=-1):
    if eps != 1e-10:
        warning("`eps` parameter is deprecated and has no effect.")
    logits = cast_to_ms_tensor(logits)
    out = ms.ops.gumbel_softmax(logits, tau, hard, dim)
    return cast_to_adapter_tensor(out)


def threshold(input, threshold, value, inplace=False):
    #TODO: threshold---function name and input name is same will raise error on Graph mode.
    input_ms = cast_to_ms_tensor(input)
    out = ms.ops.threshold(input_ms, threshold, value)
    return _inplace_assign_pynative(input, inplace, out, "threshold")

def threshold_(input, threshold, value):
    output = threshold(input, threshold, value)
    return _nn_functional_inplace_assign(input, output, 'threshold_', 'threshold')


@_primexpr
# @lru_cache(_GLOBAL_LRU_CACHE_SIZE_NN)
def _get_reduce_string(size_average, reduce):
    if size_average is None:
        size_average = True
    if reduce is None:
        reduce = True

    if size_average and reduce:
        ret = 'mean'
    elif reduce:
        ret = 'sum'
    else:
        ret = 'none'

    warning_msg = "size_average and reduce args will be deprecated, please use reduction='{}' instead."
    warning(warning_msg.format(ret))
    return ret


def smooth_l1_loss(input, target, size_average=None, reduce=None, reduction='mean', beta=1.0):
    if reduce is not None or size_average is not None:
        reduction = _get_reduce_string(size_average, reduce)

    input_ms = cast_to_ms_tensor(input)
    target = cast_to_ms_tensor(target)
    output = ms.ops.smooth_l1_loss(input_ms, target, beta, reduction)
    return cast_to_adapter_tensor(output)

def l1_loss(input, target, size_average=None, reduce=None, reduction="mean"):
    """
    Function that takes the mean element-wise absolute value difference.
    """
    if reduce is not None or size_average is not None:
        reduction = _get_reduce_string(size_average, reduce)

    input_ms = cast_to_ms_tensor(input)
    target = cast_to_ms_tensor(target)
    result = ms.ops.l1_loss(input_ms, target, reduction)
    return cast_to_adapter_tensor(result)


def mse_loss(input, target, size_average=None, reduce=None, reduction="mean"):
    """
    Measures the element-wise mean squared error.
    """
    if reduce is not None or size_average is not None:
        reduction = _get_reduce_string(size_average, reduce)

    input_ms = cast_to_ms_tensor(input)
    target = cast_to_ms_tensor(target)
    result = ms.ops.mse_loss(input_ms, target, reduction)
    return cast_to_adapter_tensor(result)

def cross_entropy(input, target, weight=None, size_average=None, ignore_index=-100,
                  reduce=None, reduction="mean", label_smoothing=0.0):
    """
    This criterion computes the cross entropy loss between input logits and target.
    """
    if reduce is not None or size_average is not None:
        reduction = _get_reduce_string(size_average, reduce)

    input_ms = cast_to_ms_tensor(input)
    target = cast_to_ms_tensor(target)
    #TODO: mindspore currently not support int64
    target_dtype = target.dtype
    if target_dtype in all_int_type:
        warning("cross_entropy: when target type is int64, there is risk of overflow.")
        target = target.astype(ms.int32)
    weight = cast_to_ms_tensor(weight)
    # unsupport float64
    result = ms.ops.cross_entropy(input_ms, target, weight, ignore_index, reduction, label_smoothing)
    return cast_to_adapter_tensor(result)

def ctc_loss(log_probs, targets, input_lengths, target_lengths, blank=0, reduction='mean', zero_infinity=False):
    log_probs = cast_to_ms_tensor(log_probs)
    targets = cast_to_ms_tensor(targets)
    #TODO: length do not support tuple
    if not isinstance(input_lengths, Tensor) or not isinstance(target_lengths, Tensor):
        raise TypeError("'input_lengths' and 'target_lengths' only support Tensor now")

    input_lengths = cast_to_ms_tensor(input_lengths)
    target_lengths = cast_to_ms_tensor(target_lengths)

    if targets.dtype not in (ms.int32, ms.int64) \
            or not (targets.dtype == input_lengths.dtype and targets.dtype == target_lengths.dtype):
        targets = targets.astype(ms.int64)
        input_lengths = input_lengths.astype(ms.int64)
        target_lengths = target_lengths.astype(ms.int64)
    result, _ = ms.ops.ctc_loss(log_probs, targets, input_lengths, target_lengths, blank, reduction, zero_infinity)
    return cast_to_adapter_tensor(result)

def gaussian_nll_loss(input, target, var, full=False, eps=1e-06, reduction='mean'):
    input_ms = cast_to_ms_tensor(input)
    target = cast_to_ms_tensor(target)
    var = cast_to_ms_tensor(var)
    rlt = ms.ops.gaussian_nll_loss(input_ms, target, var, full, eps, reduction)
    return cast_to_adapter_tensor(rlt)

def hinge_embedding_loss(input, target, margin=1.0, size_average=None, reduce=None, reduction='mean'):
    input_ms = cast_to_ms_tensor(input)
    target = cast_to_ms_tensor(target)
    if reduce is not None or size_average is not None:
        reduction = _get_reduce_string(size_average, reduce)
    if input_ms.dtype in all_int_type or target.dtype in all_int_type:
        input_ms = input_ms.astype(ms.float32)
        target = target.astype(ms.float32)
        rlt = ms.ops.hinge_embedding_loss(input_ms, target, float(margin), reduction)
        rlt = rlt.astype(ms.int64)
    else:
        rlt = ms.ops.hinge_embedding_loss(input_ms, target, float(margin), reduction)
    return cast_to_adapter_tensor(rlt)

def margin_ranking_loss(input1, input2, target, margin=0, size_average=None, reduce=None, reduction='mean'):
    input1 = cast_to_ms_tensor(input1)
    input2 = cast_to_ms_tensor(input2)
    target = cast_to_ms_tensor(target)
    if reduce is not None or size_average is not None:
        reduction = _get_reduce_string(size_average, reduce)
    rlt = ms.ops.margin_ranking_loss(input1, input2, target, float(margin), reduction)
    return cast_to_adapter_tensor(rlt)

def multilabel_margin_loss(input, target, size_average=None, reduce=None, reduction='mean'):
    input_ms = cast_to_ms_tensor(input)
    target = cast_to_ms_tensor(target)
    if target.dtype != ms.int32:
        target = target.astype(ms.int32)
    if reduce is not None or size_average is not None:
        reduction = _get_reduce_string(size_average, reduce)
    #todo: ms.ops.multilabel_margin_loss not on CPU.
    rlt = ms.ops.multilabel_margin_loss(input_ms, target, reduction)
    return cast_to_adapter_tensor(rlt)

def multilabel_soft_margin_loss(input, target, weight=None, size_average=None, reduce=None, reduction='mean'):
    input_ms = cast_to_ms_tensor(input)
    target = cast_to_ms_tensor(target)
    weight = cast_to_ms_tensor(weight)
    if reduce is not None or size_average is not None:
        reduction = _get_reduce_string(size_average, reduce)
    rlt = ms.ops.multilabel_soft_margin_loss(input_ms, target, weight, reduction)
    return cast_to_adapter_tensor(rlt)

def nll_loss(input, target, weight=None, size_average=None, ignore_index=-100,
             reduce=None, reduction="mean"):
    """
    The negative log likelihood loss.
    """
    if reduce is not None or size_average is not None:
        reduction = _get_reduce_string(size_average, reduce)

    input_ms = cast_to_ms_tensor(input)
    target = cast_to_ms_tensor(target)
    weight = cast_to_ms_tensor(weight)
    result = ms.ops.nll_loss(input_ms, target, weight, ignore_index, reduction, label_smoothing=0.0)
    return cast_to_adapter_tensor(result)

def kl_div(input, target, size_average=None, reduce=None, reduction="mean", log_target=False):
    """
    The `Kullback-Leibler divergence Loss.
    <https://en.wikipedia.org/wiki/Kullback-Leibler_divergence>`
    """
    if size_average is not None or reduce is not None:
        reduction = _get_reduce_string(size_average, reduce)

    input_ms = cast_to_ms_tensor(input)
    target = cast_to_ms_tensor(target)

    # ms.ops.kl_div no `log_target`
    if log_target is True:
        loss_pointwise = target.exp() * (target - input_ms)
        if reduction == "mean":  # default
            result = loss_pointwise.mean()
        elif reduction == "batchmean":  # mathematically correct
            result = loss_pointwise.sum() / input_ms.shape[0]
        elif reduction == "sum":
            result = loss_pointwise.sum()
        else:  # reduction == "none"
            result = loss_pointwise
    else:
        result = ms.ops.kl_div(input_ms, target, reduction)
    return cast_to_adapter_tensor(result)


def binary_cross_entropy(input, target, weight=None, size_average=None, reduce=None, reduction="mean"):
    """
    Function that measures the Binary Cross Entropy between the target and input probabilities.
    """
    if size_average is not None or reduce is not None:
        reduction = _get_reduce_string(size_average, reduce)

    input_ms = cast_to_ms_tensor(input)
    target = cast_to_ms_tensor(target)
    weight = cast_to_ms_tensor(weight)
    # unsupport float64
    result = ms.ops.binary_cross_entropy(input_ms, target, weight, reduction)
    return cast_to_adapter_tensor(result)

def binary_cross_entropy_with_logits(input, target, weight=None, size_average=None,
                                     reduce=None, reduction="mean", pos_weight=None):
    """
    Function that measures Binary Cross Entropy between target and input logits.
    """
    if size_average is not None or reduce is not None:
        reduction = _get_reduce_string(size_average, reduce)

    input_ms = cast_to_ms_tensor(input)
    target = cast_to_ms_tensor(target)
    weight = cast_to_ms_tensor(weight)
    pos_weight = cast_to_ms_tensor(pos_weight)
    # TODO: ms.ops.binary_cross_entropy_with_logits do not accept `weight` and `pos_weight` to be None
    if weight is None or pos_weight is None:
        ones_input = ms.ops.ones_like(input_ms, dtype=ms.float32)
        if weight is None:
            weight = ones_input
        if pos_weight is None:
            pos_weight = ones_input
    # unsupport float64
    result = ms.ops.binary_cross_entropy_with_logits(input_ms, target, weight, pos_weight, reduction)
    return cast_to_adapter_tensor(result)


@_primexpr
# @lru_cache(_GLOBAL_LRU_CACHE_SIZE_NN)
def _upsample_common_check(size, scale_factor):
    if size is None and scale_factor is None:
        raise ValueError("either size or scale_factor should be defined.")

    if size is not None and scale_factor is not None:
        raise ValueError("only one of size or scale_factor should be defined.")

@_primexpr
# @lru_cache(_GLOBAL_LRU_CACHE_SIZE_NN)
def _upsample_common_process_size(size, scale_factor, shape):
    input_shape = list(shape)
    input_rank = len(shape)
    if scale_factor is not None:
        size_ = input_shape[2:]
        if isinstance(scale_factor, (tuple, list)):
            if len(scale_factor) != input_rank - 2:
                raise ValueError("length of `scale_factor` not match input rank")
            for i, _ in enumerate(size_):
                size_[i] *= scale_factor[i]
                size_[i] = int(size_[i])
        else:
            for i, _ in enumerate(size_):
                size_[i] *= scale_factor
                size_[i] = int(size_[i])
    else:
        if not isinstance(size, (int, list, tuple)):
            raise TypeError("`size` should be in types of int, list and tuple.")
        if isinstance(size, int):
            size_ = [size for i in range(2, input_rank)]
        else:
            if len(size) != input_rank - 2:
                raise ValueError(
                    "Input and output must have the same number of spatial dimensions, but got "
                    f"input with spatial dimensions of {list(input_shape[2:])} and output size of {size}. "
                    "Please provide input tensor in (N, C, d1, d2, ...,dK) format and "
                    "output size in (o1, o2, ...,oK) format.")
            size_ = size
    return tuple(size_)

def upsample_nearest(input, size=None, scale_factor=None):
    _upsample_common_check(size, scale_factor)
    input_shape = input.shape
    # ms.ops.interpolate not support `scale_factor`, so here need so process.
    size_ = _upsample_common_process_size(size, scale_factor, input_shape)

    input_ms = cast_to_ms_tensor(input)
    result = ms.ops.interpolate(input_ms, size_, None, 'nearest')
    return cast_to_adapter_tensor(result)

def upsample_bilinear(input, size=None, scale_factor=None, *, align_corners=True):
    input_shape = input.shape

    if len(input_shape) != 4:
        raise ValueError("Until now, upsample_bilinear only support 4-D input.")

    _upsample_common_check(size, scale_factor)
    size_ = _upsample_common_process_size(size, scale_factor, input_shape)

    input_ms = cast_to_ms_tensor(input)

    result = ms.ops.interpolate(input_ms, size=size_, align_corners=align_corners, mode="bilinear")
    return cast_to_adapter_tensor(result)

def pairwise_distance(x1, x2, p=2.0, eps=1e-06, keepdim=False):
    x1 = cast_to_ms_tensor(x1)
    x2 = cast_to_ms_tensor(x2)
    input = x1 - x2 + eps
    input_p = ms.ops.pow(ms.ops.abs(input), p)
    input_p_sum = input_p.sum(axis=-1, keepdims=keepdim)
    out = ms.ops.pow(input_p_sum, 1.0 / p)
    return cast_to_adapter_tensor(out)


@_primexpr
# @lru_cache(_GLOBAL_LRU_CACHE_SIZE_NN)
def get_broadcast_shape(x_shape, y_shape):
    out = np.ones(x_shape) + np.ones(y_shape)
    return out.shape

def cosine_similarity(x1, x2, dim=1, eps=1e-08):
    x1 = cast_to_ms_tensor(x1)
    x2 = cast_to_ms_tensor(x2)
    if x1.shape == x2.shape:
        out = ms.ops.cosine_similarity(x1, x2, dim, eps)
        return cast_to_adapter_tensor(out)
    broadcast_shape = get_broadcast_shape(x1.shape, x2.shape)
    x1 = ms.ops.broadcast_to(x1, broadcast_shape)
    x2 = ms.ops.broadcast_to(x2, broadcast_shape)
    out = ms.ops.cosine_similarity(x1, x2, dim, eps)
    return cast_to_adapter_tensor(out)


def pdist(input, p=2):
    #TODO: ms.ops.pdist is not on Ascend.
    if is_under_ascend_context():
        inp_dim = input.dim()
        if inp_dim != 2:
            raise RuntimeError(f"pdist only supports 2D tensors, got: {inp_dim}D")
        if p < 0:
            raise RuntimeError("pdist only supports non-negative p values")

        input_ms = cast_to_ms_tensor(input)
        n, m = input_ms.shape
        x = input_ms.broadcast_to((n, n, m)).astype(ms.float32)
        y = x.transpose(1, 0, 2)
        norm = ms.ops.pow(ms.ops.abs(x-y), p)
        norm = norm.sum(axis=-1)
        if p > 0:
            norm = ms.ops.pow(norm, 1.0/p)
        select = np.ones([n, n])
        select = np.triu(select, 1).astype(np.bool8)
        select_t = ms.Tensor(select)
        out = ms.ops.masked_select(norm, select_t)
        if input_ms.dtype == ms.float64:
            warning("pdist: when input is float64, there is risk that the data will be truncated.")
            out = out.astype(input_ms.dtype)
    else:
        input_ms = cast_to_ms_tensor(input)
        out = ms.ops.pdist(input_ms, float(p))
    return cast_to_adapter_tensor(out)

@_primexpr
# @lru_cache(_GLOBAL_LRU_CACHE_SIZE_NN)
def _check_dropout_p(p):
    if p < 0.0 or p > 1.0:
        raise ValueError("dropout probability has to be between 0 and 1, " "but got {}".format(p))


def dropout1d(input, p=0.5, training=True, inplace=False):
    _check_dropout_p(p)
    if not training:
        return input

    inp_dim = input.dim()
    if inp_dim not in (2, 3):
        raise RuntimeError(f"dropout1d: Expected 2D or 3D input, but received a {inp_dim}D input. "
                           "Note that dropout1d exists to provide channel-wise dropout on inputs with 1 "
                           "spatial dimension, a channel dimension, and an optional batch dimension "
                           "(i.e. 2D or 3D inputs).")

    input_ms = cast_to_ms_tensor(input)
    out = ms.ops.dropout1d(input_ms, p)
    return _inplace_assign_pynative(input, inplace, out, "dropout1d")


def dropout2d(input, p=0.5, training=True, inplace=False):
    _check_dropout_p(p)
    if not training:
        return input

    inp_dim = input.dim()
    if inp_dim not in (3, 4):
        warn_msg = (f"dropout2d: Received a {inp_dim}-D input to dropout2d, which is deprecated " \
                    "and will result in an error in a future release. To retain the behavior " \
                    "and silence this warning, please use dropout instead. Note that dropout2d " \
                    "exists to provide channel-wise dropout on inputs with 2 spatial dimensions, " \
                    "a channel dimension, and an optional batch dimension (i.e. 3D or 4D inputs).")
        warning(warn_msg)

    input_ms = cast_to_ms_tensor(input)
    if inp_dim == 3:
        input_ms = input_ms.expand_dims(0)
        out = ms.ops.dropout2d(input_ms, p)
        out = out.squeeze(0)
    else:
        out = ms.ops.dropout2d(input_ms, p)
    return _inplace_assign_pynative(input, inplace, out, "dropout2d")


def dropout3d(input, p=0.5, training=True, inplace=False):
    _check_dropout_p(p)
    if not training:
        return input

    inp_dim = input.dim()
    if inp_dim not in (4, 5):
        warn_msg = (f"dropout3d: Received a {inp_dim}-D input to dropout3d, which is deprecated " \
                    "and will result in an error in a future release. To retain the behavior " \
                    "and silence this warning, please use dropout instead. Note that dropout3d " \
                    "exists to provide channel-wise dropout on inputs with 3 spatial dimensions, " \
                    "a channel dimension, and an optional batch dimension (i.e. 4D or 5D inputs).")
        warning(warn_msg)

    is_batched = inp_dim == 5
    input_ms = cast_to_ms_tensor(input)
    if not is_batched:
        input_ms = input_ms.expand_dims(0)
        out = ms.ops.dropout3d(input_ms, p)
        out = out.squeeze(0)
    else:
        out = ms.ops.dropout3d(input_ms, p)
    return _inplace_assign_pynative(input, inplace, out, "dropout3d")


def feature_dropout(input, p, train, inplace=False):
    _ndim = input.ndim
    if _ndim == 2:
        return dropout(input, p, train, inplace)
    elif _ndim == 3:
        return dropout1d(input, p, train, inplace)
    elif _ndim == 4:
        return dropout2d(input, p, train, inplace)
    elif _ndim == 5:
        return dropout3d(input, p, train, inplace)
    else:
        raise ValueError(f"For feature_dropout, input dimention must be in [2, 5], but got {_ndim}.")

def feature_dropout_(input, p, train):
    output = feature_dropout(input, p, train)
    return _nn_functional_inplace_assign(input, output, 'feature_dropout_', 'feature_dropout')

def dropout(input, p=0.5, training=True, inplace=False):
    _check_dropout_p(p)
    if not training:
        return input
    if p == 1.:
        return input.zero_adapter()
    if p == 0.:
        return input
    input_ms = cast_to_ms_tensor(input)
    out = ms.ops.dropout(input_ms, p=p)

    return _inplace_assign_pynative(input, inplace, out, "dropout")

def dropout_(input, p=0.5, training=True):
    output = dropout(input, p, training)
    return _nn_functional_inplace_assign(input, output, 'dropout_','dropout')

@_primexpr
# @lru_cache(_GLOBAL_LRU_CACHE_SIZE_NN)
def _get_alpha_dropout_const(p):
    # get transformation params
    alpha = 1.6732632423543772848170429916717
    scale = 1.0507009873554804934193349852946
    alpha_ = -alpha * scale
    a = ((1 - p) * (1 + p * alpha_ ** 2)) ** -0.5
    b = -a * alpha_ * p
    return alpha_, a, b


def alpha_dropout(input, p=0.5, training=False, inplace=False):
    _check_dropout_p(p)
    if not training:
        return input

    if p == 1.:
        return input.mul(0.0)

    alpha_, a, b = _get_alpha_dropout_const(p)
    input_x = cast_to_ms_tensor(input)
    dtype = input_x.dtype
    shape = input_x.shape
    random_array = ms.numpy.rand(shape, dtype=ms.float32)
    keep_mask = (random_array > ms.Tensor(p, ms.float32)).to(dtype)
    drop_mask = ms.ops.ones(shape, dtype) - keep_mask

    y = ms.ops.mul(input_x, keep_mask) + ms.ops.mul(drop_mask, alpha_)
    out = y * a + b
    return _inplace_assign_pynative(input, inplace, out, "alpha_dropout")

def alpha_dropout_(input, p=0.5, training=False):
    output = alpha_dropout(input, p, training)
    return _nn_functional_inplace_assign(input, output, 'alpha_dropout_', 'alpha_dropout')

def feature_alpha_dropout(input, p=0.5, training=False, inplace=False):
    _check_dropout_p(p)
    if not training:
        return input
    if p == 1.:
        return input.mul(0.0)

    alpha_, a, b = _get_alpha_dropout_const(p)

    input_x = cast_to_ms_tensor(input)
    dtype = input_x.dtype
    shape = input_x.shape
    ndim = input_x.ndim
    random_array = ms.numpy.rand(shape[:2], dtype=ms.float32)

    keep_mask = (random_array > ms.Tensor(p, ms.float32)).to(dtype)
    drop_mask = ms.ops.ones(shape[:2], dtype) - keep_mask
    keep_mask = keep_mask.reshape(shape[:2] + (1,) * (ndim - 2))
    drop_mask = drop_mask.reshape(shape[:2] + (1,) * (ndim - 2))
    keep_mask = ms.ops.broadcast_to(keep_mask, shape)
    drop_mask = ms.ops.broadcast_to(drop_mask, shape)

    y = ms.ops.mul(input_x, keep_mask) + ms.ops.mul(drop_mask, alpha_)
    out = y * a + b
    return _inplace_assign_pynative(input, inplace, out, "feature_alpha_dropout")

def feature_alpha_dropout_(input, p=0.5, training=False):
    output = feature_alpha_dropout(input, p, training)
    return _nn_functional_inplace_assign(input, output, 'feature_alpha_dropout_', 'feature_alpha_dropout')

def hardshrink(input, lambd=0.5):
    input_ms = cast_to_ms_tensor(input)
    out = ms.ops.hardshrink(input_ms, lambd)
    return cast_to_adapter_tensor(out)

def huber_loss(input, target, reduction='mean', delta=1.0):
    input_ms = cast_to_ms_tensor(input)
    target = cast_to_ms_tensor(target)

    loss = ms.ops.huber_loss(input_ms, target, reduction, delta)
    return cast_to_adapter_tensor(loss)

def soft_margin_loss(input, target, size_average=None, reduce=None, reduction='mean'):
    if size_average is not None or reduce is not None:
        reduction = _get_reduce_string(size_average, reduce)

    input_ms = cast_to_ms_tensor(input)
    target = cast_to_ms_tensor(target)
    #TODO: ms.ops.soft_margin_loss is not on CPU
    loss = ms.ops.soft_margin_loss(input_ms, target, reduction)
    return cast_to_adapter_tensor(loss)

def cosine_embedding_loss(
    input1,
    input2,
    target,
    margin=0,
    size_average=None,
    reduce=None,
    reduction="mean",
):
    if size_average is not None or reduce is not None:
        reduction = _get_reduce_string(size_average, reduce)

    input1 = cast_to_ms_tensor(input1)
    input2 = cast_to_ms_tensor(input2)
    target = cast_to_ms_tensor(target)
    loss = ms.ops.cosine_embedding_loss(input1, input2, target, margin, reduction)
    return cast_to_adapter_tensor(loss)

class _PairwiseDisFun(Module):
    def __init__(self, p=2.0, eps=1e-06, keepdim=False):
        super(_PairwiseDisFun, self).__init__()
        self.p = p
        self.eps = eps
        self.keepdim = keepdim

    def forward(self, x1, x2):
        return pairwise_distance(x1, x2, p=self.p, eps=self.eps, keepdim=self.keepdim)

def triplet_margin_loss(
    anchor,
    positive,
    negative,
    margin=1.0,
    p=2,
    eps=1e-6,
    swap=False,
    size_average=None,
    reduce=None,
    reduction="mean",
):
    if size_average is not None or reduce is not None:
        reduction = _get_reduce_string(size_average, reduce)

    if is_under_gpu_context():
        anchor, positive, negative = cast_to_ms_tensor((anchor, positive, negative))
        ndim = anchor.ndim
        #TODO: ms.ops.triplet_margin_loss only on GPU, and not support 1D input.
        if ndim == 1:
            anchor = anchor.expand_dims(0)
            positive = positive.expand_dims(0)
            negative = negative.expand_dims(0)
            loss = ms.ops.triplet_margin_loss(anchor, positive, negative, margin, p, eps, swap, reduction)
            if reduction == 'none':
                loss = loss.squeeze(0)
        else:
            loss = ms.ops.triplet_margin_loss(anchor, positive, negative, margin, p, eps, swap, reduction)
        #TODO: mindspore.ops.triplet_margin_loss return float32 when input is float64, wait to fix.
        if anchor.dtype == ms.float64:
            loss = loss.astype(ms.float64)
    else:
        distance_function = _PairwiseDisFun(p, eps)
        loss = triplet_margin_with_distance_loss(anchor, positive, negative, distance_function=distance_function,
                                                 margin=margin,swap=swap, reduction=reduction)
    return cast_to_adapter_tensor(loss)

def multi_margin_loss(
    input,
    target,
    p=1,
    margin=1.0,
    weight=None,
    size_average=None,
    reduce=None,
    reduction="mean",
):
    if size_average is not None or reduce is not None:
        reduction = _get_reduce_string(size_average, reduce)

    input_ms = cast_to_ms_tensor(input)
    target = cast_to_ms_tensor(target)
    weight = cast_to_ms_tensor(weight)

    #TODO: 'margin' in ms.ops.multi_margin_loss must be int, but ops.MultiMarginLoss must be float.
    margin = float(margin)
    loss = _get_cache_prim(ms.ops.MultiMarginLoss)(p, margin, reduction)

    #`input` in ms.ops.MultiMarginLoss only support (N,C), unsupport (C)
    ndim = input_ms.ndim
    if ndim == 1:
        input_ms = input_ms.expand_dims(0)
        target = target.expand_dims(0)
        output = loss(input_ms, target, weight)
        if reduction == 'none':
            output = output.squeeze(0)
    else:
        output = loss(input_ms, target, weight)
    return cast_to_adapter_tensor(output)

@_primexpr
# @lru_cache(_GLOBAL_LRU_CACHE_SIZE_NN)
def _get_avg_pool2d_const(kernel_size, stride, padding):
    if stride is None:
        stride = kernel_size

    padding = padding if isinstance(padding, tuple) else _pair(padding)
    return kernel_size, stride, padding

@_primexpr
# @lru_cache(_GLOBAL_LRU_CACHE_SIZE_NN)
def _get_avg_pool2d_const_for_ops(kernel_size, stride, padding, divisor_override):
    stride = stride if (stride is not None) else kernel_size
    divisor_override = divisor_override if (divisor_override is not None) else 0

    if isinstance(padding, int):
        padding = _quadruple(padding)
    elif isinstance(padding, (tuple, list)):
        if len(padding) == 1:
            padding = _quadruple(padding)
        elif len(padding) == 2:
            padding = (padding[0], padding[0], padding[1], padding[1])
        else:
            raise ValueError("For avg_pool2d, padding must either be a single int, or a tuple of two ints")

    return stride, padding, divisor_override


@_primexpr
# @lru_cache(_GLOBAL_LRU_CACHE_SIZE_NN)
def _check_avg_pool2d_param_value(kernel_size, stride):
    if isinstance(kernel_size, int):
        if kernel_size > 255:
            return False
    elif isinstance(kernel_size, tuple):
        for item in kernel_size:
            if item > 255:
                return False

    if stride is None:
        return True
    elif isinstance(stride, int):
        if stride > 63:
            return False
    elif isinstance(stride, tuple):
        for item in stride:
            if item > 63:
                return False
    return True


def avg_pool2d(input, kernel_size, stride=None, padding=0, ceil_mode=False, count_include_pad=True,
               divisor_override=None):
    ndim = input.ndim
    input_ms = cast_to_ms_tensor(input)
    # ms.ops.avg_pool2d only support kernel_size<=255, stride <= 63
    if _check_avg_pool2d_param_value(kernel_size, stride):
        _stride, _padding, _divisor_override = _get_avg_pool2d_const_for_ops(kernel_size, stride, padding,
            divisor_override)
        if ndim == 3:
            input_ms = input_ms.expand_dims(0)
            out = ms.ops.avg_pool2d(input_ms, kernel_size, _stride, _padding, ceil_mode, count_include_pad,
                _divisor_override)
            out = out.squeeze(0)
        else:
            out = ms.ops.avg_pool2d(input_ms, kernel_size, _stride, _padding, ceil_mode, count_include_pad,
                _divisor_override)
        return cast_to_adapter_tensor(out)

    if ceil_mode is True or count_include_pad is False or divisor_override is not None:
        raise ValueError("In avg_pool2d, when `kernel_size` > 255 or `stride` >63, \
              `ceil_mode` must be False, `count_include_pad` must be True, divisor_override must be None.")
    _kernel_size, _stride, _padding = _get_avg_pool2d_const(kernel_size, stride, padding)

    # TODO: to use ms.ops.avgpool with `pad_mode` supported 'pad'
    avg_pool_ops = _get_cache_prim(ms.ops.AvgPool)(kernel_size=_kernel_size, strides=_stride, pad_mode='valid')

    if ndim == 3:
        input_ms = input_ms.expand_dims(0)
        input_ms = _do_pad(input_ms, _padding)
        out = avg_pool_ops(input_ms)
        out = out.squeeze(0)
    else:
        input_ms = _do_pad(input_ms, _padding)
        out = avg_pool_ops(input_ms)
    return cast_to_adapter_tensor(out)

@_primexpr
# @lru_cache(_GLOBAL_LRU_CACHE_SIZE_NN)
def _get_local_response_norm_const(x_dim, size):
    if x_dim < 3:
        raise ValueError("Expected 3D or higher dimensionality"
                         f"input (got {x_dim} dimensions)")

    if x_dim == 3:
        return ((size//2, (size-1)//2), (0, 0))

    return ((size//2, (size-1)//2), (0, 0), (0, 0))

def local_response_norm(input, size, alpha=0.0001, beta=0.75, k=1.0):
    if len(input.shape) == 0:
        return input

    dim = input.dim()
    _pad = _get_local_response_norm_const(dim, size)

    input_ms = cast_to_ms_tensor(input)
    div = ms.ops.mul(input_ms, input_ms).expand_dims(axis=1)
    if dim == 3:
        div = _do_pad(div, _pad)
        div = ms.ops.avg_pool2d(div, (size, 1), stride=1).squeeze(1)
    else:
        shape = input_ms.shape
        div = div.view(shape[0], 1, shape[1], shape[2], -1)
        div = _do_pad(div, _pad)
        div = _get_cache_prim(ms.ops.AvgPool3D)((size, 1, 1), strides=1)(div).squeeze(1)
        div = div.view(shape)
    div = div * alpha + k
    div = ms.ops.pow(div, beta)
    output = input_ms / div
    return cast_to_adapter_tensor(output)


def one_hot(input, num_classes=-1):
    if num_classes == -1:
        depth = int(input.max()) + 1
    else:
        depth = num_classes

    input_ms = cast_to_ms_tensor(input)
    on_value = ms.Tensor(1.0, ms.float32)
    off_value = ms.Tensor(0.0, ms.float32)
    out = ms.ops.one_hot(input_ms, depth, on_value, off_value).astype(ms.int64)
    return cast_to_adapter_tensor(out)


def pixel_shuffle(input, upscale_factor):
    dim = input.dim()
    if dim < 3:
        raise RuntimeError("pixel_shuffle expects input to have at least 3 dimensions, "
                           "but got input with {} dimension(s)".format(dim))
    input_ms = cast_to_ms_tensor(input)
    out = ms.ops.pixel_shuffle(input_ms, upscale_factor)
    return cast_to_adapter_tensor(out)


def pixel_unshuffle(input, downscale_factor):
    dim = input.dim()
    if dim < 3:
        raise RuntimeError("pixel_shuffle expects input to have at least 3 dimensions, "
                           "but got input with {} dimension(s)".format(dim))

    input_ms = cast_to_ms_tensor(input)
    out = ms.ops.pixel_unshuffle(input_ms, downscale_factor)
    return cast_to_adapter_tensor(out)

@_primexpr
def _process_interpolate_scale_factor(scale_factor):
    if scale_factor is not None:
        if isinstance(scale_factor, (list, tuple)):
            scale_factor = [float(scale) for scale in scale_factor]
            scale_factor = tuple(scale_factor)
        else:
            scale_factor = float(scale_factor)
    return scale_factor

def interpolate(input,
                size=None,
                scale_factor=None,
                mode='nearest',
                align_corners=None,
                recompute_scale_factor=None,
                antialias=False):

    unsupported_attr(recompute_scale_factor)
    unsupported_attr(antialias)

    size = _check_int_size(size, "interpolate")

    if mode in ("nearest", "area", "nearest-exact"):
        if align_corners is not None:
            raise ValueError(
                "align_corners option can only be set with the "
                "interpolating modes: linear | bilinear | bicubic | trilinear"
            )
        align_corners = False
    else:
        if align_corners is None:
            align_corners = False

    if antialias:
        raise NotImplementedError("antialias in interpolate is not supported to True.")

    # TODO:　not support `antialias` until now.
    if antialias and not (mode in ("bilinear", "bicubic") and input.ndim == 4):
        raise ValueError("Anti-alias option is only supported for bilinear and bicubic modes")

    if mode == 'nearest':
        return upsample_nearest(input, size, scale_factor)
    # TODO: 'bilinear' only support 4D input. 3D, 5D are not support until now.
    if mode == 'bilinear':
        if recompute_scale_factor:
            input_ms = cast_to_ms_tensor(input)
            out = ms.ops.interpolate(input_ms, size=None, scale_factor=scale_factor, mode=mode,
                align_corners=align_corners, recompute_scale_factor=True)
            return cast_to_adapter_tensor(out)
        else:
            return upsample_bilinear(input, size, scale_factor, align_corners=align_corners)

    input_ms = cast_to_ms_tensor(input)
    if mode in ('linear', 'bicubic'):
        # TODO: when mode=bicubic, align_corners=False, mindspore result is the same as TensorFlow result,
        # but different from the result of PyTorch
        size =_upsample_common_process_size(size, scale_factor, input.shape)
        scale_factor = None
    elif mode in ('nearest-exact', 'area'):
        align_corners = None

    scale_factor = _process_interpolate_scale_factor(scale_factor)
    out = ms.ops.interpolate(input_ms, size, scale_factor, mode, align_corners, recompute_scale_factor)
    return cast_to_adapter_tensor(out)


@_primexpr
def _get_embedding_padding_idx(weight_shape, padding_idx):
    if padding_idx is not None:
        if padding_idx > 0:
            if padding_idx >= weight_shape[0]:
                raise ValueError("Padding_idx must be within num_embeddings")
        elif padding_idx < 0:
            if padding_idx < -weight_shape[0]:
                raise ValueError("Padding_idx must be within num_embeddings")
            padding_idx = weight_shape[0] + padding_idx
    return padding_idx


def embedding(
    input,
    weight,
    padding_idx=None,
    max_norm=None,
    norm_type=2.0,
    scale_grad_by_freq=False,
    sparse=False
):
    unsupported_attr(scale_grad_by_freq)
    unsupported_attr(sparse)

    input_ms = cast_to_ms_tensor(input)

    padding_idx = _get_embedding_padding_idx(weight.shape, padding_idx)

    # TODO: norm_type only support '2', others are not supported yet
    if norm_type != 2:
        raise NotImplementedError("`norm_type` beside 2 is not supported until now.")

    if max_norm:
        weight = _get_cache_prim(ms.nn.ClipByNorm)(axis=1)(weight, clip_norm=ms.ops.scalar_to_tensor(max_norm))

    if padding_idx:
        update = ms.ops.stop_gradient(ms.ops.expand_dims(weight[padding_idx], 0))
        indices = ms.ops.fill(ms.int32, update.shape, padding_idx)
        weight = ms.ops.tensor_scatter_elements(weight, indices, update, axis=0)

    out = ms.ops.gather(weight, input_ms, axis=0)

    return cast_to_adapter_tensor(out)


def grid_sample(input, grid, mode='bilinear', padding_mode='zeros', align_corners=None):
    input_ms = cast_to_ms_tensor(input)
    grid = cast_to_ms_tensor(grid)
    if align_corners is None:
        align_corners = False
    output = ms.ops.grid_sample(input_ms, grid, mode=mode,
                                padding_mode=padding_mode, align_corners=align_corners)
    output = cast_to_adapter_tensor(output)
    return output


@_primexpr
# @lru_cache(_GLOBAL_LRU_CACHE_SIZE_NN)
def _check_conv1d_input_shape(input_shape):
    if len(input_shape) != 3:
        raise ValueError(f"For 'conv1d', the dimension of input must be 3d, but got {len(input_shape)}.")


@_primexpr
# @lru_cache(_GLOBAL_LRU_CACHE_SIZE_NN)
def _get_conv1d_const(padding):
    pad_mode = "pad"
    if isinstance(padding, str):
        pad_mode = padding
        padding = 0
    return pad_mode, padding


def conv1d(input, weight, bias=None, stride=1, padding=0, dilation=1, groups=1):
    # TODO: not support float64, change to float32 now
    input_ms = cast_to_ms_tensor(input)
    # do not cast weight because will lose gradient
    # weight_ms = cast_to_ms_tensor(weight)
    weight_ms = weight

    input_ndim = input_ms.ndim
    if input_ndim == 2:
        input_ms = input_ms.expand_dims(0)

    is_float64 = False
    if input_ms.dtype in (ms.float64, ms.double):
        input_ms = input_ms.astype(ms.float32)
        weight_ms = weight_ms.astype(ms.float32)
        is_float64 = True

    pad_mode, padding = _get_conv1d_const(padding)
    #TODO: after ms.ops.conv1d support groups > 1, remove the code below.
    C_in = input_ms.shape[-2]
    C_out = weight_ms.shape[0]
    if is_under_ascend_context() and groups > 1 and (groups != C_in or groups != C_out):
        _input_group_size = input_ms.shape[1] // groups
        _weight_group_size = weight_ms.shape[0] // groups
        input_ms = ms.ops.split(input_ms, _input_group_size, 1)
        weight_ms = ms.ops.split(weight_ms, _weight_group_size, 0)
        outs = ()
        for i in range(groups):
            outp = ms.ops.conv1d(input_ms[i], weight_ms[i], None, stride, pad_mode, padding, dilation, 1)
            outs = outs + (outp,)
        output = ms.ops.concat(outs, 1)
    else:
        output = ms.ops.conv1d(input_ms, weight_ms, None, stride, pad_mode, padding, dilation, groups)
    if bias is not None:
        # TODO: ms.ops.biasadd also not support float64
        if bias.dtype != output.dtype:
            bias = bias.astype(output.dtype)
        output = ms.ops.bias_add(output, bias)

    if is_float64:
        output = output.astype(ms.float64)

    if input_ndim == 2:
        output = output.squeeze(0)

    return cast_to_adapter_tensor(output)


@_primexpr
# @lru_cache(_GLOBAL_LRU_CACHE_SIZE_NN)
def _get_conv2d_const(stride, padding, dilation):
    if isinstance(stride, int):
        stride = (stride, stride)
    elif len(stride)==1:
        stride = (stride[0], stride[0])
    pad_mode = "pad"
    if isinstance(padding, int):
        padding = (padding, padding)
    elif isinstance(padding, tuple):
        if len(padding)==1:
            padding = (padding[0], padding[0])

    else:
        pad_mode = padding
        padding = 0
    if isinstance(dilation, int):
        dilation = (dilation, dilation)
    elif len(dilation) == 1:
        dilation = (dilation[0], dilation[0])
    return pad_mode, stride, padding, dilation


def conv2d(input, weight, bias=None, stride=1, padding=0, dilation=1, groups=1):
    # TODO: not support float64, change to float32 now
    # TODO: on Ascend, until now, `groups` beside 1, the result may be wrong.
    input_ms = cast_to_ms_tensor(input)
    # can not cast 'weight' to 'weight_ms', because it will convert Parameter to Tensor, and will lost gradient.
    # ms.ops.conv do not use tensor function of ms.ops.con2d, so without cast_to_ms_tensor(weight), no effect
    # weight_ms = cast_to_ms_tensor(weight)
    weight_ms = weight
    is_float64 = False
    if input_ms.dtype in (ms.float64, ms.double):
        input_ms = input_ms.astype(ms.float32)
        weight_ms = weight_ms.astype(ms.float32)
        is_float64 = True

    _pad_mode, _stride, _padding, _dilation = _get_conv2d_const(stride, padding, dilation)
    #TODO: after ms.ops.conv2d support groups > 1, remove the code below.
    C_in = input_ms.shape[-3]
    C_out = weight_ms.shape[0]
    if is_under_ascend_context() and groups > 1 and (groups != C_in or groups != C_out):
        _input_group_size = input_ms.shape[1] // groups
        _weight_group_size = weight_ms.shape[0] // groups
        input_ms = ms.ops.split(input_ms, _input_group_size, 1)
        weight_ms = ms.ops.split(weight_ms, _weight_group_size, 0)
        outs = ()
        for i in range(groups):
            outp = ms.ops.conv2d(input_ms[i], weight_ms[i], None, _stride, _pad_mode, _padding, _dilation, 1)
            outs = outs + (outp,)
        output = ms.ops.concat(outs, 1)
    else:
        output = ms.ops.conv2d(input_ms, weight_ms, None, _stride, _pad_mode, _padding, _dilation, groups)
    if bias is not None:
        # TODO: ms.ops.biasadd also not support float64
        if bias.dtype != output.dtype:
            bias = bias.astype(output.dtype)
        output = ms.ops.bias_add(output, bias)

    if is_float64:
        output = output.astype(ms.float64)

    return cast_to_adapter_tensor(output)


@_primexpr
# @lru_cache(_GLOBAL_LRU_CACHE_SIZE_NN)
def _get_maxpool2d_arg_to_3d(arg, arg_name, set_value):
    if isinstance(arg, int):
        _arg = (arg, arg, set_value)
    elif isinstance(arg, (tuple, list)):
        if len(arg) == 1:
            _arg = (arg[0], arg[0], set_value)
        elif len(arg) == 2:
            _arg = tuple(arg) + (set_value,)
        else:
            raise ValueError(f"For max_pool2d() {arg_name} must be either be a single int, or a tuple of two ints, "
                             f"but got size {len(arg)}.")
    else:
        raise ValueError(f"An error occurred. Please check the validity of the value of {arg_name} in max_pool2d().")
    return _arg

@_primexpr
# @lru_cache(_GLOBAL_LRU_CACHE_SIZE_NN)
def _get_maxpool2d_arg_to_2d(arg, arg_name):
    if isinstance(arg, int):
        _arg = (arg, arg)
    elif isinstance(arg, (tuple, list)):
        if len(arg) == 1:
            _arg = (arg[0], arg[0])
        elif len(arg) == 2:
            _arg = tuple(arg)
        else:
            raise ValueError(f"For max_pool2d() {arg_name} must be either be a single int, or a tuple of two ints, "
                             f"but got size {len(arg)}.")
    else:
        raise ValueError(f"An error occurred. Please check the validity of the value of {arg_name} in max_pool2d().")
    return _arg

def max_pool2d(input, kernel_size, stride=None, padding=0, dilation=1, ceil_mode=False, return_indices=False):
    input_ms = cast_to_ms_tensor(input)
    if input_ms.dtype in all_int_type:
        raise TypeError("'max_pool2d' not implemented for int.")

    stride = stride if (stride is not None) else kernel_size
    input_shape = input_ms.shape
    ndim = input_ms.ndim
    min_ndim = 3
    max_ndim = 4
    if return_indices or ceil_mode or dilation != 1 or padding != 0:
        _kernel_size = _get_maxpool2d_arg_to_3d(kernel_size, "kernel_size", 1)
        _stride = _get_maxpool2d_arg_to_3d(stride, "stride", 1)
        _padding = _get_maxpool2d_arg_to_3d(padding, "padding", 0)
        _dilation = _get_maxpool2d_arg_to_3d(dilation, "dilation", 1)
        if ndim == min_ndim:
            _input_ms = input_ms.reshape((1,) + input_shape + (1,))
        elif ndim == max_ndim:
            _input_ms = input_ms.reshape(input_shape + (1,))
        else:
            raise TypeError(f"max_pool2d() Expected 3D or 4D input tensor, but got input.ndim == {ndim}.")

        # ms.ops.max_pool2d has poor performance, also have problem when return_indices==True in CPU/GPU,
        # and only supported float16 in ascend.
        out = ms.ops.max_pool3d(_input_ms, _kernel_size, _stride, _padding, _dilation, ceil_mode, return_indices)
        if return_indices:
            output, argmax = out
            return cast_to_adapter_tensor((output.reshape(output.shape[max_ndim - ndim:max_ndim]),
                                           argmax.reshape(argmax.shape[max_ndim - ndim:max_ndim])))
        return cast_to_adapter_tensor(out.reshape(out.shape[max_ndim - ndim:max_ndim]))

    # To accelerate
    _kernel_size = _get_maxpool2d_arg_to_2d(kernel_size, "kernel_size")
    _stride = _get_maxpool2d_arg_to_2d(stride, "stride")
    _max_pool = _get_cache_prim(ms.ops.MaxPool)(kernel_size=_kernel_size, strides=_stride, pad_mode='valid')

    if ndim == min_ndim:
        input_ms = input_ms.expand_dims(0)
        out = _max_pool(input_ms)
        out = out.squeeze(0)
    elif ndim == max_ndim:
        out = _max_pool(input_ms)
    else:
        raise TypeError(f"max_pool2d() Expected 3D or 4D input tensor, but got input.ndim == {ndim}.")
    return cast_to_adapter_tensor(out)


@_primexpr
# @lru_cache(_GLOBAL_LRU_CACHE_SIZE_NN)
def _get_max_unpool_args(kernel_size, stride, padding):
    if isinstance(kernel_size, list):
        kernel_size = tuple(kernel_size)

    if isinstance(stride, list):
        stride = tuple(stride)

    if isinstance(padding, list):
        padding = tuple(padding)
    return kernel_size, stride, padding

def max_unpool1d(input, indices, kernel_size, stride=None, padding=0, output_size=None):
    input_ms = cast_to_ms_tensor(input)
    indices = cast_to_ms_tensor(indices)
    kernel_size, stride, padding = _get_max_unpool_args(kernel_size, stride, padding)

    if output_size is not None:
        output_size = tuple(output_size)
    out = ms.ops.max_unpool1d(input_ms, indices, kernel_size, stride, padding, output_size)
    return cast_to_adapter_tensor(out)

def max_unpool2d(input, indices, kernel_size, stride=None, padding=0, output_size=None):
    input_ms = cast_to_ms_tensor(input)
    indices = cast_to_ms_tensor(indices)
    kernel_size, stride, padding = _get_max_unpool_args(kernel_size, stride, padding)

    if output_size is not None:
        output_size = tuple(output_size)
    out = ms.ops.max_unpool2d(input_ms, indices, kernel_size, stride, padding, output_size)
    return cast_to_adapter_tensor(out)

def max_unpool3d(input, indices, kernel_size, stride=None, padding=0, output_size=None):
    input_ms = cast_to_ms_tensor(input)
    indices = cast_to_ms_tensor(indices)
    kernel_size, stride, padding = _get_max_unpool_args(kernel_size, stride, padding)

    if output_size is not None:
        output_size = tuple(output_size)
    out = ms.ops.max_unpool3d(input_ms, indices, kernel_size, stride, padding, output_size)
    return cast_to_adapter_tensor(out)


@_primexpr
# @lru_cache(_GLOBAL_LRU_CACHE_SIZE_NN)
def _get_linear_output_shape(input_shape, weight_shape, input_rank, weight_rank):
    shape_out= ()
    if input_rank > 1:
        shape_out = shape_out + input_shape[:-1]
    if weight_rank == 2:
        shape_out = shape_out + (weight_shape[0],)
    return shape_out

@_primexpr
# @lru_cache(_GLOBAL_LRU_CACHE_SIZE_NN)
def _check_linear_shape(weight_rank, input_shape, weight_shape):
    if weight_rank not in (1, 2):
        raise ValueError("For nn.functional.linear, weight only support 2D or 1D input"
                            f"but got {weight_rank}D input")

    if input_shape[-1] != weight_shape[-1]:
        raise ValueError("For nn.functional.linear, size mismatch,"
                            f"got input with shape {input_shape}, and weight with shape {weight_shape}.")

def linear(input, weight, bias=None):
    input_ms = cast_to_ms_tensor(input)

    dtype_op = _get_cache_prim(ms.ops.DType)()
    rank_op = _get_cache_prim(ms.ops.Rank)()
    shape_op = _get_cache_prim(ms.ops.Shape)()
    reshape_op = _get_cache_prim(ms.ops.Reshape)()
    bias_add_op = _get_cache_prim(ms.ops.BiasAdd)()

    dtype1 = dtype_op(input_ms)
    dtype2 = dtype_op(weight)
    if not _check_same_type(dtype1, dtype2):
        input_ms = input_ms.astype(ms.float32)
        weight = weight.astype(ms.float32)

    input_rank, weight_rank = rank_op(input_ms), rank_op(weight)
    input_shape, weight_shape = shape_op(input_ms), shape_op(weight)
    _check_linear_shape(weight_rank, input_shape, weight_shape)

    # infers the shape of the output
    shape_out = _get_linear_output_shape(input_shape, weight_shape, input_rank, weight_rank)

    _matmul = _get_cache_prim(ms.ops.MatMul)(False, True)

    input_ms = _expand(input_ms, 2)
    weight = _expand(weight, 2)

    if rank_op(input_ms) > 2:
        input_ms = reshape_op(input_ms, (-1, input_shape[-1]))
    output = _matmul(input_ms, weight)
    if bias is not None:
        bias = _expand(bias, 1)
        # if output's rank bigger than 5, using output = ms.ops.add(output, bias)
        output = bias_add_op(output, bias)
    output = reshape_op(output, shape_out)
    return cast_to_adapter_tensor(output)

def bilinear(input1, input2, weight, bias=None):
    input1 = cast_to_ms_tensor(input1)
    input2 = cast_to_ms_tensor(input2)
    weight = cast_to_ms_tensor(weight)
    input1_shape = input1.shape
    input2_shape = input2.shape
    if len(input1_shape) != 2:
        input1 = input1.reshape((-1, input1_shape[-1]))
    _matmul = _get_cache_prim(ms.ops.MatMul)(False, False)
    x = _matmul(input1, weight.permute(1, 0, 2).reshape(weight.shape[1], -1))
    if len(input2_shape) != 2:
        input2 = input2.reshape((-1, input2_shape[-1]))
    x = ms.ops.mul(x, ms.ops.tile(input2, (1, weight.shape[0])))
    x = x.reshape(x.shape[0], weight.shape[0], -1)
    x = ms.ops.reduce_sum(x, -1)
    if bias is not None:
        bias = cast_to_ms_tensor(bias)
        # not support float64
        x = ms.ops.bias_add(x, bias)
    output = x.reshape(*input1_shape[:-1], -1)
    return cast_to_adapter_tensor(output)


def lp_pool1d(input, norm_type, kernel_size, stride=None, ceil_mode=False):
    input_ms = cast_to_ms_tensor(input)
    output = ms.ops.lp_pool1d(input_ms, norm_type, kernel_size, stride, ceil_mode)
    return cast_to_adapter_tensor(output)


def lp_pool2d(input, norm_type, kernel_size, stride=None, ceil_mode=False):
    input_ms = cast_to_ms_tensor(input)
    ndim = input_ms.ndim
    if ndim == 3:
        input_ms = input_ms.expand_dims(0)
        output = ms.ops.lp_pool2d(input_ms, norm_type, kernel_size, stride, ceil_mode)
        output = output.squeeze(0)
    else:
        output = ms.ops.lp_pool2d(input_ms, norm_type, kernel_size, stride, ceil_mode)
    return cast_to_adapter_tensor(output)


def fractional_max_pool2d(input_x, kernel_size, output_size=None, output_ratio=None, return_indices=False,
                          _random_samples=None):
    input_ms = cast_to_ms_tensor(input_x)
    if _random_samples is not None:
        _random_samples = cast_to_ms_tensor(_random_samples)
    out = ms.ops.fractional_max_pool2d(input_ms, kernel_size, output_size, output_ratio, return_indices,
                                       _random_samples)
    return cast_to_adapter_tensor(out)

def fractional_max_pool3d(input_x, kernel_size, output_size=None, output_ratio=None, return_indices=False,
                          _random_samples=None):
    input_ms = cast_to_ms_tensor(input_x)
    if _random_samples is not None:
        _random_samples = cast_to_ms_tensor(_random_samples)
    out = ms.ops.fractional_max_pool3d(input_ms, kernel_size, output_size, output_ratio, return_indices,
                                       _random_samples)
    return cast_to_adapter_tensor(out)


@_primexpr
# @lru_cache(_GLOBAL_LRU_CACHE_SIZE_NN)
def _check_avg_pool1d_param_value(kernel_size, stride, padding, ndim):
    if ndim != 3:
        return False, kernel_size, stride, padding

    flag = True
    if isinstance(kernel_size, int):
        if kernel_size > 255:
            flag = False
    elif isinstance(kernel_size, tuple):
        if len(kernel_size) != 1:
            raise ValueError("avg_pool1d() argument 'kernel_size' should contain one int.")
        kernel_size = kernel_size[0]
        if kernel_size > 255:
            flag = False

    if stride is None:
        stride = kernel_size
    elif isinstance(stride, int):
        if stride > 63:
            flag = False
    elif isinstance(stride, tuple):
        if len(stride) != 1:
            raise ValueError("avg_pool1d() argument 'stride' should contain one int.")
        stride = stride[0]
        if stride > 63:
            flag = False
    if isinstance(padding, list):
        padding = tuple(padding)

    return flag, kernel_size, stride, padding

@_primexpr
# @lru_cache(_GLOBAL_LRU_CACHE_SIZE_NN)
def _get_avgpool1d_arg_to_2d(arg, arg_name, set_value):
    if isinstance(arg, int):
        _arg = (arg, set_value)
    elif isinstance(arg, (tuple, list)):
        if len(arg) == 1:
            _arg = (arg[0], set_value)
        else:
            raise ValueError(f"For avg_pool1d() {arg_name} must be an int or int list of size 1 "
                             f"but got size {len(arg)}.")
    else:
        raise ValueError(f"An error occurred. Please check the validity of the value of {arg_name} in avg_pool1d().")
    return _arg

def avg_pool1d(input, kernel_size, stride=None, padding=0, ceil_mode=False, count_include_pad=True):
    ndim = input.ndim
    input_ms = cast_to_ms_tensor(input)

    # ms.ops.avg_pool1d only support kernel_size<=255, stride <= 63
    flag, _kernel_size, _stride, _padding = _check_avg_pool1d_param_value(kernel_size, stride, padding, ndim)
    if flag:
        out = ms.ops.avg_pool1d(input_ms, _kernel_size, _stride, _padding, ceil_mode, count_include_pad)
        return cast_to_adapter_tensor(out)

    if ceil_mode is True or count_include_pad is False:
        raise ValueError("In avg_pool1d, when `kernel_size` > 255 or `stride` > 63, \
              `ceil_mode` must be False and `count_include_pad` must be True.")

    stride = stride if (stride is not None) else kernel_size
    _kernel_size = _get_avgpool1d_arg_to_2d(kernel_size, "kernel_size", 1)
    _stride = _get_avgpool1d_arg_to_2d(stride, "stride", 1)
    _padding = _get_avgpool1d_arg_to_2d(padding, "padding", 0)

    avg_pool_ops = _get_cache_prim(ms.ops.AvgPool)(kernel_size=_kernel_size, strides=_stride, pad_mode='valid')

    input_shpae = input_ms.shape
    min_ndim = 2
    max_ndim = 3
    if ndim == min_ndim:
        input_ms = input_ms.reshape((1,) + input_shpae + (1,))
    else:
        input_ms = input_ms.reshape(input_shpae + (1,))
    input_ms = _do_pad(input_ms, _padding)
    out = avg_pool_ops(input_ms)
    return cast_to_adapter_tensor(out.reshape(out.shape[max_ndim - ndim:max_ndim]))


@_primexpr
# @lru_cache(_GLOBAL_LRU_CACHE_SIZE_NN)
def _get_avg_pool3d_const(kernel_size, stride, padding, divisor_override):
    _stride = stride if (stride is not None) else kernel_size
    _divisor_override = divisor_override if (divisor_override is not None) else 0

    if isinstance(padding, (tuple, list)):
        if len(padding) == 1:
            _padding = _sextuple(padding)
        elif len(padding) == 3:
            _padding = (padding[0], padding[0], padding[1], padding[1], padding[2], padding[2])
        else:
            raise ValueError(f"For avg_pool3d, len tuple padding should be 3, but got {padding}.")
    else:
        _padding = padding

    return _stride, _padding, _divisor_override

def avg_pool3d(input, kernel_size, stride=None, padding=0, ceil_mode=False, count_include_pad=True,
               divisor_override=None):
    input_ms = cast_to_ms_tensor(input)
    _stride, _padding, _divisor_override = _get_avg_pool3d_const(kernel_size, stride, padding, divisor_override)
    if input_ms.ndim == 4:
        _input_ms = input_ms.expand_dims(0)
        out = ms.ops.avg_pool3d(_input_ms, kernel_size, _stride, _padding, ceil_mode, count_include_pad,
                                _divisor_override)
        out = out.squeeze(0)
    else:
        out = ms.ops.avg_pool3d(input_ms, kernel_size, _stride, _padding, ceil_mode, count_include_pad,
                                _divisor_override)
    return cast_to_adapter_tensor(out)

@_primexpr
# @lru_cache(_GLOBAL_LRU_CACHE_SIZE_NN)
def _get_maxpool1d_arg_to_3d(arg, arg_name, set_value):
    if isinstance(arg, int):
        _arg = (arg, set_value, set_value)
    elif isinstance(arg, (tuple, list)):
        if len(arg) == 1:
            _arg = (arg[0], set_value, set_value)
        else:
            raise ValueError(f"For max_pool1d() {arg_name} must be an int or int list of size 1 "
                             f"but got size {len(arg)}.")
    else:
        raise ValueError(f"An error occurred. Please check the validity of the value of {arg_name} in max_pool1d().")
    return _arg

@_primexpr
# @lru_cache(_GLOBAL_LRU_CACHE_SIZE_NN)
def _get_maxpool1d_arg_to_2d(arg, arg_name, set_value):
    if isinstance(arg, int):
        _arg = (arg, set_value)
    elif isinstance(arg, (tuple, list)):
        if len(arg) == 1:
            _arg = (arg[0], set_value)
        else:
            raise ValueError(f"For max_pool1d() {arg_name} must be an int or int list of size 1 "
                             f"but got size {len(arg)}.")
    else:
        raise ValueError(f"An error occurred. Please check the validity of the value of {arg_name} in max_pool1d().")
    return _arg

def max_pool1d(input, kernel_size, stride=None, padding=0, dilation=1, ceil_mode=False, return_indices=False):
    input_ms = cast_to_ms_tensor(input)
    if input_ms.dtype in all_int_type:
        raise TypeError("'max_pool1d' not implemented for int.")

    stride = stride if (stride is not None) else kernel_size
    input_shape = input_ms.shape
    ndim = input_ms.ndim
    min_ndim = 2
    max_ndim = 3
    if return_indices or ceil_mode or dilation != 1 or padding != 0:
        if ndim == min_ndim:
            _input_ms = input_ms.reshape((1,) + input_shape + (1, 1))
        elif ndim == max_ndim:
            _input_ms = input_ms.reshape(input_shape + (1, 1))
        else:
            raise TypeError(f"max_pool1d() Expected 2D or 3D input tensor, but got input.ndim == {ndim}.")

        _kernel_size = _get_maxpool1d_arg_to_3d(kernel_size, "kernel_size", 1)
        _stride = _get_maxpool1d_arg_to_3d(stride, "stride", 1)
        _padding = _get_maxpool1d_arg_to_3d(padding, "padding", 0)
        _dilation = _get_maxpool1d_arg_to_3d(dilation, "dilation", 1)

        # ms.ops.max_pool2d has poor performance, also have problem when return_indices==True in CPU/GPU,
        # and only supported float16 in ascend.
        out = ms.ops.max_pool3d(_input_ms, _kernel_size, _stride, _padding, _dilation, ceil_mode, return_indices)
        if return_indices:
            output, argmax = out
            return cast_to_adapter_tensor((output.reshape(output.shape[max_ndim - ndim:max_ndim]),
                                           argmax.reshape(argmax.shape[max_ndim - ndim:max_ndim])))
        return cast_to_adapter_tensor(out.reshape(out.shape[max_ndim - ndim:max_ndim]))

    # To accelerate
    _kernel_size = _get_maxpool1d_arg_to_2d(kernel_size, "kernel_size", 1)
    _stride = _get_maxpool1d_arg_to_2d(stride, "stride", 1)

    if ndim == min_ndim:
        _input_ms = input_ms.reshape((1,) + input_shape + (1,))
    elif ndim == max_ndim:
        _input_ms = input_ms.reshape(input_shape + (1,))
    else:
        raise TypeError(f"max_pool1d() Expected 2D or 3D input tensor, but got input.ndim == {ndim}.")

    _max_pool = _get_cache_prim(ms.ops.MaxPool)(kernel_size=_kernel_size, strides=_stride, pad_mode='valid')
    out = _max_pool(_input_ms)
    out = out.reshape(out.shape[max_ndim - ndim:max_ndim])
    return cast_to_adapter_tensor(out)


@_primexpr
# @lru_cache(_GLOBAL_LRU_CACHE_SIZE_NN)
def _get_maxpool3d_arg(arg, arg_name):
    if isinstance(arg, int):
        _arg = arg
    elif isinstance(arg, (tuple, list)):
        if len(arg) == 1:
            _arg = (arg[0], arg[0], arg[0])
        elif len(arg) == 3:
            _arg = tuple(arg)
        else:
            raise ValueError(f"For max_pool3d() {arg_name} must be an int or int list of size 3 "
                             f"but got size {len(arg)}.")
    else:
        raise ValueError(f"An error occurred. Please check the validity of the value of {arg_name} in max_pool3d().")
    return _arg

def max_pool3d(input, kernel_size, stride=None, padding=0, dilation=1, ceil_mode=False, return_indices=False):
    input_ms = cast_to_ms_tensor(input)
    input_shape = input.shape
    min_ndim = 4
    max_ndim = 5
    ndim = input_ms.ndim
    if ndim == min_ndim:
        _input_ms = input.reshape((1,) + input_shape)
    elif ndim == max_ndim:
        _input_ms = input_ms
    else:
        raise TypeError(f"max_pool3d() Expected 4D or 5D input tensor, but got input.ndim == {ndim}.")

    kernel_size = _get_maxpool3d_arg(kernel_size, "kernel_size")
    stride = _get_maxpool3d_arg(stride, "stride")
    padding = _get_maxpool3d_arg(padding, "padding")
    dilation = _get_maxpool3d_arg(dilation, "dilation")

    out = ms.ops.max_pool3d(_input_ms, kernel_size, stride, padding, dilation, ceil_mode, return_indices)

    if ndim == min_ndim:
        if return_indices:
            output, argmax = out
            out = (output.squeeze(0), argmax.squeeze(0))
        else:
            out = out.squeeze(0)
    return cast_to_adapter_tensor(out)

@_primexpr
def _deconv_output_length(pad_mode, input_length, filter_size, stride_size, dilation_size, padding):
    """Calculate the width and height of output."""
    length = 0
    filter_size = filter_size + (filter_size - 1) * (dilation_size - 1)
    if pad_mode == 'valid':
        if filter_size - stride_size > 0:
            length = input_length * stride_size + filter_size - stride_size
        else:
            length = input_length * stride_size
    elif pad_mode == 'same':
        length = input_length * stride_size
    elif pad_mode == 'pad':
        length = input_length * stride_size - padding + filter_size - stride_size

    return length

@_primexpr
def _conv_transpose1d_check_output_padding(output_padding):
    _output_padding = _single(output_padding)
    if _output_padding != (0,):
        raise NotImplementedError("for nn.functional.conv_transpose1d, `output_padding` not support yet.")

@_primexpr
def _get_conv_transpose1d_channel(input_shape, weight_shape, groups):
    in_channel = input_shape[1]
    out_channel = weight_shape[1] * groups
    kernel_size = weight_shape[2]
    return in_channel, out_channel, kernel_size

@_primexpr
def _get_conv_transpose1d_pad_mode(kernel_size, stride, padding, output_padding):
    if stride != 1 and padding == (kernel_size - 1) // 2 and output_padding == stride - 1:
        pad_mode = 'same'
        padding = 0
        raise Warning("pad_mode = same is some thing wrong, please switch to others")
    elif padding == 0 and output_padding == 0:
        pad_mode = 'valid'
        padding = 0
    else:
        pad_mode = 'pad'
    return pad_mode, padding

@_primexpr
def _process_conv_transpose1d_const(kernel_size, stride, dilation, padding):
    kernel_size = _single(kernel_size)
    stride = _single(stride)
    dilation = _single(dilation)
    padding = _pair(padding)
    kernel_size = (1,) + kernel_size
    stride = (1,) + stride
    dilation = (1,) + dilation
    padding = (0, 0) + padding
    return kernel_size, stride, dilation, padding


def conv_transpose1d(input, weight, bias=None, stride=1, padding=0, output_padding=0, groups=1, dilation=1):
    _conv_transpose1d_check_output_padding(output_padding)

    x = cast_to_ms_tensor(input)
    # do not need to cast weight, because it did not use mindspore's tensor method in the code below.
    # weight = cast_to_ms_tensor(weight)

    if x.ndim != 3:
        raise ValueError("the rank of input tensor should be 3.")
    if weight.ndim != 3:
        raise ValueError("the rank of weight tensor should be 3")

    input_shape = x.shape
    weight_shape = weight.shape
    in_channel, out_channel, kernel_size = \
                _get_conv_transpose1d_channel(input_shape, weight_shape, groups)
    _pad_mode, padding = \
                _get_conv_transpose1d_pad_mode(kernel_size, stride, padding, output_padding)

    _kernel_size, _stride, _dilation, _padding = \
                _process_conv_transpose1d_const(kernel_size, stride, dilation, padding)

    _conv2d_transpose = _get_cache_prim(ms.ops.Conv2DBackpropInput)(out_channel=in_channel,
                                                                    kernel_size=_kernel_size,
                                                                    mode=1,
                                                                    pad_mode=_pad_mode,
                                                                    pad=_padding,
                                                                    stride=_stride,
                                                                    dilation=_dilation,
                                                                    group=groups)
    x = ms.ops.expand_dims(x, 2)
    weight = ms.ops.expand_dims(weight, 2)
    n, _, w = input_shape
    h = 1
    h_out = _deconv_output_length(_pad_mode, h, _kernel_size[0],
                                  _stride[0], _dilation[0], _padding[0] + _padding[1])
    w_out = _deconv_output_length(_pad_mode, w, _kernel_size[1],
                                  _stride[1], _dilation[1], _padding[2] + _padding[3])
    output = _conv2d_transpose(x, weight, (n, out_channel, h_out, w_out))
    if bias is not None:
        output = ms.ops.bias_add(output, bias)
    output = ms.ops.squeeze(output, 2)
    return cast_to_adapter_tensor(output)

@_primexpr
def _conv_transpose2d_check_output_padding(output_padding):
    _output_padding = _pair(output_padding)
    if _output_padding != (0, 0):
        raise NotImplementedError("for nn.functional.conv_transpose2d, `output_padding` not support yet.")

@_primexpr
def _get_conv_transpose2d_channel(input_shape, weight_shape, groups):
    in_channel = input_shape[1]
    out_channel = weight_shape[1] * groups
    kernel_size = weight_shape[2:]
    return in_channel, out_channel, kernel_size

@_primexpr
def _get_conv_transpose2d_pad_mode(padding, output_padding):
    if padding == 0 and output_padding == 0:
        pad_mode = 'valid'
        padding = 0
    else:
        pad_mode = 'pad'
    return pad_mode, padding

@_primexpr
def _process_conv_transpose2d_const(kernel_size, stride, dilation, padding):
    kernel_size = _pair(kernel_size)
    stride = _pair(stride)
    dilation = _pair(dilation)
    padding = _pair(padding)
    padding = (padding[0], padding[0], padding[1], padding[1])
    return kernel_size, stride, dilation, padding

def conv_transpose2d(input, weight, bias=None, stride=1, padding=0, output_padding=0, groups=1, dilation=1):
    _conv_transpose2d_check_output_padding(output_padding)

    inputs = cast_to_ms_tensor(input)
    # do not need to cast weight, because it did not use mindspore's tensor method in the code below.
    # weight = cast_to_ms_tensor(weight)
    if inputs.ndim != 4:
        raise ValueError("the rank of inputs tensor should be 4.")
    if weight.ndim != 4:
        raise ValueError("the rank of weight tensor should be 4")

    input_shape = inputs.shape
    weight_shape = weight.shape

    in_channel, out_channel, kernel_size = \
                    _get_conv_transpose2d_channel(input_shape, weight_shape, groups)
    _pad_mode, padding = \
                    _get_conv_transpose2d_pad_mode(padding, output_padding)
    _kernel_size, _stride, _dilation, _padding = \
                    _process_conv_transpose2d_const(kernel_size, stride, dilation, padding)

    _conv2d_transpose = _get_cache_prim(ms.ops.Conv2DTranspose)(out_channel=in_channel,
                                                                kernel_size=_kernel_size,
                                                                mode=1,
                                                                pad_mode=_pad_mode,
                                                                pad=_padding,
                                                                stride=_stride,
                                                                dilation=_dilation,
                                                                group=groups)

    n, _, h, w = input_shape
    h_out = _deconv_output_length(_pad_mode, h, _kernel_size[0],
                                  _stride[0], _dilation[0], _padding[0] + _padding[1])
    w_out = _deconv_output_length(_pad_mode, w, _kernel_size[1],
                                  _stride[1], _dilation[1], _padding[2] + _padding[3])

    output = _conv2d_transpose(inputs, weight, (n, out_channel, h_out, w_out))
    if bias is not None:
        output = ms.ops.bias_add(output, bias)
    return cast_to_adapter_tensor(output)


@_primexpr
# @lru_cache(_GLOBAL_LRU_CACHE_SIZE_NN)
def _get_conv_transpose3d_const(input_shape, weight_shape, groups, padding):
    if len(input_shape) != 5:
        raise ValueError("the rank of inputs tensor should be 5.")
    if len(weight_shape) != 5:
        raise ValueError("the rank of weight tensor should be 5")

    in_channel = input_shape[1]
    out_channel = weight_shape[1] * groups
    kernel_size = weight_shape[2:]
    pad_mode = 'pad'
    if isinstance(padding, int):
        ms_padding = padding
    else:
        ms_padding = _repeat_tuple(padding, 2)
    return in_channel, out_channel, kernel_size, pad_mode, ms_padding

def conv_transpose3d(input, weight, bias=None, stride=1, padding=0, output_padding=0, groups=1, dilation=1):
    input_ms = cast_to_ms_tensor(input)
    # do not cast weight and bias to ms_tensor, because will cause lost gradient
    # weight = cast_to_ms_tensor(weight)
    # bias = cast_to_ms_tensor(bias) if bias is not None else bias
    in_channel, out_channel, kernel_size, pad_mode, ms_padding = _get_conv_transpose3d_const(input_ms.shape,
                                                                                             weight.shape,
                                                                                             groups,
                                                                                             padding)

    _conv_3d_transpose = _get_cache_prim(ms.ops.Conv3DTranspose)(in_channel= in_channel,
                                                                 out_channel=out_channel,
                                                                 kernel_size=kernel_size,
                                                                 mode=1,
                                                                 pad_mode=pad_mode,
                                                                 pad=ms_padding,
                                                                 stride=stride,
                                                                 dilation=dilation,
                                                                 group=groups,
                                                                 output_padding=output_padding,
                                                                 data_format='NCDHW')

    # ms.ops.Conv3DTranspose not supported bias yet
    out = _conv_3d_transpose(input_ms, weight)
    if bias is not None:
        out = _get_cache_prim(ms.ops.BiasAdd)(data_format='NCDHW')(out, bias)
    return cast_to_adapter_tensor(out)


def affine_grid(theta, size, align_corners=None):
    theta = cast_to_ms_tensor(theta)
    if align_corners is None:
        align_corners = False

    # TODO：the input argument[theta] must be a type of {Tensor[Float16], Tensor[Float32]}
    if theta.dtype == ms.float64:
        theta = theta.astype(ms.float32)
    output = ms.ops.affine_grid(theta, size, align_corners)
    return cast_to_adapter_tensor(output)


def _do_batch_norm(inputs, running_mean, running_var, weight, bias, trainning, momentum, eps):
    inputs_ms = cast_to_ms_tensor(inputs)
    if inputs_ms.ndim > 4:
        inputs_shape = inputs_ms.shape
        inputs_ms = ms.ops.reshape(inputs_ms, inputs_shape[:2] + (-1,) + inputs_shape[-1:])
        output = ms.ops.batch_norm(inputs_ms, running_mean, running_var, weight, bias, trainning, momentum, eps)
        output = output.reshape(inputs_shape)
    else:
        output = ms.ops.batch_norm(inputs_ms, running_mean, running_var, weight, bias, trainning, momentum, eps)
    return cast_to_adapter_tensor(output)

def batch_norm(input, running_mean, running_var, weight=None, bias=None, training=False, momentum=0.1,
               eps=1e-05):
    if training is False and (running_mean is None or running_var is None):
        raise RuntimeError("running_mean and running_var must be defined in evaluation mode")

    if training is True and isinstance(running_mean, Parameter) and \
                            isinstance(running_var, Parameter) and \
                            isinstance(weight, Parameter) and \
                            isinstance(bias, Parameter):
        return _do_batch_norm(input, running_mean, running_var, weight, bias, True, momentum, eps)

    if training is False and isinstance(running_mean, Tensor) and \
                             isinstance(running_var, Tensor) and \
                             isinstance(weight, Tensor) and \
                             isinstance(bias, Tensor):
        return _do_batch_norm(input, running_mean, running_var, weight, bias, False, momentum, eps)

    # if want to use 'ms.ops.batch_norm', every input must not be None and should obey the 'Tensor', 'Parameter' rules
    # And in GRAPH-MODE,  we can not dynamic create Parameter in forward proceedure.
    # So, use code below to deal with some inputs are None or not obeying the 'Tensor' and 'Parameter' rules.
    # But, `running_mean` and `running_var` can not be updated in GRAPH-MODE yet.
    input_ms = cast_to_ms_tensor(input)
    reduced_dim = tuple(i for i in range(input_ms.dim()) if i != 1)
    normalized_shape = [1] * len(input_ms.shape)
    normalized_shape[1] = input_ms.shape[1]
    if training:
        mean = input_ms.mean(axis=reduced_dim, keep_dims=True)
        var = input_ms.var(reduced_dim, keepdims=True, ddof=False)
        out = (input_ms - mean) / ms.ops.sqrt(var + eps)
        if running_mean is not None or running_var is not None:
            # In GRAPH-MODE, 'assign_value' can not take effect in mindspore.
            # So, the running_mean and running_var can not be updated.
            if graph_mode_condition():
                raise RuntimeError("nn.functional.batch_norm: under graph-mode, when `training` is True, "
                                   "`running_mean` and `running_var` are only allow 'None' yet.")
            mean_update = mean.squeeze()
            var_update = input_ms.var(axis=reduced_dim, ddof=True)
            if running_mean is not None:
                running_mean.assign_value((1 - momentum) * running_mean + momentum * mean_update)
            if running_var is not None:
                running_var.assign_value((1 - momentum) * running_var + momentum * var_update)
    else:
        out = (input_ms - running_mean.view(*normalized_shape)) / ms.ops.sqrt(running_var.view(*normalized_shape) + eps)
    if weight is not None:
        out = out * weight.view(*normalized_shape)
    if bias is not None:
        out = out + bias.view(*normalized_shape)
    return cast_to_adapter_tensor(out)


def group_norm(input, num_groups, weight=None, bias=None, eps=1e-05):
    # TODO: This interface has a significant accuracy error under float16.
    inputs_dtype = input.dtype
    inputs = cast_to_ms_tensor(input).astype(ms.float32)
    # it is not necessary to cast weight and bias
    inputs_shape = inputs.shape
    inputs_rank = len(inputs_shape)

    shape = (inputs_shape[0],) + (num_groups, inputs_shape[1] // num_groups) + inputs_shape[2:]
    normalized_shape = [1] * inputs_rank
    normalized_shape[1] = inputs_shape[1]
    reduced_dim = tuple(i for i in range(len(shape) - 1, 1, -1))
    inputs = inputs.reshape(*shape)
    mean = inputs.mean(axis=reduced_dim, keep_dims=True)
    var = inputs.var(axis=reduced_dim, keepdims=True, ddof=False)
    out = (inputs - mean) / ms.ops.sqrt(var + eps)
    out = out.reshape(*inputs_shape).astype(inputs_dtype)
    if weight is not None:
        out = out * weight.view(*normalized_shape)
    if bias is not None:
        out = out + bias.view(*normalized_shape)
    return cast_to_adapter_tensor(out)


def instance_norm(input, running_mean=None, running_var=None, weight=None, bias=None, use_input_stats=True,
                  momentum=0.1, eps=1e-05):
    if not use_input_stats and (running_mean is None or running_var is None):
        raise RuntimeError("Expected running_mean and running_var to be defined when use_input_stats is false")

    if is_under_gpu_context() and isinstance(running_mean, Parameter) and \
                                  isinstance(running_var, Parameter) and \
                                  isinstance(weight, Parameter) and \
                                  isinstance(bias, Parameter):
        inputs_ms = cast_to_ms_tensor(input)
        _op = _get_cache_prim(ms.ops.operations.InstanceNorm)(epsilon=eps, momentum=momentum)
        output = _op(inputs_ms, weight, bias, running_mean, running_var)[0]
        return cast_to_adapter_tensor(output)

    # TODO: ms.ops.operations.InstanceNorm not support on CPU/Ascend. use code below instead.
    inputs = cast_to_ms_tensor(input)
    # unnesseary to cast 'weight' and 'bias'
    # can not cast 'running_mean', 'running_var', bacause will update them in-place
    inputs_ndim = inputs.ndim
    inputs_shape = inputs.shape

    if inputs_ndim < 3:
        raise ValueError("ValueError: Expected more than 1 spatial element when training, "
                        f"got input size {inputs_shape}")

    reduced_dim = tuple(i for i in range(2, inputs_ndim))
    normalized_shape = [1] * inputs_ndim
    normalized_shape[1] = inputs_shape[1]

    shape = [1] * inputs_ndim
    shape[:2] = inputs_shape[:2]

    if use_input_stats:
        mean = inputs.mean(axis=reduced_dim)
        var = inputs.var(axis=reduced_dim, ddof=False)
        out = (inputs - mean.view(*shape)) / ms.ops.sqrt(var.view(*shape) + eps)
        # TODO: graph mode the inplace assign don't take effect.
        if running_mean is not None or running_var is not None:
            if graph_mode_condition():
                raise RuntimeError("nn.functional.instance_norm: under graph-mode, when `training` is True, "
                                   "`running_mean` and `running_var` are only allow 'None' yet.")
            mean_update = mean.mean(0)
            var_update = inputs.var(axis=reduced_dim, ddof=True).mean(0)
            if running_mean is not None:
                running_mean.assign_value((1 - momentum) * running_mean + momentum * mean_update)
            if running_var is not None:
                running_var.assign_value((1 - momentum) * running_var + momentum * var_update)
    else:
        out = (inputs - running_mean.view(*normalized_shape)) \
                     / ms.ops.sqrt(running_var.view(*normalized_shape) + eps)
    if weight is not None:
        out = out * weight.view(*normalized_shape)
    if bias is not None:
        out = out + bias.view(*normalized_shape)
    return cast_to_adapter_tensor(out)


def layer_norm(input, normalized_shape, weight=None, bias=None, eps=1e-05):
    inputs = cast_to_ms_tensor(input)
    # It is not necessary to cast weight and bias
    if weight is None:
        weight = ms.Tensor(np.ones(normalized_shape), inputs.dtype)
    if bias is None:
        bias = ms.Tensor(np.zeros(normalized_shape), inputs.dtype)

    # Can not check shape here , because under GRAPH-MODE with dynamic-shape
    # When 'raise ValueError' and 'return output' show up in different branch in the same function,
    # 'join fail' will occurs.

    # if inputs.shape[-len(normalized_shape):] != normalized_shape:
    #     raise ValueError("For layer_norm, normalized_shape should fit inputs' shape"
    #                      f"but got input_shape: {inputs.shape}, normalized_shape: {normalized_shape}")

    begin_axis = inputs.ndim - len(normalized_shape)
    _layer_norm = _get_cache_prim(ms.ops.LayerNorm)(begin_axis, begin_axis, float(eps))
    out = _layer_norm(inputs, weight, bias)
    return cast_to_adapter_tensor(out[0])


def prelu(input, weight):
    #TODO:ms.ops.prelu only suports float16 and float32, not float64.
    input_ms = cast_to_ms_tensor(input)
    # weight will be Parameter and can not be cast to tensor, will lost weights.
    # ms.ops.prelu do not use tensor function of weight, so without cast_to_ms_tensor(weight), not effect.
    # weight = cast_to_ms_tensor(weight)
    if is_under_ascend_context() and input_ms.ndim < 2:
        shape = input_ms.shape
        input_ms = _expand(input_ms, 2)
        output = ms.ops.prelu(input_ms, weight)
        output = output.reshape(shape)
    else:
        output = ms.ops.prelu(input_ms, weight)
    return cast_to_adapter_tensor(output)


def poisson_nll_loss(input, target, log_input=True, full=False, size_average=None, eps=1e-08, reduce=None,
                     reduction='mean'):
    #TODO: no ms.ops.poisson_nll_loss
    input_ms = cast_to_ms_tensor(input)
    target = cast_to_ms_tensor(target)
    if reduce is not None or size_average is not None:
        reduction = _get_reduce_string(size_average, reduce)
    if reduction not in ('none', 'mean', 'sum'):
        raise ValueError(reduction + " is not valid")

    if log_input:
        ret = ms.ops.exp(input) - target * input
    else:
        ret = input_ms - target * ms.ops.log(input_ms + eps)
    if full:
        cond = ms.ops.gt(target, 1)
        out = target * ms.ops.log(target) - target + 0.5 * ms.ops.log(2 * pi * target)
        out = ms.ops.select(cond, out, ms.ops.zeros_like(input_ms))
        ret = ret + out
    if reduction == "mean":
        ret = ms.ops.mean(ret)
    elif reduction == "sum":
        ret = ms.ops.sum(ret)
    return cast_to_adapter_tensor(ret)


def triplet_margin_with_distance_loss(anchor, positive, negative, *, distance_function=None, margin=1.0,
                                      swap=False, reduction='mean'):
    distance_function = distance_function if distance_function is not None else pairwise_distance

    #TODO: no ms.ops.poisson_nll_loss

    anchor = cast_to_ms_tensor(anchor)
    positive = cast_to_ms_tensor(positive)
    negative = cast_to_ms_tensor(negative)
    positive_dist = distance_function(anchor, positive)
    negative_dist = distance_function(anchor, negative)

    if swap:
        swap_dist = distance_function(positive, negative)
        negative_dist = ms.ops.minimum(negative_dist, swap_dist)

    output = ms.ops.clamp(positive_dist - negative_dist + margin, min=0.0)

    if reduction == "mean":
        ret = output.mean()
    elif reduction == "sum":
        ret = output.sum()
    else:
        ret = output
    return cast_to_adapter_tensor(ret)


@_primexpr
# @lru_cache(_GLOBAL_LRU_CACHE_SIZE_NN)
def _get_conv3d_const(stride, padding, dilation):
    if isinstance(stride, int):
        stride = (stride, stride, stride)
    elif len(stride)==1:
        stride = (stride[0], stride[0], stride[0])
    pad_mode = "pad"
    if isinstance(padding, int):
        padding = (padding, padding, padding)
    elif isinstance(padding, tuple):
        if len(padding)==1:
            padding = (padding[0], padding[0], padding[0])

    else:
        pad_mode = padding
        padding = 0
    if isinstance(dilation, int):
        dilation = (dilation, dilation, dilation)
    elif len(dilation) == 1:
        dilation = (dilation[0], dilation[0], dilation[0])
    return pad_mode, padding, stride, dilation


def conv3d(input, weight, bias=None, stride=1, padding=0, dilation=1, groups=1):
    # TODO: not support float64, change to float32 now
    # TODO: on Ascend, ms.ops.conv3d only support dilation and groups to be 1.
    input_ms = cast_to_ms_tensor(input)
    # without cast_to_ms_tensor(weight) for performance
    weight_ms = weight
    is_float64 = False
    if input_ms.dtype in (ms.float64, ms.double):
        input_ms = input_ms.astype(ms.float32)
        weight_ms = weight_ms.astype(ms.float32)
        is_float64 = True

    _pad_mode, _padding, _stride, _dilation = _get_conv3d_const(stride, padding, dilation)
    if is_under_ascend_context() and groups != 1:
        _input_group_size = input_ms.shape[1] // groups
        _weight_group_size = weight_ms.shape[0] // groups
        input_ms = ms.ops.split(input_ms, _input_group_size, 1)
        weight_ms = ms.ops.split(weight_ms, _weight_group_size, 0)
        outs = ()
        for i in range(groups):
            outp = ms.ops.conv3d(input_ms[i], weight_ms[i], None, _stride, _pad_mode, _padding, _dilation, 1)
            outs = outs + (outp,)
        output = ms.ops.concat(outs, 1)
    else:
        output = ms.ops.conv3d(input_ms, weight_ms, None, _stride, _pad_mode, _padding, _dilation, groups)
    if bias is not None:
        # TODO: ms.ops.biasadd also not support float64
        if bias.dtype != output.dtype:
            bias = bias.astype(output.dtype)
        output = ms.ops.bias_add(output, bias)

    if is_float64:
        output = output.astype(ms.float64)

    return cast_to_adapter_tensor(output)


def unfold(input, kernel_size, dilation=1, padding=0, stride=1):
    input_ms = cast_to_ms_tensor(input)
    output = ms.ops.unfold(input_ms, kernel_size, dilation, padding, stride)
    return cast_to_adapter_tensor(output)


def fold(input, output_size, kernel_size, dilation=1, padding=0, stride=1):
    input_ms = cast_to_ms_tensor(input)
    ndim = input_ms.ndim
    if ndim == 2:
        input_ms = input_ms.expand_dims(0)
    output = ms.ops.fold(input_ms, ms.Tensor(output_size, dtype=ms.int32), kernel_size, dilation, padding, stride)
    if ndim == 2:
        output = output.squeeze(0)
    return cast_to_adapter_tensor(output)

def multi_head_attention_forward(query, key, value, embed_dim_to_check, num_heads, in_proj_weight,
                                 in_proj_bias, bias_k, bias_v, add_zero_attn, dropout_p, out_proj_weight,
                                 out_proj_bias, training=True, key_padding_mask=None, attn_mask=None,
                                 use_separate_proj_weight=False, q_proj_weight=None, k_proj_weight=None,
                                 v_proj_weight=None, static_k=None, static_v=None, average_attn_weights=True,
                                 k_is_v=False, q_is_k=False):
    query = cast_to_ms_tensor(query)
    key = cast_to_ms_tensor(key)
    value = cast_to_ms_tensor(value)
    key_padding_mask = cast_to_ms_tensor(key_padding_mask)
    attn_mask = cast_to_ms_tensor(attn_mask)
    static_k = cast_to_ms_tensor(static_k)
    static_v = cast_to_ms_tensor(static_v)
    #ms multi_head_attention_forward will raise error in BatchMatMul when attn_mask.dtype=float64
    if isinstance(attn_mask, ms.Tensor):
        attn_mask = attn_mask.astype(ms.float32)
    in_proj_weight = ms.ops.Identity()(in_proj_weight) if in_proj_weight is not None else None
    in_proj_bias = ms.ops.Identity()(in_proj_bias) if in_proj_bias is not None else None
    bias_k = ms.ops.Identity()(bias_k) if bias_k is not None else None
    bias_v = ms.ops.Identity()(bias_v) if bias_v is not None else None
    out_proj_weight = ms.ops.Identity()(out_proj_weight) if out_proj_weight is not None else None
    out_proj_bias = ms.ops.Identity()(out_proj_bias) if out_proj_bias is not None else None
    q_proj_weight = ms.ops.Identity()(q_proj_weight) if q_proj_weight is not None else None
    k_proj_weight = ms.ops.Identity()(k_proj_weight) if k_proj_weight is not None else None
    v_proj_weight = ms.ops.Identity()(v_proj_weight) if v_proj_weight is not None else None
    # TODO: older ver of torch doesn't have is_causal arg
    attn_output, attn_output_weights = ms.ops.function.nn_func.multi_head_attention_forward(
        query, key, value, embed_dim_to_check, num_heads,
        in_proj_weight, in_proj_bias, bias_k, bias_v, add_zero_attn, dropout_p,
        out_proj_weight, out_proj_bias, training=training,
        key_padding_mask=key_padding_mask, attn_mask=attn_mask,
        use_separate_proj_weight=use_separate_proj_weight,
        q_proj_weight=q_proj_weight, k_proj_weight=k_proj_weight,
        v_proj_weight=v_proj_weight, static_k=static_k, static_v=static_v,
        average_attn_weights=average_attn_weights, k_is_v=k_is_v, q_is_k=q_is_k)
    return cast_to_adapter_tensor(attn_output), cast_to_adapter_tensor(attn_output_weights)

def channel_shuffle(inputs, groups):
    x = cast_to_ms_tensor(inputs)
    x_shape = x.shape
    n, c = x_shape[0], x_shape[1]
    out = ms.ops.reshape(x, (n, groups, c // groups, -1))
    out = ms.ops.transpose(out, (0, 2, 1, 3))
    out = ms.ops.reshape(out, x_shape)
    return cast_to_adapter_tensor(out)


_pad_func = pad
def constant_pad_nd(input, pad, value=0):
    return _pad_func(input, pad, 'constant', value)

# TODO: Use the following code to accelerate
#  @ms.jit
#  @ms.trace
#  def fun():
#      ....
#  however, `cast_to_adapter_tensor` is not allowed in the current `trace` decorated function.
@ms.jit
def scaled_dot_product_attention(query, key, value, attn_mask=None, dropout_p=0.0, is_causal=False, scale=None):
    query_ms = cast_to_ms_tensor(query)
    key_ms = cast_to_ms_tensor(key)
    value_ms = cast_to_ms_tensor(value)

    L, S = query_ms.shape[-2], key_ms.shape[-2]
    query_last_dim = query_ms.shape[-1]
    key_dtype = key_ms.dtype
    scale_factor = 1 / ms.ops.sqrt(ms.Tensor(query_last_dim, dtype=key_dtype)) if scale is None else scale
    attn_bias = ms.ops.zeros((L, S), dtype=query_ms.dtype)
    if is_causal:
        assert attn_mask is None
        temp_mask = ms.ops.ones((L, S), dtype=ms.bool_)
        temp_mask = ms.ops.tril(temp_mask, 0)
        attn_bias = attn_bias.masked_fill(ms.ops.logical_not(temp_mask), float("-inf"))
        attn_bias.astype(query_ms.dtype)

    if attn_mask is not None:
        attn_mask_ms = cast_to_ms_tensor(attn_mask)
        if attn_mask_ms.dtype == ms.bool_:
            attn_bias = attn_bias.masked_fill(ms.ops.logical_not(attn_mask_ms), float("-inf"))
        else:
            attn_bias += attn_mask_ms

    key_transpose = ms.ops.swapaxes(key_ms, -2, -1)
    attn_weight = query_ms @ key_transpose * scale_factor
    attn_weight += attn_bias
    attn_weight = ms.ops.softmax(attn_weight, -1)
    _check_dropout_p(dropout_p)
    if dropout_p != 0.:
        attn_weight = ms.ops.dropout(attn_weight, p=dropout_p)
    output = attn_weight @ value_ms
    return cast_to_adapter_tensor(output)

# No corresponding api in pytorch, just using api prompt_flash_attention internally.
# prompt_flash_attention only support on Ascend.
def prompt_flash_attention(query, key, value, attn_mask=None,
                           actual_seq_lengths=None, actual_seq_lengths_kv=None, padding_mask=None,
                           dep_scale1=None, quant_scale1=None,
                           deq_scale2=None, quant_scale2=None, quant_offset2=None,
                           num_heads=0, scale_value=1.0,
                           pre_tokens=2147483547, next_tokens=0, input_layout='BSH',
                           num_key_value_heads=0, sparse_mode=0):
    query_ms = cast_to_ms_tensor(query)
    key_ms = cast_to_ms_tensor(key)
    value_ms = cast_to_ms_tensor(value)
    if attn_mask is not None:
        attn_mask = cast_to_ms_tensor(attn_mask)
    if padding_mask is not None:
        padding_mask = cast_to_ms_tensor(padding_mask)
    if actual_seq_lengths is not None:
        actual_seq_lengths = cast_to_ms_tensor(actual_seq_lengths)
    pfa_op = PromptFlashAttention(num_heads, scale_value=scale_value,
                                  pre_tokens=pre_tokens, next_tokens=next_tokens,
                                  input_layout=input_layout,
                                  num_key_value_heads=num_key_value_heads,
                                  sparse_mode=sparse_mode)
    output_ms = pfa_op(query_ms, key_ms, value_ms, attn_mask, actual_seq_lengths, actual_seq_lengths_kv,
                       padding_mask, dep_scale1, quant_scale1, deq_scale2, quant_scale2, quant_offset2)
    pfa_output = cast_to_adapter_tensor(output_ms[0])
    return pfa_output
