#!/usr/bin/env python
# -*- coding: utf-8 -*-
from mindtorch.utils import unsupported_attr

class TensorType:
    def __init__(self, dim):
        unsupported_attr(dim)
        raise NotImplementedError("`TensorType` is not implemented now.")
