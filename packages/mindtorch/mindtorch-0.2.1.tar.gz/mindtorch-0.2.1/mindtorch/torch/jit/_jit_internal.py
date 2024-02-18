import sys
from mindtorch.torch.logging import warning

if sys.version_info[:2] > (3, 7):
    from typing import Final # pylint: disable=W0611
else:
    from typing_extensions import Final # pylint: disable=W0611

def unused(fn):
    warning("Currently, torch.jit.unused is not effectived.")
    return fn
