from mindspore.experimental.optim import Adam as Adam_MS
from mindtorch.torch.optim.optimizer import _Optimizer, _is_tensor
from mindtorch.torch.tensor import tensor

class Adam(_Optimizer, Adam_MS):
    def __init__(self, *args, **kwargs):
        Adam_MS.__init__(self, *args, **kwargs)
        _Optimizer.__init__(self)

    def __setstate__(self, state):
        _Optimizer.__setstate__(self, state)
        for group in self.param_groups:
            group.setdefault('amsgrad', False)
            group.setdefault('maximize', False)

        state_values = list(self.state.values())
        step_is_tensor = (len(state_values) != 0) and _is_tensor(state_values[0]['step'])
        if not step_is_tensor:
            for s in state_values:
                s['step'] = tensor(float(s['step']))

    def state_dict(self):
        return super()._ms_state_dict('exp_avg', 'exp_avg_sq', 'max_exp_avg_sq', 'state_step')

    def load_state_dict(self, state_dict):
        return super()._ms_load_state_dict(state_dict, 'exp_avg', 'exp_avg_sq', 'max_exp_avg_sq', 'state_step')
