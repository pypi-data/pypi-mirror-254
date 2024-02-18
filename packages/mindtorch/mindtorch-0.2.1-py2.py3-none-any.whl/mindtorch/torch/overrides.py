from mindtorch.torch.tensor import Tensor

def is_tensor_like(inp):
    return isinstance(inp, Tensor) or hasattr(type(inp), "__torch_function__")
