from mindtorch.utils import unsupported_attr
from mindtorch.torch.logging import warning

def manual_seed(seed):
    unsupported_attr(seed)
    warning("Currently, torch.cuda.manual_seed is not effectived. If you want to limit randomness, "
            "please call the torch.manual_seed interface for unified configuration.")

def manual_seed_all(seed):
    unsupported_attr(seed)
    warning("Currently, torch.cuda.manual_seed_all is not effectived.")
