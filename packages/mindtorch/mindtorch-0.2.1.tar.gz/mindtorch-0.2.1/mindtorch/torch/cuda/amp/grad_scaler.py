import inspect
from collections import defaultdict
from enum import Enum
import mindspore as ms
from mindspore.amp import DynamicLossScaler, all_finite
import mindspore.ops as ops
from mindtorch.torch.nn.parameter import Parameter
from mindtorch.torch.tensor import tensor
from  mindtorch.torch.common.dtype import float32, int32
from mindtorch.torch.logging import warning
from mindtorch.utils import graph_mode_condition

class OptState(Enum):
    READY = 0
    UNSCALED = 1
    STEPPED = 2

def _refresh_per_optimizer_state():
    return {"stage": OptState.READY, "found_inf_per_device": {}}

def _assign(x1, x2):
    return x1.assign_value(x2)

_hypermap = ops.HyperMap()

class GradScaler(DynamicLossScaler):
    def __init__(self,
                 init_scale=2.**16,
                 growth_factor=2.0,
                 backoff_factor=0.5,
                 growth_interval=2000,
                 enabled=True):
        self._enabled = enabled

        if self._enabled:
            if init_scale < 1.0:
                raise ValueError("The argument 'scale_value' must be > 1, but got {}".format(init_scale))
            if growth_factor <= 1.0:
                raise ValueError("The growth factor must be > 1.0.")
            if backoff_factor >= 1.0:
                raise ValueError("The backoff factor must be < 1.0.")
            if not isinstance(growth_interval, int) or growth_interval < 0:
                raise ValueError(" The growth_interval must be int and > 0")

            # init_scale -> scale_value
            # growth_factor -> scale_factor
            # growth_interval -> scale_window
            # growth_tracker -> counter

            self._init_scale = init_scale
            self.scale_value = Parameter(tensor(init_scale, dtype=float32), name="scale_value", requires_grad=False)
            self.scale_factor = growth_factor
            self._backoff_factor = backoff_factor
            self.scale_window = growth_interval

            self._init_growth_tracker = 0
            # for mindspore
            self.counter = Parameter(tensor(0, dtype=int32), name="counter", requires_grad=False)
            self._per_optimizer_states = defaultdict(_refresh_per_optimizer_state)

    def _check_inf(self, grads):
        return {'all': ms.ops.logical_not(all_finite(grads))}

    def scale(self, outputs):
        if not self._enabled:
            return outputs
        return DynamicLossScaler.scale(self, outputs)

    def unscale_(self, optimizer, grads):
        if not self._enabled:
            return

        optimizer_state = self._per_optimizer_states[id(optimizer)]
        if optimizer_state["stage"] is OptState.UNSCALED:
            raise RuntimeError("unscale_() has already been called on this optimizer since the last update().")
        elif optimizer_state["stage"] is OptState.STEPPED:
            raise RuntimeError("unscale_() is being called after step().")

        optimizer_state['found_inf_per_device'] = self._check_inf(grads)
        if graph_mode_condition():
            raise RuntimeError("Under graph mode, GradScalar not support unscale_(), please use unscale(). "
                               "Example: change 'scaler.unscale_(optimizer, grads)' to "
                               "'grads = scaler.unscale(optimizer, grads)'")
        _hypermap(_assign, grads, DynamicLossScaler.unscale(self, grads))
        optimizer_state["stage"] = OptState.UNSCALED

    def unscale(self, optimizer, grads):
        if not self._enabled:
            return grads

        optimizer_state = self._per_optimizer_states[id(optimizer)]
        optimizer_state["found_inf_per_device"] = self._check_inf(grads)
        optimizer_state["stage"] = OptState.UNSCALED
        return DynamicLossScaler.unscale(self, grads)

    def _maybe_opt_step(self, optimizer, grads, optimizer_state, *args, **kwargs):
        retval = None
        if not sum(v.asnumpy().tolist() for v in optimizer_state["found_inf_per_device"].values()):
            retval = optimizer.step(grads, *args, **kwargs)
        return retval

    def step(self, optimizer, grads, *args, **kwargs):
        if not self._enabled:
            return optimizer.step(grads)

        if "closure" in kwargs:
            raise RuntimeError("Closure use is not currently supported if GradScaler is enabled.")

        optimizer_state = self._per_optimizer_states[id(optimizer)]

        if optimizer_state["stage"] is OptState.STEPPED:
            raise RuntimeError("step() has already been called since the last update().")

        retval = None

        if (hasattr(optimizer, "_step_supports_amp_scaling") and optimizer._step_supports_amp_scaling):
            kwargs_ = kwargs
            has_grad_scaler_kwarg = "grad_scaler" in inspect.signature(optimizer.step).parameters
            if has_grad_scaler_kwarg:
                warning(
                    "GradScaler is going to stop passing itself as a keyword argument to the passed " \
                    "optimizer. In the near future GradScaler registers `grad_scale: Tensor` and " \
                    "`found_inf: Tensor` to the passed optimizer and let the optimizer use them directly." \
                )
                kwargs_.update({"grad_scaler": self})
            else:
                scaler = self._get_scale_async()
                found_inf = optimizer_state["found_inf_per_device"]
                optimizer.grad_scale = None if optimizer_state["stage"] == OptState.UNSCALED else scaler
                optimizer.found_inf = found_inf
            retval = optimizer.step(grads, *args, **kwargs_)
            optimizer_state["stage"] = OptState.STEPPED
            if not has_grad_scaler_kwarg:
                del optimizer.grad_scale
                del optimizer.found_inf
            return retval

        if optimizer_state["stage"] is OptState.READY:
            self.unscale_(optimizer, grads)

        retval = self._maybe_opt_step(optimizer, grads, optimizer_state, *args, **kwargs)

        optimizer_state["stage"] = OptState.STEPPED
        return retval

    def adjust(self, grads_finite):
        one = ops.ones((), self.scale_value.dtype)
        scale_mul_factor = self.scale_value * self.scale_factor
        scale_value = ops.select(
            grads_finite,
            ops.select(
                self.counter == (self.scale_window - 1),
                ops.select(ops.isfinite(scale_mul_factor),
                           scale_mul_factor,
                           self.scale_value),
                self.scale_value),
            ops.maximum(one, self.scale_value * self._backoff_factor))
        ops.assign(self.scale_value, scale_value)

        counter = ((self.counter + 1) % self.scale_window) * grads_finite
        ops.assign(self.counter, counter)
        return True

    def update(self, new_scale=None):
        if not self._enabled:
            return

        if new_scale is not None:
            # Accept a new user-defined scale.
            if isinstance(new_scale, float):
                self.scale_value.set_data(ms.Tensor(new_scale))
            else:
                self.scale_value.set_data(new_scale)
        else:
            found_infs = [found_inf
                          for state in self._per_optimizer_states.values()
                          for found_inf in state["found_inf_per_device"].values()]
            found_inf_combined = found_infs[0]
            if len(found_infs) > 1:
                for i in range(1, len(found_infs)):
                    found_inf_combined = ms.ops.logical_or(found_inf_combined, found_infs[i])
            self.adjust(ms.ops.logical_not(found_inf_combined))

    def _get_scale_async(self):
        return self.scale_value

    def get_scale(self):
        if self._enabled:
            return self._init_scale if self.scale_value is None \
                   else self._get_scale_async().item()
        else:
            return 1.0

    def get_growth_factor(self):
        return self.scale_factor

    def set_growth_factor(self, new_factor):
        self.scale_factor = new_factor

    def get_backoff_factor(self):
        return self._backoff_factor

    def set_backoff_factor(self, new_factor):
        self._backoff_factor = new_factor

    def get_growth_interval(self):
        return self.scale_window

    def set_growth_interval(self, new_interval):
        self.scale_window = new_interval

    def _get_growth_tracker(self):
        if self._enabled:
            return self._init_growth_tracker if self.counter is None else self.counter.item()
        else:
            return 0

    def is_enabled(self):
        return self._enabled

    def state_dict(self):
        return {"scale": self.get_scale(),
                "growth_factor": self.scale_factor,
                "backoff_factor": self._backoff_factor,
                "growth_interval": self.scale_window,
                "_growth_tracker": self._get_growth_tracker()} if self._enabled else {}

    def load_state_dict(self, state_dict):
        if not self._enabled:
            return

        if len(state_dict) == 0:
            raise RuntimeError("The source state dict is empty, possibly because it was saved "
                               "from a disabled instance of GradScaler.")

        self._init_scale = state_dict["scale"]
        if self.scale_value is not None:
            self.scale_value.set_data(state_dict["scale"])
        self.scale_factor = state_dict["growth_factor"]
        self._backoff_factor = state_dict["backoff_factor"]
        self.scale_window = state_dict["growth_interval"]
        if self.counter is not None:
            self.counter.set_data(state_dict["_growth_tracker"])

    def __getstate__(self):
        state = self.__dict__.copy()
        if self._enabled:
            state['scale_value'] = state['scale_value'].asnumpy()
            state['counter'] = state['counter'].asnumpy()
        return state

    def __setstate__(self, state):
        if 'init_scale' in state:
            state['scale_value'] = Parameter(tensor(state['init_scale'].numpy()).to(float32))
            del state['init_scale']
        if 'scale_value' in state:
            state['scale_value'] = Parameter(tensor(state['scale_value']).to(float32))
        if 'counter' in state:
            state['counter'] = Parameter(tensor(state['counter']).to(int32))
        if 'growth_factor' in state:
            state['scale_factor'] = state['growth_factor']
            del state['growth_factor']
        if 'growth_interval' in state:
            state['scale_window'] = state['growth_interval']
            del state['growth_interval']
        self.__dict__.update(state)
