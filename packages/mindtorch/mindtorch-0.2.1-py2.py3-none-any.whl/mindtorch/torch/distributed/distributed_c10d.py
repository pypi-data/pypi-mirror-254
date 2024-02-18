from datetime import timedelta
from typing import Any, Dict, Optional, Union, overload, List

from mindspore.context import ParallelMode
from mindspore.communication.management import init, create_group, GlobalComm, destroy_group
from mindspore.communication._comm_helper import (_is_available, _is_initialized, _get_backend, _is_hccl_available,
                                                  _is_nccl_available, _is_mpi_available, _get_group_ranks)
from mindspore import Tensor
import mindspore as ms

from mindtorch.utils import unsupported_attr
from mindtorch.torch.logging import warning

BACKEND_DEVICE_TARGET_DICT = {
    'nccl': 'GPU',
    'hccl': 'Ascend',
}


class ReduceOp:
    SUM = ...
    PRODUCT = ...
    MIN = ...
    MAX = ...
    BAND = ...
    BOR = ...
    BXOR = ...
    PREMUL_SUM = ...
    UNUSED = ...


class ProcessGroup:
    # TODO: implemented the following methods after the operators supported.
    @overload
    def broadcast(
            self,
            tensors: List[Tensor],
            opts=None,
    ) -> None: ...

    @overload
    def broadcast(
            self,
            tensor: Tensor,
            root: int,
    ) -> None: ...

    @overload
    def allreduce(
            self,
            tensors: List[Tensor],
            opts=None,
    ) -> None: ...

    @overload
    def allreduce(
            self,
            tensors: List[Tensor],
            op=ReduceOp.SUM,
    ) -> None: ...

    @overload
    def allreduce(
            self,
            tensor: Tensor,
            op=ReduceOp.SUM,
    ) -> None: ...

    @overload
    def reduce(
            self,
            tensors: List[Tensor],
            opts=None,
    ) -> None: ...

    @overload
    def reduce(
            self,
            tensor: Tensor,
            root: int,
            op=ReduceOp.SUM,
    ) -> None: ...

    @overload
    def allgather(
            self,
            output_tensors: List[List[Tensor]],
            input_tensors: List[Tensor],
            opts=None,
    ) -> None: ...

    @overload
    def allgather(
            self,
            output_tensors: List[Tensor],
            input_tensor: Tensor,
    ) -> None: ...

    @overload
    def gather(
            self,
            output_tensors: List[List[Tensor]],
            input_tensors: List[Tensor],
            opts=None,
    ) -> None: ...

    @overload
    def gather(
            self,
            output_tensors: List[Tensor],
            input_tensor: Tensor,
            root: int,
    ) -> None: ...

    @overload
    def scatter(
            self,
            output_tensors: List[Tensor],
            input_tensors: List[List[Tensor]],
            opts=None,
    ) -> None: ...

    @overload
    def scatter(
            self,
            output_tensor: Tensor,
            input_tensors: List[Tensor],
            root: int,
    ) -> None: ...

    @overload
    def reduce_scatter(
            self,
            output_tensors: List[Tensor],
            input_tensors: List[List[Tensor]],
            opts=None,
    ) -> None: ...

    @overload
    def reduce_scatter(
            self,
            output_tensors: Tensor,
            input_tensor: List[Tensor],
    ) -> None: ...

    @overload
    def alltoall_base(
            self,
            output_tensor: Tensor,
            input_tensor: Tensor,
            output_split_sizes: List[int],
            input_split_sizes: List[int],
            opts=None,
    ) -> None: ...

    @overload
    def alltoall_base(
            self,
            output: Tensor,
            input: Tensor,
            output_split_sizes: List[int],
            input_split_sizes: List[int],
    ) -> None: ...

    @overload
    def alltoall(
            self,
            output_tensor: List[Tensor],
            input_tensor: List[Tensor],
            opts=None,
    ) -> None: ...

    @overload
    def alltoall(
            self,
            output: List[Tensor],
            input: List[Tensor],
    ) -> None: ...

    @overload
    def send(
            self,
            tensors: List[Tensor],
            dstRank: int,
            tag: int,
    ) -> None: ...

    @overload
    def recv(
            self,
            tensors: List[Tensor],
            srcRank: int,
            tag: int,
    ) -> None: ...


_pg_map: Dict[ProcessGroup, str] = {}


def init_process_group(
        backend: Union[str],
        init_method: Optional[str] = None,
        timeout: timedelta = None,
        world_size: int = -1,
        rank: int = -1,
        store: Optional = None,
        group_name: str = "",
        pg_options: Optional[Any] = None,
):
    global _pg_map
    if backend not in BACKEND_DEVICE_TARGET_DICT:
        raise ValueError('{} is not supported.'.format(backend))
    device_target = ms.get_context('device_target')
    backend_device_target = BACKEND_DEVICE_TARGET_DICT[backend]
    if device_target != backend_device_target:
        raise ValueError('If backend is {}, the device_target must be {}.'.format(backend, backend_device_target))
    init()
    device_num = get_world_size()
    if world_size != device_num:
        raise ValueError('The world_size:{} is not equal to the device_num:{}.'.format(world_size, device_num))
    ms.set_auto_parallel_context(parallel_mode=ParallelMode.DATA_PARALLEL, gradients_mean=True, device_num=device_num,
                                 parameter_broadcast=True)

    pg = ProcessGroup()
    _pg_map[pg] = GlobalComm.WORLD_COMM_GROUP

    unsupported_attr(init_method)
    unsupported_attr(timeout)
    unsupported_attr(rank)
    unsupported_attr(store)
    unsupported_attr(group_name)
    unsupported_attr(pg_options)


def new_group(ranks: Optional[List[int]] = None,
              timeout: Optional[timedelta] = None,
              backend: Optional[str] = None,
              pg_options: Optional[Any] = None):
    global _pg_map
    if ranks is None:
        return None
    if not isinstance(ranks, list):
        raise TypeError("The dtype of ranks must be `list`, but got `{}`".format(type(ranks)))
    if len(ranks) == get_world_size():
        return None
    for i, rank in enumerate(ranks):
        if not isinstance(rank, int):
            raise TypeError("The dtype of ranks[{}] must be `int`, but got `{}`".format(i, type(rank)))
    rank = get_rank()
    if rank not in ranks:
        return None
    pg = ProcessGroup()
    name = 'group_{}'.format(len(_pg_map))
    create_group(name, ranks)
    _pg_map[pg] = name
    unsupported_attr(timeout)
    unsupported_attr(backend)
    unsupported_attr(pg_options)
    return pg


def get_rank(group: Optional[ProcessGroup] = None):
    group = GlobalComm.WORLD_COMM_GROUP if group is None else _pg_map[group]
    return ms.communication.get_rank(group)


def get_world_size(group: Optional[ProcessGroup] = None):
    group = GlobalComm.WORLD_COMM_GROUP if group is None else _pg_map[group]
    return ms.communication.get_group_size(group)


def destroy_process_group(group: Optional[ProcessGroup] = None):
    global _pg_map
    if group is None:
        del_pg_list = list()
        for pg in _pg_map:
            name = _pg_map[pg]
            if name != GlobalComm.WORLD_COMM_GROUP:
                destroy_group(name)
                del_pg_list.append(pg)
        for pg in del_pg_list:
            del _pg_map[pg]
    else:
        if group in _pg_map:
            name = _pg_map[group]
            if name != GlobalComm.WORLD_COMM_GROUP:
                destroy_group(name)
                del _pg_map[group]


def _get_pg_name(group: Union[ProcessGroup, None]):
    if group is None:
        return GlobalComm.WORLD_COMM_GROUP
    if isinstance(group, ProcessGroup):
        if group in _pg_map:
            return _pg_map[group]
        raise ValueError("The `group` is not existed.")
    raise TypeError('The dtype of `group` must be `ProcessGroup`, but got {}'.format(type(group)))


def is_available():
    return _is_available()


def is_initialized():
    return _is_initialized()


def is_mpi_available():
    return _is_mpi_available()


def is_nccl_available():
    device_target = ms.get_context('device_target')
    if device_target == 'Ascend':
        warning("On Ascend, the result of is_hccl_available() is returned. " \
                "If you do not want to see this log, please use that API.")
        return _is_hccl_available()
    return _is_nccl_available()


def is_hccl_available():
    return _is_hccl_available()


def get_backend():
    return _get_backend()


def get_process_group_ranks(group: Union[ProcessGroup, None]):
    if group is None:
        return _get_group_ranks(GlobalComm.WORLD_COMM_GROUP)
    pg_name = _pg_map[group]
    return _get_group_ranks(pg_name)
