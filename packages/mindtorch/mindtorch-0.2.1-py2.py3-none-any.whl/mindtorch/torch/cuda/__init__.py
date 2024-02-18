#!/usr/bin/env python
# -*- coding: utf-8 -*-
import re
import mindspore as ms
from mindspore.communication.management import init, get_group_size

from mindtorch.utils import get_backend
from mindtorch.torch.tensor import BoolTensor, ByteTensor, CharTensor, ShortTensor, IntTensor, HalfTensor, \
                                     FloatTensor, DoubleTensor, LongTensor, BFloat16Tensor
import mindtorch.torch.cuda.amp as amp
from mindtorch.torch.cuda.random import manual_seed_all, manual_seed
from mindtorch.torch.logging import warning
from ._utils import _get_device_index

def is_available():
    backend = get_backend()
    if backend in ('GPU', 'Ascend') :
        return True
    return False

def current_device():
    return 0

def device_count():
    # TODO Use this method when supported
    # init()
    # return get_group_size()
    return 1

def set_device(device):
    device = _get_device_index(device)
    if device >= 0:
        current_device_id = ms.get_context('device_id')
        if current_device_id != device:
            warning(f'Note that, device_id [{current_device_id}] has been in effect, and it '
                    f'can not be set repeatedly to [{device}].')
        else:
            ms.context.set_context(device_id=device)
