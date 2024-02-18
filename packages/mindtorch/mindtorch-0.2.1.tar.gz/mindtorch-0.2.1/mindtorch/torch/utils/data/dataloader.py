r"""Definition of the DataLoader and associated iterators that subclass _BaseDataLoaderIter

To support these two classes, in `./_utils` we define many utility methods and
functions to be run in multiprocessing. E.g., the data loading worker loop is
in `./_utils/worker.py`.
"""
from __future__ import absolute_import

import functools
import itertools
import logging
import os
import queue
import math
import multiprocessing as multiprocessing
from typing import Any, Callable, Iterable, TypeVar, Generic, Sequence, List, Optional, Union
import numpy as np
import mindtorch.torch as torch
# import mindtorch.torch.utils.data.graph_settings

from mindtorch.torch._utils import ExceptionWrapper
from mindtorch.torch._six import string_classes
# from mindspore import communication as dist
from mindtorch.torch.logging import warning

from . import (
    # IterDataPipe,
    # MapDataPipe,
    IterableDataset,
    Sampler,
    SequentialSampler,
    RandomSampler,
    BatchSampler,
    Dataset,
    )

# from mindtorch.torch.utils.data.datapipes.datapipe import _IterDataPipeSerializationWrapper, _MapDataPipeSerializationWrapper

from . import _utils

__all__ = [
    "DataLoader",
    "get_worker_info",
    "default_collate",
    "default_convert",
]

_MP_MODE_ENV = os.environ.get('ENABLE_FORK_UTILS')

if _MP_MODE_ENV == "1":
    os.environ['MS_ENABLE_FORK_UTILS'] = '1'
else:
    multiprocessing.set_start_method('spawn', force=True)


T_co = TypeVar('T_co', covariant=True)
T = TypeVar('T')
_worker_init_fn_t = Callable[[int], None]

# Ideally we would parameterize `DataLoader` by the return type of `collate_fn`, but there is currently no way to have that
# type parameter set to a default value if the user doesn't pass in a custom 'collate_fn'.
# See https://github.com/python/mypy/issues/3737.
_collate_fn_t = Callable[[List[T]], Any]


default_collate: _collate_fn_t = _utils.collate.default_collate
default_convert = _utils.collate.default_convert
default_convert_numpy = _utils.collate.default_convert_numpy
_SharedQueue = _utils.queue._SharedQueue
get_worker_info = _utils.worker.get_worker_info
collate_nbytes = _utils.collate.collate_nbytes
logger = logging.getLogger(__name__)

def MIN_POWER_TWO(cap):
    n = cap - 1
    n |= n >> 1
    n |= n >> 2
    n |= n >> 4
    n |= n >> 8
    n |= n >> 16
    return n + 1

class _DatasetKind(object):
    Map = 0
    Iterable = 1

    @staticmethod
    def create_fetcher(kind, dataset, auto_collation, collate_fn, drop_last):
        if kind == _DatasetKind.Map:
            return _utils.fetch._MapDatasetFetcher(dataset, auto_collation, collate_fn, drop_last)
        else:
            return _utils.fetch._IterableDatasetFetcher(dataset, auto_collation, collate_fn, drop_last)


class _InfiniteConstantSampler(Sampler):
    r"""Analogous to ``itertools.repeat(None, None)``.

    Args:
        data_source (Dataset): dataset to sample from
    """

    def __init__(self):
        super(_InfiniteConstantSampler, self).__init__(None)

    def __iter__(self):
        while True:
            yield None


# def _get_distributed_settings():
#     if dist.is_available and dist.is_initialized():
#         return dist.get_world_size(), dist.get_rank() #TODO
#     else:
#         return 1, 0


# def _sharding_worker_init_fn(worker_init_fn, world_size, rank_id, worker_id):
#     global_worker_id = worker_id
#     info = torch.utils.data.get_worker_info()
#     total_workers = info.num_workers
#     datapipe = info.dataset
#     # To distribute elements across distributed process evenly, we should shard data on distributed
#     # processes first then shard on worker processes
#     total_workers *= world_size
#     global_worker_id = global_worker_id * world_size + rank_id
#     mindtorch.torch.utils.data.graph_settings.apply_sharding(datapipe, total_workers, global_worker_id)
#     if worker_init_fn is not None:
#         worker_init_fn(worker_id)


class DataLoader(Generic[T_co]):
    r"""
    Data loader. Combines a dataset and a sampler, and provides an iterable over
    the given dataset.


    Args:
        dataset (Dataset): dataset from which to load the data.
        batch_size (int, optional): how many samples per batch to load
            (default: ``1``).
        shuffle (bool, optional): set to ``True`` to have the data reshuffled
            at every epoch (default: ``False``).
        sampler (Sampler or Iterable, optional): defines the strategy to draw
            samples from the dataset. Can be any ``Iterable`` with ``__len__``
            implemented. If specified, :attr:`shuffle` must not be specified.
        batch_sampler (Sampler or Iterable, optional): like :attr:`sampler`, but
            returns a batch of indices at a time. Mutually exclusive with
            :attr:`batch_size`, :attr:`shuffle`, :attr:`sampler`,
            and :attr:`drop_last`.
        num_workers (int, optional): how many subprocesses to use for data
            loading. ``0`` means that the data will be loaded in the main process.
            (default: ``0``)
        collate_fn (callable, optional): merges a list of samples to form a
            mini-batch of Tensor(s).  Used when using batched loading from a
            map-style dataset.
        pin_memory (bool, optional): If ``True``, the data loader will copy Tensors
            into device/CUDA pinned memory before returning them.  If your data elements
            are a custom type, or your :attr:`collate_fn` returns a batch that is a custom type,
            see the example below.
        drop_last (bool, optional): set to ``True`` to drop the last incomplete batch,
            if the dataset size is not divisible by the batch size. If ``False`` and
            the size of dataset is not divisible by the batch size, then the last batch
            will be smaller. (default: ``False``)
        timeout (numeric, optional): if positive, the timeout value for collecting a batch
            from workers. Should always be non-negative. (default: ``0``)
        worker_init_fn (callable, optional): If not ``None``, this will be called on each
            worker subprocess with the worker id (an int in ``[0, num_workers - 1]``) as
            input, after seeding and before data loading. (default: ``None``)
        generator (torch.Generator, optional): If not ``None``, this RNG will be used
            by RandomSampler to generate random indexes and multiprocessing to generate
            `base_seed` for workers. (default: ``None``)
        prefetch_factor (int, optional, keyword-only arg): Number of batches loaded
            in advance by each worker. ``2`` means there will be a total of
            2 * num_workers batches prefetched across all workers. (default: ``2``)
        persistent_workers (bool, optional): If ``True``, the data loader will not shutdown
            the worker processes after a dataset has been consumed once. This allows to
            maintain the workers `Dataset` instances alive. (default: ``False``)
        pin_memory_device (str, optional): the data loader will copy Tensors
            into device pinned memory before returning them if pin_memory is set to true.


    .. warning:: If the ``spawn`` start method is used, :attr:`worker_init_fn`
                 cannot be an unpicklable object, e.g., a lambda function. See
                 :ref:`multiprocessing-best-practices` on more details related
                 to multiprocessing in PyTorch.

    .. warning:: ``len(dataloader)`` heuristic is based on the length of the sampler used.
                 When :attr:`dataset` is an :class:`~torch.utils.data.IterableDataset`,
                 it instead returns an estimate based on ``len(dataset) / batch_size``, with proper
                 rounding depending on :attr:`drop_last`, regardless of multi-process loading
                 configurations. This represents the best guess PyTorch can make because PyTorch
                 trusts user :attr:`dataset` code in correctly handling multi-process
                 loading to avoid duplicate data.

                 However, if sharding results in multiple workers having incomplete last batches,
                 this estimate can still be inaccurate, because (1) an otherwise complete batch can
                 be broken into multiple ones and (2) more than one batch worth of samples can be
                 dropped when :attr:`drop_last` is set. Unfortunately, PyTorch can not detect such
                 cases in general.

                 See `Dataset Types`_ for more details on these two types of datasets and how
                 :class:`~torch.utils.data.IterableDataset` interacts with
                 `Multi-process data loading`_.

    .. warning:: See :ref:`reproducibility`, and :ref:`dataloader-workers-random-seed`, and
                 :ref:`data-loading-randomness` notes for random seed related questions.
    """
    dataset: Dataset[T_co]
    batch_size: Optional[int]
    num_workers: int
    pin_memory: bool
    drop_last: bool
    timeout: float
    sampler: Union[Sampler, Iterable]
    pin_memory_device: str
    prefetch_factor: int
    _iterator : Optional['_BaseDataLoaderIter']
    __initialized = False

    def __init__(self, dataset: Dataset[T_co], batch_size: Optional[int] = 1,
                 shuffle: Optional[bool] = None, sampler: Union[Sampler, Iterable, None] = None,
                 batch_sampler: Union[Sampler[Sequence], Iterable[Sequence], None] = None,
                 num_workers: int = 1, collate_fn: Optional[_collate_fn_t] = None,
                 pin_memory: bool = False, drop_last: bool = False,
                 timeout: float = 0, worker_init_fn: Optional[_worker_init_fn_t] = None,
                 multiprocessing_context=None, generator=None,
                 *, prefetch_factor: int = 2,
                 persistent_workers: bool = False,
                 pin_memory_device: str = ""):
        # torch._C._log_api_usage_once("python.data_loader")

        if num_workers < 0:
            raise ValueError('num_workers option should be non-negative; '
                             'use num_workers=0 to disable multiprocessing.')

        if timeout < 0:
            raise ValueError('timeout option should be non-negative')

        if num_workers == 0 and prefetch_factor != 2:
            raise ValueError('prefetch_factor option could only be specified in multiprocessing.'
                             'let num_workers > 0 to enable multiprocessing.')
        assert prefetch_factor > 0

        if persistent_workers and num_workers == 0:
            raise ValueError('persistent_workers option needs num_workers > 0')

        self.dataset = dataset
        self.num_workers = num_workers
        self.prefetch_factor = prefetch_factor
        self.pin_memory = pin_memory
        self.pin_memory_device = pin_memory_device
        self.timeout = timeout
        self.worker_init_fn = worker_init_fn
        self.multiprocessing_context = multiprocessing_context

        if self.pin_memory:
            warning("Don't support pin_memory now.")

        if len(pin_memory_device) != 0:
            warning("Don't support set pin_memory_device now.")

        # Adds several forward compatibilities so classic DataLoader can work with DataPipes
        # 1. _DataPipeSerializationWrapper container makes it easier to serialize without redefining pickler
        # 2. Additional worker init function will take care of sharding in MP and Distributed
        # if isinstance(self.dataset, IterDataPipe):
        #     self.dataset = _IterDataPipeSerializationWrapper(self.dataset)
        #     ws, rank = _get_distributed_settings()
        #     if num_workers > 0:
        #         self.worker_init_fn = functools.partial(
        #             _sharding_worker_init_fn, self.worker_init_fn, ws, rank)
        #     else:
        #         mindtorch.torch.utils.data.graph_settings.apply_sharding(self.dataset, ws, rank)
        # elif isinstance(self.dataset, MapDataPipe):
        #     self.dataset = _MapDataPipeSerializationWrapper(self.dataset)
        #     ws, rank = _get_distributed_settings()
        #     if num_workers > 0:
        #         self.worker_init_fn = functools.partial(
        #             _sharding_worker_init_fn, self.worker_init_fn, ws, rank)
        #     else:
        #         mindtorch.torch.utils.data.graph_settings.apply_sharding(self.dataset, ws, rank)


        # Arg-check dataset related before checking samplers because we want to
        # tell users that iterable-style datasets are incompatible with custom
        # samplers first, so that they don't learn that this combo doesn't work
        # after spending time fixing the custom sampler errors.
        if isinstance(dataset, IterableDataset):
            self._dataset_kind = _DatasetKind.Iterable
            # NOTE [ Custom Samplers and IterableDataset ]
            #
            # `IterableDataset` does not support custom `batch_sampler` or
            # `sampler` since the key is irrelevant (unless we support
            # generator-style dataset one day...).
            #
            # For `sampler`, we always create a dummy sampler. This is an
            # infinite sampler even when the dataset may have an implemented
            # finite `__len__` because in multi-process data loading, naive
            # settings will return duplicated data (which may be desired), and
            # thus using a sampler with length matching that of dataset will
            # cause data lost (you may have duplicates of the first couple
            # batches, but never see anything afterwards). Therefore,
            # `Iterabledataset` always uses an infinite sampler, an instance of
            # `_InfiniteConstantSampler` defined above.
            #
            # A custom `batch_sampler` essentially only controls the batch size.
            # However, it is unclear how useful it would be since an iterable-style
            # dataset can handle that within itself. Moreover, it is pointless
            # in multi-process data loading as the assignment order of batches
            # to workers is an implementation detail so users can not control
            # how to batchify each worker's iterable. Thus, we disable this
            # option. If this turns out to be useful in future, we can re-enable
            # this, and support custom samplers that specify the assignments to
            # specific workers.
            # if isinstance(dataset, IterDataPipe):
            #     if shuffle is not None:
            #         dataset = mindtorch.torch.utils.data.graph_settings.apply_shuffle_settings(dataset, shuffle=shuffle)
            # We cannot check `shuffle is not None` here, since previously `shuffle=False` was the default.
            if shuffle not in {False, None}:
                raise ValueError(
                    "DataLoader with IterableDataset: expected unspecified "
                    "shuffle option, but got shuffle={}".format(shuffle))

            if sampler is not None:
                # See NOTE [ Custom Samplers and IterableDataset ]
                raise ValueError(
                    "DataLoader with IterableDataset: expected unspecified "
                    "sampler option, but got sampler={}".format(sampler))
            elif batch_sampler is not None:
                # See NOTE [ Custom Samplers and IterableDataset ]
                raise ValueError(
                    "DataLoader with IterableDataset: expected unspecified "
                    "batch_sampler option, but got batch_sampler={}".format(batch_sampler))
        else:
            shuffle = bool(shuffle)
            self._dataset_kind = _DatasetKind.Map



        if sampler is not None and shuffle:
            raise ValueError('sampler option is mutually exclusive with '
                             'shuffle')

        if batch_sampler is not None:
            # auto_collation with custom batch_sampler
            if batch_size != 1 or shuffle or sampler is not None or drop_last:
                raise ValueError('batch_sampler option is mutually exclusive '
                                 'with batch_size, shuffle, sampler, and '
                                 'drop_last')
            batch_size = None
            drop_last = False
        elif batch_size is None:
            # no auto_collation
            if drop_last:
                raise ValueError('batch_size=None option disables auto-batching '
                                 'and is mutually exclusive with drop_last')

        if sampler is None:  # give default samplers
            if self._dataset_kind == _DatasetKind.Iterable:
                # See NOTE [ Custom Samplers and IterableDataset ]
                sampler = _InfiniteConstantSampler()
            else:  # map-style
                if shuffle:
                    sampler = RandomSampler(dataset, generator=generator)  # type: ignore[arg-type]
                else:
                    sampler = SequentialSampler(dataset)  # type: ignore[arg-type]

        if batch_size is not None and batch_sampler is None:
            # auto_collation without custom batch_sampler
            batch_sampler = BatchSampler(sampler, batch_size, drop_last)

        self.batch_size = batch_size
        self.drop_last = drop_last
        self.sampler = sampler
        self.batch_sampler = batch_sampler
        self.generator = generator

        if collate_fn is None:
            if self._auto_collation:
                collate_fn = _utils.collate.default_collate
            else:
                collate_fn = _utils.collate.default_convert_numpy

        self.collate_fn = collate_fn

        if _MP_MODE_ENV != "1":
            self.persistent_workers = num_workers > 0
        else:
            self.persistent_workers = persistent_workers

        self.__initialized = True
        self._IterableDataset_len_called = None  # See NOTE [ IterableDataset and __len__ ]

        self._iterator = None

        self.check_worker_number_rationality()

        self.maxsize = 128 # Default shared cache size of multiprocessing Queue
        # torch.set_vital('Dataloader', 'enabled', 'True')  # type: ignore[attr-defined]
        if self.num_workers > 0:
            origin_num_workers = self.num_workers
            self.num_workers = 1
            temp_dataloaderiter = _MultiProcessingDataLoaderIter(self, self.maxsize)
            try:
                single_data = next(temp_dataloaderiter)
            except Exception as e:
                single_data = None
                # warn_info = "There is something wrong during pre computed the maxsize of multiprocessing " \
                #             "queue, and the default value of 128MB will be used. Exception: " + str(e)
                # warning(warn_info)

            del temp_dataloaderiter
            self.num_workers = origin_num_workers

            if single_data is not None:
                nbytes = collate_nbytes(single_data)
                del single_data
                # This factor is used for share cache redundancy in multiprocessing Queue
                relaxation_ratio = 1.2
                nbytes = math.ceil(max(int(nbytes) >> 20, 1) * relaxation_ratio)
                self.maxsize = MIN_POWER_TWO(nbytes)

        if _MP_MODE_ENV != "1":
            self._iterator = self._get_iterator()
            self.is_first_iter = True

    def _get_iterator(self) -> '_BaseDataLoaderIter':
        if self.num_workers == 0:
            return _SingleProcessDataLoaderIter(self)
        else:
            self.check_worker_number_rationality()
            return _MultiProcessingDataLoaderIter(self, self.maxsize)

    @property
    def multiprocessing_context(self):
        return self.__multiprocessing_context

    @multiprocessing_context.setter
    def multiprocessing_context(self, multiprocessing_context):
        if multiprocessing_context is not None:
            if self.num_workers > 0:
                if isinstance(multiprocessing_context, string_classes):
                    valid_start_methods = multiprocessing.get_all_start_methods()
                    if multiprocessing_context not in valid_start_methods:
                        raise ValueError(
                            ('multiprocessing_context option '
                             'should specify a valid start method in {!r}, but got '
                             'multiprocessing_context={!r}').format(valid_start_methods, multiprocessing_context))
                    # error: Argument 1 to "get_context" has incompatible type "Union[str, bytes]"; expected "str"  [arg-type]
                    multiprocessing_context = multiprocessing.get_context(multiprocessing_context)  # type: ignore[arg-type]

                if not isinstance(multiprocessing_context, multiprocessing.context.BaseContext):
                    raise TypeError(('multiprocessing_context option should be a valid context '
                                     'object or a string specifying the start method, but got '
                                     'multiprocessing_context={}').format(multiprocessing_context))
            else:
                raise ValueError(('multiprocessing_context can only be used with '
                                  'multi-process loading (num_workers > 0), but got '
                                  'num_workers={}').format(self.num_workers))

        self.__multiprocessing_context = multiprocessing_context

    def __setattr__(self, attr, val):
        if self.__initialized and attr in (
                'batch_size', 'batch_sampler', 'sampler', 'drop_last', 'dataset', 'persistent_workers'):
            raise ValueError('{} attribute should not be set after {} is '
                             'initialized'.format(attr, self.__class__.__name__))

        super(DataLoader, self).__setattr__(attr, val)

    # We quote '_BaseDataLoaderIter' since it isn't defined yet and the definition can't be moved up
    # since '_BaseDataLoaderIter' references 'DataLoader'.
    def __iter__(self) -> '_BaseDataLoaderIter':
        # When using a single worker the returned iterator should be
        # created everytime to avoid reseting its state
        # However, in the case of a multiple workers iterator
        # the iterator is only created once in the lifetime of the
        # DataLoader object so that workers can be reused
        if self.persistent_workers and self.num_workers > 0:
            if self._iterator is None:
                self._iterator = self._get_iterator()
            elif self.is_first_iter:
                self.is_first_iter = False
            else:
                self._iterator._reset(self)
            return self._iterator
        else:
            return self._get_iterator()

    @property
    def _auto_collation(self):
        return self.batch_sampler is not None

    @property
    def _index_sampler(self):
        # The actual sampler used for generating indices for `_DatasetFetcher`
        # (see _utils/fetch.py) to read data at each time. This would be
        # `.batch_sampler` if in auto-collation mode, and `.sampler` otherwise.
        # We can't change `.sampler` and `.batch_sampler` attributes for BC
        # reasons.
        if self._auto_collation:
            return self.batch_sampler
        else:
            return self.sampler

    def __len__(self) -> int:
        if self._dataset_kind == _DatasetKind.Iterable:
            length = self._IterableDataset_len_called = len(self.dataset)  # type: ignore[assignment, arg-type]
            if self.batch_size is not None:  # IterableDataset doesn't allow custom sampler or batch_sampler
                from math import ceil
                if self.drop_last:
                    length = length // self.batch_size
                else:
                    length = ceil(length / self.batch_size)
            return length
        else:
            return len(self._index_sampler)

    def check_worker_number_rationality(self):
        def _create_warning_msg(num_worker_suggest, num_worker_created, cpuset_checked):

            suggested_max_worker_msg = ((
                "Our suggested max number of worker in current system is {}{}, which is smaller "
                "than what this DataLoader is going to create.").format(
                    num_worker_suggest,
                    ("" if cpuset_checked else " (`cpuset` is not taken into account)"))
            ) if num_worker_suggest is not None else (
                "DataLoader is not able to compute a suggested max number of worker in current system.")

            warn_msg = (
                "This DataLoader will create {} worker processes in total. {} "
                "Please be aware that excessive worker creation might get DataLoader running slow or even freeze, "
                "lower the worker number to avoid potential slowness/freeze if necessary.").format(
                    num_worker_created,
                    suggested_max_worker_msg)
            return warn_msg

        if not self.num_workers or self.num_workers == 0:
            return

        # try to compute a suggested max number of worker based on system's resource
        max_num_worker_suggest = None
        cpuset_checked = False
        if hasattr(os, 'sched_getaffinity'):
            try:
                max_num_worker_suggest = len(os.sched_getaffinity(0))
                cpuset_checked = True
            except Exception:
                pass
        if max_num_worker_suggest is None:
            # os.cpu_count() could return Optional[int]
            # get cpu count first and check None in order to satify mypy check
            cpu_count = os.cpu_count()
            if cpu_count is not None:
                max_num_worker_suggest = cpu_count

        if max_num_worker_suggest is None:
            warning(_create_warning_msg(
                max_num_worker_suggest,
                self.num_workers,
                cpuset_checked))
            return

        if self.num_workers > max_num_worker_suggest:
            warning(_create_warning_msg(
                max_num_worker_suggest,
                self.num_workers,
                cpuset_checked))

    def _get_shared_seed(self):
        # if isinstance(self.dataset, IterDataPipe):
        #     # _shared_seed = torch.empty((), dtype=torch.int64).random_(generator=self.generator).item()
        #     _shared_seed = np.random.randint(2**31)
        #     # TODO torch.dist
        #     if dist.is_available() and dist.is_initialized():
        #         rank = dist.get_rank()
        #         ws = dist.get_world_size()
        #         store = dist.distributed_c10d._get_default_store()
        #         if rank == 0:
        #             _shared_seed_str = str(_shared_seed)
        #             store.set(_utils.DATAPIPE_SHARED_SEED, _shared_seed_str)
        #             logger.info(f"Shared seed ({_shared_seed_str}) sent to store on rank 0")
        #             # Use 'add' instead of 'get' since for some store implementations 'add'
        #             # doesn't work well with 'get'.
        #             _shared_seed_recv_cnt = store.add(_utils.DATAPIPE_SHARED_SEED_COUNTER, 1)
        #             start = time.time()
        #             while _shared_seed_recv_cnt < ws:
        #                 time.sleep(_utils.DATAPIPE_SHARED_SEED_CHECK_INTERVAL)
        #                 _shared_seed_recv_cnt = store.add(_utils.DATAPIPE_SHARED_SEED_COUNTER, 0)
        #                 if timedelta(seconds=(time.time() - start)) > \
        #                         timedelta(seconds=_utils.DATAPIPE_SHARED_SEED_DEFAULT_TIMEOUT):
        #                     raise RuntimeError("Timed out receiving the signal from the distribtued store on "
        #                                        "Rank 0 that all other Ranks have received the shared seed. "
        #                                        f"(world_size={ws}, received={_shared_seed_recv_cnt}, "
        #                                        f"timeout={_utils.DATAPIPE_SHARED_SEED_DEFAULT_TIMEOUT})")
        #             # Reset after all distributed processes have received the shared seed
        #             store.set(_utils.DATAPIPE_SHARED_SEED, "")
        #             _shared_seed_recv_cnt = store.add(_utils.DATAPIPE_SHARED_SEED_COUNTER, -ws)
        #             assert _shared_seed_recv_cnt == 0
        #         else:
        #             _shared_seed_str = ""
        #             start = time.time()
        #             while len(_shared_seed_str) == 0:
        #                 time.sleep(_utils.DATAPIPE_SHARED_SEED_CHECK_INTERVAL)
        #                 _shared_seed_str = store.get(_utils.DATAPIPE_SHARED_SEED)
        #                 if timedelta(seconds=(time.time() - start)) > \
        #                         timedelta(seconds=_utils.DATAPIPE_SHARED_SEED_DEFAULT_TIMEOUT):
        #                     raise RuntimeError("Timed out receiving the shared seed from the distribtued store "
        #                                        f"on Rank {rank}. (world_size={ws}, "
        #                                        f"timeout={_utils.DATAPIPE_SHARED_SEED_DEFAULT_TIMEOUT})")
        #             logger.info(f"Shared seed ({_shared_seed_str}) received from store on rank {rank}")
        #             _shared_seed_recv_cnt = store.add(_utils.DATAPIPE_SHARED_SEED_COUNTER, 1)
        #             # Exit only when all ranks received seed, otherwise we are at risk that current rank
        #             # will reach same section of the code again while rank zero still in the previous iteration
        #             while _shared_seed_recv_cnt > 0:
        #                 time.sleep(_utils.DATAPIPE_SHARED_SEED_CHECK_INTERVAL)
        #                 _shared_seed_recv_cnt = store.add(_utils.DATAPIPE_SHARED_SEED_COUNTER, 0)
        #             _shared_seed = int(_shared_seed_str)
        #     return _shared_seed
        # else:
        return None


class _BaseDataLoaderIter(object):
    def __init__(self, loader: DataLoader) -> None:
        self._dataset = loader.dataset
        self._shared_seed = loader._get_shared_seed()
        # if isinstance(self._dataset, IterDataPipe): #TODO datapipe
        #     shared_rng = torch.Generator()
        #     shared_rng.manual_seed(self._shared_seed)
        #     self._dataset = mindtorch.torch.utils.data.graph_settings.apply_shuffle_seed(self._dataset, shared_rng)
        self._dataset_kind = loader._dataset_kind
        self._IterableDataset_len_called = loader._IterableDataset_len_called
        self._auto_collation = loader._auto_collation
        self._drop_last = loader.drop_last
        self._index_sampler = loader._index_sampler
        self._num_workers = loader.num_workers
        self._prefetch_factor = loader.prefetch_factor
        # for other backends, pin_memory_device need to set. if not set
        # default behaviour is CUDA device. if pin_memory_device is selected
        # and pin_memory is not set, the default behaviour false.
        # if (len(loader.pin_memory_device) == 0):#TODO pin_memory
        #     # self._pin_memory = loader.pin_memory and torch.cuda.is_available()  #TODO torch.cuda.is_available() 无对应mindspore 算子
        #     self._pin_memory = loader.pin_memory
        #     self._pin_memory_device = None
        # else:
        #     if not loader.pin_memory:
        #         warn_msg = ("pin memory device is set and pin_memory flag is not used then device pinned memory won't be used"
        #                     "please set pin_memory to true, if you need to use the device pin memory")
        #         warning(warn_msg)
        #
        #     self._pin_memory = loader.pin_memory
        #     self._pin_memory_device = loader.pin_memory_device
        self._timeout = loader.timeout
        self._collate_fn = loader.collate_fn
        self._sampler_iter = iter(self._index_sampler)
        # self._base_seed = torch.empty((), dtype=torch.int64).random_(generator=loader.generator).item() #TODO
        self._base_seed = np.random.randint(2**31)
        self._persistent_workers = loader.persistent_workers
        self._num_yielded = 0
        self._profile_name = "enumerate(DataLoader)#{}.__next__".format(self.__class__.__name__)

    def __iter__(self) -> '_BaseDataLoaderIter':
        return self

    def _reset(self, loader, first_iter=False):
        self._sampler_iter = iter(self._index_sampler)
        self._num_yielded = 0
        self._IterableDataset_len_called = loader._IterableDataset_len_called
        self._shared_seed = loader._get_shared_seed()
        # if isinstance(self._dataset, IterDataPipe): #TODO pipe
        #     shared_rng = torch.Generator()
        #     shared_rng.manual_seed(self._shared_seed)
        #     self._dataset = mindtorch.torch.utils.data.graph_settings.apply_shuffle_seed(self._dataset, shared_rng)

    def _next_index(self):
        return next(self._sampler_iter)  # may raise StopIteration

    def _next_data(self):
        raise NotImplementedError

    def __next__(self) -> Any:
        if self._sampler_iter is None:
            self._reset()  # type: ignore[call-arg]
        data = self._next_data()
        self._num_yielded += 1
        if self._dataset_kind == _DatasetKind.Iterable and \
                    self._IterableDataset_len_called is not None and \
                    self._num_yielded > self._IterableDataset_len_called:
            warn_msg = ("Length of IterableDataset {} was reported to be {} (when accessing len(dataloader)), but {} "
                            "samples have been fetched. ").format(self._dataset, self._IterableDataset_len_called,
                                                                  self._num_yielded)
            if self._num_workers > 0:
                warn_msg += ("For multiprocessing data-loading, this could be caused by not properly " \
                             "configuring the IterableDataset replica at each worker. ")
            warning(warn_msg)
        return data

    next = __next__  # Python 2 compatibility

    def __len__(self) -> int:
        return len(self._index_sampler)

    def __getstate__(self):
        raise NotImplementedError("{} cannot be pickled", self.__class__.__name__)


class _SingleProcessDataLoaderIter(_BaseDataLoaderIter):
    def __init__(self, loader, init_maxsize = False):
        super(_SingleProcessDataLoaderIter, self).__init__(loader)
        if not init_maxsize:
            assert self._timeout == 0
            assert self._num_workers == 0

        self._dataset_fetcher = _DatasetKind.create_fetcher(
            self._dataset_kind, self._dataset, self._auto_collation, self._collate_fn, self._drop_last)

    def _next_data(self):
        index = self._next_index()  # may raise StopIteration
        data = self._dataset_fetcher.fetch(index)  # may raise StopIteration
        # if self._pin_memory:#TODO pin_memory
        #     data = _utils.pin_memory.pin_memory(data, self._pin_memory_device)
        # convert to tensor
        if self._collate_fn == default_collate or self._collate_fn == default_convert_numpy:
            data = default_convert(data)
        return data


class _MultiProcessingDataLoaderIter(_BaseDataLoaderIter):
    def __init__(self, loader, maxsize = 64):
        super(_MultiProcessingDataLoaderIter, self).__init__(loader)

        assert self._num_workers > 0
        assert self._prefetch_factor > 0

        if loader.multiprocessing_context is None:
            multiprocessing_context = multiprocessing
        else:
            multiprocessing_context = loader.multiprocessing_context

        self._worker_init_fn = loader.worker_init_fn
        # No certainty which module multiprocessing_context is
        # self._worker_result_queue = multiprocessing_context.Queue()  # type: ignore[var-annotated]
        self._worker_result_queue = _SharedQueue(loader.num_workers * loader.prefetch_factor, max_rowsize=maxsize) # a queue using shared memory for better performance.
        self._worker_pids_set = False
        self._shutdown = False
        self._workers_done_event = multiprocessing_context.Event()

        self._index_queues = []
        self._workers = []
        for i in range(self._num_workers):
            # No certainty which module multiprocessing_context is
            index_queue = multiprocessing_context.Queue()  # type: ignore[var-annotated]
            # Need to `cancel_join_thread` here!
            # See sections (2) and (3b) above.
            index_queue.cancel_join_thread()
            w = multiprocessing_context.Process(
                target=_utils.worker._worker_loop,
                args=(self._dataset_kind, self._dataset, index_queue,
                      self._worker_result_queue, self._workers_done_event,
                      self._auto_collation, self._collate_fn, self._drop_last,
                      self._base_seed, self._worker_init_fn, i, self._num_workers,
                      self._persistent_workers, self._shared_seed))
            w.daemon = True
            # NB: Process.start() actually take some time as it needs to
            #     start a process and pass the arguments over via a pipe.
            #     Therefore, we only add a worker to self._workers list after
            #     it started, so that we do not call .join() if program dies
            #     before it starts, and __del__ tries to join but will get:
            #     AssertionError: can only join a started process.
            w.start()
            self._index_queues.append(index_queue)
            self._workers.append(w)

        # if self._pin_memory:#TODO pin_memory
        #     self._pin_memory_thread_done_event = threading.Event()
        #
        #     # Queue is not type-annotated
        #     self._data_queue = queue.Queue()  # type: ignore[var-annotated]
        #     pin_memory_thread = threading.Thread(
        #         target=_utils.pin_memory._pin_memory_loop,
        #         args=(self._worker_result_queue, self._data_queue,
        #               torch.cuda.current_device(),
        #               self._pin_memory_thread_done_event, self._pin_memory_device))  #TODO
        #     pin_memory_thread.daemon = True
        #     pin_memory_thread.start()
        #     # Similar to workers (see comment above), we only register
        #     # pin_memory_thread once it is started.
        #     self._pin_memory_thread = pin_memory_thread
        # else:
        self._data_queue = self._worker_result_queue

        # In some rare cases, persistent workers (daemonic processes)
        # would be terminated before `__del__` of iterator is invoked
        # when main process exits
        # It would cause failure when pin_memory_thread tries to read
        # corrupted data from worker_result_queue
        # atexit is used to shutdown thread and child processes in the
        # right sequence before main process exits
        # if self._persistent_workers and self._pin_memory: #TODO pin_memory
        #     import atexit
        #     for w in self._workers:
        #         atexit.register(_MultiProcessingDataLoaderIter._clean_up_worker, w)

        # .pid can be None only before process is spawned (not the case, so ignore)
        # _utils.signal_handling._set_worker_pids(id(self), tuple(w.pid for w in self._workers))  # type: ignore[misc]
        # _utils.signal_handling._set_SIGCHLD_handler()
        self._worker_pids_set = True
        self._reset(loader, first_iter=True)

    def _reset(self, loader, first_iter=False):
        super()._reset(loader, first_iter)
        self._send_idx = 0  # idx of the next task to be sent to workers
        self._rcvd_idx = 0  # idx of the next task to be returned in __next__
        # information about data not yet yielded, i.e., tasks w/ indices in range [rcvd_idx, send_idx).
        # map: task idx => - (worker_id,)        if data isn't fetched (outstanding)
        #                  \ (worker_id, data)   if data is already fetched (out-of-order)
        self._task_info = {}
        self._tasks_outstanding = 0  # always equal to count(v for v in task_info.values() if len(v) == 1)
        # A list of booleans representing whether each worker still has work to
        # do, i.e., not having exhausted its iterable dataset object. It always
        # contains all `True`s if not using an iterable-style dataset
        # (i.e., if kind != Iterable).
        # Not that this indicates that a worker still has work to do *for this epoch*.
        # It does not mean that a worker is dead. In case of `_persistent_workers`,
        # the worker will be reset to available in the next epoch.
        self._workers_status = [True for i in range(self._num_workers)]
        # Reset the worker queue cycle so it resumes next epoch at worker 0
        self._worker_queue_idx_cycle = itertools.cycle(range(self._num_workers))
        # We resume the prefetching in case it was enabled
        if not first_iter:
            for idx in range(self._num_workers):
                self._index_queues[idx].put(_utils.worker._ResumeIteration(self._shared_seed))
            resume_iteration_cnt = self._num_workers
            while resume_iteration_cnt > 0:
                return_idx, return_data = self._get_data()
                if isinstance(return_idx, _utils.worker._ResumeIteration):
                    assert return_data is None
                    resume_iteration_cnt -= 1
        # prime the prefetch loop
        for _ in range(self._prefetch_factor * self._num_workers):
            self._try_put_index()

    def _try_get_data(self, timeout=_utils.MP_STATUS_CHECK_INTERVAL):
        # Tries to fetch data from `self._data_queue` once for a given timeout.
        # This can also be used as inner loop of fetching without timeout, with
        # the sender status as the loop condition.
        #
        # This raises a `RuntimeError` if any worker died expectedly. This error
        # can come from either the SIGCHLD handler in `_utils/signal_handling.py`
        # (only for non-Windows platforms), or the manual check below on errors
        # and timeouts.
        #
        # Returns a 2-tuple:
        #   (bool: whether successfully get data, any: data if successful else None)
        try:
            data = self._data_queue.get(timeout=timeout)
            return (True, data)
        except Exception as e:
            # At timeout and error, we manually check whether any worker has
            # failed. Note that this is the only mechanism for Windows to detect
            # worker failures.
            failed_workers = []
            for worker_id, w in enumerate(self._workers):
                if self._workers_status[worker_id] and not w.is_alive():
                    failed_workers.append(w)
                    self._mark_worker_as_unavailable(worker_id)
            if len(failed_workers) > 0:
                pids_str = ', '.join(str(w.pid) for w in failed_workers)
                raise RuntimeError('DataLoader worker (pid(s) {}) exited unexpectedly'.format(pids_str)) from e
            if isinstance(e, queue.Empty):
                return (False, None)
            import tempfile
            import errno
            try:
                # Raise an exception if we are this close to the FDs limit.
                # Apparently, trying to open only one file is not a sufficient
                # test.
                # See NOTE [ DataLoader on Linux and open files limit ]
                fds_limit_margin = 10
                fs = [tempfile.NamedTemporaryFile() for i in range(fds_limit_margin)]
            except OSError as e:
                if e.errno == errno.EMFILE:
                    raise RuntimeError(
                        "Too many open files. Communication with the"
                        " workers is no longer possible. Please increase the"
                        " limit using `ulimit -n` in the shell.") from None
            raise

    def _get_data(self):
        # Fetches data from `self._data_queue`.
        #
        # We check workers' status every `MP_STATUS_CHECK_INTERVAL` seconds,
        # which we achieve by running `self._try_get_data(timeout=MP_STATUS_CHECK_INTERVAL)`
        # in a loop. This is the only mechanism to detect worker failures for
        # Windows. For other platforms, a SIGCHLD handler is also used for
        # worker failure detection.
        #
        # If `pin_memory=True`, we also need check if `pin_memory_thread` had
        # died at timeouts.
        if self._timeout > 0:
            success, data = self._try_get_data(self._timeout)
            if success:
                return data
            else:
                raise RuntimeError('DataLoader timed out after {} seconds'.format(self._timeout))
        # elif self._pin_memory:
        #     while self._pin_memory_thread.is_alive():
        #         success, data = self._try_get_data()
        #         if success:
        #             return data
        #     else:
        #         # while condition is false, i.e., pin_memory_thread died.
        #         raise RuntimeError('Pin memory thread exited unexpectedly')
        #     # In this case, `self._data_queue` is a `queue.Queue`,. But we don't
        #     # need to call `.task_done()` because we don't use `.join()`.
        else:
            while True:
                success, data = self._try_get_data()
                if success:
                    return data

    def _next_data(self):
        while True:
            # If the worker responsible for `self._rcvd_idx` has already ended
            # and was unable to fulfill this task (due to exhausting an `IterableDataset`),
            # we try to advance `self._rcvd_idx` to find the next valid index.
            #
            # This part needs to run in the loop because both the `self._get_data()`
            # call and `_IterableDatasetStopIteration` check below can mark
            # extra worker(s) as dead.
            while self._rcvd_idx < self._send_idx:
                info = self._task_info[self._rcvd_idx]
                worker_id = info[0]
                if len(info) == 2 or self._workers_status[worker_id]:  # has data or is still active
                    break
                del self._task_info[self._rcvd_idx]
                self._rcvd_idx += 1
            else:
                # no valid `self._rcvd_idx` is found (i.e., didn't break)
                if not self._persistent_workers:
                    self._shutdown_workers()
                raise StopIteration

            # Now `self._rcvd_idx` is the batch index we want to fetch

            # Check if the next sample has already been generated
            if len(self._task_info[self._rcvd_idx]) == 2:
                data = self._task_info.pop(self._rcvd_idx)[1]
                return self._process_data(data)

            assert not self._shutdown and self._tasks_outstanding > 0
            idx, data = self._get_data()
            self._tasks_outstanding -= 1
            if self._dataset_kind == _DatasetKind.Iterable:
                # Check for _IterableDatasetStopIteration
                if isinstance(data, _utils.worker._IterableDatasetStopIteration):
                    if self._persistent_workers:
                        self._workers_status[data.worker_id] = False
                    else:
                        self._mark_worker_as_unavailable(data.worker_id)
                    self._try_put_index()
                    continue

            if idx != self._rcvd_idx:
                # store out-of-order samples
                self._task_info[idx] += (data,)
            else:
                del self._task_info[idx]
                return self._process_data(data)

    def _try_put_index(self):
        assert self._tasks_outstanding < self._prefetch_factor * self._num_workers

        try:
            index = self._next_index()
        except StopIteration:
            return
        for _ in range(self._num_workers):  # find the next active worker, if any
            worker_queue_idx = next(self._worker_queue_idx_cycle)
            if self._workers_status[worker_queue_idx]:
                break
        else:
            # not found (i.e., didn't break)
            return
        if isinstance(index, torch.Tensor):
            index = index.asnumpy()
        elif isinstance(index, (tuple, list)) and isinstance(index[0], torch.Tensor):
            index = [i.asnumpy() for i in index]
        self._index_queues[worker_queue_idx].put((self._send_idx, index))
        self._task_info[self._send_idx] = (worker_queue_idx,)
        self._tasks_outstanding += 1
        self._send_idx += 1

    def _process_data(self, data):
        self._rcvd_idx += 1
        self._try_put_index()
        if isinstance(data, ExceptionWrapper):
            data.reraise()
        # convert data to Tensor
        if self._collate_fn == default_collate or self._collate_fn == default_convert_numpy:
            data = default_convert(data)
        return data

    def _mark_worker_as_unavailable(self, worker_id, shutdown=False):
        # Mark a worker as having finished its work e.g., due to
        # exhausting an `IterableDataset`. This should be used only when this
        # `_MultiProcessingDataLoaderIter` is going to continue running.

        assert self._workers_status[worker_id] or (self._persistent_workers and shutdown)

        # Signal termination to that specific worker.
        q = self._index_queues[worker_id]
        # Indicate that no more data will be put on this queue by the current
        # process.
        q.put(None)

        # Note that we don't actually join the worker here, nor do we remove the
        # worker's pid from C side struct because (1) joining may be slow, and
        # (2) since we don't join, the worker may still raise error, and we
        # prefer capturing those, rather than ignoring them, even though they
        # are raised after the worker has finished its job.
        # Joinning is deferred to `_shutdown_workers`, which it is called when
        # all workers finish their jobs (e.g., `IterableDataset` replicas) or
        # when this iterator is garbage collected.

        self._workers_status[worker_id] = False

        assert self._workers_done_event.is_set() == shutdown

    def _shutdown_workers(self):
        # Called when shutting down this `_MultiProcessingDataLoaderIter`.
        # See NOTE [ Data Loader Multiprocessing Shutdown Logic ] for details on
        # the logic of this function.
        python_exit_status = _utils.python_exit_status
        if python_exit_status is True or python_exit_status is None:
            # See (2) of the note. If Python is shutting down, do no-op.
            return
        # Normal exit when last reference is gone / iterator is depleted.
        # See (1) and the second half of the note.
        if not self._shutdown:
            self._shutdown = True
            try:
                # Normal exit when last reference is gone / iterator is depleted.
                # See (1) and the second half of the note.

                # Exit `pin_memory_thread` first because exiting workers may leave
                # corrupted data in `worker_result_queue` which `pin_memory_thread`
                # reads from.
                if hasattr(self, '_pin_memory_thread'):
                    # Use hasattr in case error happens before we set the attribute.
                    self._pin_memory_thread_done_event.set()
                    # Send something to pin_memory_thread in case it is waiting
                    # so that it can wake up and check `pin_memory_thread_done_event`
                    self._worker_result_queue.put((None, None))
                    self._pin_memory_thread.join()
                    self._worker_result_queue.cancel_join_thread()
                    self._worker_result_queue.close()

                # Exit workers now.
                self._workers_done_event.set()
                for worker_id in range(len(self._workers)):
                    # Get number of workers from `len(self._workers)` instead of
                    # `self._num_workers` in case we error before starting all
                    # workers.
                    # If we are using workers_status with persistent_workers
                    # we have to shut it down because the worker is paused
                    if self._persistent_workers or self._workers_status[worker_id]:
                        self._mark_worker_as_unavailable(worker_id, shutdown=True)
                for w in self._workers:
                    # We should be able to join here, but in case anything went
                    # wrong, we set a timeout and if the workers fail to join,
                    # they are killed in the `finally` block.
                    w.join(timeout=_utils.MP_STATUS_CHECK_INTERVAL)
                for q in self._index_queues:
                    q.cancel_join_thread()
                    q.close()
            finally:
                # Even though all this function does is putting into queues that
                # we have called `cancel_join_thread` on, weird things can
                # happen when a worker is killed by a signal, e.g., hanging in
                # `Event.set()`. So we need to guard this with SIGCHLD handler,
                # and remove pids from the C side data structure only at the
                # end.
                #
                # FIXME: Unfortunately, for Windows, we are missing a worker
                #        error detection mechanism here in this function, as it
                #        doesn't provide a SIGCHLD handler.
                if self._worker_pids_set:
                    # _utils.signal_handling._remove_worker_pids(id(self))
                    self._worker_pids_set = False
                for w in self._workers:
                    if w.is_alive():
                        # Existing mechanisms try to make the workers exit
                        # peacefully, but in case that we unfortunately reach
                        # here, which we shouldn't, (e.g., pytorch/pytorch#39570),
                        # we kill the worker.
                        w.terminate()

    # staticmethod is used to remove reference to `_MultiProcessingDataLoaderIter`
    @staticmethod
    def _clean_up_worker(w):
        try:
            w.join(timeout=_utils.MP_STATUS_CHECK_INTERVAL)
        finally:
            if w.is_alive():
                w.terminate()

    def __del__(self):
        self._shutdown_workers()
