#!/usr/bin/env python
# -*- coding: utf-8 -*-
from mindspore.common.api import set_adapter_config
from mindspore._extends.parse import trope as T
from mindspore._extends.parse.resources import convert_object_map

from mindtorch.torch.tensor import Tensor
from mindtorch.torch.nn import Parameter
from mindtorch.torch._register import register_multitype_ops
from mindtorch.torch._register import register_standard_method as S
from mindtorch.torch._register.register_utils import create_tensor

convert_object_map[T.add] = register_multitype_ops.add              # x+y
convert_object_map[T.sub] = register_multitype_ops.sub              # x-y
convert_object_map[T.mul] = register_multitype_ops.mul              # x*y
convert_object_map[T.truediv] = register_multitype_ops.div          # x/y
convert_object_map[T.getitem] = register_multitype_ops.getitem      # x[0]
convert_object_map[T.setitem] = register_multitype_ops.setitem      # x[0]=y
convert_object_map[T.floordiv] = register_multitype_ops.floordiv    # x//y
convert_object_map[T.mod] = register_multitype_ops.mod              # x%y
convert_object_map[T.pow] = register_multitype_ops.pow_             # x**y
convert_object_map[T.and_] = register_multitype_ops.bitwise_and     # x&y
convert_object_map[T.or_] = register_multitype_ops.bitwise_or       # x|y
convert_object_map[T.xor] = register_multitype_ops.bitwise_xor      # x^y
convert_object_map[T.neg] = register_multitype_ops.negative         # -x
convert_object_map[T.not_] = register_multitype_ops.logical_not     # not x
convert_object_map[T.eq] = register_multitype_ops.equal             # x==y
convert_object_map[T.ne] = register_multitype_ops.not_equal         # x!=y
convert_object_map[T.lt] = register_multitype_ops.less              # x < y
convert_object_map[T.gt] = register_multitype_ops.greater           # x > y
convert_object_map[T.le] = register_multitype_ops.less_equal        # x <= y
convert_object_map[T.ge] = register_multitype_ops.greater_equal     # x >= y
convert_object_map[T.contains] = register_multitype_ops.in_         # x in y
convert_object_map[T.not_contains] = register_multitype_ops.not_in_ # x not in y
convert_object_map[T.matmul] = S.adapter_matmul                     # x @ y
convert_object_map[T.invert] = S.adapter_invert                     # ~x
convert_object_map[T.abs] = S.adapter_abs                           # abs(x)
convert_object_map[T.round] = S.adapter_round                       # round(x)
convert_object_map[T.max] = S.adapter_max                           # max(x)
convert_object_map[T.min] = S.adapter_min                           # min(x)
convert_object_map[T.sum] = S.adapter_sum                           # sum(x)
# convert_object_map[Tensor] = create_tensor

def register_mindtorch_tensor():
    adapter_config = {"Tensor": Tensor, "Parameter": Parameter, "convert_object_map": convert_object_map}
    set_adapter_config(adapter_config)

register_mindtorch_tensor()
