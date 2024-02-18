from mindtorch.torch.nn.modules.module import Module
from mindtorch.torch.nn.modules.linear import Identity
import mindtorch.torch.functional as torch_func
import mindtorch.torch.nn.functional as torch_nn_func

class FloatFunctional(Module):
    def __init__(self):
        super(FloatFunctional, self).__init__()
        self.activation_post_process = Identity()

    def forward(self, x):
        raise RuntimeError("FloatFunctional is not intended to use the " +
                           "'forward'. Please use the underlying operation")

    def add(self, x, y):
        r = torch_func.add(x, y)
        r = self.activation_post_process(r)
        return r

    def add_scalar(self, x, y):
        r = torch_func.add(x, y)
        # Note: this operation is not observed because the observation is not
        # needed for the quantized op.
        return r

    def mul(self, x, y):
        r = torch_func.mul(x, y)
        r = self.activation_post_process(r)
        return r

    def mul_scalar(self, x, y):
        r = torch_func.mul(x, y)
        # Note: this operation is not observed because the observation is not
        # needed for the quantized op.
        return r

    def cat(self, x, dim=0):
        r = torch_func.cat(x, dim=dim)
        r = self.activation_post_process(r)
        return r

    def add_relu(self, x, y):
        r = torch_func.add(x, y)
        r = torch_nn_func.relu(r)
        r = self.activation_post_process(r)
        return r

class FXFloatFunctional(Module):
    def forward(self, x):
        raise RuntimeError("FloatFunctional is not intended to use the " +
                           "'forward'. Please use the underlying operation")

    def add(self, x, y):
        r = torch_func.add(x, y)
        return r

    def add_scalar(self, x, y):
        r = torch_func.add(x, y)
        return r

    def mul(self, x, y):
        r = torch_func.mul(x, y)
        return r

    def mul_scalar(self, x, y):
        r = torch_func.mul(x, y)
        return r

    def cat(self, x, dim=0):
        r = torch_func.cat(x, dim=dim)
        return r

    def add_relu(self, x, y):
        r = torch_func.add(x, y)
        r = torch_nn_func.relu(r)
        return r
