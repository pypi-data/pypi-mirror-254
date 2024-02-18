#!/usr/bin/env python
# -*- coding: utf-8 -*-

from .activation import *
from .linear import *
from .flatten import *
from .conv import *
from .distance import *
from .batchnorm import *
from .instancenorm import *
from .pooling import *
from .unpooling import *
from .loss import *
from .padding import *
from .rnn import *
from .sparse import *
from .module import Module
from .container import Sequential, ModuleList, ModuleDict, ParameterList, ParameterDict
from .dropout import Dropout, Dropout1d, Dropout2d, Dropout3d, AlphaDropout, FeatureAlphaDropout
from .upsampling import *
from .normalization import *
from .pixelshuffle import *
from .channelshuffle import *
from .fold import *
from .adaptive import AdaptiveLogSoftmaxWithLoss
from .transformer import *

__all__ = [
    'Linear',
    'Bilinear',
    'Flatten',
    'Unflatten',

    'Conv1d',
    'Conv2d',
    'Conv3d',
    'ConvTranspose1d',
    'ConvTranspose2d',
    'ConvTranspose3d',
    'Fold',
    'Unfold',

    'BatchNorm1d',
    'BatchNorm2d',
    'BatchNorm3d',
    'SyncBatchNorm',
    'InstanceNorm1d',
    'InstanceNorm2d',
    'InstanceNorm3d',

    'FractionalMaxPool2d',
    'FractionalMaxPool3d',
    'AdaptiveAvgPool1d',
    'AdaptiveAvgPool2d',
    'AdaptiveAvgPool3d',
    'AdaptiveMaxPool1d',
    'AdaptiveMaxPool2d',
    'AdaptiveMaxPool3d',
    'MaxPool1d',
    'MaxPool2d',
    'MaxPool3d',
    'AvgPool1d',
    'AvgPool2d',
    'AvgPool3d',
    'LPPool1d',
    'LPPool2d',
    'Identity',
    'MaxUnpool1d',
    'MaxUnpool2d',
    'MaxUnpool3d',

    'ReLU',
    'ReLU6',
    'Hardtanh',
    'SiLU',
    'Hardswish',
    'LeakyReLU',
    'Sigmoid',
    'RReLU',
    'PReLU',
    'SELU',
    'CELU',
    'GELU',
    'Mish',
    'Softshrink',
    'Hardshrink',
    'Tanh',
    'Tanhshrink',
    'Threshold',
    'Softplus',
    'Softsign',
    'Softmax',
    'LogSoftmax',
    'Softmax2d',
    'Softmin',
    'GLU',
    'AdaptiveLogSoftmaxWithLoss',

    'MultiheadAttention',
    'Hardsigmoid',

    'Module',
    'Sequential',
    'ModuleList',
    "ParameterList",
    "ParameterDict",
    "ModuleDict",


    'Dropout',
    'Dropout1d',
    'Dropout2d',
    'Dropout3d',
    'AlphaDropout',
    'FeatureAlphaDropout',

    'Upsample',
    'SmoothL1Loss',
    'L1Loss',
    'MSELoss',
    'CrossEntropyLoss',
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
    'MultiLabelMarginLoss',
    'MultiLabelSoftMarginLoss',
    'TripletMarginWithDistanceLoss',
    'MarginRankingLoss',
    'CTCLoss',

    'LogSigmoid',
    'ELU',
    'ConstantPad1d',
    'ConstantPad2d',
    'ConstantPad3d',
    'ReflectionPad1d',
    'ReflectionPad2d',
    'ReflectionPad3d',
    'ZeroPad2d',
    'ReplicationPad1d',
    'ReplicationPad2d',
    'ReplicationPad3d',

    'RNN',
    'GRU',
    'LSTM',
    'RNNCell',
    'GRUCell',
    'LSTMCell',

    'LayerNorm',
    'GroupNorm',
    'LocalResponseNorm',

    'UpsamplingNearest2d',
    'UpsamplingBilinear2d',

    'PairwiseDistance',
    'CosineSimilarity',

    'Embedding',

    'PixelShuffle',
    'PixelUnshuffle',

    'ChannelShuffle',

    'TransformerEncoderLayer',
    'TransformerDecoderLayer',
    'TransformerEncoder',
    'TransformerDecoder',
    'Transformer'
]
