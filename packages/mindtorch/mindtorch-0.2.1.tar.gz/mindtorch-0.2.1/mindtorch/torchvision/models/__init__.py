#!/usr/bin/env python
# -*- coding: utf-8 -*-

from .alexnet import *
from .resnet import *
from .vgg import *
from .squeezenet import *
from .inception import *
from .densenet import *
from .googlenet import *  #  The batchnorm layer leads to erroneous inceptionv3 results.
from .mobilenet import *
from .mnasnet import *
from .shufflenetv2 import *
from . import segmentation
from . import detection
from . import video
from . import quantization
