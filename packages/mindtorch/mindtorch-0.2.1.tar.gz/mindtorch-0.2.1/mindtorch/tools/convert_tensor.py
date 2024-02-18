#!/usr/bin/env python
# -*- coding: utf-8 -*-
import re
from collections.abc import Mapping, Sequence
from mindtorch.tools.utils import try_import
import mindspore as ms
from mindspore.common import dtype as mstype
from mindtorch.torch.tensor import Tensor

string_classes = (str, bytes)
np_str_obj_array_pattern = re.compile(r'[SaUO]')

def convert_to_ms_tensor(data):

    torch = try_import("torch")

    _dtypeConvertor = {
        torch.float16: mstype.float16,
        torch.float32: mstype.float32,
        torch.float64: mstype.float64,
        torch.int8: mstype.int8,
        torch.int16: mstype.int16,
        torch.int32: mstype.int32,
        torch.int64: mstype.int64,
        torch.uint8: mstype.uint8,
        torch.bool: mstype.bool_,
        torch.complex64: mstype.complex64,
        torch.complex128: mstype.complex128,
        torch.long: mstype.int64,
        torch.bfloat16: mstype.bfloat16,
        mstype.float16: mstype.float16,
        mstype.float32: mstype.float32,
        mstype.float64: mstype.float64,
        mstype.int8: mstype.int8,
        mstype.int16: mstype.int16,
        mstype.int32: mstype.int32,
        mstype.int64: mstype.int64,
        mstype.uint8: mstype.uint8,
        mstype.complex64: mstype.complex64,
        mstype.complex128: mstype.complex128,
        mstype.bfloat16: mstype.float16,
    }

    elem_type = type(data)
    if isinstance(data, torch.Tensor):
        origin_dtype = data.dtype
        origin_dtype = _dtypeConvertor[origin_dtype]
        data = data.numpy()
        return Tensor(data, dtype=origin_dtype)
    elif elem_type.__module__ == 'numpy' and elem_type.__name__ != 'str_' \
            and elem_type.__name__ != 'string_':
            if elem_type.__name__ == 'ndarray' \
                and np_str_obj_array_pattern.search(data.dtype.str) is not None:
                return data
            return Tensor(data)
    elif isinstance(data, float):
        return Tensor(data, dtype=ms.float32)
    elif isinstance(data, int):
        return Tensor(data, dtype=ms.int64)
    elif isinstance(data, Mapping):
        try:
            return elem_type({key: convert_to_ms_tensor(data[key]) for key in data})
        except TypeError:
            return {key: convert_to_ms_tensor(data[key]) for key in data}
    elif isinstance(data, tuple) and hasattr(data, '_fields'):
        return elem_type(*(convert_to_ms_tensor(d) for d in data))
    elif isinstance(data, (tuple, list)):
        return [convert_to_ms_tensor(d) for d in data]
    elif isinstance(data, Sequence) and not isinstance(data, string_classes):
        try:
            return elem_type([convert_to_ms_tensor(d) for d in data])
        except TypeError:
            return [convert_to_ms_tensor(d) for d in data]
    elif isinstance(data, string_classes):
        return data
    elif isinstance(data, ms.Tensor):
        return data
    else:
        raise TypeError("data must be tensor, numpy arrays, numbers, dicts or lists; but got {}".format(elem_type))