import mindspore as ms
from mindtorch.torch.tensor import cast_to_ms_tensor, cast_to_adapter_tensor
from mindtorch.torch.common._inner import _out_inplace_assign

__all__ = [
    'expm1',
]

def expm1(input, *, out=None):
    input_ms = cast_to_ms_tensor(input)
    output = ms.ops.expm1(input_ms)
    return _out_inplace_assign(out, output, "expm1")
