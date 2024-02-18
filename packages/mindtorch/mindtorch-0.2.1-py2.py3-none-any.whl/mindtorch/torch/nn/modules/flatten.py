#!/usr/bin/env python
# -*- coding: utf-8 -*-
import mindtorch.torch.functional as adapter_F
from .module import Module

__all__ = ['Flatten', 'Unflatten']

class Flatten(Module):
    def __init__(self, start_dim=1, end_dim=-1):
        super(Flatten, self).__init__()
        self.start_dim = start_dim
        self.end_dim = end_dim

    def forward(self, input):
        return adapter_F.flatten(input, self.start_dim, self.end_dim)

    def extra_repr(self) -> str:
        return 'start_dim={}, end_dim={}'.format(
            self.start_dim, self.end_dim
        )


class Unflatten(Module):
    def __init__(self, dim, unflattened_size):
        super(Unflatten, self).__init__()

        if isinstance(dim, str):
            raise TypeError("Until Now, `dim` not support type of str in `Unflatten`")

        self.dim = dim
        self.unflattened_size = unflattened_size

    def forward(self, input):
        return adapter_F.unflatten(input, self.dim, self.unflattened_size)

    def extra_repr(self) -> str:
        return 'dim={}, unflattened_size={}'.format(self.dim, self.unflattened_size)
