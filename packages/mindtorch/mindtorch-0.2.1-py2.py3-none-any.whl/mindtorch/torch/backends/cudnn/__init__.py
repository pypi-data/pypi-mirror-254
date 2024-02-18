import os
from mindtorch.torch.common.dtype import half, float, double
from mindtorch.utils import get_backend, unsupported_attr

_cudnn = None
__cudnn_version = None

if _cudnn is not None:
    def _init():
        global __cudnn_version
        if __cudnn_version is None:
            __cudnn_version = _cudnn.getVersionInt()
            runtime_version = _cudnn.getRuntimeVersion()
            compile_version = _cudnn.getCompileVersion()
            runtime_major, runtime_minor, _ = runtime_version
            compile_major, compile_minor, _ = compile_version
            # Different major versions are always incompatible
            # Starting with cuDNN 7, minor versions are backwards-compatible
            # Not sure about MIOpen (ROCm), so always do a strict check
            if runtime_major != compile_major:
                cudnn_compatible = False
            elif runtime_major < 7 or not _cudnn.is_cuda:
                cudnn_compatible = runtime_minor == compile_minor
            else:
                cudnn_compatible = runtime_minor >= compile_minor
            if not cudnn_compatible:
                base_error_msg = (f'cuDNN version incompatibility: '
                                  f'PyTorch was compiled  against {compile_version} '
                                  f'but found runtime version {runtime_version}. '
                                  f'PyTorch already comes bundled with cuDNN. '
                                  f'One option to resolving this error is to ensure PyTorch '
                                  f'can find the bundled cuDNN.')

                if 'LD_LIBRARY_PATH' in os.environ:
                    ld_library_path = os.environ.get('LD_LIBRARY_PATH', '')
                    if any(substring in ld_library_path for substring in ['cuda', 'cudnn']):
                        raise RuntimeError(f'{base_error_msg}'
                                           f'Looks like your LD_LIBRARY_PATH contains incompatible version of cudnn'
                                           f'Please either remove it from the path or install cudnn {compile_version}')
                    else:
                        raise RuntimeError(f'{base_error_msg}'
                                           f'one possibility is that there is a '
                                           f'conflicting cuDNN in LD_LIBRARY_PATH.')
                else:
                    raise RuntimeError(base_error_msg)

        return True
else:
    def _init():
        return False


def version():
    """Returns the version of cuDNN"""
    if not _init():
        return None
    return __cudnn_version


CUDNN_TENSOR_DTYPES = {
    half,
    float,
    double,
}


def is_available():
    r"""Returns a bool indicating if CUDNN is currently available."""
    backend = get_backend()
    if backend == 'GPU':
        return True
    return False


def is_acceptable(tensor):
    unsupported_attr(tensor)
    return False


# Add type annotation for the replaced module
enabled: bool
deterministic: bool
benchmark: bool
allow_tf32: bool
