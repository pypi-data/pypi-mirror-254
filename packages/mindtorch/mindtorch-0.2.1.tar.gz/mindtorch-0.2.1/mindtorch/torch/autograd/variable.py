#!/usr/bin/env python
# -*- coding: utf-8 -*-
from mindtorch.utils import unsupported_attr
from mindtorch.torch.tensor import Tensor


class Variable(Tensor):
    def __init__(self, data, grad=None, requires_grad=None, volatile=None, creator=None):
        unsupported_attr(data)
        unsupported_attr(grad)
        unsupported_attr(requires_grad)
        unsupported_attr(volatile)
        unsupported_attr(creator)
        msg = "The Variable API has been deprecated, use Tensor instead."
        raise RuntimeError(msg)
