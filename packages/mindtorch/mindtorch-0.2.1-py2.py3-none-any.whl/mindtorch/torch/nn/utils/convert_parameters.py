# #!/usr/bin/env python
# # -*- coding: utf-8 -*-
import mindspore as ms
from mindtorch.torch._ref import typename
from mindtorch.torch.tensor import Tensor, cast_to_adapter_tensor, cast_to_ms_tensor

def parameters_to_vector(parameters):
    # Flag for the device where the parameter is located
    # param_device = None

    vec = []
    for param in parameters:
        # Ensure the parameters are located in the same device
        #TODO: unspport check device
        # param_device = _check_param_device(param, param_device)

        vec.append(param.view(-1))

    vec = cast_to_ms_tensor(vec)
    output = ms.ops.cat(vec)
    return cast_to_adapter_tensor(output)


def vector_to_parameters(vec, parameters):
    # Ensure vec of type Tensor
    if not isinstance(vec, Tensor):
        raise TypeError('expected torch.Tensor, but got: {}'.format(typename(vec)))
    # Flag for the device where the parameter is located
    # param_device = None

    # Pointer for slicing the vector for each parameter
    pointer = 0
    for param in parameters:
        # Ensure the parameters are located in the same device
        #TODO: unspport check device
        # param_device = _check_param_device(param, param_device)

        # The length of the parameter
        num_param = param.numel()
        # Slice the vector, reshape it, and replace the old data of the parameter
        param.data = vec[pointer:pointer + num_param].view_as(param).data

        # Increment the pointer
        pointer += num_param


def _check_param_device(param, old_param_device):
    # Meet the first parameter
    if old_param_device is None:
        old_param_device = param.get_device() if param.is_cuda else -1
    else:
        warn = False
        if param.is_cuda:  # Check if in same GPU
            warn = (param.get_device() != old_param_device)
        else:  # Check if in CPU
            warn = (old_param_device != -1)
        if warn:
            raise TypeError('Found two parameters on different devices, this is currently not supported.')
    return old_param_device
