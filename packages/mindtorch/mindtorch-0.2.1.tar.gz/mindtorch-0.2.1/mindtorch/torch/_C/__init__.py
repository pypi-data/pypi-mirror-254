from mindtorch.torch._C.Generator import *
from mindtorch.utils import unsupported_attr
from mindtorch.torch.logging import warning

def _jit_set_profiling_mode(profiling_flag):
    unsupported_attr(profiling_flag)
    warning("Currently, _jit_set_profiling_mode is not effectived.")
    return False

def _jit_set_profiling_executor(profiling_flag):
    unsupported_attr(profiling_flag)
    warning("Currently, _jit_set_profiling_executor is not effectived.")
    return False
