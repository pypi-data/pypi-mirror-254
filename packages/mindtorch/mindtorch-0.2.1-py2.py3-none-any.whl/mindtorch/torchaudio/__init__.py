from mindtorch.torchaudio import (  # noqa: F401
#     _extension,
#     compliance,
    datasets,
    functional,
#     io,
#     kaldi_io,
#     models,
#     pipelines,
#     sox_effects,
    transforms,
#     utils,
)
from mindtorch.torchaudio.backend import get_audio_backend, list_audio_backends, set_audio_backend, utils
utils._init_audio_backend()

__version__ = version = "0.12.1"

__all__ = [
    # "io",
    # "compliance",
    "datasets",
    "functional",
    # "models",
    # "pipelines",
    # "kaldi_io",
    # "utils",
    # "sox_effects",
    "transforms",
    "list_audio_backends",
    "get_audio_backend",
    "set_audio_backend",
]
