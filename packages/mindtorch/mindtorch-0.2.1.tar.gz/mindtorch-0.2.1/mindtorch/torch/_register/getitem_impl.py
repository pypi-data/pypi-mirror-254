
#!/usr/bin/env python
# -*- coding: utf-8 -*-
import mindspore as ms
from mindspore import dtype as mstype
from mindspore.ops.composite.multitype_ops import _compile_utils as compile_utils


def _tensor_getitem_by_tensor(data, tensor_index):
    if tensor_index.dtype == mstype.bool_:
        ms_shape_len = len(data.shape)
        index_shape_len = len(tensor_index.shape)
        out_shape = [-1]
        while index_shape_len < ms_shape_len:
            out_shape.append(data.shape[index_shape_len])
            tensor_index = tensor_index.expand_dims(-1)
            index_shape_len += 1
        out = ms.ops.masked_select(data, tensor_index)
        if len(out_shape) > 1:
            out = out.reshape(out_shape)
    else:
        out = compile_utils.tensor_index_by_tensor(data, tensor_index)
    return out


def _tensor_getitem_by_number(data, number_index):
    if isinstance(number_index, bool):
        if number_index:
            return data.expand_dims(0)
        else:
            index = ms.Tensor(False)
            out = ms.ops.masked_select(data, index)
            return out
    return compile_utils.tensor_index_by_number(data, number_index)


def _tensor_getitem_by_tuple(data, tuple_index):
    if isinstance(tuple_index[0], bool):
        if False in tuple_index:
            index = ms.Tensor(False)
            out = ms.ops.masked_select(data, index)
            return out
        else:
            return data.expand_dims(0)
    return compile_utils.tensor_index_by_tuple(data, tuple_index)
