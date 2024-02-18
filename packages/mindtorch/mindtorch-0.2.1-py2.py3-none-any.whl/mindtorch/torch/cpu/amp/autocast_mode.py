#!/usr/bin/env python
# -*- coding: utf-8 -*-
from mindtorch.torch.common.dtype import float16
from mindtorch.torch.amp.autocast_mode import autocast as base_autocast


class autocast(base_autocast):
    def __init__(self, enabled=True, dtype=float16, cache_enabled=True):
        super().__init__("cpu", enabled=enabled, dtype=dtype, cache_enabled=cache_enabled)
