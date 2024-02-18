# Functional DataPipe
from mindtorch.torch.utils.data.datapipes.map.callable import MapperMapDataPipe as Mapper
from mindtorch.torch.utils.data.datapipes.map.combinatorics import ShufflerMapDataPipe as Shuffler
from mindtorch.torch.utils.data.datapipes.map.combining import (
    ConcaterMapDataPipe as Concater,
    ZipperMapDataPipe as Zipper
)
from mindtorch.torch.utils.data.datapipes.map.grouping import (
    BatcherMapDataPipe as Batcher
)
from mindtorch.torch.utils.data.datapipes.map.utils import SequenceWrapperMapDataPipe as SequenceWrapper


__all__ = ['Batcher', 'Concater', 'Mapper', 'SequenceWrapper', 'Shuffler', 'Zipper']

# Please keep this list sorted
assert __all__ == sorted(__all__)
