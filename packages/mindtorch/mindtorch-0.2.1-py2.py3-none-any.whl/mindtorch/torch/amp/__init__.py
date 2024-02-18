#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys
import mindspore as ms
import mindtorch.torch.nn as nn
from mindtorch.torch.nn import Module, Sequential
from mindtorch.torch.tensor import cast_to_adapter_tensor
from mindtorch.torch.amp.autocast_mode import autocast

all = [
    'autocast',
    'auto_mixed_precision'
]


class _CastToAdapter(Module):
    """Wrap amp net for mindtorch, cast network from ms.nn.Cell to nn.Module."""
    def __init__(self, net):
        super(_CastToAdapter, self).__init__()
        self._ms_amp_net = net

    def forward(self, *inputs):
        output = self._ms_amp_net(*inputs)
        return cast_to_adapter_tensor(output)


def auto_mixed_precision(network, amp_level="auto"):
    """
    This API wraps ms.amp.auto_mixed_precision() for cast adapter type.
    https://www.mindspore.cn/tutorials/zh-CN/r2.0/advanced/mixed_precision.html
    """
    # This is an internal interface, only for debugging.
    # After calling this API, use amp_net.trainable_params() to replace amp_net.parameters().
    if amp_level == "auto":
        device_target = ms.get_context('device_target')
        if device_target == "GPU":
            amp_level = "O2"
        elif device_target == "Ascend":
            amp_level = "O3"
        else:
            raise ValueError("Level `auto` only support when `device_target` is GPU or Ascend.")

    amp_net = ms.amp.auto_mixed_precision(network, amp_level)
    return _CastToAdapter(amp_net)


# for mindspore auto mixed precision
ms.rewrite.symbol_tree_builder.SymbolTreeBuilder.entry_function = "forward"
ms.rewrite.parsers.class_def_parser.ClassDefParser.entry_function = "forward"
ms.rewrite.parsers.assign_parser.AssignParser.types_for_cell_container.append(Sequential)

class ToDtype(Module):
    def __init__(self):
        super(ToDtype, self).__init__()

    def forward(self, x, dtype):
        return x.to(dtype)

nn_modules_list = [ToDtype]
nn_modules = sys.modules['mindtorch.torch.nn']
nn_modules_dir = dir(nn_modules)
for module_name in nn_modules_dir:
    module_obj = getattr(nn_modules, module_name)
    if isinstance(module_obj, type) and issubclass(module_obj, Module):
        nn_modules_list.append(module_obj)

ms.rewrite.namespace._subtree_black_list.extend(nn_modules_list)
ms.train.amp._config_amp(enable_rewrite=True, cast_op=ToDtype)

ms.train.amp.AMP_WHITE_LIST.extend([nn.Conv1d,
                                    nn.Conv2d,
                                    nn.Conv3d,
                                    nn.Linear,
                                    nn.LSTMCell,
                                    nn.RNNCell,
                                    nn.GRUCell])

ms.train.amp.AMP_BLACK_LIST.extend([nn.BatchNorm1d,
                                    nn.BatchNorm2d,
                                    nn.BatchNorm3d,
                                    nn.LayerNorm])
