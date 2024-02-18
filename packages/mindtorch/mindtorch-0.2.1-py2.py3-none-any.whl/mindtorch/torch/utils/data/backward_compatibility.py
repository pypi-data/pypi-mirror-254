from mindtorch.torch.logging import warning

def worker_init_fn(worker_id):
    warning("Usage of backward_compatibility.worker_init_fn is deprecated" \
            " as DataLoader automatically applies sharding in every worker")
