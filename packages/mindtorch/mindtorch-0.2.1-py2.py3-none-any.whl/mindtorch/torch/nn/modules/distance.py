#!/usr/bin/env python
# -*- coding: utf-8 -*-

import mindtorch.torch.nn.functional as ms_torch_nn_func
from .module import Module

__all__ = ['PairwiseDistance', 'CosineSimilarity']

class PairwiseDistance(Module):
    def __init__(self, p=2.0, eps=1e-6, keepdim=False):
        super(PairwiseDistance, self).__init__()
        self.norm = p
        self.eps = eps
        self.keepdim = keepdim

    def forward(self, x1, x2):
        return ms_torch_nn_func.pairwise_distance(x1, x2, self.norm, self.eps, self.keepdim)


class CosineSimilarity(Module):
    def __init__(self, dim=1, eps=1e-8):
        super(CosineSimilarity, self).__init__()
        self.dim = dim
        self.eps = eps

    def forward(self, x1, x2):
        return ms_torch_nn_func.cosine_similarity(x1, x2, self.dim, self.eps)
