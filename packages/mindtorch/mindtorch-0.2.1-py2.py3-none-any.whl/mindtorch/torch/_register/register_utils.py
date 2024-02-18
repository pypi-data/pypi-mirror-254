#!/usr/bin/env python
# -*- coding: utf-8 -*-
import mindspore as ms
from mindspore import dtype as mstype
from mindspore.ops.operations import _inner_ops as inner
from mindtorch.torch.tensor import Tensor as adapter_Tensor


def convert_to_ms_tensor(x):
    return inner.convert_to_ms_tensor(x)


def convert_to_adapter_tensor(x):
    return inner.convert_to_adapter_tensor(x)


def convert_output(out):
    if isinstance(out, ms.Tensor):
        out = convert_to_adapter_tensor(out)
    return out


def get_registed_fn(ops, *type_names):
    types = tuple(map(mstype.typing.str_to_type, type_names))
    for sigs, fn in ops.entries:
        if len(sigs) != len(types):
            continue
        if any(not mstype._issubclass_(type_, sig) for sig, type_ in zip(sigs, types)):
            continue
        return fn
    raise ValueError(f"For 'MultitypeFuncGraph', cannot find fn match given types: {types}.")


def _multitype_ops_tensor_calcu(ops, func1, func2):
    @ops.register("Tensor")
    def _tensor(x):
        if isinstance(x, adapter_Tensor):
            x = convert_to_ms_tensor(x)
            out = func1(x)
            out = convert_output(out)
        else:
            out = func2(x)
        return out

def update_multitype_ops_tensor_with_fn(ops, func1):
    func2 = get_registed_fn(ops, "Tensor")
    _multitype_ops_tensor_calcu(ops, func1, func2)

def update_multitype_ops_tensor(ops):
    func = get_registed_fn(ops, "Tensor")
    _multitype_ops_tensor_calcu(ops, func, func)


def _multitype_ops_tensor_tensor_calcu(ops, func1, func2):
    @ops.register("Tensor", "Tensor")
    def _tensor_and_tensor(x, y):
        if isinstance(x, adapter_Tensor) and isinstance(y, adapter_Tensor):
            x = convert_to_ms_tensor(x)
            y = convert_to_ms_tensor(y)
            out = func1(x, y)
            out = convert_output(out)
        else:
            out = func2(x, y)
        return out

def update_multitype_ops_tensor_tensor_with_fn(ops, func1):
    func2 = get_registed_fn(ops, "Tensor", "Tensor")
    _multitype_ops_tensor_tensor_calcu(ops, func1, func2)

def update_multitype_ops_tensor_tensor(ops):
    func = get_registed_fn(ops, "Tensor", "Tensor")
    _multitype_ops_tensor_tensor_calcu(ops, func, func)


def _multitype_ops_number_tensor_calcu(ops, func1, func2):
    @ops.register("Number", "Tensor")
    def _number_and_tensor(x, y):
        if isinstance(y, adapter_Tensor):
            y = convert_to_ms_tensor(y)
            out = func1(x, y)
            out = convert_output(out)
        else:
            out = func2(x, y)
        return out

def update_multitype_ops_number_tensor_with_fn(ops, func1):
    func2 = get_registed_fn(ops, "Number", "Tensor")
    _multitype_ops_number_tensor_calcu(ops, func1, func2)

def update_multitype_ops_number_tensor(ops):
    func = get_registed_fn(ops, "Number", "Tensor")
    _multitype_ops_number_tensor_calcu(ops, func, func)


def _multitype_ops_tensor_number_calcu(ops, func1, func2):
    @ops.register("Tensor", "Number")
    def _tensor_and_number(x, y):
        if isinstance(x, adapter_Tensor):
            x = convert_to_ms_tensor(x)
            out = func1(x, y)
            out = convert_output(out)
        else:
            out = func2(x, y)
        return out

def update_multitype_ops_tensor_number_with_fn(ops, func1):
    func2 = get_registed_fn(ops, "Tensor", "Number")
    _multitype_ops_tensor_number_calcu(ops, func1, func2)

def update_multitype_ops_tensor_number(ops):
    func = get_registed_fn(ops, "Tensor", "Number")
    _multitype_ops_tensor_number_calcu(ops, func, func)


def _multitype_ops_tuple_tensor_calcu(ops, func1, func2):
    @ops.register("Tuple", "Tensor")
    def _tuple_and_tensor(x, y):
        if isinstance(y, adapter_Tensor):
            y = convert_to_ms_tensor(y)
            out = func1(x, y)
            out = convert_output(out)
        else:
            out = func2(x, y)
        return out


def update_multitype_ops_tuple_tensor_with_fn(ops, func1):
    func2 = get_registed_fn(ops, "Tuple", "Tensor")
    _multitype_ops_tuple_tensor_calcu(ops, func1, func2)

def update_multitype_ops_tuple_tensor(ops):
    func = get_registed_fn(ops, "Tuple", "Tensor")
    _multitype_ops_tuple_tensor_calcu(ops, func, func)


def _multitype_ops_tensor_tuple_calcu(ops, func1, func2):
    @ops.register("Tensor", "Tuple")
    def _tensor_and_tuple(x, y):
        if isinstance(x, adapter_Tensor):
            x = convert_to_ms_tensor(x)
            out = func1(x, y)
            out = convert_output(out)
        else:
            out = func2(x, y)
        return out


def update_multitype_ops_tensor_tuple_with_fn(ops, func1):
    func2 = get_registed_fn(ops, "Tensor", "Tuple")
    _multitype_ops_tensor_tuple_calcu(ops, func1, func2)

def update_multitype_ops_tensor_tuple(ops):
    func = get_registed_fn(ops, "Tensor", "Tuple")
    _multitype_ops_tensor_tuple_calcu(ops, func, func)


def _multitype_ops_list_tensor_calcu(ops, func1, func2):
    @ops.register("List", "Tensor")
    def _list_and_tensor(x, y):
        if isinstance(y, adapter_Tensor):
            y = convert_to_ms_tensor(y)
            out = func1(x, y)
            out = convert_output(out)
        else:
            out = func2(x, y)
        return out

def update_multitype_ops_list_tensor_with_fn(ops, func1):
    func2 = get_registed_fn(ops, "List", "Tensor")
    _multitype_ops_list_tensor_calcu(ops, func1, func2)

def update_multitype_ops_list_tensor(ops):
    func = get_registed_fn(ops, "List", "Tensor")
    _multitype_ops_list_tensor_calcu(ops, func, func)


def _multitype_ops_tensor_list_calcu(ops, func1, func2):
    @ops.register("Tensor", "List")
    def _tensor_and_list(x, y):
        if isinstance(x, adapter_Tensor):
            x = convert_to_ms_tensor(x)
            out = func1(x, y)
            out = convert_output(out)
        else:
            out = func2(x, y)
        return out

def update_multitype_ops_tensor_list_with_fn(ops, func1):
    func2 = get_registed_fn(ops, "Tensor", "List")
    _multitype_ops_tensor_list_calcu(ops, func1, func2)

def update_multitype_ops_tensor_list(ops):
    func = get_registed_fn(ops, "Tensor", "List")
    _multitype_ops_tensor_list_calcu(ops, func, func)


def _multitype_ops_tensor_none_calcu(ops, func1, func2):
    @ops.register("Tensor", "None")
    def _tensor_and_none(x, y):
        if isinstance(x, adapter_Tensor):
            x = convert_to_ms_tensor(x)
            out = func1(x, y)
            out = convert_output(out)
        else:
            out = func2(x, y)
        return out

def update_multitype_ops_tensor_none_with_fn(ops, func1):
    func2 = get_registed_fn(ops, "Tensor", "None")
    _multitype_ops_tensor_none_calcu(ops, func1, func2)

def update_multitype_ops_tensor_none(ops):
    func = get_registed_fn(ops, "Tensor", "None")
    _multitype_ops_tensor_none_calcu(ops, func, func)


def _multitype_ops_tensor_slice_calcu(ops, func1, func2):
    @ops.register("Tensor", "Slice")
    def _tensor_and_slice(x, y):
        if isinstance(x, adapter_Tensor):
            x = convert_to_ms_tensor(x)
            out = func1(x, y)
            out = convert_output(out)
        else:
            out = func2(x, y)
        return out

def update_multitype_ops_tensor_slice_with_fn(ops, func1):
    func2 = get_registed_fn(ops, "Tensor", "Slice")
    _multitype_ops_tensor_slice_calcu(ops, func1, func2)

def update_multitype_ops_tensor_slice(ops):
    func = get_registed_fn(ops, "Tensor", "Slice")
    _multitype_ops_tensor_slice_calcu(ops, func, func)

def update_multitype_ops_setitem_tensor(ops):
    def register_for_setitem(sigs, fn):
        @ops.register(*sigs)
        def _tensor_setitem(data, index, value):
            if isinstance(data, adapter_Tensor):
                data = convert_to_ms_tensor(data)
                out = fn(data, index, value)
                out = convert_to_adapter_tensor(out)
            else:
                out = fn(data, index, value)
            return out

    entries = ops.entries.copy()
    for sigs, fn in entries:
        if mstype._issubclass_(sigs[0], mstype.tensor_type):
            register_for_setitem(sigs, fn)

def create_tensor(*data):
    return convert_to_adapter_tensor(ms.Tensor(*data))
