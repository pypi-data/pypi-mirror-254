from ..nn.modules.container import Sequential
from .._utils import warning

__all__ = [
    "checkpoint", "checkpoint_sequential",
]


def checkpoint(function, *args, use_reentrant: bool = True, **kwargs):
    #preserve = kwargs.pop('preserve_rng_state', True)
    if kwargs and use_reentrant:
        raise ValueError("Unexpected keyword arguments: " + ",".join(arg for arg in kwargs))

    warning("`checkpoint` is not currently supported, please delete it, and you can implement "
            "similar capabilities with reference to https://www.mindspore.cn/tutorials/experts"
            "/en/r2.1/parallel/recompute.html")
    return function(*args)


def checkpoint_sequential(functions, segments, input, use_reentrant=True, **kwargs):
    preserve = kwargs.pop('preserve_rng_state', True)
    if kwargs:
        raise ValueError("Unexpected keyword arguments: " + ",".join(arg for arg in kwargs))

    def run_function(start, end, functions):
        def forward(input):
            for j in range(start, end + 1):
                input = functions[j](input)
            return input
        return forward

    if isinstance(functions, Sequential):
        functions = list(functions.children())

    segment_size = len(functions) // segments
    # the last chunk has to be non-volatile
    end = -1
    for start in range(0, segment_size * (segments - 1), segment_size):
        end = start + segment_size - 1
        input = checkpoint(
            run_function(start, end, functions),
            input,
            use_reentrant=use_reentrant,
            preserve_rng_state=preserve
        )
    return run_function(end + 1, len(functions) - 1, functions)(input)
