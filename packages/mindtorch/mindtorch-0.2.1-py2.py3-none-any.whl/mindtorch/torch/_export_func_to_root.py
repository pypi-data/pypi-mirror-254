import sys
from mindtorch.torch.tensor import Tensor

this_module = sys.modules['mindtorch.torch']

nn_func_modules = sys.modules['mindtorch.torch.nn.functional']
nn_func_list = dir(nn_func_modules)
# nn_func_black_list contains functions that are in 'nn.funtional.xxx' but not in 'torch.xxx'.
nn_func_black_list = ['relu', 'sigmoid', 'softmax', 'tanh', 'unfold', 'adaptive_avg_pool2d', 'adaptive_avg_pool3d',
                      'adaptive_max_pool2d', 'adaptive_max_pool3d', 'affine_grid', 'all_float_and_complex_type',
                      'all_int_type', 'avg_pool2d', 'avg_pool3d', 'binary_cross_entropy', 'cast_to_adapter_tensor',
                      'cast_to_ms_tensor', 'cross_entropy', 'dropout1d', 'dropout2d', 'dropout3d', 'elu', 'elu_',
                      'fold', 'fractional_max_pool2d', 'fractional_max_pool3d', 'gaussian_nll_loss', 'gelu',
                      'get_broadcast_shape', 'glu', 'graph_mode_condition', 'grid_sample', 'graph_mode_condition',
                      'grid_sample', 'gumbel_softmax', 'hardsigmoid', 'hardswish', 'hardtanh', 'hardtanh_',
                      'huber_loss', 'interpolate', 'is_under_ascend_context', 'is_under_gpu_context',
                      'l1_loss', 'leaky_relu_', 'linear', 'local_response_norm', 'logsigmoid', 'lp_pool1d',
                      'lp_pool2d', 'max_unpool1d', 'max_unpool2d', 'max_unpool3d', 'mish', 'ms', 'mse_loss',
                      'multi_head_attention_forward', 'multi_margin_loss', 'multilabel_margin_loss',
                      'multilabel_soft_margin_loss', 'nll_loss', 'normalize', 'np', 'one_hot', 'pad', 'pi',
                      'pixel_unshuffle', 'relu6', 'silu', 'smooth_l1_loss', 'soft_margin_loss', 'soft_margin_loss',
                      'softmin', 'softplus', 'softshrink', 'softsign', 'tanhshrink', 'unsupported_attr',
                      'triplet_margin_with_distance_loss', 'upsample', 'upsample_bilinear', 'upsample_nearest',
                      'warnings']

def export_nn_func():
    for func_name in nn_func_list:
        # four cases that func will not be exported:
        # 1. internal func                          --`func_name.startswith('_')`
        # 2. func in 'nn_func_black_list'           --`func_name not in nn_func_black_list`
        # 3. func has been exported to this module  --`getattr(this_module, func_name, None) is None`
        # 4. func is not type of function           --`hasattr(func, '__call__')`
        if not func_name.startswith('_') and func_name not in nn_func_black_list \
            and getattr(this_module, func_name, None) is None:
            func = getattr(nn_func_modules, func_name)
            if func is not None and hasattr(func, '__call__'):
                setattr(this_module, func_name, func)

tensor_func_list = dir(Tensor)
# tensor_fun_black_list contains functions that are in 'tensor.xxx' but not in 'torch.xxx'
tensor_fun_black_list = ['hardshrink', 'log_softmax', 'relu', 'sigmoid', 'softmax', 'tanh',
                         'absolute_', 'adapter_flag', 'add_', 'addbmm_', 'addcdiv_', 'addcmul_', 'addr_', 'adjoint',
                         'aminmax', 'apply_', 'approximiate_equal', 'arctan2', 'arctan2_', 'argmax_with_value',
                         'argmin_with_value', 'argwhere', 'asnumpy', 'asnumpy_of_slice_persistent_data',
                         'assign_value', 'assign_value_cpp', 'astype', 'atan2_', 'backward', 'baddbmm_',
                         'bernoulli_', 'bitwise_and_', 'bitwise_left_shift', 'bitwise_left_shift_', 'bitwise_not_',
                         'bitwise_or_', 'bitwise_right_shift', 'bitwise_right_shift_', 'bitwise_xor_',
                         'broadcast_to', 'byte', 'cauchy', 'cauchy_', 'char', 'choose', 'col2im', 'conj_physical',
                         'conj_physical_', 'const_arg', 'contiguous', 'copy', 'copy_', 'copy_adapter', 'copysign',
                         'copysign_', 'corrcoef', 'cov', 'cpu', 'cumprod_', 'cumsum_', 'data', 'data_sync',
                         'delta_seed', 'diagonal_scatter', 'diff', 'digamma_', 'dim', 'div_', 'divide_',
                         'dsplit', 'eigvals', 'element_size', 'eq_', 'erfinv_', 'expand', 'expand_as', 'expand_dims',
                         'exponential_', 'fill', 'fill_adapter', 'fill_diagonal', 'fill_diagonal_', 'fills',
                         'float_power', 'float_power_', 'floor_divide_', 'flush_from_cache', 'fmax', 'fmin', 'fmod_',
                         'fold', 'frexp', 'gather_elements', 'gather_nd', 'ge_', 'geometric_', 'getitem_index_info',
                         'grad', 'greater_', 'greateer_equal_', 'gt_', 'has_init', 'histogram', 'hsplit', 'hypot_',
                         'igamma', 'igamma_', 'igammac', 'igammac_', 'index_add_', 'index_copy_', 'index_fill_',
                         'index_of_parent_', 'index_reduce', 'index_reduce_', 'init', 'init_data', 'init_finished',
                         'init_flag', 'inner', 'inplace_update', 'inv', 'invert', 'is_conj', 'is_cuda', 'is_init',
                         'is_neg', 'is_persistent_data', 'is_quantized', 'item', 'itemset', 'itemsize', 'ldexp',
                         'ldexp_', 'le_', 'lerp_', 'less_', 'less_equal_', 'lgamma_', 'log_matrix_determinant',
                         'log_normal', 'log_normal_', 'logical_and_', 'logical_not_', 'logical_or_', 'logical_xor_',
                         'lt_', 'mH', 'mT', 'map_', 'masked_fill_', 'masked_scatter_', 'matrix_determinant',
                         'moveaxis', 'msort', 'mul_', 'multiply_', 'mvlgamma_', 'nan_to_num', 'nan_to_num_',
                         'nanmean', 'nanmedian', 'narrow_copy', 'nbytes', 'ndim', 'ndimension', 'ne_', 'nelement',
                         'new', 'new_empty', 'new_full', 'new_ones', 'new_tensor', 'new_zeros', 'nextafter_',
                         'normal_adapter', 'not_equal_', 'numpy', 'offload', 'offload_file_path', 'param_info',
                         'parent_tensor_', 'permute', 'persistent_data_from_numpy', 'polygamma_', 'positive',
                         'pow_', 'ptp', 'put_', 'random_', 'random_adapter', 'random_categorical', 'ravel',
                         'remainder_', 'renorm_', 'repeat', 'requires_grad', 'requires_grad_', 'reshape_as',
                         'resize', 'resize_', 'resize_as', 'resolve_conj', 'resolve_neg', 'reverse',
                         'reverse_sequence', 'scatter_', 'scatter_add_', 'scatter_div', 'scatter_max',
                         'scatter_min', 'scatter_mul', 'scatter_reduce', 'scatter_reduce_', 'scatter_sub',
                         'select_scatter', 'set_cast_dtype', 'set_const_arg', 'set_dtype', 'set_init_flag',
                         'setitem_index_info', 'sgn_', 'shape', 'sign_', 'sinc', 'sinc_', 'size',
                         'slice_num_of_persistent_data', 'slice_num_of_persistent_data_', 'slice_scatter',
                         'slice_shape_of_persistent_data', 'slice_shape_of_persistent_data_', 'soft_shrink',
                         'squeeze_', 'stride', 'stride', 'strides', 'stub', 'stub_sync', 'sub_', 'subtract_',
                         'sum_to_size', 'swapaxes', 'swapdims', 't_', 'take_along_dim', 'tensor_split', 'tile',
                         'to', 'to_coo', 'to_csr', 'tolist', 'top_k', 'transpose_', 'tril_', 'true_divide_',
                         'type_as', 'unflatten', 'unfold', 'uniform_', 'uniform_adapter', 'unique_with_pad',
                         'unsorted_segment_max', 'unsorted_segment_min', 'unsorted_segment_prod', 'unsqueeze_',
                         'value', 'view', 'view_as', 'virtual_flag', 'vsplit', 'xdivy', 'xlogy', 'xlogy_',
                         'zero_adapter', 'type']


def warp_tensor_ops(func_name):
    def wrap_tensor_func_to_torch(tensor, *args, **kwargs):
        return getattr(tensor, func_name)(*args, **kwargs)
    return wrap_tensor_func_to_torch

def export_tensor_func():
    for func_name in tensor_func_list:
        # four cases that func will not be exported:
        # 1. internal func                          --`func_name.startswith('_')`
        # 2. func in 'tensor_fun_black_list'        --`func_name not in tensor_fun_black_list`
        # 3. func has been exported to this module  --`getattr(this_module, func_name, None) is None`
        # 4. func is not type of function           --`hasattr(func, '__call__')`
        if not func_name.startswith('_') and func_name not in tensor_fun_black_list \
            and getattr(this_module, func_name, None) is None:
            func = getattr(Tensor, func_name, None)
            if func is not None and hasattr(func, '__call__'):
                setattr(this_module, func_name, warp_tensor_ops(func_name))

def _export_func_to_root():
    # Can not change order between 'export_nn_func()' and 'export_tensor_func()'.
    # Because it can achieve: the functions with the same name as in 'nn.functional' in 'tensor' will not
    # be exported repeatedly, so functions with the same name in 'nn.functional' will not be overwritten.
    export_nn_func()
    export_tensor_func()
