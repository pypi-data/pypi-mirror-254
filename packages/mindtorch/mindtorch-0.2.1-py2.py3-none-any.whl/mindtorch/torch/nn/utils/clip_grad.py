import mindspore as ms
from mindspore.ops.function.clip_func import get_square_sum, apply_global_norm
from mindspore import _checkparam as Validator
from mindtorch.utils import unsupported_attr, graph_mode_condition
from mindtorch.torch.tensor import cast_to_adapter_tensor

__all__ = ['clip_grad_norm_', 'clip_grad_norm', 'clip_grad_value', 'clip_grad_value_']

_hypermap = ms.ops.HyperMap()

def _assign(x1, x2):
    return x1.assign_value(x2)

class _ClipByGlobalNorm(ms.nn.Cell):
    def __init__(self, clip_norm=1.0, use_norm=None):
        """Initialize _ClipByGlobalNorm."""
        super(_ClipByGlobalNorm, self).__init__()
        # Add interface. This parameter is not used at present
        if use_norm is not None:
            raise ValueError(f"For '{self.cls_name}', input 'use_norm' only supports None currently, "
                             f"but got 'use_norm': {use_norm}")
        Validator.check_number("clip_norm", clip_norm, 0.0, Validator.GT, self.cls_name)
        self.clip_norm = ms.Tensor([clip_norm], ms.float32)
        self.hyper_map = ms.ops.HyperMap()
        self.greater_equal = ms.ops.GreaterEqual()

    def construct(self, x):
        square_sum = self.hyper_map(get_square_sum, x)
        _global_norm = ms.ops.sqrt(ms.ops.addn(square_sum))
        cond = self.greater_equal(_global_norm, self.clip_norm)
        global_norm = ms.ops.select(cond, _global_norm, self.clip_norm)
        clip_x = self.hyper_map(ms.ops.partial(apply_global_norm, self.clip_norm, global_norm), x)
        return clip_x, _global_norm[0]


def clip_grad_norm(parameters, max_norm, grads, norm_type=2.0, error_if_nonfinite=False, foreach=None):
    unsupported_attr(foreach)
    unsupported_attr(parameters)
    if error_if_nonfinite:
        raise NotImplementedError("`error_if_nonfinite=True` in 'clip_grad_norm' not support yet.")

    if norm_type != 2.0:
        raise NotImplementedError("`norm_type` in 'clip_grad_norm' beside 2.0 is not supported yet.")

    if not isinstance(grads, tuple) or not isinstance(grads[0], ms.Tensor):
        raise ValueError("'clip_grad_norm_' need to pass `grads`, "
                         "which can be get from 'mindspore.ops.grad' or mindspore.ops.value_and_grad.")

    # rewrite _ClipByGlobalNorm to support return total_norm
    new_grads, total_norm = _ClipByGlobalNorm(max_norm, None)(grads)
    return new_grads, cast_to_adapter_tensor(total_norm)

def clip_grad_norm_(parameters, max_norm, grads, norm_type=2.0, error_if_nonfinite=False, foreach=None):
    if graph_mode_condition():
        raise RuntimeError("Under graph mode, adapter not support in-place operation. "
                           "So please use 'clip_grad_norm' to replace 'clip_grad_norm_'")

    new_grads, total_norm = clip_grad_norm(parameters, max_norm, grads, norm_type, error_if_nonfinite, foreach)
    _hypermap(_assign, grads, new_grads)
    return total_norm

def clip_grad_value(parameters, clip_value, grads, foreach=None):
    unsupported_attr(foreach)
    unsupported_attr(parameters)
    if not isinstance(grads, tuple) or not isinstance(grads[0], ms.Tensor):
        raise ValueError("'clip_grad_value_' need to pass `grads`, "
                         "which can be get from 'mindspore.ops.grad' or mindspore.ops.value_and_grad.")
    # If clip_value < 0, _clip_value_min will greater than _clip_value_max
    # It is a special case with a special behavious, which ms.ops.clip_by_value can accept.
    _clip_value_min = -clip_value
    _clip_value_max = clip_value
    grads = ms.ops.clip_by_value(grads, _clip_value_min, _clip_value_max)
    return grads

def clip_grad_value_(parameters, clip_value, grads, foreach=None):
    if graph_mode_condition():
        raise RuntimeError("Under graph mode, adapter not support in-place operation. "
                           "So please use 'clip_grad_value' to replace 'clip_grad_value_'")

    new_grads = clip_grad_value(parameters, clip_value, grads, foreach)
    _hypermap(_assign, grads, new_grads)
