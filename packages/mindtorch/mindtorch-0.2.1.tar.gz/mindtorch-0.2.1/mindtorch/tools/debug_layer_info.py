import os
import warnings
import numpy as np

from mindtorch.torch.logging import _setup_logger
from mindtorch.torch.tensor import cast_to_adapter_tensor
import mindspore as ms

adapter_print_header = True
torch_print_header = True

def hook_func(frame, type_info, tensor_info, name=None):
    if frame == "pytorch":
        import torch
    else:
        import mindtorch.torch as torch

    def tensor_basic_info(x, prefix):
        # all adapter tensors are converted to mindspore._c_expression.Tensor by HookBackward in this func
        input = x
        if frame == "mindtorch":
            input = x.asnumpy()
            # TODO: remove ms._c_expression.Tensor after ms bug fixed
            if not isinstance(x, (torch.Tensor, ms._c_expression.Tensor)):
                warnings.warn(f"The {prefix} is a {type(x)}, please use 'x = torch.cast_to_adapter_tensor(x)' "
                              f"convert to torch.Tensor.")
        elif frame == 'pytorch':
            input = x.cpu().detach().numpy()
        print(f"The {prefix} is a tensor with shape: {input.shape}, "
              f"and type: {input.dtype}.")
        # mindspore._c_expression.Tensor doesn't support ndim
        if len(input.shape) == 0:
            print(f"The {prefix} is {x}.")
        else:
            if input.dtype == np.bool_:
                print(f"The max value in {prefix} is {input.max():.4f}, min value is {input.min():.4f}.")
            else:
                print(f"The max value in {prefix} is {input.max():.4f}, min value is {input.min():.4f}, "
                    f"mean value is {input.mean():.4f}.")

    def hook_function(module, inputs, outputs):
        global adapter_print_header, torch_print_header
        if adapter_print_header and frame == 'mindtorch':
            print(f"\n>>> layer input and output info from mindtorch :")
            adapter_print_header = False
        elif torch_print_header and frame == 'pytorch':
            print(f"\n>>> layer input and output info from pytorch :")
            torch_print_header = False

        print("------------------------------", '[forward]:' + name, "------------------------------")

        for i, input in enumerate(inputs):
            if type_info:
                print(f"The inputs[{i}] is a {type(input)}.")
            if tensor_info and isinstance(input, torch.Tensor):
                tensor_basic_info(input, f"inputs[{i}]")

        def bwd_hook_func(prefix):
            def bwd_output_hook(grad):
                if prefix == "outputs[0]":
                    print("------------------------------", '[backward]:' + name, "------------------------------")
                if isinstance(grad, (list, tuple)):
                    grad = grad[0]
                tensor_basic_info(grad, prefix)
            return bwd_output_hook

        def output_tensor_reg_hook(outputs, index):
            if isinstance(outputs, (tuple, list)):
                res = []
                for i, output in enumerate(outputs):
                    output_hooked_tensors = output_tensor_reg_hook(output, i)
                    res.append(output_hooked_tensors)
                return res
            elif isinstance(outputs, torch.Tensor):
                output = outputs
                if type_info:
                    print(f"The outputs[{index}] is a {type(output)}.")
                if tensor_info:
                    tensor_basic_info(output, f"outputs[{index}]")
                    if frame == 'pytorch':
                        if output.requires_grad:
                            output.register_hook(bwd_hook_func(f"outputs[{index}]"))
                    else:
                        hook = ms.ops.HookBackward(bwd_hook_func(f"outputs[{index}]"))
                        output = cast_to_adapter_tensor(hook(output))
                        return output

        return output_tensor_reg_hook(outputs, 0)

    return hook_function

def params_basic_info(parameter, name):
    print(f"'{name}' with shape: {parameter.cpu().detach().numpy().shape}, "
          f"and type: {parameter.cpu().detach().numpy().dtype}.")
    if parameter.ndim == 0:
        print(f"{name} is {parameter}.")
    else:
        print(f"The max value in '{name}' is {parameter.max():.4f}, min value is {parameter.min():.4f}, "
              f"mean value is {parameter.float().mean():.4f}.")

def debug_layer_info(model, frame="mindtorch", type_info=False, tensor_info=True, params_info=True):
    if frame == "pytorch":
        import torch
    else:
        import mindtorch.torch as torch
        os.environ['MSA_LOG'] = '2'
        _setup_logger()

    if not isinstance(model, torch.nn.Module):
        raise ValueError(f"For debug_layer_info, `model` must be a nn.Module, but get a {type(model)} type.")

    print(f"\n>>> parameter and buffer info from {frame} :")

    if params_info:
        for name, parameter in model.named_parameters():
            params_basic_info(parameter, name)
        for name, buf in model.named_buffers():
            params_basic_info(buf, name)

    # TODO: wrap non-nn APIs
    # from mindtorch.tools.wrap_tensor import initialize_hook
    # hook_func_partial = functools.partial(hook_func, frame, type_info, tensor_info)
    # initialize_hook(hook_func_partial)

    for name, module in model.named_modules():
        if module is not None:
            module.register_forward_hook(hook_func(frame, type_info, tensor_info, name))