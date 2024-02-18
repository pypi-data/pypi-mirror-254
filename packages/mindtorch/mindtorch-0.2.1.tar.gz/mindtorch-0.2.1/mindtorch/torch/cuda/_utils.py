from mindtorch.torch.types import device as torch_device
from mindtorch.utils import unsupported_attr

def _get_device_index(device, optional=False, allow_cpu=False):
    unsupported_attr(optional)
    if isinstance(device, str):
        device = torch_device(device)
    if isinstance(device, torch_device):
        if allow_cpu:
            if device.type.lower() not in ['cuda', 'cpu', 'ascend']:
                raise ValueError('Expected a cuda or cpu device, but got: {}'.format(device))
        elif device.type.lower() != 'cuda' and device.type.lower() != 'ascend':
            raise ValueError('Expected a cuda or ascend device, but got: {}'.format(device))
        return device.index
    if isinstance(device, int):
        return device
    raise ValueError("The input　device of _get_device_index is abnormal, please check.")
