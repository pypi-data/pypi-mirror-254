#!/usr/bin/env python
# -*- coding: utf-8 -*-
from mindtorch.utils import unsupported_attr
from mindtorch.torch.nn import Module


class Function(Module):
    """Base class to create custom `autograd.Function`

    Examples::

        >>> class Exp(Function):
        >>>     def __init__(self):
        >>>         super(Exp, self).__init__()
        >>>
        >>>     def forward(self, i):
        >>>         result = i.exp()
        >>>         return result
        >>>
        >>>     def bprop(self, i, out, grad_output):
        >>>         return grad_output * out
        >>>
        >>> # Use non-static forward method:
        >>> output = Exp()(input)
    """
    def __init__(self, *args, **kwargs):
        unsupported_attr(args)
        unsupported_attr(kwargs)
        super(Function, self).__init__()

    def apply(self, *args, **kwargs):
        """
        # Don not use it by calling the apply method.
        """
        unsupported_attr(args)
        unsupported_attr(kwargs)
        raise RuntimeError("To create a custom autograd.Function, please use 'def forward(self, ...)' and "
                           "'def bprop(self, ..., out, dout)' instead of 'forward()' and 'backward()' static methods. "
                           "Then, use it as normal module class, do not call the class method 'apply'."
                           "Please refer to the following example: https://openi.pcl.ac.cn/OpenI/MSAdapter/src/"
                           "branch/master/doc/torch/USER_GUIDE.md#user-content-4-2-1-%E8%87%AA%E5%AE%9A%E4%B9%89module")
