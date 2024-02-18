#!/usr/bin/env python
# -*- coding: utf-8 -*-

from .variable import Variable
from .function import Function
from .grad_mode import *
from . import functional

# MindSpore's autodiff mechanism is different from PyTorch' autograd， so it cannot be fully benchmarked.
# Users can directly use the autograd API of MindSpore.

__all__ = ["Variable", "Function", 'grad_mode']
