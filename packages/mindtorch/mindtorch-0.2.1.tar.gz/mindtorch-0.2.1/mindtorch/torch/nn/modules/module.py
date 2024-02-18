#!/usr/bin/env python
# -*- coding: utf-8 -*-

import itertools
from collections import OrderedDict, namedtuple
from typing import Mapping, List

import mindspore as ms
from mindspore.nn import Cell
from mindspore import Tensor as ms_Tensor
from mindtorch.torch.overrides import is_tensor_like
from mindtorch.torch.tensor import Tensor, _dtypeDict, cast_to_ms_tensor
from mindtorch.torch.nn.parameter import Parameter
from mindtorch.utils import unsupported_attr
from mindtorch.torch.types import device as device_class
from mindtorch.torch.common.dtype import all_complex_type, all_float_and_complex_type
from mindtorch.torch.functional import empty_like
from mindtorch.torch.logging import warning


__all__ = ['Module']


_global_parameter_registration_hooks = OrderedDict()
_global_module_registration_hooks = OrderedDict()
_global_buffer_registration_hooks = OrderedDict()

_EXTRA_STATE_KEY_SUFFIX = '_extra_state'


class _IncompatibleKeys(namedtuple('IncompatibleKeys', ['missing_keys', 'unexpected_keys'])):
    def __repr__(self):
        if not self.missing_keys and not self.unexpected_keys:
            return '<All keys matched successfully>'
        return super().__repr__()

    __str__ = __repr__


class Module(Cell):
    def __init__(self, auto_prefix=True, flags=None):
        super(Module, self).__init__(auto_prefix, flags)
        # Some class members in same usage are defined in mindspore.nn.Cell, so Module reuses them
        # If re-difine these members with different names, Module should deal with data synchronization issue,
        # which is easy to make mistakes and unnecessary. Belows are the two different of members name
        # refers to torch.nn.Module
        # _parameters -> _params
        # _modules -> _cells

        # use object.__setattr__ to accelerate, because self.__setattr__ has too much procedure
        object.__setattr__(self, 'training', True)
        object.__setattr__(self, '_buffers', OrderedDict())
        object.__setattr__(self, '_non_persistent_buffers_set', set())
        object.__setattr__(self, '_state_dict_hooks', OrderedDict())
        object.__setattr__(self, '_state_dict_pre_hooks', OrderedDict())
        object.__setattr__(self, '_version', 1)

    @property
    def _parameters(self):
        return self._params

    @property
    def _modules(self):
        return self._cells

    def __del__(self):
        pass

    def __repr__(self):
        extra_str = self.extra_repr()
        info_str = self.__class__.__name__ + '('
        if self._cells:
            sub_str = '\n'
            if extra_str:
                sub_str += '{}\n'.format(self.extra_repr())
            for key, value in self._cells.items():
                sub_str += '  ({}): {}\n'.format(key, repr(value))
            sub_str = sub_str.replace('\n', '\n') + ')'
            info_str += sub_str
        else:
            info_str += extra_str + ')'
        return info_str

    def __delattr__(self, name):
        if name in self._buffers:
            del self._buffers[name]
            self._non_persistent_buffers_set.discard(name)
        else:
            super().__delattr__(name)

    def __getattr__(self, name):
        if '_buffers' in self.__dict__:
            buffers = self.__dict__['_buffers']
            if name in buffers:
                return buffers[name]

        return super().__getattr__(name)

    def __setattr__(self, name, value):
        params = self.__dict__.get('_params')
        modules = self.__dict__.get('_cells')
        buffers = self.__dict__.get('_buffers')
        _non_persistent_buffers_set = self.__dict__.get('_non_persistent_buffers_set')

        def remove_from(*dict_or_sets):
            for d in dict_or_sets:
                if name in d:
                    if isinstance(d, dict):
                        delattr(self, name)
                    else:
                        d.discard(name)

        if isinstance(value, Parameter):
            if params is None:
                raise AttributeError(
                    "cannot assign parameters before Module.__init__() call")
            if hasattr(self, name) and name not in params:
                remove_from(self.__dict__, buffers, modules, _non_persistent_buffers_set)
            super().__setattr__(name, value)
        elif isinstance(value, Module):
            if modules is None:
                raise AttributeError(
                    "cannot assign parameters before Module.__init__() call")
            if hasattr(self, name) and name not in modules:
                remove_from(self.__dict__, params, buffers, _non_persistent_buffers_set)
            super().__setattr__(name, value)
        elif buffers is not None and name in buffers:
            if value is not None and not isinstance(value, Tensor):
                raise TypeError("cannot assign '{}' as buffer '{}' "
                                "(torch.Tensor or None expected)"
                                .format(type(value), name))

            for hook in _global_buffer_registration_hooks.values():
                output = hook(self, name, value)
                if output is not None:
                    value = output
            if hasattr(self, '_is_adapter_norm') and name in ('running_mean', 'running_var') \
                and name in self._params and isinstance(value, ms_Tensor):
                self._params[name].set_data(value, slice_shape=True)
                buffers[name] = self._params[name]
            else:
                buffers[name] = value
        else:
            super().__setattr__(name, value)

    def _save_to_state_dict(self, destination, prefix, keep_vars):
        for name, param in self._parameters.items():
            if param is not None:
                destination[prefix + name] = param if keep_vars else param.detach()
        for name, buf in self._buffers.items():
            if buf is not None and name not in self._non_persistent_buffers_set:
                destination[prefix + name] = buf if keep_vars else buf.detach()
        extra_state_key = prefix + _EXTRA_STATE_KEY_SUFFIX
        if getattr(self.__class__, "get_extra_state", Module.get_extra_state) is not Module.get_extra_state:
            destination[extra_state_key] = self.get_extra_state()

    def state_dict(self, *args, destination=None, prefix='', keep_vars=False):
        # TODO: Remove `args` and the parsing logic when BC allows.
        if len(args) > 0:
            if destination is None:
                destination = args[0]
            if len(args) > 1 and prefix == '':
                prefix = args[1]
            if len(args) > 2 and keep_vars is False:
                keep_vars = args[2]

        if destination is None:
            destination = OrderedDict()
            destination._metadata = OrderedDict()

        local_metadata = dict(version=self._version)
        if hasattr(destination, "_metadata"):
            destination._metadata[prefix[:-1]] = local_metadata
        self._save_to_state_dict(destination, prefix, keep_vars)
        # name_cells() will filter the same cells.
        # for name, module in self.name_cells().items():
        for name, module in self._modules.items():
            # Add 'isinstance(module, Module)' conditions in case to go into mindspore.nn.Cell.
            # In some case we will use api from mindspore.nn to do the computations
            if module is not None and isinstance(module, Module):
                module.state_dict(destination=destination, prefix=prefix + name + '.', keep_vars=keep_vars)
        for hook in self._state_dict_hooks.values():
            hook_result = hook(self, destination, prefix, local_metadata)
            if hook_result is not None:
                destination = hook_result
        return destination

    def _convert_state_dict(self, state_dict):
        ms_state_dict = {}
        for name, param in state_dict.items():
            if isinstance(param, ms.Tensor):
                param = Parameter(param, name=name)
            ms_state_dict[name] = param
        return ms_state_dict

    def _load_from_state_dict(self, state_dict, prefix, local_metadata, strict,
                              missing_keys, unexpected_keys, error_msgs):

        unsupported_attr(local_metadata)
        # TODO:
        # for hook in self._load_state_dict_pre_hooks.values():
        #     hook(state_dict, prefix, local_metadata, strict, missing_keys, unexpected_keys, error_msgs)

        persistent_buffers = {k: v for k, v in self._buffers.items() if k not in self._non_persistent_buffers_set}
        local_name_params = itertools.chain(self._parameters.items(), persistent_buffers.items())
        local_state = {k: v for k, v in local_name_params if v is not None}

        for name, param in local_state.items():
            key = prefix + name
            if key in state_dict:
                input_param = state_dict[key]
                if not is_tensor_like(input_param):
                    error_msgs.append('While copying the parameter named "{}", '
                                      'expected torch.Tensor or Tensor-like object from checkpoint but '
                                      'received {}'
                                      .format(key, type(input_param)))
                    continue

                # TODO: Do not support is_param_lazy.
                # # This is used to avoid copying uninitialized parameters into
                # # non-lazy modules, since they dont have the hook to do the checks
                # # in such case, it will error when accessing the .shape attribute.
                # is_param_lazy = torch.nn.parameter.is_lazy(param)
                # # Backward compatibility: loading 1-dim tensor from 0.3.* to version 0.4+
                # if not is_param_lazy and len(param.shape) == 0 and len(input_param.shape) == 1:
                #     input_param = input_param[0]
                #
                # if not is_param_lazy and input_param.shape != param.shape:
                #     # local shape should match the one in checkpoint
                #     error_msgs.append('size mismatch for {}: copying a param with shape {} from checkpoint, '
                #                       'the shape in current model is {}.'
                #                       .format(key, input_param.shape, param.shape))
                #     continue
                try:
                    def _copy_param(param, input_param):
                        input_ms = cast_to_ms_tensor(input_param)
                        if len(param.shape) > 0 and input_ms != param.shape:
                            output = ms.ops.broadcast_to(input_ms, param.shape)
                        else:
                            output = input_ms
                        output = output.astype(param.dtype)
                        param.assign_value(output)

                    _copy_param(param, input_param)
                except Exception as ex: # pylint: disable=broad-except
                    error_msgs.append('While copying the parameter named "{}", '
                                      'whose dimensions in the model are {} and '
                                      'whose dimensions in the checkpoint are {}, '
                                      'an exception occurred : {}.'
                                      .format(key, param.size(), input_param.size(), ex.args))
            elif strict:
                missing_keys.append(key)

        extra_state_key = prefix + _EXTRA_STATE_KEY_SUFFIX
        if getattr(self.__class__, "set_extra_state", Module.set_extra_state) is not Module.set_extra_state:
            if extra_state_key in state_dict:
                self.set_extra_state(state_dict[extra_state_key])
            elif strict:
                missing_keys.append(extra_state_key)
        elif strict and (extra_state_key in state_dict):
            unexpected_keys.append(extra_state_key)

        if strict:
            for key in state_dict.keys():
                if key.startswith(prefix) and key != extra_state_key:
                    input_name = key[len(prefix):]
                    input_name = input_name.split('.', 1)[0]  # get the name of param/buffer/child
                    if input_name not in self._modules and input_name not in local_state:
                        unexpected_keys.append(key)

    def load_state_dict(self, state_dict, strict=True):
        if not isinstance(state_dict, Mapping):
            raise TypeError("Expected state_dict to be dict-like, got {}.".format(type(state_dict)))

        missing_keys: List[str] = []
        unexpected_keys: List[str] = []
        error_msgs: List[str] = []

        # copy state_dict so _load_from_state_dict can modify it
        metadata = getattr(state_dict, '_metadata', None)
        state_dict = OrderedDict(state_dict)
        if metadata is not None:
            # mypy isn't aware that "_metadata" exists in state_dict
            state_dict._metadata = metadata  # type: ignore[attr-defined]

        def load(module, prefix=''):
            # Add 'isinstance(module, Module)' conditions in case to go into mindspore.nn.Cell.
            if not isinstance(module, Module):
                return
            local_metadata = {} if metadata is None else metadata.get(prefix[:-1], {})
            module._load_from_state_dict(
                state_dict, prefix, local_metadata, True, missing_keys, unexpected_keys, error_msgs)
            for name, child in module._modules.items():
                if child is not None:
                    load(child, prefix + name + '.')

            # TODO: # Note that the hook can modify missing_keys and unexpected_keys.
            # incompatible_keys = _IncompatibleKeys(missing_keys, unexpected_keys)
            # for hook in module._load_state_dict_post_hooks.values():
            #     out = hook(module, incompatible_keys)
            #     assert out is None, (
            #         "Hooks registered with ``register_load_state_dict_post_hook`` are not"
            #         "expected to return new values, if incompatible_keys need to be modified,"
            #         "it should be done inplace."
            #     )

        load(self)
        del load

        if strict:
            if len(unexpected_keys) > 0:
                error_msgs.insert(
                    0, 'Unexpected key(s) in state_dict: {}. '.format(
                        ', '.join('"{}"'.format(k) for k in unexpected_keys)))
            if len(missing_keys) > 0:
                error_msgs.insert(
                    0, 'Missing key(s) in state_dict: {}. '.format(
                        ', '.join('"{}"'.format(k) for k in missing_keys)))

        if len(error_msgs) > 0:
            raise RuntimeError('Error(s) in loading state_dict for {}:\n\t{}'.format(
                               self.__class__.__name__, "\n\t".join(error_msgs)))
        return _IncompatibleKeys(missing_keys, unexpected_keys)

    def extra_repr(self):
        r"""Set the extra representation of the module"""
        return ''

    def construct(self, *inputs, **kwargs):
        return self.forward(*inputs, **kwargs)

    def _run_forward_pre_hook(self, inputs):
        for fn in self._forward_pre_hook.values():
            ret = fn(self, inputs)
            if ret is not None:
                if not isinstance(ret, tuple):
                    inputs = (ret,)
                else:
                    inputs = ret
        return inputs

    def _run_forward_hook(self, inputs, output):
        for fn in self._forward_hook.values():
            ret = fn(self, inputs, output)
            if ret is not None:
                output = ret
        return output

    def _run_construct(self, cast_inputs, kwargs):
        """Run the construct function"""
        if self._enable_forward_pre_hook:
            cast_inputs = self._run_forward_pre_hook(cast_inputs)
        if self._enable_backward_hook:
            output = self._backward_hook_construct(*cast_inputs)
        elif hasattr(self, "_shard_fn"):
            output = self._shard_fn(*cast_inputs, **kwargs)
        else:
            output = self.construct(*cast_inputs, **kwargs)
        if self._enable_forward_hook:
            output = self._run_forward_hook(cast_inputs, output)

        return output

    def forward(self, *inputs, **kwargs):
        raise NotImplementedError("The forward method must be implemented by inherited class")

    def train(self, mode=True):
        self.set_train(mode)
        return self

    def eval(self):
        self.set_train(False)
        return self

    def requires_grad_(self, requires_grad=True):
        for p in self.parameters():
            p.requires_grad_(requires_grad)
        return self

    def modules(self):
        for _, module in self.named_modules():
            yield module

    def named_modules(self, memo=None, prefix='', remove_duplicate=True):
        if memo is None:
            memo = set()
        if self not in memo:
            if remove_duplicate:
                memo.add(self)
            yield prefix, self
            for name, module in self._cells.items():
                if module is None or not isinstance(module, Module):
                    continue
                submodule_prefix = prefix + ('.' if prefix else '') + name
                for m in module.named_modules(memo, submodule_prefix, remove_duplicate):
                    yield m

    def _parameters_and_names(self, name_prefix='', expand=True):
        cells = []
        if expand:
            cells = self.cells_and_names(name_prefix=name_prefix)
        else:
            cells.append((name_prefix, self))

        params_set = set()
        for cell_name, cell in cells:
            params = cell._params.items()
            for par_name, par in params:
                if par.inited_param is not None:
                    par = par.inited_param
                if par is not None and id(par) not in params_set:
                    params_set.add(id(par))
                    par_new_name = par_name
                    if cell_name:
                        par_new_name = cell_name + '.' + par_new_name
                        # TODO Update parameter names to avoid duplicates
                        par.name = par_new_name
                    yield par_new_name, par

    def add_module(self, name, module):
        for hook in _global_module_registration_hooks.values():
            output = hook(self, name, module)
            if output is not None:
                module = output
        self.insert_child_to_cell(name, module)

    def _get_name(self):
        return self.__class__.__name__

    def get_submodule(self, target):
        if target == "":
            return self
        atoms = target.split(".")
        mod = self

        for item in atoms:
            if not hasattr(mod, item):
                raise AttributeError(mod._get_name() + " has no "
                                     "attribute `" + item + "`")

            mod = getattr(mod, item)

            if not isinstance(mod, Module):
                raise AttributeError("`" + item + "` is not "
                                     "an nn.Module")

        return mod

    def get_parameter(self, target):
        module_path, _, param_name = target.rpartition(".")

        mod = self.get_submodule(module_path)

        if not hasattr(mod, param_name):
            raise AttributeError(mod._get_name() + " has no attribute `"
                                 + param_name + "`")

        param = getattr(mod, param_name)

        if not isinstance(param, Parameter):
            raise AttributeError("`" + param_name + "` is not an "
                                 "nn.Parameter")

        return param

    def get_buffer(self, target):
        module_path, _, buffer_name = target.rpartition(".")

        mod = self.get_submodule(module_path)

        if not hasattr(mod, buffer_name):
            raise AttributeError(mod._get_name() + " has no attribute `"
                                 + buffer_name + "`")

        buffer = getattr(mod, buffer_name)

        if buffer_name not in mod._buffers:
            raise AttributeError("`" + buffer_name + "` is not a buffer")

        return buffer

    def get_extra_state(self):
        raise RuntimeError(
            "Reached a code path in Module.get_extra_state() that should never be called.")

    def set_extra_state(self, state):
        raise RuntimeError(
            "Reached a code path in Module.set_extra_state() that should never be called.")

    def _apply(self, fn):
        for module in self.children():
            module._apply(fn)

        def compute_should_use_set_data(tensor, tensor_applied):
            if tensor.dtype != tensor_applied.dtype:
                return False
            return True

        for key, param in self.parameters_and_names(expand=False):
            if param is None:
                continue

            # Do not use _apply in computation, just for init usage, because can not avoid gradient now.
            param_applied = fn(param)

            should_use_set_data = compute_should_use_set_data(param, param_applied)
            if should_use_set_data:
                param.set_data(param_applied)
                out_param = param
            else:
                out_param = Parameter(param_applied, param.requires_grad)
                self.insert_param_to_cell(key, out_param)
                if hasattr(self, '_is_adapter_norm') and key in ('running_mean', 'running_var'):
                    # rebuild link between buffer and parameter.
                    self._buffers[key] = out_param

        for key, buf in self._buffers.items():
            if buf is not None:
                if hasattr(self, '_is_adapter_norm') and key in ('running_mean', 'running_var'):
                    if isinstance(buf, Parameter):
                        # when is parameter, mean has been process in parameters_and_names branch
                        continue
                self._buffers[key] = fn(buf)

        return self

    def float(self):
        return self._apply(lambda t: t.float() if t.is_floating_point() else t)

    def double(self):
        return self._apply(lambda t: t.double() if t.is_floating_point() else t)

    def half(self):
        return self._apply(lambda t: t.half() if t.is_floating_point() else t)

    def bfloat16(self):
        return self._apply(lambda t: t.bfloat16() if t.is_floating_point() else t)

    def to_empty(self, *, device=None):
        return self._apply(lambda t: empty_like(t, device=device))

    def register_module(self, name, module):
        """Alias for :func:`add_module`."""
        self.add_module(name, module)

    def named_parameters(self, prefix='', recurse=True, remove_duplicate=True):
        gen = self._named_members(
            lambda module: module._params.items(),
            prefix=prefix, recurse=recurse, remove_duplicate=remove_duplicate, from_param=True)
        yield from gen

    def named_children(self):
        r"""Returns an iterator over immediate children modules, yielding both
        the name of the module as well as the module itself.

        Yields:
            (string, Module): Tuple containing a name and child module

        Example::

            >>> for name, module in model.named_children():
            >>>     if name in ['conv4', 'conv5']:
            >>>         print(module)

        """
        memo = set()
        for name, module in self._cells.items():
            if module is not None and module not in memo:
                memo.add(module)
                yield name, module

    def children(self):
        r"""Returns an iterator over immediate children modules.

        Yields:
            Module: a child module
        """
        for _, module in self.named_children():
            yield module

    def apply(self, fn=None):
        r"""Applies ``fn`` recursively to every submodule (as returned by ``.children()``)
        as well as self. Typical use includes initializing the parameters of a model
        (see also :ref:`nn-init-doc`).

        Args:
            fn (:class:`Module` -> None): function to be applied to each submodule

        Returns:
            Module: self

        Example::

            >>> def init_weights(m):
            >>>     print(m)
            >>>     if type(m) == nn.Linear:
            >>>         m.weight.fill_(1.0)
            >>>         print(m.weight)
            >>> net = nn.Sequential(nn.Linear(2, 2), nn.Linear(2, 2))
            >>> net.apply(init_weights)
        """

        for module in self.children():
            module.apply(fn)
        fn(self)
        return self

    def parameters(self, recurse=True):
        for _, param in self.named_parameters(recurse=recurse):
            yield param

    def register_buffer(self, name, tensor, persistent=True):
        r"""Adds a buffer to the module.

               This is typically used to register a buffer that should not to be
               considered a model parameter. For example, BatchNorm's ``running_mean``
               is not a parameter, but is part of the module's state. Buffers, by
               default, are persistent and will be saved alongside parameters. This
               behavior can be changed by setting :attr:`persistent` to ``False``. The
               only difference between a persistent buffer and a non-persistent buffer
               is that the latter will not be a part of this module's
               :attr:`state_dict`.

               Buffers can be accessed as attributes using given names.

               Args:
                   name (string): name of the buffer. The buffer can be accessed
                       from this module using the given name
                   tensor (Tensor or None): buffer to be registered. If ``None``, then operations
                       that run on buffers, such as :attr:`cuda`, are ignored. If ``None``,
                       the buffer is **not** included in the module's :attr:`state_dict`.
                   persistent (bool): whether the buffer is part of this module's
                       :attr:`state_dict`.
               """
        unsupported_attr(persistent)

        if '_buffers' not in self.__dict__:
            raise AttributeError("cannot assign buffer before Module.__init__() call.")
        elif not isinstance(name, str):
            raise TypeError("buffer name should be a string. "
                            "Got {}".format(type(name)))
        elif '.' in name:
            raise KeyError("buffer name can't contain \".\"")
        elif name == '':
            raise KeyError("buffer name can't be empty string \"\"")
        elif hasattr(self, name) and name not in self._buffers and \
            not hasattr(self, '_is_adapter_norm') and name not in ('running_mean', 'running_var'):
            raise KeyError("attribute '{}' already exists".format(name))
        elif tensor is not None and not isinstance(tensor, ms_Tensor):
            raise TypeError("cannot assign '{}' object to buffer '{}' "
                            "(Tensor or None required)"
                            .format(type(tensor), name))
        else:
            if hasattr(self, '_is_adapter_norm') and name in ('running_mean', 'running_var') \
                and name in self._params and isinstance(tensor, ms_Tensor):
                # if 'running_mean', 'running_var' in self._param and tensor is not None
                # update them, and use ref of them as _buffers[name].
                # Otherwise, just update _buffers[name]
                self._params[name].set_data(tensor, slice_shape=True)
                self._buffers[name] = self._params[name]
            else:
                self._buffers[name] = tensor
            if persistent:
                self._non_persistent_buffers_set.discard(name)
            else:
                self._non_persistent_buffers_set.add(name)


    def _named_members(self, get_members_fn, prefix='', recurse=True, remove_duplicate=True, *, from_param=False):
        r"""Helper method for yielding various names + members of modules."""
        memo = set()
        modules = self.named_modules(prefix=prefix, remove_duplicate=remove_duplicate) if recurse else [(prefix, self)]
        for module_prefix, module in modules:
            members = get_members_fn(module)
            for k, v in members:
                # `running_mean` and `running_var should be in buffer.
                # But mindspore primitive only support `Parameter`.
                # Therefore, in adapter, there are declared as `Parameter`.
                # To avoid exporting them in "module.parameters()", do the following filtering.
                if isinstance(v, Parameter) and k in ("running_mean", "running_var") and \
                   hasattr(module, '_is_adapter_norm') and from_param:
                    continue
                if v is None or v in memo:
                    continue
                if remove_duplicate:
                    memo.add(v)
                name = module_prefix + ('.' if module_prefix else '') + k
                # To update `Parameter.name`.
                # Because when `Parameter` is lazy initialized in Modules, its name cannot be updated.
                # That may cause some problem, such as duplicated parameter's name in a Module,
                # which is not allowed in mindspore pipeline.
                # To Avoid such problem, update name when get parameters in Module.
                if isinstance(v, Parameter):
                    if len(v.name) <= len(name):
                        v.name = name
                yield name, v

    def named_buffers(self, prefix='', recurse=True, remove_duplicate=True):
        gen = self._named_members(
            lambda module: module._buffers.items(),
            prefix=prefix, recurse=recurse, remove_duplicate=remove_duplicate)
        yield from gen

    def buffers(self, recurse=True):
        for _, buf in self.named_buffers(recurse=recurse):
            yield buf

    def _cast_to_dtype(self, dtype):
        if dtype is not None:
            # TODO: if not (dtype.is_floating_point or dtype.is_complex):
            if not dtype in all_float_and_complex_type:
                raise TypeError('nn.Module.to only accepts floating point or complex '
                                'dtypes, but got desired dtype={}'.format(dtype))
            # TODO:if dtype.is_complex:
            if dtype in all_complex_type:
                warning(
                    "Complex modules are a new feature under active development whose design may change, "
                    "and some modules might not work as expected when using complex tensors as parameters or buffers."
                )

        def convert(t):
            return t.to(dtype if t.is_floating_point() or t.is_complex() else None)

        return self._apply(convert)


    def to(self, *args, **kwargs):
        # TODO:
        # Note that this API requires the user to ensure the correctness of the input currently,
        # and only the function of modifying device is available.

        args_len = len(args)
        kwargs_len = len(kwargs)

        if args_len == 0 and kwargs_len == 0:
            raise ValueError("Module.to is missing inputs, please check.")
        if "dtype" in kwargs:
            set_dtype = kwargs.get("dtype")
            return self._cast_to_dtype(set_dtype)
        elif "tensor" in kwargs:
            set_dtype = kwargs.get("tensor").dtype
            return self._cast_to_dtype(set_dtype)
        elif "memory_format" in kwargs:
            raise ValueError("Module.to is not support set 'memory_format' now, please check.")
        if args_len == 0:
            return self

        if args[0] in _dtypeDict.values():
            return self._cast_to_dtype(args[0])
        if isinstance(args[0], Tensor):
            set_dtype = args[0].dtype
            return self._cast_to_dtype(set_dtype)

        if not isinstance(args[0], (str, device_class, int)):
            raise ValueError("The inputs of Tensor.to is abnormal, please check. Currently only support "
                             "'device', 'dtype' and 'tensor'.")

        if args_len > 1 and args[1] in _dtypeDict.values():
            return self._cast_to_dtype(args[1])

        return self

    def register_parameter(self, name, param):
        """Adds a parameter to the module.

        The parameter can be accessed as an attribute using given name.

        Args:
            name (string): name of the parameter. The parameter can be accessed
                from this module using the given name
            param (Parameter or None): parameter to be added to the module. If
                ``None``, then operations that run on parameters, such as :attr:`cuda`,
                are ignored. If ``None``, the parameter is **not** included in the
                module's :attr:`state_dict`.
        """
        # Until now, input check use the check below before mindspore check in 'insert_param_to_cell'
        # because the check order in mindspore has some problem.
        if '_params' not in self.__dict__:
            raise AttributeError("cannot assign parameter before Module.__init__() call")
        elif not isinstance(name, str):
            raise TypeError("parameter name should be a string. Got {}".format(type(name)))
        elif '.' in name:
            raise KeyError("parameter name can't contain \".\"")
        elif name == '':
            raise KeyError("parameter name can't be empty string \"\"")
        elif hasattr(self, name) and name not in self._params:
            raise KeyError("attribute '{}' already exists".format(name))
        elif not isinstance(param, Parameter) and param is not None:
            raise TypeError("cannot assign '{}' object to parameter '{}' "
                            "(nn.Parameter or None required)"
                            .format(type(param), name))

        for hook in _global_parameter_registration_hooks.values():
            output = hook(self, name, param)
            if output is not None:
                param = output

        # mindspore.cell.insert_param_to_cell not allow insert None value, so use the code below.
        # self.insert_param_to_cell(name, param)
        if isinstance(param, Parameter) and param.name == "Parameter":
            param.name = name
        self._params[name] = param

    def type(self, dst_type):
        return self._apply(lambda t: t.type(dst_type))

    def cuda(self, device=None):
        unsupported_attr(device)
        return self

    def cpu(self, device=None):
        unsupported_attr(device)
        return self

    def share_memory(self):
        # share_memory mindspore do not support, do nothings
        return self

    def __dir__(self):
        module_attrs = dir(self.__class__)
        attrs = list(self.__dict__.keys())
        parameters = list(self._params.keys())
        modules = list(self._cells.keys())
        buffers = list(self._buffers.keys())
        keys = module_attrs + attrs + parameters + modules + buffers

        # Eliminate attrs that are not legal Python variable names
        keys = [key for key in keys if not key[0].isdigit()]

        return sorted(keys)

    def register_forward_hook(self, hook):
        return ms.nn.Cell.register_forward_hook(self, hook)

    def register_forward_pre__hook(self, hook):
        return ms.nn.Cell.register_forward_pre_hook(self, hook)

    # TODO:
    # to support modifying Module inside hook func
    def register_backward_hook(self, hook):
        return ms.nn.Cell.register_backward_hook(self, hook)

    def zero_grad(self, set_to_none=True):
        unsupported_attr(set_to_none)
