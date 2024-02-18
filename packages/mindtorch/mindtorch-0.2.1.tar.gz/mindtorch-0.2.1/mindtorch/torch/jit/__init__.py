#!/usr/bin/env python
# -*- coding: utf-8 -*-
import mindspore as ms
from mindtorch.utils import unsupported_attr
from mindtorch.torch.logging import warning
from mindtorch.torch.jit._jit_internal import Final, unused

def is_tracing():
    return False

def is_scripting():
    return False

def script(obj, optimize=None, _frames_up=0, _rcb=None, example_inputs=None):
    unsupported_attr(optimize)
    unsupported_attr(_frames_up)
    unsupported_attr(_rcb)
    unsupported_attr(example_inputs)
    warning("`jit.script`'s function is not complete, it is equivalent to 'mindspore.jit', please refer: "
            "https://www.mindspore.cn/docs/zh-CN/r2.1/api_python/mindspore/mindspore.jit.html#mindspore.jit")
    return ms.jit(obj)


def ignore(drop=False, **kwargs):
    warning("`jit.ignore` is an empty function that has no ignored function now.")
    unsupported_attr(kwargs)

    if callable(drop):
        return drop

    def decorator(fn):
        return fn

    return decorator

def _overload_method(func):
    unsupported_attr(func)
    warning("`jit._overload_method` is an empty function that has not implemented now.")

def interface(obj):
    unsupported_attr(obj)
    warning("`jit.interface` is an empty function that has not implemented now.")
