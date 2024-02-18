import numpy as np
import mindspore as ms
import mindspore.nn as nn
from scipy.linalg import lu, lu_factor, lu_solve
import mindtorch.torch.common.dtype as msdapter_dtype

_error_msg = "[numpy backward issue.] For '{}', it can not backward, please use other function instead."
class NumpyCommon(nn.Cell):
    def __init__(self, op_name=None):
        super().__init__()
        self.op_name = op_name

#TODO: NumpyLstsq constructs the same output that torch.lstsq generates
#Later, torch.lstsq will be deprecated and used linalg.lstsq instead, the NumpyLstsq will be deprecated as well
class NumpyLstsq(NumpyCommon):
    def construct(self, input, A):
        type_np = A.dtype
        shape_np = A.shape
        input_np = input.asnumpy()
        A_np = A.asnumpy()
        output = ms.Tensor(np.linalg.lstsq(A_np, input_np)[0])
        #TODO: linalg.lstsq not support qr as return, thus the qr will be set to zeros
        qr = ms.ops.zeros(shape_np, type_np)
        return output, qr
    def bprop(self, input, A, out, dout):
        raise RuntimeError(_error_msg.format(self.op_name))

#TODO: NumpyLstsq constructs the same output that torch.linalg.lstsq generates
class NumpyFullLstsq(NumpyCommon):
    def __init__(self, op_name=None, rcond=None):
        super().__init__()
        self.op_name = op_name
        self.rcond = rcond
    def construct(self, a, b):
        a = a.asnumpy()
        b = b.asnumpy()
        output = np.linalg.lstsq(a, b, rcond=self.rcond)
        x = ms.Tensor(output[0])
        residuals = ms.Tensor(output[1])
        rank = ms.Tensor(output[2])
        s = ms.Tensor(output[3])
        return x, residuals, rank, s
    def bprop(self, a, b, out, dout):
        raise RuntimeError(_error_msg.format(self.op_name))

class NumpyEigvals(NumpyCommon):
    def construct(self, A):
        A_np = A.asnumpy()
        output = np.linalg.eigvals(A_np)
        if A_np.dtype is np.float64 or A_np.dtype is np.complex128:
            output = output.astype(np.complex128)
        else:
            output = output.astype(np.complex64)
        return ms.Tensor(output)
    def bprop(self, A, out, dout):
        raise RuntimeError(_error_msg.format(self.op_name))

def _svd_not_compute_uv(input, full_matrices=False):
    input_np = input.asnumpy()
    output = np.linalg.svd(input_np, full_matrices, compute_uv=False)
    return ms.Tensor(output)

def _svd_compute_uv(input, full_matrices=False):
    input_np = input.asnumpy()
    output = np.linalg.svd(input_np, full_matrices, compute_uv=True)
    u = ms.Tensor(output[0])
    s = ms.Tensor(output[1])
    v_np = output[2]
    #TODO: Currently ms.ops.swapaxes has problem on GRAPH mode
    v_np = np.swapaxes(v_np, -1, -2)
    v = ms.Tensor(v_np)
    return s, u, v

class NumpySvd(NumpyCommon):
    def construct(self, input, full_matrices=False, compute_uv=True):
        if compute_uv:
            output = _svd_compute_uv(input, full_matrices)
        else:
            output = _svd_not_compute_uv(input, full_matrices)
        return output
    def bprop(self, input, full_matrices, compute_uv, out, dout):
        raise RuntimeError(_error_msg.format(self.op_name))

class NumpySvdvals(NumpyCommon):
    def construct(self, input, full_matrices=False):
        output = _svd_not_compute_uv(input, full_matrices)
        return output
    def bprop(self, input, full_matrices, out, dout):
        raise RuntimeError(_error_msg.format(self.op_name))

class NumpyI0(NumpyCommon):
    def construct(self, A):
        if A.dtype in msdapter_dtype.all_int_type:
            A = A.astype(ms.float32)
        A_np = A.asnumpy()
        output = ms.Tensor(np.i0(A_np))
        return output
    def bprop(self, A, out, dout):
        raise RuntimeError(_error_msg.format(self.op_name))

class NumpyLU(NumpyCommon):
    def construct(self, A, pivot):
        A_np = A.asnumpy()
        output = lu(A_np, permute_l=False, overwrite_a=False, check_finite=True)
        p = ms.Tensor(output[0]).astype(A.dtype)
        l = ms.Tensor(output[1])
        u = ms.Tensor(output[2])
        output = (p, l, u) if pivot else (l, u)
        return output
    def bprop(self, A, pivot, out, dout):
        raise RuntimeError(_error_msg.format(self.op_name))

class NumpyLUSolve(NumpyCommon):
    def construct(self, B, LU, pivots, adjoint=False):
        B_np = B.asnumpy()
        LU_np = LU.asnumpy()
        pivots = pivots.asnumpy() - 1
        trans = 2 if adjoint else 0
        A = (LU_np, pivots)
        output = lu_solve(A, B_np, trans)
        return ms.Tensor(output)
    def bprop(self, B, LU, pivots, adjoint, out, dout):
        raise RuntimeError(_error_msg.format(self.op_name))

class NumpyLUFactor(NumpyCommon):
    def construct(self, A):
        A_np = A.asnumpy()
        output = lu_factor(A_np, overwrite_a=False, check_finite=True)
        lu = ms.Tensor(output[0])
        pivots = ms.Tensor(output[1]) + 1
        return lu, pivots
    def bprop(self, A, out, dout):
        raise RuntimeError(_error_msg.format(self.op_name))

class NumpyEigh(NumpyCommon):
    def construct(self, A, lower=True, eigvals_only=True):
        A_np = A.asnumpy()
        UPLO = 'L' if lower else 'U'
        output = np.linalg.eigh(A_np, UPLO=UPLO)
        return ms.Tensor(output[0]) if eigvals_only else (ms.Tensor(output[0]), ms.Tensor(output[1]))
    def bprop(self, A, lower, eigvals_only, out, dout):
        raise RuntimeError(_error_msg.format(self.op_name))

class NumpyFmax(NumpyCommon):
    def construct(self, input, other):
        input = input.asnumpy()
        other = other.asnumpy()
        output = ms.Tensor(np.fmax(input, other))
        return output
    def bprop(self, input, other, out, dout):
        raise RuntimeError(_error_msg.format(self.op_name))

class NumpyFmin(NumpyCommon):
    def construct(self, input, other):
        input = input.asnumpy()
        other = other.asnumpy()
        output = ms.Tensor(np.fmin(input, other))
        return output
    def bprop(self, input, other, out, dout):
        raise RuntimeError(_error_msg.format(self.op_name))

class NumpyFft(NumpyCommon):
    def construct(self, input, n, dim, norm):
        input = input.asnumpy()
        output = np.fft.fft(input, n, axis=dim, norm=norm)
        if input.dtype not in (np.float64, np.complex128):
            output = output.astype(np.complex64)
        return ms.Tensor(output)
    def bprop(self, input, n, dim, norm, out, dout):
        raise RuntimeError(_error_msg.format(self.op_name))

class NumpyRfft(NumpyCommon):
    def construct(self, input, n, dim, norm):
        input = input.asnumpy()
        output = np.fft.rfft(input, n, axis=dim, norm=norm)
        if input.dtype not in (np.float64, np.complex128):
            output = output.astype(np.complex64)
        return ms.Tensor(output)
    def bprop(self, input, n, dim, norm, out, dout):
        raise RuntimeError(_error_msg.format(self.op_name))

class NumpySolve(NumpyCommon):
    def construct(self, A, B):
        A_np = A.asnumpy()
        B_np = B.asnumpy()
        output = ms.Tensor(np.linalg.solve(A_np, B_np))
        return output
    def bprop(self, A, B, out, dout):
        raise RuntimeError(_error_msg.format(self.op_name))

class NumpyPoisson(NumpyCommon):
    def construct(self, input):
        input_np = input.asnumpy()
        output = ms.Tensor.from_numpy(np.random.poisson(input_np, None)).to(dtype=input.dtype)
        return output
    def bprop(self, input, out, dout):
        raise RuntimeError(_error_msg.format(self.op_name))
