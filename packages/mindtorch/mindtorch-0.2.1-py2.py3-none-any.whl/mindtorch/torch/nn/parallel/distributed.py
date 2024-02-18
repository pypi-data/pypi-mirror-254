from mindspore.nn.wrap.grad_reducer import DistributedGradReducer
from mindspore.communication.management import GlobalComm
from mindspore import ops
import mindspore as ms

from mindtorch.torch import distributed as dist
from mindtorch.torch.distributed.distributed_c10d import _get_pg_name
from mindtorch.torch.nn.modules.module import Module
from mindtorch.utils import unsupported_attr
from mindtorch.torch.logging import warning

class DistributedDataParallel(Module):
    def __init__(
            self,
            module,
            device_ids=None,
            output_device=None,
            dim=0,
            broadcast_buffers=True,
            process_group=None,
            bucket_cap_mb=25,
            find_unused_parameters=False,
            check_reduction=False,
            gradient_as_bucket_view=False,
            static_graph=False,
    ):
        super(DistributedDataParallel, self).__init__()
        ms.set_auto_parallel_context(comm_fusion={"allreduce": {"mode": "size", "config": bucket_cap_mb}})
        if ms.get_context('mode') == ms.PYNATIVE_MODE:
            warning("`bucket_cap_mb` takes effect only in graph mode.")

        self.network = module
        device_num = dist.get_world_size(process_group)
        pg_name = GlobalComm.WORLD_COMM_GROUP if process_group is None else _get_pg_name(process_group)
        self.grad_reducer = DistributedGradReducer(module.trainable_params(), degree=device_num, group=pg_name)

        self.modules_buffers = list()
        self.broadcast_buffers = broadcast_buffers
        if broadcast_buffers:
            for param in module.get_parameters():
                if not param.requires_grad:
                    self.modules_buffers.append(param)
        self.broadcast = ops.Broadcast(0, pg_name)

        unsupported_attr(device_ids)
        unsupported_attr(output_device)
        unsupported_attr(dim)
        unsupported_attr(find_unused_parameters)
        unsupported_attr(check_reduction)
        unsupported_attr(gradient_as_bucket_view)
        unsupported_attr(static_graph)

    def will_sync_module_buffers(self):
        return self.broadcast_buffers and len(self.modules_buffers) > 0

    def _sync_buffers(self):
        for buffer in self.modules_buffers:
            remote_buffer = self.broadcast(buffer)
            buffer.set_data(remote_buffer)

    def forward(self, *inputs, **kwargs):
        if self.will_sync_module_buffers():
            self._sync_buffers()
        self.network(*inputs, **kwargs)

    def all_reduce(self, grads):
        grads = self.grad_reducer(grads)
        return grads

    def gather(self, outputs, output_device):
        # TODO: implemented the method after the operators supported.
        unsupported_attr(outputs)
        unsupported_attr(output_device)

    def scatter(self, inputs, kwargs, device_ids):
        # TODO: implemented the method after the operators supported.
        unsupported_attr(inputs)
        unsupported_attr(kwargs)
        unsupported_attr(device_ids)

def _find_tensors(obj):
    unsupported_attr(obj)
    raise NotImplementedError("`_find_tensors` is not implemented now.")
