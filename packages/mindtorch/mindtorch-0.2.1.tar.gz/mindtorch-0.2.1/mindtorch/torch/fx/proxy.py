#!/usr/bin/env python
# -*- coding: utf-8 -*-
from mindtorch.torch.logging import warning

__all__ = ['Proxy']


class Proxy:
    """
    ``Proxy`` objects are ``Node`` wrappers that flow through the
    program during symbolic tracing and record all the operations
    (``torch`` function calls, method calls, operators) that they touch
    into the growing FX Graph.
    """
    def __init__(self, node, tracer=None):
        warning("`fx.Proxy` is an empty class.")
        self.tracer = tracer
        self.node = node
