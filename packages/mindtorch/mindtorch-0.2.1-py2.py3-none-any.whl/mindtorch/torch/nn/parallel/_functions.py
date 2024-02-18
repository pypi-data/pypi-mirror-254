from mindtorch import unsupported_attr
from mindtorch.torch.autograd import Function


class Scatter(Function):
    def __init__(self):
        super().__init__()
        raise NotImplementedError("`Scatter` is not implemented now.")

def _get_stream(device: int):
    unsupported_attr(device)
    raise NotImplementedError("`_get_stream` is not implemented now.")
