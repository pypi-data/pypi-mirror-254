import mindspore as ms

def is_available():
    r"""Returns whether PyTorch is built with OpenMP support."""
    return ms.communication._comm_helper._is_mpi_available()
