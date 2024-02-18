from .distributed import DistributedDataParallel
from .data_parallel import DataParallel

__all__ = [
    'DistributedDataParallel',
    'DataParallel'
]
