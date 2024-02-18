#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Parameter interface"""
import sys
import numbers
import inspect
from functools import reduce
import mindspore as ms
import mindspore._checkparam as validator
from mindspore.common import dtype as mstype
from mindspore._c_expression import Tensor as Tensor_
from mindspore.parallel._ps_context import _is_role_worker, _clone_hash_table
from mindspore.parallel._ps_context import _insert_accumu_init_info
from mindtorch.torch.tensor import Tensor, cast_to_ms_tensor, cast_to_adapter_tensor
from mindtorch.torch.common.dtype import _msdtype2typeDict

__all__ = ['Parameter', 'ParameterTuple']

def init_to_value(init):
    """
    Get value of initializer.

    Returns:
        Value of the initializer.

    Raises:
        ValueError: The value of the argument 'init' is not correct.
    """
    if isinstance(init, str):
        if init == 'zeros':
            return 0.0
        if init == 'ones':
            return 1.0
        raise ValueError("The argument 'init' should be one of values in ['zeros', 'ones'].")
    if isinstance(init, numbers.Number):
        return float(init)
    raise ValueError("The argument 'init' should be number or string, but got {}.".format(type(init)))

class Parameter(ms.Parameter):
    _base_type = {}
    def __new__(cls, data, *args, **kwargs):
        init_data_flag = bool(isinstance(data, ms.Tensor) and data.has_init)
        rc = sys.getrefcount(data)
        input_class, *class_init_args = Parameter._get_parameter_new_args(data, rc)
        new_type = Parameter._get_base_class(input_class)
        obj = input_class.__new__(new_type)
        input_class.__init__(obj, *class_init_args)
        obj.init_mode = None
        obj.is_default_input_init = init_data_flag
        if obj.has_init:
            obj.init_mode = data
        return obj

    def __reduce_ex__(self, _):
        data = self
        if self.init_mode is not None:
            data = self.init_mode
        else:
            # cast to break deep infinite loop while deepcopy
            data = ms.Tensor(self)
        return (
            Parameter, (data, self.requires_grad, self.name, self.layerwise_parallel))

    def __init__(self, data, requires_grad=True, name=None, layerwise_parallel=False, parallel_optimizer=True):
        self.adapter_flag = True
        super().__init__(default_input=data, name=name, requires_grad=requires_grad,
                         layerwise_parallel=layerwise_parallel, parallel_optimizer=parallel_optimizer)

    def __deepcopy__(self, memodict):
        new_obj = Parameter(self)
        new_obj.name = self.name
        new_obj._inited_param = self._inited_param
        return new_obj

    def __str__(self):
        if self.init_finished:
            Tensor_.data_sync(self.data, True)
        return f'Parameter containing: {Tensor_.__repr__(self.data)}, requires_grad={self.requires_grad})'

    @staticmethod
    def _get_base_class(input_class):
        input_class_name = Parameter.__name__
        if input_class_name in Parameter._base_type:
            new_type = Parameter._base_type.get(input_class_name)
        else:
            new_type = type(input_class_name, (Parameter, input_class), {})
            Parameter._base_type[input_class_name] = new_type
        return new_type

    @property
    def dtype(self):
        dtype = super(Parameter, self).dtype
        return _msdtype2typeDict.get(str(dtype), dtype)

    @property
    def data(self):
        """Return the parameter object."""
        return self

    @data.setter
    def data(self, data):
        ms_data = cast_to_ms_tensor(data)
        self.set_data(ms_data, True)

    def _update_tensor_data(self, data):
        """Update the parameter by a Tensor."""
        if isinstance(self, ms.Tensor):
            self.init_flag = False
            self.init = None
            return self.assign_value(data)
        new_param = Parameter(data, self.name, self.requires_grad)
        new_param.param_info = self.param_info
        return new_param

    @staticmethod
    def _from_tensor(tensor, *args, **kwargs):
        """Create a `Parameter` that data is shared from a `Tensor`."""
        if not isinstance(tensor, Tensor_):
            raise TypeError(f"The type of input must be Tensor, but got {type(tensor)}.")
        param = Tensor_.__new__(Parameter)
        Tensor_.__init__(param, tensor)
        param.init = None
        param.init_mode = None
        param.is_default_input_init = False
        Parameter.__init__(param, tensor, *args, **kwargs)
        return param

    def requires_grad_(self, requires_grad=True):
        self.requires_grad = requires_grad
        return self

    def detach(self):
        return cast_to_adapter_tensor(ms.Parameter.value(self))

    def numel(self):
        shape = self.shape
        return reduce((lambda x, y: x * y), shape) if shape else 1

    def nelement(self):
        return self.numel()

    def item(self):
        if self.numel() > 1:
            raise ValueError("only one element tensors can be converted to Python scalars")
        output = self.asnumpy().reshape(-1).tolist()
        return output[0]

    def stride(self, dim=None):
        bytelen = self.itemsize
        output = list(self.strides)
        for i in range(len(output)):
            output[i] = output[i]//bytelen
        output = tuple(output)
        if dim is not None:
            output = output[dim]
        return output

    def is_signed(self):
        return self.dtype in mstype.signed_type

    def is_complex(self):
        return self.dtype in mstype.complex_type

    def is_floating_point(self):
        return self.dtype in [mstype.float32, mstype.float16, mstype.float64]


def _init_parameter_api():
    param_func = dir(Parameter)
    tensor_dict = Tensor.__dict__

    for attr in tensor_dict:
        if attr not in param_func:
            func = inspect.getattr_static(Tensor, attr)
            setattr(Parameter, attr, func)

_init_parameter_api()


class ParameterTuple(tuple):
    """
    Inherited from tuple, ParameterTuple  is used to save multiple parameter.

    Note:
        It is used to store the parameters of the network into the parameter tuple collection.
    """
    def __new__(cls, iterable):
        """Create instance object of ParameterTuple."""
        data = tuple(iterable)
        ids = set()
        names = set()
        for x in data:
            if not isinstance(x, Parameter):
                raise TypeError(f"For ParameterTuple initialization, "
                                f"ParameterTuple input should be 'Parameter' collection, "
                                f"but got a {type(iterable)}. ")
            if id(x) not in ids:
                if x.name in names:
                    raise ValueError("The value {} , its name '{}' already exists. "
                                     "Please set a unique name for the parameter.".format(x, x.name))
                names.add(x.name)
                ids.add(id(x))
        return tuple.__new__(ParameterTuple, tuple(data))

    def clone(self, prefix, init='same'):
        """
        Clone the parameters in ParameterTuple element-wisely to generate a new ParameterTuple.

        Args:
            prefix (str): Namespace of parameter, the prefix string will be added to the names of parameters
                in parametertuple.

            init (Union[Tensor, str, numbers.Number]): Clone the shape and dtype of Parameters in ParameterTuple and
                set  data according to `init`. Default: 'same'.
                If `init` is a `Tensor` , set the new Parameter data to the input Tensor.
                If `init` is `numbers.Number` , set the new Parameter data to the input number.
                If `init` is a `str`, data will be seted according to the initialization method of the same name in
                the `Initializer`.
                If `init` is 'same', the new Parameter has the same value with the original Parameter.


        Returns:
            Tuple, the new Parameter tuple.
        """
        validator.check_str_by_regular(prefix)
        new = []
        for x in self:
            x1 = x.clone(init)
            x1.name = prefix + "." + x1.name
            new.append(x1)

            if not x1.cache_enable:
                continue

            if _is_role_worker():
                _clone_hash_table(x.name, x.key, x1.name, x1.key)
                _insert_accumu_init_info(x1.name, init_to_value(init))
        return ParameterTuple(new)

    def __parameter_tuple__(self):
        """For parse check."""
