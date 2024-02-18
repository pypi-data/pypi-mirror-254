
#!/usr/bin/env python
# -*- coding: utf-8 -*-
from mindtorch.torch.common.dtype import float16
from mindtorch.torch.amp.autocast_mode import autocast as base_autocast
from mindtorch.utils import unsupported_attr

class autocast(base_autocast):
    def __init__(self, enabled=True, dtype=float16, cache_enabled=True):
        super().__init__("cuda", enabled=enabled, dtype=dtype, cache_enabled=cache_enabled)


def custom_fwd(fwd=None, *, cast_inputs=None):
    unsupported_attr(fwd)
    unsupported_attr(cast_inputs)
    raise NotImplementedError("The use of `@custom_fwd` is not currently supported, please use "
                              "`mindspore.amp.auto_mixed_precision()` or `tensor.astype(ms.float16)' instead."
                              "Please refer to examples: https://openi.pcl.ac.cn/OpenI/MSAdapter/src/branch/"
                              "master/doc/torch/USER_GUIDE.md")

def custom_bwd(bwd):
    unsupported_attr(bwd)
    raise NotImplementedError("The use of `@custom_bwd` is not currently supported, please use "
                              "`mindspore.amp.auto_mixed_precision()` or `tensor.astype(ms.float16)' instead."
                              "Please refer to examples: https://openi.pcl.ac.cn/OpenI/MSAdapter/src/branch/"
                              "master/doc/torch/USER_GUIDE.md")
