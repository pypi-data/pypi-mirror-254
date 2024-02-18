#!/usr/bin/env python
# -*- coding: utf-8 -*-


import mindspore as ms
from mindtorch.torch.common._inner import _out_inplace_assign
import mindtorch.torch._register_numpy_primitive  as numpy_cell

def fft(input, n=None, dim=-1, norm=None, out=None):
    # TODO: To use ms.ops.fft after it support
    fft_op = numpy_cell.NumpyFft('fft')
    output = fft_op(input, n, dim, norm)
    return _out_inplace_assign(out, output, "fft")


def rfft(input, n=None, dim=-1, norm=None, *, out=None):
    # TODO: To use ms.ops.rfft after it support
    rfft_op = numpy_cell.NumpyRfft('rfft')
    output = rfft_op(input, n, dim, norm)
    return _out_inplace_assign(out, ms.Tensor(output), "rfft")
