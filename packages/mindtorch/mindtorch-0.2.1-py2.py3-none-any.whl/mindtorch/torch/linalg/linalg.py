#!/usr/bin/env python
# -*- coding: utf-8 -*-

import mindspore as ms
from mindspore.ops.primitive import _primexpr
from mindspore.ops._primitive_cache import _get_cache_prim
from mindspore.scipy.ops import SolveTriangular
from mindtorch.torch.common._inner import _out_inplace_assign
from mindtorch.utils import unsupported_attr, pynative_mode_condition, \
                             is_under_gpu_context, is_under_ascend_context, set_multiple_name_tuple
from mindtorch.torch.tensor import cast_to_ms_tensor, cast_to_adapter_tensor, custom_matmul
from mindtorch.torch.tensor import Tensor as adapter_tensor
from mindtorch.torch.common.dtype import finfo
import mindtorch.torch._register_numpy_primitive  as numpy_cell


def eigh(A, UPLO='L', *, out=None): # TODO use numpy api now
    lower = bool(UPLO == 'L')
    eigh_op = numpy_cell.NumpyEigh('eigh')
    output = eigh_op(A, lower, False)
    return _out_inplace_assign(out, output, "eigh")

def solve(A, B, *, left=True, out=None):# TODO use numpy api now
    unsupported_attr(left)
    solve_op = numpy_cell.NumpySolve('solve')
    output = solve_op(A, B)
    return _out_inplace_assign(out, output, "solve")

#TODO: eig currently not support on GPU
def eig(A, *, out=None):
    if is_under_gpu_context():
        raise NotImplementedError("for adapter, eig not supported on GPU")
    input_ms = cast_to_ms_tensor(A)
    output = ms.ops.eig(input_ms)
    return _out_inplace_assign(out, output, "eig")

def slogdet(A, *, out=None):
    A = cast_to_ms_tensor(A)
    sign, output = ms.ops.slogdet(A)
    return _out_inplace_assign(out, (sign, output), "slogdet")

def det(A, *, out=None):
    A = cast_to_ms_tensor(A)
    output = ms.ops.det(A)
    return _out_inplace_assign(out, output, "det")

def cholesky(A, *, upper=False, out=None):
    # TODO: ms.ops.cholesky to support complex type
    A = cast_to_ms_tensor(A)
    output = ms.ops.cholesky(A, upper)
    return _out_inplace_assign(out, output, "cholesky")

def cholesky_ex(A, *, upper=False, check_errors=False, out=None):
    #TODO: currently cholesky_ex not support check_errors=True
    # TODO: ms.ops.cholesky to support complex type
    if check_errors:
        raise NotImplementedError("cholesky_ex currently not supported check_errors=True")
    A = cast_to_ms_tensor(A)
    if A.ndim > 2:
        info = ms.ops.zeros(A.shape[:-2], dtype=ms.int32)
    else:
        info = 0
    output = ms.ops.cholesky(A, upper)
    output = (output, info)
    return _out_inplace_assign(out, output, "cholesky_ex")

def inv(A, *, out=None):
    A = cast_to_ms_tensor(A)
    output = ms.ops.inverse(A)
    return _out_inplace_assign(out, output, "inv")

def inv_ex(A, *, check_errors=False, out=None):
    #TODO: currently inv_ex not support check_errors=True
    if check_errors:
        raise NotImplementedError("inv_ex currently not supported check_errors=True")
    A = cast_to_ms_tensor(A)
    if A.ndim > 2:
        info = ms.ops.zeros(A.shape[:-2], dtype=ms.int32)
    else:
        info = 0
    output = ms.ops.inverse(A)
    output = (output, info)
    return _out_inplace_assign(out, output, "inv_ex")

def matmul(input, other, *, out=None):
    input_ms = cast_to_ms_tensor(input)
    other = cast_to_ms_tensor(other)
    # TODO: repalce with output = ms.ops.matmul(input_ms, other)
    output = custom_matmul(input_ms, other)
    return _out_inplace_assign(out, output, "matmul")

def diagonal(A, *, offset=0, dim1=-2, dim2=-1):
    A = cast_to_ms_tensor(A)
    output = ms.ops.diagonal(A, offset=offset, dim1=dim1, dim2=dim2)
    return cast_to_adapter_tensor(output)

def multi_dot(tensors, *, out=None):
    input_ms = cast_to_ms_tensor(tensors)
    output = ms.numpy.multi_dot(input_ms)
    return _out_inplace_assign(out, output, "multi_dot")

def householder_product(A, tau, *, out=None):
    input_ms = cast_to_ms_tensor(A)
    input2 = cast_to_ms_tensor(tau)
    output = ms.ops.orgqr(input_ms, input2)
    return _out_inplace_assign(out, output, "householder_product")

#TODO: Currently not support 3-D (*, M, N) input
def lu(A, *, pivot=True, out=None):
    lu_op = numpy_cell.NumpyLU('lu')
    output = lu_op(A, pivot)
    return _out_inplace_assign(out, output, "lu")

#TODO: Currently not support 3-D (*, M, N) input
def lu_factor(A, *, pivot=True, out=None):
    #TODO: Mindspore does not support pivot=False condition
    if not pivot:
        raise NotImplementedError("lu_factor currently not supported pivot=False")
    lu_factor_op = numpy_cell.NumpyLUFactor('lu_factor')
    output = lu_factor_op(A)
    return _out_inplace_assign(out, output, "lu_factor")

#TODO: Currently not support 3-D (*, M, N) input
#TODO: currently lu_factor not support check_errors
def lu_factor_ex(A, *, pivot=True, check_errors=False, out=None):
    #TODO: Mindspore does not support pivot=False condition
    if not pivot:
        raise NotImplementedError("lu_factor_ex currently not supported pivot=False")
    if check_errors:
        raise NotImplementedError("lu_factor_ex currently not supported check_errors=True")
    lu_factor_ex_op = numpy_cell.NumpyLUFactor('lu_factor_ex')
    lu, pivots = lu_factor_ex_op(A)
    output = (lu, pivots, 0)
    return _out_inplace_assign(out, output, "lu_factor_ex")

def lu_solve(B, LU, pivots, *, left=True, adjoint=False, out=None):
    #TODO: Currently does not support left
    if not left:
        raise NotImplementedError("lu_solve currently not supported left=False")
    lu_solve_op = numpy_cell.NumpyLUSolve('lu_solve')
    output = lu_solve_op(B, LU, pivots, adjoint=adjoint)
    return _out_inplace_assign(out, output, "lu_solve")

def lstsq(a, b, rcond=None, *, out=None):
    lstsq_op = numpy_cell.NumpyFullLstsq('lstsq', rcond)
    x, residuals, rank, s = lstsq_op(a, b)
    rank = int(rank)
    return _out_inplace_assign(out, (x, residuals, rank, s), "lstsq")

def qr(input, mode="reduced", *, out=None):
    input_ms = cast_to_ms_tensor(input)
    output = ms.ops.qr(input_ms, mode)
    return _out_inplace_assign(out, output, "qr")

def vander(x, N=None, *, out=None):
    x = cast_to_ms_tensor(x)
    #TODO: ms.ops.vander() result == increasing=False
    output = ms.numpy.vander(x, N, increasing=True)
    return _out_inplace_assign(out, output, "vander")

def eigvals(A, *, out=None):
    A = cast_to_ms_tensor(A)
    #TODO: eigvals currently not support
    if not is_under_gpu_context():
        output, _ = ms.ops.eig(A)
    else:
        #TODO: not support backward
        eigvals_op = numpy_cell.NumpyEigvals('eigvals')
        output = eigvals_op(A)
        if A.dtype in (ms.float64, ms.complex128):
            output = output.astype(ms.complex128)
    return _out_inplace_assign(out, output, "eigvals")

def svd(A, full_matrices=True, *, driver=None, out=None):
    #TODO: not support driver is not None
    if driver is not None:
        raise NotImplementedError("Currently only support driver equals to none")
    input_ms = cast_to_ms_tensor(A)
    if is_under_ascend_context():
        svd_op = numpy_cell.NumpySvd('svd')
        s, u, v = svd_op(input_ms, full_matrices)
    else:
        s, u, v = ms.ops.svd(input_ms, full_matrices=full_matrices)
    v = ms.ops.swapaxes(v, -1, -2)
    output = (u, s, v)
    if pynative_mode_condition():
        svd_namedtuple = set_multiple_name_tuple('svd', 'U, S, Vh')
        output = svd_namedtuple(cast_to_adapter_tensor(u), cast_to_adapter_tensor(s), cast_to_adapter_tensor(v))
        return output
    return _out_inplace_assign(out, output, "svd")

def svdvals(A, *, driver=None, out=None):
    #TODO: not support driver is not None
    if driver is not None:
        raise NotImplementedError("Currently only support driver equals to none")
    input_ms = cast_to_ms_tensor(A)
    if is_under_ascend_context():
        svdvals_op = numpy_cell.NumpySvdvals('svdvals')
        output = svdvals_op(input_ms)
    else:
        output = ms.ops.svd(input_ms, compute_uv=False)
    return _out_inplace_assign(out, output, "svdvals")

def matrix_power(input, n, *, out=None):
    input_ms = cast_to_ms_tensor(input)
    input_type = input_ms.dtype
    if input_type not in (ms.float32, ms.float16):
        input_ms = input_ms.astype(ms.float32)
    if not is_under_gpu_context():
        output = ms.ops.matrix_power(input_ms, n)
    else:
        #TODO: used ops func on GPU
        output = ms.numpy.matrix_power(input_ms, n)
    if input_type not in (ms.float32, ms.float16):
        output = output.astype(input_type)
    return _out_inplace_assign(out, output, "matrix_power")

#TODO: pinv currently not support on Ascend
def pinv(A, *, atol=None, rtol=None, hermitian=False, out=None):
    if is_under_ascend_context():
        raise NotImplementedError("pinverse currently not supported on Ascend")
    A = cast_to_ms_tensor(A)
    output = ms.ops.pinv(A, atol=atol, rtol=rtol, hermitian=hermitian)
    return _out_inplace_assign(out, output, "pinv")

def eigvalsh(A, UPLO='L', *, out=None):
    A = cast_to_ms_tensor(A)
    lower = bool(UPLO == 'L')
    eigvalsh_op = numpy_cell.NumpyEigh('eigvalsh')
    output = eigvalsh_op(A, lower, True)
    if output.dtype in (ms.complex64, ms.complex128):
        output = output.real()
    return _out_inplace_assign(out, output, "eigvalsh")

def norm(A, ord=None, dim=None, keepdim=False, *, out=None, dtype=None):
    A = cast_to_ms_tensor(A)
    output = ms.ops.norm(A, ord=ord, dim=dim, keepdim=keepdim, dtype=dtype)
    output = output.astype(A.dtype)
    return _out_inplace_assign(out, output, "norm")

def vector_norm(A, ord=2, dim=None, keepdim=False, *, dtype=None, out=None):
    A = cast_to_ms_tensor(A)
    if dim is None:
        A = A.flatten()
    output = ms.ops.norm(A, ord=ord, dim=dim, keepdim=keepdim, dtype=dtype)
    return _out_inplace_assign(out, output, "vector_norm")

@_primexpr
# @lru_cache(_GLOBAL_LRU_CACHE_SIZE)
def _check_vecdot_input_validity(x, y, dim):
    if not isinstance(x, adapter_tensor) or not isinstance(y, adapter_tensor):
        raise TypeError("For vecdot, x or y must be Tensor.")
    if not isinstance(dim, int):
        raise TypeError(f"For vecdot, the dim should be int, but got {type(dim)}.")
    ndim = x.ndim if x.ndim > y.ndim else y.ndim
    if dim < -ndim or dim >= ndim:
        raise ValueError("For vecdot, the dim is out of range.")

# TODO: vecdot is only supported in torch2.0
def vecdot(x, y, *, dim=- 1, out=None):
    _check_vecdot_input_validity(x, y, dim)
    x = cast_to_ms_tensor(x)
    y = cast_to_ms_tensor(y)
    if x.dtype == ms.complex64 or x.dtype == ms.complex128:
        x = x.conj()
    output = x * y
    output = output.sum(axis=dim)
    return _out_inplace_assign(out, output, "vecdot")

def matrix_norm(A, ord='fro', dim=(-2, -1), keepdim=False, *, dtype=None, out=None):
    # `p` can not support value beside ['fro', 'nuc', inf, -inf, 0, 1, -1, 2, -2]
    A = cast_to_ms_tensor(A)
    if dtype is None:
        dtype = A.dtype
    output = ms.ops.matrix_norm(A, ord=ord, axis=dim, keepdims=keepdim, dtype=dtype)
    output = output.astype(dtype)
    return _out_inplace_assign(out, output, "matrix_norm")

def matrix_rank(A, *, atol=None, rtol=None, hermitian=False, out=None):
    #TODO: If hermitian=True, torch will check whether the input A is a hermitian tensor, which is difficult in ms
    unsupported_attr(hermitian)
    A = cast_to_ms_tensor(A)
    s = svdvals(A)
    if atol is None:
        atol = finfo(s.dtype).eps * max(A.shape)
    if rtol is None:
        rtol = finfo(s.dtype).eps
    s1, _ = ms.ops.max(s)
    s1 = s1.float()
    tol = max(atol, rtol * s1)
    output = ms.ops.sum((s > tol).astype(ms.int64), dim=-1)
    return _out_inplace_assign(out, output, "matrix_rank")

def cross(input, other, *, dim=-1, out=None):
    if is_under_gpu_context():
        raise NotImplementedError("cross currently not supported on GPU")
    input_ms = cast_to_ms_tensor(input)
    other = cast_to_ms_tensor(other)
    output = ms.ops.cross(input_ms, other, dim)
    return _out_inplace_assign(out, output, "cross")

def solve_triangular(A, B, *, upper, left=True, unitriangular=False, out=None):
    if is_under_ascend_context():
        raise NotImplementedError("solve_triangular currently not supported on Ascend")
    if not left:
        raise NotImplementedError("Currently only support left equals to True")
    A = cast_to_ms_tensor(A)
    B = cast_to_ms_tensor(B)
    solve_op = _get_cache_prim(SolveTriangular)(lower=(not upper), unit_diagonal=unitriangular)
    output = solve_op(A, B)
    return _out_inplace_assign(out, output, "solve_triangular")

def cond(A, p=None, *, out=None):
    A = cast_to_ms_tensor(A)
    if A.dtype in (ms.float64, ms.complex128):
        output = ms.ops.cond(A, p).astype(ms.float64)
    else:
        output = ms.ops.cond(A, p).astype(ms.float32)
    return _out_inplace_assign(out, output, "cond")
