import mindspore as ms
from mindtorch.utils import unsupported_attr
from mindtorch.torch.tensor import cast_to_adapter_tensor, cast_to_ms_tensor

__all__ = ['vjp', 'jvp', 'jacobian']

def vjp(func, inputs, v=None, create_graph=False, strict=False):
    if strict is True or create_graph is True:
        raise NotImplementedError("vjp not support `strict` and `create_graph` yet.")

    if not isinstance(inputs, (list, tuple)):
        inputs = (inputs,)

    if v is not None and not isinstance(v, (list, tuple)):
        v = (v,)

    # Can not cast to mindspore tensor, because ms.vjp will run forward operation of `func`
    # In func, adapter api will be call. So need to ensure inputs to be adapter Tensor.
    # inputs = cast_to_ms_tensor(inputs)
    v = cast_to_ms_tensor(v)
    func_output, fn = ms.vjp(func, *inputs)
    if v is not None:
        vjp_output = fn(*v)
    else:
        if ms.ops.size(func_output) != 1:
            raise RuntimeError("The vector v can only be None if the user-provided "
                               "function returns a single Tensor with a single element.")
        v = ms.ops.ones_like(func_output)
        vjp_output = fn(v)
    if len(vjp_output) == 1:
        vjp_output = vjp_output[0]
    return cast_to_adapter_tensor(func_output), cast_to_adapter_tensor(vjp_output)


def jvp(func, inputs, v=None, create_graph=False, strict=False):
    if strict is True or create_graph is True:
        raise NotImplementedError("jvp not support `strict` and `create_graph` yet.")

    # Can not cast to mindspore tensor, because ms.jvp will run forward operation of `func`
    # In func, adapter api will be call. So need to ensure inputs to be adapter Tensor.
    # inputs = cast_to_ms_tensor(inputs)
    v = cast_to_ms_tensor(v)

    if v is None:
        if isinstance(inputs, tuple) or inputs.nelement() != 1:
            raise RuntimeError("The vector v can only be None if the input to "
                    "the user-provided function is a single Tensor "
                    "with a single element.")
        v = ms.ops.ones_like(inputs)

    func_output, jvp_output = ms.jvp(func, inputs, v)
    return cast_to_adapter_tensor(func_output), cast_to_adapter_tensor(jvp_output)


def jacobian(func, inputs, create_graph=False, strict=False, vectorize=False, strategy="reverse-mode"):
    if strict is True or create_graph is True:
        raise NotImplementedError("jacobian not support `strict` and `create_graph` yet.")
    unsupported_attr(vectorize)
    # can not cast inputs to ms tensor, because ms.jacrev and ms.jacfwd will run forward of func.
    # inputs = cast_to_ms_tensor(inputs)

    if strategy == "reverse_mode":
        _jacobian = ms.jacrev
    else:
        _jacobian = ms.jacfwd

    if isinstance(inputs, (tuple, list)):
        _op = _jacobian(func, grad_position=tuple(range(len(inputs))))
        output = _op(*inputs)
    else:
        _op = _jacobian(func, grad_position=0)
        output = _op(inputs)

    return cast_to_adapter_tensor(output)
