#!/usr/bin/env python
# -*- coding: utf-8 -*-

import mindtorch.torch.nn.functional as F
from mindtorch.torch.logging import warning
from .module import Module


__all__ = [
    'SmoothL1Loss',
    'L1Loss',
    'MSELoss',
    'CrossEntropyLoss',
    'CTCLoss',
    'NLLLoss',
    'KLDivLoss',
    'BCELoss',
    'BCEWithLogitsLoss',
    'HuberLoss',
    'SoftMarginLoss',
    'CosineEmbeddingLoss',
    'MultiMarginLoss',
    'TripletMarginLoss',
    'PoissonNLLLoss',
    'GaussianNLLLoss',
    'HingeEmbeddingLoss',
    'MarginRankingLoss',
    'MultiLabelMarginLoss',
    'MultiLabelSoftMarginLoss',
    'TripletMarginWithDistanceLoss',
]

class _Loss(Module):
    def __init__(self, size_average=None, reduce=None, reduction='mean'):
        super(_Loss, self).__init__()
        if size_average is not None or reduce is not None:
            self.reduction: str = self._get_reduce_string(size_average, reduce)
        else:
            self.reduction = reduction

    def _get_reduce_string(self, size_average, reduce):
        if size_average is None:
            size_average = True
        if reduce is None:
            reduce = True

        if size_average and reduce:
            ret = 'mean'
        elif reduce:
            ret = 'sum'
        else:
            ret = 'none'

        warning_msg = "size_average and reduce args will be deprecated, please use reduction='{}' instead."
        warning(warning_msg.format(ret))
        return ret

class _WeightedLoss(_Loss):
    def __init__(self, weight=None, size_average=None, reduce=None, reduction='mean'):
        super(_WeightedLoss, self).__init__(size_average, reduce, reduction)
        if weight is not None:
            self.register_buffer('weight', weight)
        else:
            self.weight = None


class SmoothL1Loss(_Loss):
    """Creates a criterion that uses a squared term if the absolute element-wise error falls below
    beta and an L1 term otherwise.
    """
    def __init__(self, size_average=None, reduce=None, reduction='mean', beta=1.0):
        super(SmoothL1Loss, self).__init__(size_average, reduce, reduction)
        self.beta = beta

    def forward(self, logits, lables):
        return F.smooth_l1_loss(logits, lables, reduction=self.reduction, beta=self.beta)


class L1Loss(_Loss):
    """Creates a criterion that measures the mean absolute error (MAE) between each element in
    the input and target.
    """

    def forward(self, input, target):
        return F.l1_loss(input, target, reduction=self.reduction)

class MSELoss(_Loss):
    """Creates a criterion that measures the mean squared error (squared L2 norm) between each element in
    the input and target.
    """

    def forward(self, input, target):
        return F.mse_loss(input, target, reduction=self.reduction)

class KLDivLoss(_Loss):
    """The Kullback-Leibler divergence loss."""

    def __init__(self, size_average=None, reduce=None, reduction='mean', log_target=False):
        super(KLDivLoss, self).__init__(size_average, reduce, reduction)
        self.log_target = log_target

    def forward(self, input, target):
        return F.kl_div(input, target, reduction=self.reduction, log_target=self.log_target)


class CrossEntropyLoss(_WeightedLoss):
    """
    This criterion computes the cross entropy loss between input logits and target.
    """

    def __init__(self, weight=None, size_average=None, ignore_index=-100,
                 reduce=None, reduction='mean', label_smoothing=0.0):
        super(CrossEntropyLoss, self).__init__(weight, size_average, reduce, reduction)
        self.ignore_index = ignore_index
        self.label_smoothing = label_smoothing

    def forward(self, input, target):
        return F.cross_entropy(input, target, weight=self.weight,
                               ignore_index=self.ignore_index, reduction=self.reduction,
                               label_smoothing=self.label_smoothing)


class NLLLoss(_WeightedLoss):
    """
    The negative log likelihood loss. It is useful to train a classification problem with `C` classes.
    """

    def __init__(self, weight=None, size_average=None, ignore_index=-100, reduce=None, reduction='mean'):
        super(NLLLoss, self).__init__(weight, size_average, reduce, reduction)
        self.ignore_index = ignore_index

    def forward(self, input, target):
        return F.nll_loss(input, target, weight=self.weight, ignore_index=self.ignore_index, reduction=self.reduction)


class BCELoss(_WeightedLoss):
    """Creates a criterion that measures the Binary Cross Entropy between the target and
    the input probabilities:
    """

    def forward(self, input, target):
        return F.binary_cross_entropy(input, target, weight=self.weight, reduction=self.reduction)


class BCEWithLogitsLoss(_WeightedLoss):
    """This loss combines a `Sigmoid` layer and the `BCELoss` in one single
    class. This version is more numerically stable than using a plain `Sigmoid`
    followed by a `BCELoss` as, by combining the operations into one layer,
    we take advantage of the log-sum-exp trick for numerical stability.
    """
    def __init__(self, weight=None, size_average=None, reduce=None, reduction='mean', pos_weight=None):
        super(BCEWithLogitsLoss, self).__init__(weight, size_average, reduce, reduction)
        if pos_weight is not None:
            self.register_buffer('pos_weight', pos_weight)
        else:
            self.pos_weight = None

    def forward(self, input, target):
        return F.binary_cross_entropy_with_logits(input, target, self.weight,
                                                  pos_weight=self.pos_weight,
                                                  reduction=self.reduction)


class HuberLoss(_Loss):
    def __init__(self, reduction='mean', delta=1.0):
        super().__init__(reduction=reduction)
        self.delta = delta

    def forward(self, input, target):
        return F.huber_loss(input, target, reduction=self.reduction, delta=self.delta)


class SoftMarginLoss(_Loss):

    def forward(self, input, target):
        return F.soft_margin_loss(input, target, reduction=self.reduction)


class CosineEmbeddingLoss(_Loss):
    def __init__(self, margin=0., size_average=None, reduce=None, reduction='mean'):
        super(CosineEmbeddingLoss, self).__init__(size_average, reduce, reduction)
        self.margin = margin

    def forward(self, input1, input2, target):
        return F.cosine_embedding_loss(input1, input2, target, margin=self.margin, reduction=self.reduction)


class MultiMarginLoss(_WeightedLoss):
    def __init__(self, p=1, margin=1, weight=None, size_average=None,
                 reduce=None, reduction: str='mean'):
        super(MultiMarginLoss, self).__init__(weight, size_average, reduce, reduction)
        if p not in (1, 2):
            raise ValueError("only p == 1 and p == 2 supported")
        if weight is not None and weight.dim() != 1:
            raise ValueError(f"For MultiMarginLoss, `weight` must be 1-D, but got {weight.dim()}-D.")

        self.p = p
        self.margin = margin

    def forward(self, input, target):
        return F.multi_margin_loss(input, target, p=self.p, margin=self.margin,
                                   weight=self.weight, reduction=self.reduction)

class TripletMarginLoss(_Loss):
    def __init__(self, margin=1.0, p=2., eps=1e-6, swap=False, size_average=None,
                 reduce=None, reduction: str='mean'):
        super(TripletMarginLoss, self).__init__(size_average, reduce, reduction)
        self.margin = margin
        self.p = p
        self.eps = eps
        self.swap = swap

    def forward(self, anchor, positive, negative):
        return F.triplet_margin_loss(anchor, positive, negative, margin=self.margin, p=self.p,
                                     eps=self.eps, swap=self.swap, reduction=self.reduction)


class PoissonNLLLoss(_Loss):
    def __init__(self, log_input=True, full=False, size_average=None, eps=1e-8, reduce=None, reduction='mean'):
        super(PoissonNLLLoss, self).__init__(size_average, reduce, reduction)
        self.log_input = log_input
        self.full = full
        self.eps = eps

    def forward(self, log_input, target):
        return F.poisson_nll_loss(log_input, target, log_input=self.log_input, full=self.full,
                                  eps=self.eps, reduction=self.reduction)


class GaussianNLLLoss(_Loss):
    def __init__(self, *, full=False, eps=1e-6, reduction='mean'):
        super(GaussianNLLLoss, self).__init__(None, None, reduction)
        self.full = full
        self.eps = eps

    def forward(self, input, target, var):
        return F.gaussian_nll_loss(input, target, var, full=self.full, eps=self.eps, reduction=self.reduction)


class MarginRankingLoss(_Loss):
    def __init__(self, margin=0., size_average=None, reduce=None, reduction='mean'):
        super(MarginRankingLoss, self).__init__(size_average, reduce, reduction)
        self.margin = margin

    def forward(self, input1, input2, target):
        return F.margin_ranking_loss(input1, input2, target, self.margin, reduction=self.reduction)


class HingeEmbeddingLoss(_Loss):
    def __init__(self, margin=1.0, size_average=None, reduce=None, reduction='mean'):
        super(HingeEmbeddingLoss, self).__init__(size_average, reduce, reduction)
        self.margin = margin

    def forward(self, input, target):
        return F.hinge_embedding_loss(input, target, self.margin, reduction=self.reduction)


class MultiLabelMarginLoss(_Loss):
    def forward(self, input, target):
        return F.multilabel_margin_loss(input, target, reduction=self.reduction)


class MultiLabelSoftMarginLoss(_WeightedLoss):
    def forward(self, input, target):
        return F.multilabel_soft_margin_loss(input, target, self.weight, reduction=self.reduction)


class TripletMarginWithDistanceLoss(_Loss):
    def __init__(self, *, distance_function=None,
                 margin: float = 1.0, swap: bool = False, reduction: str = 'mean'):
        super(TripletMarginWithDistanceLoss, self).__init__(size_average=None, reduce=None, reduction=reduction)
        self.distance_function = distance_function
        self.margin = margin
        self.swap = swap

    def forward(self, anchor, positive, negative):
        return F.triplet_margin_with_distance_loss(anchor, positive, negative,
                                                   distance_function=self.distance_function,
                                                   margin=self.margin, swap=self.swap, reduction=self.reduction)

class CTCLoss(_Loss):
    def __init__(self, blank=0, reduction='mean', zero_infinity=False):
        super(CTCLoss, self).__init__(reduction=reduction)
        self.blank = blank
        self.zero_infinity = zero_infinity

    def forward(self, log_probs, targets, input_lengths, target_lengths):
        return F.ctc_loss(log_probs, targets, input_lengths, target_lengths, self.blank, self.reduction,
                          self.zero_infinity)
