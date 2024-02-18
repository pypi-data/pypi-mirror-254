#!/usr/bin/env python
# -*- coding: utf-8 -*-
from mindtorch.utils import unsupported_attr

__all__ = ['Library', 'impl', 'define']


def _return_error():
    raise RuntimeError("`torch.library` is not currently supported, please use `mindspore.ops.Custom()` to define "
                       "operators. Please refer to examples: "
                       "https://www.mindspore.cn/docs/zh-CN/r2.1/api_python/ops/mindspore.ops.Custom.html")

class Library:
    def __init__(self, ns, kind, dispatch_key=""):
        unsupported_attr(ns)
        unsupported_attr(kind)
        unsupported_attr(dispatch_key)
        _return_error()

def impl(lib, name, dispatch_key=""):
    unsupported_attr(lib)
    unsupported_attr(name)
    unsupported_attr(dispatch_key)
    _return_error()

def define(lib, schema, alias_analysis=""):
    unsupported_attr(lib)
    unsupported_attr(schema)
    unsupported_attr(alias_analysis)
    _return_error()
