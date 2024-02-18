#!/usr/bin/env python
# -*- coding: utf-8 -*-
import itertools

import mindspore.ops as P
from mindspore.ops.operations import _inner_ops as inner
from mindspore.communication.management import get_group_size, get_rank
import mindspore._checkparam as validator
from mindspore.communication import management
import mindspore.context as context

from mindtorch.torch.nn import init
from mindtorch.torch.functional import empty
from mindtorch.torch.nn.parameter import Parameter
from mindtorch.utils import unsupported_attr
from mindtorch.torch.tensor import cast_to_ms_tensor, cast_to_adapter_tensor, tensor, Tensor
from .module import Module


__all__ = ['BatchNorm1d', 'BatchNorm2d', 'BatchNorm3d',
           'SyncBatchNorm']

class _NormBase(Module):
    """Common base of _InstanceNorm and _BatchNorm"""
    def __init__(
        self,
        num_features,
        eps=1e-5,
        momentum=0.1,
        affine=True,
        track_running_stats=True,
        device=None,
        dtype=None
    ):
        unsupported_attr(device)
        unsupported_attr(dtype)

        super(_NormBase, self).__init__()
        self._is_adapter_norm = True
        self.num_features = num_features
        self.eps = eps
        self.momentum = momentum
        self.affine = affine
        self.track_running_stats = track_running_stats
        self.weight = Parameter(empty(num_features), requires_grad=affine)
        self.bias = Parameter(empty(num_features), requires_grad=affine)
        # 'running_mean' and 'running_var' have to be Parameter
        # because mindspore.ops.BatchNorm require them to be Parameter when 'is_training' is True
        self.running_mean = Parameter(empty(num_features), requires_grad=False)
        self.running_var = Parameter(empty(num_features), requires_grad=False)
        self.register_buffer('running_mean', self.running_mean)
        self.register_buffer('running_var', self.running_var)
        self.reset_parameters()
        if not self.track_running_stats:
            self.momentum = 0.0

    def reset_running_stats(self):
        init.zeros_(self.running_mean)
        init.ones_(self.running_var)
        if self.track_running_stats:
            # Not used, only for loading pth files saved from torch.
            self.register_buffer('num_batches_tracked', tensor(0))

    def reset_parameters(self):
        self.reset_running_stats()
        init.ones_(self.weight)
        init.zeros_(self.bias)


    def extra_repr(self):
        return (
            "{num_features}, eps={eps}, momentum={momentum}, affine={affine}, "
            "track_running_stats={track_running_stats}".format(**self.__dict__)
        )

    def _load_from_state_dict(
        self,
        state_dict,
        prefix,
        local_metadata,
        strict,
        missing_keys,
        has_load,
        error_msgs,
    ):
        if self.track_running_stats:
            num_batches_tracked_key = prefix + "num_batches_tracked"
            if num_batches_tracked_key not in state_dict:
                state_dict[num_batches_tracked_key] = tensor(0)

        if not self.track_running_stats:
            running_mean_key = prefix + "running_mean"
            if running_mean_key not in state_dict:
                state_dict[running_mean_key] = init.ones_(Tensor(self.num_features))

            running_var_key = prefix + "running_var"
            if running_var_key not in state_dict:
                state_dict[running_var_key] = init.zeros_(Tensor(self.num_features))

        if not self.affine:
            weight_key = prefix + "weight"
            if weight_key not in state_dict:
                state_dict[weight_key] = init.ones_(Tensor(self.num_features))

            bias_key = prefix + "bias"
            if bias_key not in state_dict:
                state_dict[bias_key] = init.zeros_(Tensor(self.num_features))

        super()._load_from_state_dict(
            state_dict,
            prefix,
            local_metadata,
            strict,
            missing_keys,
            has_load,
            error_msgs,
        )


class _BatchNorm(_NormBase):
    """Common base of BatchNorm"""

    def __init__(
        self,
        num_features,
        eps=1e-5,
        momentum=0.1,
        affine=True,
        track_running_stats=True,
        device=None,
        dtype=None
    ):
        factory_kwargs = {'device': device, 'dtype': dtype}
        super(_BatchNorm, self).__init__(num_features, eps, momentum, affine, track_running_stats, **factory_kwargs)

        #TODO: currently momentum only support float input
        self.bn_train = P.BatchNorm(is_training=True,
                                    epsilon=self.eps,
                                    momentum=float(self.momentum),
                                    data_format='NCHW')

        self.bn_infer = P.BatchNorm(is_training=False, epsilon=self.eps, data_format='NCHW')

    def _check_input_dim(self, input):
        raise NotImplementedError

    def _check_rank_ids(self, process_groups, rank_size):
        seen = set()
        for rid in itertools.chain(*process_groups):
            validator.check_int_range(rid, 0, rank_size, validator.INC_LEFT, "rank id in process_groups", self.cls_name)
            if rid in seen:
                raise ValueError(f"For '{self.cls_name}', rank id in 'process_groups' must not be duplicated, "
                                 f"but got {process_groups}.")
            seen.add(rid)

    def _create_sync_groups(self):
        for i in range(len(self.process_groups)):
            validator.check_isinstance("process_groups[%d]" % i, self.process_groups[i], list)
            self.group_device_num = len(self.process_groups[i])
            if self.rank_id in self.process_groups[i] and self.group_device_num > 1:
                self.is_global = True
                global SYNC_BN_GROUP_NAME
                if SYNC_BN_GROUP_NAME == "":
                    SYNC_BN_GROUP_NAME = "sync_bn_group%d" % i
                    management.create_group(SYNC_BN_GROUP_NAME, self.process_groups[i])

    def forward(self, input):
        self._check_input_dim(input)

        input_ms = cast_to_ms_tensor(input)
        # TODO cast Parameter
        # Here use Ops instead of 'nn.functional.batch_norm', because latter may be poor performance.
        if self.training or (not self.training and not self.track_running_stats):
            output = self.bn_train(input_ms,
                                   self.weight,
                                   self.bias,
                                   self.running_mean,
                                   self.running_var)[0]
        else:
            output = self.bn_infer(input_ms,
                                   self.weight,
                                   self.bias,
                                   self.running_mean,
                                   self.running_var)[0]
        return cast_to_adapter_tensor(output)


class BatchNorm1d(_BatchNorm):
    def _check_input_dim(self, input):
        if len(input.shape) not in (2, 3):
            raise ValueError(
                "expected 2D or 3D input (got {}D input)".format(input.dim())
            )
        return True


class BatchNorm2d(_BatchNorm):
    r"""Applies Batch Normalization over a 4D input (a mini-batch of 2D inputs
    with additional channel dimension) as described in the paper
    `Batch Normalization: Accelerating Deep Network Training by Reducing
    Internal Covariate Shift <https://arxiv.org/abs/1502.03167>`__ .

    .. math::

        y = \frac{x - \mathrm{E}[x]}{ \sqrt{\mathrm{Var}[x] + \epsilon}} * \gamma + \beta

    The mean and standard-deviation are calculated per-dimension over
    the mini-batches and :math:`\gamma` and :math:`\beta` are learnable parameter vectors
    of size `C` (where `C` is the input size). By default, the elements of :math:`\gamma` are set
    to 1 and the elements of :math:`\beta` are set to 0. The standard-deviation is calculated
    via the biased estimator, equivalent to `mindtorch.torch.var(input, unbiased=False)`.

    Also by default, during training this layer keeps running estimates of its
    computed mean and variance, which are then used for normalization during
    evaluation. The running estimates are kept with a default :attr:`momentum`
    of 0.1.

    If :attr:`track_running_stats` is set to ``False``, this layer then does not
    keep running estimates, and batch statistics are instead used during
    evaluation time as well.

    .. note::
        This :attr:`momentum` argument is different from one used in optimizer
        classes and the conventional notion of momentum. Mathematically, the
        update rule for running statistics here is
        :math:`\hat{x}_\text{new} = (1 - \text{momentum}) \times \hat{x} + \text{momentum} \times x_t`,
        where :math:`\hat{x}` is the estimated statistic and :math:`x_t` is the
        new observed value.

    Because the Batch Normalization is done over the `C` dimension, computing statistics
    on `(N, H, W)` slices, it's common terminology to call this Spatial Batch Normalization.

    Args:
        num_features: :math:`C` from an expected input of size
            :math:`(N, C, H, W)`
        eps: a value added to the denominator for numerical stability.
            Default: 1e-5
        momentum: the value used for the running_mean and running_var
            computation. Can be set to ``None`` for cumulative moving average
            (i.e. simple average). Default: 0.1
        affine: a boolean value that when set to ``True``, this module has
            learnable affine parameters. Default: ``True``
        track_running_stats: a boolean value that when set to ``True``, this
            module tracks the running mean and variance, and when set to ``False``,
            this module does not track such statistics, and initializes statistics
            buffers :attr:`running_mean` and :attr:`running_var` as ``None``.
            When these buffers are ``None``, this module always uses batch statistics.
            in both training and eval modes. Default: ``True``

    Shape:
        - Input: :math:`(N, C, H, W)`
        - Output: :math:`(N, C, H, W)` (same shape as input)

    Examples::

        >>> # With Learnable Parameters
        >>> m = nn.BatchNorm2d(100)
        >>> # Without Learnable Parameters
        >>> m = nn.BatchNorm2d(100, affine=False)
        >>> input = mindtorch.torch.randn(20, 100, 35, 45)
        >>> output = m(input)
    """

    def _check_input_dim(self, input):
        if len(input.shape) != 4:
            raise ValueError("expected 4D input (got {}D input)".format(input.dim()))
        return True


class BatchNorm3d(_BatchNorm):
    def __init__(self,
                 num_features,
                 eps=1e-5,
                 momentum=0.1,
                 affine=True,
                 track_running_stats=True,
                 device=None,
                 dtype=None):
        factory_kwargs = {'device': device, 'dtype': dtype}
        super(BatchNorm3d, self).__init__(num_features, eps, momentum, affine, track_running_stats, **factory_kwargs)
        self.reshape = P.Reshape()

    def forward(self, input):
        self._check_input_dim(input)

        input_ms = cast_to_ms_tensor(input)
        x_shape = input_ms.shape
        input_ms = self.reshape(input_ms, (x_shape[0], x_shape[1], x_shape[2] * x_shape[3], x_shape[4]))

        if self.training or (not self.training and not self.track_running_stats):
            bn2d_out = self.bn_train(input_ms,
                                     self.weight,
                                     self.bias,
                                     self.running_mean,
                                     self.running_var)[0]
        else:
            bn2d_out = self.bn_infer(input_ms,
                                     self.weight,
                                     self.bias,
                                     self.running_mean,
                                     self.running_var)[0]

        bn3d_out = self.reshape(bn2d_out, x_shape)
        return cast_to_adapter_tensor(bn3d_out)

    def _check_input_dim(self, input):
        if len(input.shape) != 5:
            raise ValueError("expected 5D input (got {}D input)".format(input.dim()))
        return True


class SyncBatchNorm(_BatchNorm):
    def __init__(
        self,
        num_features,
        eps=1e-5,
        momentum=0.1,
        affine=True,
        track_running_stats=True,
        process_group=None,
        device=None,
        dtype=None
    ):
        factory_kwargs = {'device': device, 'dtype': dtype}
        super(SyncBatchNorm, self).__init__(
            num_features, eps, momentum, affine, track_running_stats, **factory_kwargs
        )
        self.process_groups = process_group
        global SYNC_BN_GROUP_NAME
        if self.process_groups != 0:
            self.rank_id = get_rank()
            self.rank_size = get_group_size()
            if self.process_groups is not None:
                validator.check_isinstance("process_groups", self.process_groups, list)
                self._check_rank_ids(self.process_groups, self.rank_size)
                self._create_sync_groups()
            elif self.rank_size > 1:
                self.is_global = True
                self.group_device_num = self.rank_size
                self.device_list = list(range(0, self.rank_size))
                if context.get_context("device_target") == "Ascend":
                    if SYNC_BN_GROUP_NAME == "":
                        SYNC_BN_GROUP_NAME = "sync_bn_group0"
                        management.create_group(SYNC_BN_GROUP_NAME, self.device_list)
                elif context.get_context("device_target") == "GPU":
                    if SYNC_BN_GROUP_NAME == "":
                        SYNC_BN_GROUP_NAME = "nccl_world_group"

        self.bn_train = inner.SyncBatchNorm(epsilon=self.eps,
                                            momentum=self.momentum,
                                            group=SYNC_BN_GROUP_NAME,
                                            device_num=self.group_device_num)

    def _check_input_dim(self, input):
        if len(input.shape) < 4:
            raise ValueError(
                "expected at least 2D input (got {}D input)".format(input.dim())
            )
        return True
