#!/usr/bin/env python
# -*- coding: utf-8 -*-
import contextlib
from mindspore import _no_grad as no_grad
from mindspore.common.api import _pynative_executor
from mindtorch.utils import graph_mode_condition

class enable_grad(contextlib.ContextDecorator):
    """
    Context Manager to enable gradient calculation. When enter this context, we will enable calculate
    gradient. When exit this context, we will resume its prev state.
    Currently, it can only use in Pynative mode. It also can be used as decorator.
    """

    def __init__(self):
        if graph_mode_condition():
            raise RuntimeError("For enable_grad feature, currently only support Pynative mode, but got Graph mode.")
        self.prev = False

    def __enter__(self):
        self.prev = _pynative_executor.enable_grad()
        _pynative_executor.set_enable_grad(True)

    def __exit__(self, exc_type, exc_value, traceback):
        _pynative_executor.set_enable_grad(self.prev)
        return False

class inference_mode(contextlib.ContextDecorator):
    '''
    inference_mode is a more extreme version of no-grad mode, can speed up even more.
    In torch, the different behavious between inference mode and no-grad is that, the tensor create under
    inference mode context can not used in autograd later, and torch.is_inference() will return True on this tensor.
    Here, mindspore can not retrict tensor to be used in autograd later and will still perform tensor tracking.
    So here, inference_mode is equivalent to no-grad temporarily.
    '''

    def __init__(self, mode=True):
        if graph_mode_condition():
            raise RuntimeError("For inference_mode feature, currently only support Pynative mode, but got Graph mode.")
        self.prev = False
        self.mode = mode

    def __enter__(self):
        self.prev_state = _pynative_executor.enable_grad()
        _pynative_executor.set_enable_grad(not self.mode)

    def __exit__(self, exc_type, exc_value, traceback):
        _pynative_executor.set_enable_grad(self.prev_state)
        return False

    def clone(self):
        return self.__class__(self.mode)

class set_grad_enabled(contextlib.ContextDecorator):
    def __init__(self, mode):
        if graph_mode_condition():
            raise RuntimeError("For set_grad_enabled feature, currently only support Pynative mode, "
                               "but got Graph mode.")
        self.prev = _pynative_executor.enable_grad()
        _pynative_executor.set_enable_grad(mode)
        self.mode = mode

    def __enter__(self):
        pass

    def __exit__(self, exc_type, exc_value, traceback):
        _pynative_executor.set_enable_grad(self.prev)

    def clone(self):
        return self.__class__(self.mode)

def is_grad_enabled():
    if graph_mode_condition():
        raise RuntimeError("For is_grad_enabled feature, currently only support Pynative mode, "
                           "but got Graph mode.")
    return _pynative_executor.enable_grad()

def is_inference_mode_enabled():
    if graph_mode_condition():
        raise RuntimeError("For is_inference_mode_enabled feature, "
                           "currently only support Pynative mode, but got Graph mode.")
    return not _pynative_executor.enable_grad()

__all__ = ['no_grad', 'enable_grad', 'set_grad_enabled', 'is_grad_enabled', 'inference_mode',
           'is_inference_mode_enabled']
