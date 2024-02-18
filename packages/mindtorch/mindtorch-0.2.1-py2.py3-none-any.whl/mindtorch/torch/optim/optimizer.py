import abc
from collections import OrderedDict, defaultdict
from collections.abc import Iterable
from copy import deepcopy
from itertools import chain
import mindspore as ms
from mindspore.experimental.optim import Optimizer as Optimizer_MS
from mindtorch.torch.tensor import Tensor, tensor, cast_to_ms_tensor
from mindtorch.utils import unsupported_attr

class _RequiredParameter():
    """Singleton class representing a required parameter for an Optimizer."""
    def __repr__(self):
        return "<required parameter>"

required = _RequiredParameter()

class _Optimizer:
    def __init__(self):
        self._optimizer_step_pre_hooks=OrderedDict()
        self._optimizer_step_post_hooks=OrderedDict()

        self._patch_step_function()

    def _is_inner_optimizer(self):
        return True

    def __getstate__(self):
        return {
            'defaults': self.defaults,
            'state': self.state,
            'param_groups': self.param_groups,
        }
    def __setstate__(self, state):
        self.__dict__.update(state)
        if '_optimizer_step_pre_hooks' not in self.__dict__:
            self._optimizer_step_pre_hooks = OrderedDict()
        if '_optimizer_step_post_hooks' not in self.__dict__:
            self._optimizer_step_post_hooks = OrderedDict()
        self._patch_step_function()
        self.defaults.setdefault('differentiable', False)

    def __repr__(self):
        format_string = self.__class__.__name__ + ' ('
        for i, group in enumerate(self.param_groups):
            format_string += '\n'
            format_string += 'Parameter Group {0}\n'.format(i)
            for key in sorted(group.keys()):
                if key != 'params':
                    format_string += '    {0}: {1}\n'.format(key, group[key])
        format_string += ')'
        return format_string

    @staticmethod
    def profile_hook_step(func):
        unsupported_attr(func)
        raise NotImplementedError("For Optimizer, 'profile_hook_step' not support yet.")

    def _patch_step_function(self):
        self._zero_grad_profile_name = "Optimizer.zero_grad#{}.zero_grad".format(self.__class__.__name__)
        # hook not support yet.
        # hooked = getattr(self.__class__.step, "hooked", None)
        # if not hooked:
        #     self.__class__.step = self.profile_hook_step(self.__class__.step)
        #     self.__class__.step.hooked = True

    def register_step_pre_hook(self):
        raise NotImplementedError("For optimizer, 'register_step_pre_hook' is not supported yet.")

    def register_step_post_hook(self):
        raise NotImplementedError("For optimizer, 'register_step_post_hook' is not supported yet.")

    def state_dict(self):
        r"""Returns the state of the optimizer as a :class:`dict`.

        It contains two entries:

        * state - a dict holding current optimization state. Its content
            differs between optimizer classes.
        * param_groups - a list containing all parameter groups where each
            parameter group is a dict
        """
        # Save order indices instead of Tensors
        param_mappings = {}
        start_index = 0

        def pack_group(group):
            nonlocal start_index
            packed = {k: v for k, v in group.items() if k != 'params'}
            if 'lr' in packed.keys():
                if isinstance(packed['lr'], ms.Tensor):
                    packed['lr'] = packed['lr'].asnumpy().tolist()
            param_mappings.update({id(p): i for i, p in enumerate(group['params'], start_index)
                                   if id(p) not in param_mappings})
            packed['params'] = [param_mappings[id(p)] for p in group['params']]
            start_index += len(packed['params'])
            return packed
        param_groups = [pack_group(g) for g in self.param_groups]
        # Remap state to use order indices as keys
        packed_state = {(param_mappings[id(k)] if isinstance(k, Tensor) else k): v
                        for k, v in self.state.items()}
        return {
            'state': packed_state,
            'param_groups': param_groups,
        }

    def load_state_dict(self, state_dict):
        r"""Loads the optimizer state.

        Args:
            state_dict (dict): optimizer state. Should be an object returned
                from a call to :meth:`state_dict`.
        """
        # deepcopy, to be consistent with module API
        state_dict = deepcopy(state_dict)
        # Validate the state_dict
        groups = self.param_groups
        saved_groups = state_dict['param_groups']

        if len(groups) != len(saved_groups):
            raise ValueError("loaded state dict has a different number of "
                             "parameter groups")
        param_lens = (len(g['params']) for g in groups)
        saved_lens = (len(g['params']) for g in saved_groups)
        if any(p_len != s_len for p_len, s_len in zip(param_lens, saved_lens)):
            raise ValueError("loaded state dict contains a parameter group "
                             "that doesn't match the size of optimizer's group")

        # Update the state
        id_map = dict(zip(chain.from_iterable((g['params'] for g in saved_groups)),
                      chain.from_iterable((g['params'] for g in groups))))

        def cast(param, value, key=None):
            r"""Make a deep copy of value, casting all tensors to device of param."""
            if isinstance(value, Tensor):
                # Floating-point types are a bit special here. They are the only ones
                # that are assumed to always match the type of params.
                # Make sure state['step'] is not casted https://github.com/pytorch/pytorch/issues/74424
                if key != "step":
                    if param.is_floating_point():
                        value = value.to(param.dtype)
                    value = value.to(param.device)
                return value
            elif isinstance(value, dict):
                return {k: cast(param, v, key=k) for k, v in value.items()}
            elif isinstance(value, Iterable):
                return type(value)(cast(param, v) for v in value)
            else:
                return value

        # Copy state assigned to params (and cast tensors to appropriate types).
        # State that is not assigned to params is copied as is (needed for
        # backward compatibility).
        state = defaultdict(dict)
        for k, v in state_dict['state'].items():
            if k in id_map:
                param = id_map[k]
                state[param] = cast(param, v)
            else:
                state[k] = v

        # Update parameter groups, setting their 'params' value
        def update_group(group, new_group):
            new_group['params'] = group['params']
            if 'lr' in group.keys():
                if isinstance(group['lr'], ms.Parameter):
                    new_group['lr'] = ms.Parameter(ms.Tensor(new_group['lr'], ms.float32), group['lr'].name)
            return new_group
        param_groups = [
            update_group(g, ng) for g, ng in zip(groups, saved_groups)]
        self.__setstate__({'state': state, 'param_groups': param_groups})

    def _ms_state_dict(self, *ms_params_name):
        _state_dict = _Optimizer.state_dict(self)
        def _save(ms_params):
            if isinstance(ms_params, Iterable):
                _state = []
                for p in ms_params:
                    _state.append(_save(p))
            else:
                _state = tensor(ms_params.asnumpy())
            return _state

        for name in ms_params_name:
            ms_params = getattr(self, name, None)
            if ms_params is not None:
                _state_dict[name] = _save(ms_params)
        return _state_dict

    def _ms_load_state_dict(self, state_dict, *ms_params_name):
        _Optimizer.load_state_dict(self, state_dict)

        def _load(ms_params, state_tensor, name):
            if isinstance(ms_params, Iterable):
                if not isinstance(state_tensor, Iterable):
                    raise ValueError(f"state_dict of ms_param '{name}' is not correct. please check. "
                                     f"(ms_param '{name}' is Iterable, but state_dict['{name}'] is not.)")
                if len(ms_params) != len(state_tensor):
                    raise ValueError(f"state_dict of ms_param '{name}' is not correct. please check. "
                                     f"(length of ms_param '{name}' and state_dict['{name}'] are not equal, "
                                     f"get {len(ms_params)} and {len(state_tensor)}")
                for i, _ in enumerate(ms_params):
                    _load(ms_params[i], state_tensor[i], name)
            else:
                _data = cast_to_ms_tensor(state_tensor)
                try:
                    ms_params.set_data(_data)
                except Exception as e:
                    raise ValueError(f"state_dict of ms_param '{name}' is not correct. please check. "
                                     f"({e})") from e

        for name in ms_params_name:
            ms_params = getattr(self, name, None)
            if ms_params is None:
                continue
            _params = state_dict.get(name, None)
            # If name in state_dict, use state_dict[name], because it was saved from MindTorch.
            if _params is not None:
                _load(ms_params, _params, name)
            else:
                _state = state_dict.get('state', None)
                # If name in state_dict['state'], it was saved from PyTorch. Load that to MindTorch.
                if _state is not None:
                    # _state is a dict like: {0:{name: Tensor}, 1:{name:Tensor}}
                    for k, state in _state.items():
                        _params = state.get(name, None)
                        # assert name in state.
                        if _params is not None:
                            _load(ms_params[k], _params, name)

    def step(self, grads, closure=None):
        loss = None
        if closure is not None:
            loss = closure()
        self.construct(grads)
        return loss

class _OptimizerMeta(abc.ABCMeta, type(Optimizer_MS)):
    """
    Meta class for Optimizer. Used internally.
    """

class Optimizer(_Optimizer, Optimizer_MS, metaclass=_OptimizerMeta):
    def __init__(self, *args, **kwargs):
        Optimizer_MS.__init__(self, *args, **kwargs)
        _Optimizer.__init__(self)

    @classmethod
    def __subclasshook__(cls, sub):
        """
        Subclass with _is_inner_optimizer attr will be instance of Optimizer
        """
        if cls is Optimizer:
            if any("_is_inner_optimizer" in s.__dict__ for s in sub.__mro__):
                return True
        return NotImplemented

def _is_tensor(obj):
    return isinstance(obj, Tensor)
