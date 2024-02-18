#!/usr/bin/env python
# -*- coding: utf-8 -*-

import mindspore as ms
from mindtorch.utils import unsupported_attr
from mindtorch.torch.common._inner import _out_inplace_assign
from mindtorch.torch.tensor import cast_to_ms_tensor
from mindtorch.torch._default_dtype import get_default_dtype, all_float_type

def range(start, end, step=1, *, out=None, dtype=None, layout=None, device=None, requires_grad=False):
    unsupported_attr(layout)
    unsupported_attr(device)
    unsupported_attr(requires_grad)
    if dtype is None:
        dtype = get_default_dtype()
    start = ms.Tensor(start, dtype=dtype)
    end = ms.Tensor(end+0.001, dtype=dtype)
    # TODO This function is deprecated and will be removed in a future release
    # because its behavior is inconsistent with Python’s range builtin. Instead, use torch.arange(),
    # which produces values in [start, end).
    step = ms.Tensor(step, dtype=dtype)
    output = ms.ops.range(start, end, step)
    return _out_inplace_assign(out, output, "range")


def arange(start, end=None, step=1, *, out=None, dtype=None,
        layout=None, device=None, requires_grad=False):
    unsupported_attr(layout)
    unsupported_attr(device)
    unsupported_attr(requires_grad)
    start = cast_to_ms_tensor(start)
    end = cast_to_ms_tensor(end)
    step = cast_to_ms_tensor(step)
    output =  ms.ops.arange(start=start, end=end, step=step, dtype=dtype)
    if dtype is None and output.dtype in all_float_type:
        default_dtype = get_default_dtype()
        output = output.astype(default_dtype)

    return _out_inplace_assign(out, output, "arange")
