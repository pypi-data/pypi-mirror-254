from mindtorch.utils import unsupported_attr
from mindtorch.torch.nn.modules.module import Module


class DataParallel(Module):
    def __init__(self, module, device_ids=None, output_device=None, dim=0):
        super().__init__()
        unsupported_attr(module)
        unsupported_attr(device_ids)
        unsupported_attr(output_device)
        unsupported_attr(dim)
        raise NotImplementedError("`DataParallel` is not implemented now.")
