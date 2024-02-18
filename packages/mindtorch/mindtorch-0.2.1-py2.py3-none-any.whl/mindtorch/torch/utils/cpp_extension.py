from mindtorch.utils import unsupported_attr


class BuildExtension():
    def __init__(self):
        raise NotImplementedError("`BuildExtension` is not implemented now.")


def CppExtension(name, sources, *args, **kwargs):
    unsupported_attr(name)
    unsupported_attr(sources)
    unsupported_attr(args)
    unsupported_attr(kwargs)
    raise NotImplementedError("`CppExtension` is not implemented now.")


def CUDAExtension(name, sources, *args, **kwargs):
    unsupported_attr(name)
    unsupported_attr(sources)
    unsupported_attr(args)
    unsupported_attr(kwargs)
    raise NotImplementedError("`CUDAExtension` is not implemented now.")
