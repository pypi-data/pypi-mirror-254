from mindspore.experimental.optim import SGD as SGD_MS
from mindtorch.torch.optim.optimizer import _Optimizer
from mindtorch.utils import unsupported_attr

_default_lr = 0.01
class SGD(_Optimizer, SGD_MS):
    def __init__(self, params, lr=None, momentum=0, dampening=0,
                 weight_decay=0, nesterov=False, *, maximize=False, foreach=None,
                 differentiable=False):
        unsupported_attr(foreach)
        unsupported_attr(differentiable)
        if lr is None:
            for p_dict in params:
                if not isinstance(p_dict, dict) or 'lr' not in p_dict:
                    raise ValueError("parameter group didn't specify a value of required optimization parameter lr.")
            # Fake lr. The above code guarantees that every param_group has its own 'lr' setting.
            # So the following _default_lr won't take effect, just for the input args of mindspore SGD.
            lr = _default_lr
        SGD_MS.__init__(self, params, lr, momentum, dampening, weight_decay, nesterov, maximize=maximize)
        _Optimizer.__init__(self)

    def __setstate__(self, state):
        _Optimizer.__setstate__(self, state)
        for group in self.param_groups:
            group.setdefault('nesterov', False)
            group.setdefault('maximize', False)

    def state_dict(self):
        return super()._ms_state_dict('accum')

    def load_state_dict(self, state_dict):
        return super()._ms_load_state_dict(state_dict, 'accum')
