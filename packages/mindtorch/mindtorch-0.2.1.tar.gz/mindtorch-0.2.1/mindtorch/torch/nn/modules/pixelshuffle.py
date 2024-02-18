from mindtorch.torch.nn.modules.module import Module
from mindtorch.torch.nn.functional import pixel_shuffle, pixel_unshuffle

__all__ = ['PixelShuffle', 'PixelUnshuffle']

class PixelShuffle(Module):
    def __init__(self, upscale_factor):
        super(PixelShuffle, self).__init__()
        self.upscale_factor = upscale_factor

    def forward(self, input):
        return pixel_shuffle(input, self.upscale_factor)

    def extra_repr(self) -> str:
        return 'upscale_factor={}'.format(self.upscale_factor)

class PixelUnshuffle(Module):
    def __init__(self, downscale_factor):
        super(PixelUnshuffle, self).__init__()
        self.downscale_factor = downscale_factor

    def forward(self, input):
        return pixel_unshuffle(input, self.downscale_factor)

    def extra_repr(self) -> str:
        return 'downscale_factor={}'.format(self.downscale_factor)
