import mindspore as ms

from mindtorch.torch.tensor import cast_to_ms_tensor, cast_to_adapter_tensor
from mindtorch.torch.nn.modules.batchnorm import _NormBase

__all__ = ['InstanceNorm1d', 'InstanceNorm2d', 'InstanceNorm3d']


class _InstanceNorm(_NormBase):
    def __init__(
        self,
        num_features,
        eps=1e-5,
        momentum=0.1,
        affine=False,
        track_running_stats=False,
        device=None,
        dtype=None
    ):
        factory_kwargs = {'device': device, 'dtype': dtype}
        super(_InstanceNorm, self).__init__(
            num_features, eps, momentum, affine, track_running_stats, **factory_kwargs)
        self.instance_bn = ms.ops.operations.InstanceNorm(epsilon=self.eps, momentum=float(self.momentum))

    def _check_input_dim(self, ndim):
        raise NotImplementedError

    def _get_no_batch_dim(self):
        raise NotImplementedError

    def forward(self, input):
        # here should not use 'nn.functional.instance_norm', because it has worse performance.
        input_ms = cast_to_ms_tensor(input)
        ndim = input_ms.ndim
        self._check_input_dim(ndim)
        if ndim == self._get_no_batch_dim():
            input_ms = input_ms.unsqueeze(0)
            output = self.instance_bn(input_ms,
                                      self.weight,
                                      self.bias,
                                      self.running_mean,
                                      self.running_var)[0]
            output = output.squeeze(0)
        else:
            output = self.instance_bn(input_ms,
                                      self.weight,
                                      self.bias,
                                      self.running_mean,
                                      self.running_var)[0]
        output = cast_to_adapter_tensor(output)
        return output


class InstanceNorm1d(_InstanceNorm):
    def _get_no_batch_dim(self):
        return 2

    def _check_input_dim(self, ndim):
        if ndim not in (2, 3):
            raise ValueError('expected 2D or 3D input (got {}D input)'
                             .format(ndim))


class InstanceNorm2d(_InstanceNorm):
    def _get_no_batch_dim(self):
        return 3

    def _check_input_dim(self, ndim):
        if ndim not in (3, 4):
            raise ValueError('expected 3D or 4D input (got {}D input)'
                             .format(ndim))


class InstanceNorm3d(_InstanceNorm):
    def _get_no_batch_dim(self):
        return 4

    def _check_input_dim(self, ndim):
        if ndim not in (4, 5):
            raise ValueError('expected 4D or 5D input (got {}D input)'
                             .format(ndim))
