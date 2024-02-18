#!/usr/bin/env python
# -*- coding: utf-8 -*-
from mindtorch.torch.common.dtype import float16
from mindtorch.utils import unsupported_attr

class autocast():
    def __init__(self, device_type, enabled=True, dtype=float16, cache_enabled=True):
        unsupported_attr(device_type)
        unsupported_attr(enabled)
        unsupported_attr(dtype)
        unsupported_attr(cache_enabled)
        raise NotImplementedError("The use of `with autocast` is not currently supported, "
                                  "please use `mindspore.amp.auto_mixed_precision()` instead. "
                                  "Please refer to examples: "
                                  "https://openi.pcl.ac.cn/OpenI/MSAdapter/src/branch/master/USER_GUIDE.md")

    def __enter__(self):
        pass

    def __exit__(self, exc_type, exc_val, exc_tb):
        pass

    def __call__(self, func):
        pass
