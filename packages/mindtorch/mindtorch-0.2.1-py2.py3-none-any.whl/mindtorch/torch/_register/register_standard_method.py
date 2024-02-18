#!/usr/bin/env python
# -*- coding: utf-8 -*-
from mindspore import dtype as mstype
from mindspore._extends.parse import trope as T
from mindspore._extends.parse.resources import convert_object_map
from mindtorch.torch.tensor import Tensor as adapter_Tensor
from mindtorch.torch._register.register_utils import convert_to_ms_tensor, convert_to_adapter_tensor


matmul_fn = convert_object_map.get(T.matmul)
invert_fn = convert_object_map.get(T.invert)
abs_fn = convert_object_map.get(T.abs)
round_fn = convert_object_map.get(T.round)
max_fn = convert_object_map.get(T.max)
min_fn = convert_object_map.get(T.min)
sum_fn = convert_object_map.get(T.sum)


def adapter_matmul(x, y):
    if isinstance(x, adapter_Tensor) and isinstance(y, adapter_Tensor):
        x = convert_to_ms_tensor(x)
        y = convert_to_ms_tensor(y)
        out = matmul_fn(x, y)
        out = convert_to_adapter_tensor(out)
    else:
        out = matmul_fn(x, y)
    return out


def adapter_invert(x):
    if isinstance(x, adapter_Tensor):
        x = convert_to_ms_tensor(x)
        if x.dtype != mstype.bool_:
            out = - 1 - x
        else:
            out = invert_fn(x)
        out = convert_to_adapter_tensor(out)
    else:
        out = invert_fn(x)
    return out


def adapter_abs(x):
    if isinstance(x, adapter_Tensor):
        x = convert_to_ms_tensor(x)
        out = abs_fn(x)
        out = convert_to_adapter_tensor(out)
    else:
        out = abs_fn(x)
    return out


def adapter_round(*data):
    if (len(data) == 1 and isinstance(data[0], adapter_Tensor)) or \
      (len(data) == 2 and isinstance(data[0], adapter_Tensor) and data[1] is None):
        x = data[0]
        x = convert_to_ms_tensor(x)
        out = round_fn(x)
        out = convert_to_adapter_tensor(out)
    else:
        out = round_fn(*data)
    return out


def _has_adapter_tensor(*data):
    if len(data) == 1 and isinstance(data[0], adapter_Tensor):
        return True
    for elem in data:
        if isinstance(elem, adapter_Tensor):
            return True
    return False


def adapter_max(*data):
    if _has_adapter_tensor(*data):
        out = max_fn(*data)
        out = convert_to_adapter_tensor(out)
    else:
        out = max_fn(*data)
    return out


def adapter_min(*data):
    if _has_adapter_tensor(*data):
        out = min_fn(*data)
        out = convert_to_adapter_tensor(out)
    else:
        out = min_fn(*data)
    return out


def adapter_sum(*data):
    if _has_adapter_tensor(*data):
        out = sum_fn(*data)
        out = convert_to_adapter_tensor(out)
    else:
        out = sum_fn(*data)
    return out
