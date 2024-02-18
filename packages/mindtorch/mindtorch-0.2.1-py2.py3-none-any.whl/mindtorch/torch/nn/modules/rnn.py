#!/usr/bin/env python
# -*- coding: utf-8 -*-
import numbers
import math

import mindspore as ms
from mindspore.nn.layer.rnns import _DynamicRNNRelu, _DynamicRNNTanh, _DynamicLSTMCPUGPU, _DynamicLSTMAscend, \
                                    _DynamicGRUAscend, _DynamicGRUCPUGPU
from mindspore.nn.layer.rnn_cells import _rnn_tanh_cell, _rnn_relu_cell, _lstm_cell, _gru_cell
from mindspore.ops._primitive_cache import _get_cache_prim

from mindtorch.torch.nn.modules.module import Module
from mindtorch.torch.tensor import cast_to_ms_tensor, cast_to_adapter_tensor
from mindtorch.torch.nn.parameter import Parameter
from mindtorch.torch.functional import empty, zeros
from mindtorch.torch.nn import init
from mindtorch.utils import unsupported_attr, is_under_ascend_context
from mindtorch.torch.nn.utils.rnn import PackedSequence, pad_packed_sequence
from mindtorch.torch.logging import warning

def _apply_permutation(tensor, permutation, dim=1):
    return tensor.index_select(dim, permutation)

class RNNBase(Module):
    def __init__(self, mode, input_size, hidden_size,
                 num_layers=1, bias=True, batch_first=False,
                 dropout=0., bidirectional=False, proj_size=0,
                 device=None, dtype=None):
        unsupported_attr(device)
        super(RNNBase, self).__init__()
        self.mode = mode
        self.input_size = input_size
        self.hidden_size = hidden_size
        self.num_layers = num_layers
        self.bias = bias
        self.batch_first = batch_first
        self.dropout = float(dropout)
        self.bidirectional = bidirectional
        self.proj_size = proj_size
        self.num_directions = 2 if bidirectional else 1

        if not isinstance(dropout, numbers.Number) or not 0 <= dropout <= 1 or \
                isinstance(dropout, bool):
            raise ValueError("dropout should be a number in range [0, 1] "
                             "representing the probability of an element being "
                             "zeroed")
        if dropout > 0 and num_layers == 1:
            warning("dropout option adds dropout after all but last " \
                    "recurrent layer, so non-zero dropout expects " \
                    "num_layers greater than 1, but got dropout={} and " \
                    "num_layers={}".format(dropout, num_layers))
        if proj_size < 0:
            raise ValueError("proj_size should be a positive integer or zero to disable projections")
        if proj_size >= hidden_size:
            raise ValueError("proj_size has to be smaller than hidden_size")

        if mode == 'LSTM':
            gate_size = 4 * hidden_size
        elif mode == 'GRU':
            if is_under_ascend_context() and hidden_size % 16 != 0:
                raise ValueError(f"GRU on ascend do not support hidden size that is not divisible by 16, "
                                 f"but get hidden size {hidden_size}, please reset the argument.")
            gate_size = 3 * hidden_size
        elif mode == 'RNN_TANH':
            gate_size = hidden_size
        elif mode == 'RNN_RELU':
            gate_size = hidden_size
        else:
            raise ValueError("Unrecognized RNN mode: " + mode)

        self._flat_weights_names = []
        self._all_weights = []
        for layer in range(num_layers):
            for direction in range(self.num_directions):
                real_hidden_size = proj_size if proj_size > 0 else hidden_size
                layer_input_size = input_size if layer == 0 else real_hidden_size * self.num_directions

                w_ih = Parameter(empty((gate_size, layer_input_size), dtype=dtype))
                w_hh = Parameter(empty((gate_size, real_hidden_size), dtype=dtype))
                b_ih = Parameter(empty(gate_size, dtype=dtype))
                b_hh = Parameter(empty(gate_size, dtype=dtype))
                layer_params = ()
                if self.proj_size == 0:
                    if bias:
                        layer_params = (w_ih, w_hh, b_ih, b_hh)
                    else:
                        layer_params = (w_ih, w_hh)
                else:
                    w_hr = Parameter(empty((proj_size, hidden_size), dtype=dtype))
                    if bias:
                        layer_params = (w_ih, w_hh, b_ih, b_hh, w_hr)
                    else:
                        layer_params = (w_ih, w_hh, w_hr)

                suffix = '_reverse' if direction == 1 else ''
                param_names = ['weight_ih_l{}{}', 'weight_hh_l{}{}']
                if bias:
                    param_names += ['bias_ih_l{}{}', 'bias_hh_l{}{}']
                if self.proj_size > 0:
                    param_names += ['weight_hr_l{}{}']
                param_names = [x.format(layer, suffix) for x in param_names]

                for name, param in zip(param_names, layer_params):
                    setattr(self, name, param)
                self._flat_weights_names.extend(param_names)
                self._all_weights.append(param_names)

        self._flat_weights = \
            [(lambda wn: getattr(self, wn) if hasattr(self, wn) else None)(wn) for wn in self._flat_weights_names]
        self.reset_parameters()

    def __setattr__(self, attr, value):
        if hasattr(self, "_flat_weights_names") and attr in self._flat_weights_names:
            # keep self._flat_weights up to date if you do self.weight = ...
            idx = self._flat_weights_names.index(attr)
            self._flat_weights[idx] = value
        super(RNNBase, self).__setattr__(attr, value)

    def flatten_parameters(self):
        # flatten_parameters is to register the _flat_weights to cudnn, for performance improvement.
        # However mindtorch has not support yet, so here do nothings.
        warning("'flatten_parameters' in RNN/GRU/LSTM do not actually take effect to improve performence. "
                "mindtorch has not supported yet.")

    def reset_parameters(self) -> None:
        stdv = 1.0 / math.sqrt(self.hidden_size) if self.hidden_size > 0 else 0
        for weight in self.parameters():
            init.uniform_(weight, -stdv, stdv)

    def check_input(self, input, batch_sizes):
        expected_input_dim = 2 if batch_sizes is not None else 3
        if input.ndim != expected_input_dim:
            raise RuntimeError(
                'input must have {} dimensions, got {}'.format(expected_input_dim, input.ndim))
        if self.input_size != input.shape[-1]:
            raise RuntimeError(
                'input.size(-1) must be equal to input_size. Expected {}, got {}'.format(
                    self.input_size, input.shape[-1]))

    def get_expected_hidden_size(self, input, batch_sizes, *, from_packed=False, is_batched=True):
        if batch_sizes is not None:
            mini_batch = int(batch_sizes[0])
        else:
            if not from_packed:
                if not is_batched:
                    # if not is_batched, it means mindtorch has expand dim on dim-1 as batch dim.
                    mini_batch = input.shape[1]
                else:
                    mini_batch = input.shape[0] if self.batch_first else input.shape[1]
            else:
                # if input is from packed_sequence, the input batch dim is always 1.
                mini_batch = input.shape[1]
        num_directions = 2 if self.bidirectional else 1
        if self.proj_size > 0:
            expected_hidden_size = (self.num_layers * num_directions,
                                    mini_batch, self.proj_size)
        else:
            expected_hidden_size = (self.num_layers * num_directions,
                                    mini_batch, self.hidden_size)
        return expected_hidden_size

    def check_hidden_size(self, hx, expected_hidden_size,
                          msg: str = 'Expected hidden size {}, got {}'):
        if hx.shape != expected_hidden_size:
            raise RuntimeError(msg.format(expected_hidden_size, list(hx.shape)))

    def check_forward_args(self, input, hidden, batch_sizes, *, from_packed=False, is_batched=True):
        self.check_input(input, batch_sizes)
        expected_hidden_size = self.get_expected_hidden_size(input,
                                                             batch_sizes,
                                                             from_packed=from_packed,
                                                             is_batched=is_batched)

        self.check_hidden_size(hidden, expected_hidden_size)

    def extra_repr(self):
        s = '{input_size}, {hidden_size}'
        if self.proj_size != 0:
            s += ', proj_size={proj_size}'
        if self.num_layers != 1:
            s += ', num_layers={num_layers}'
        if self.bias is not True:
            s += ', bias={bias}'
        if self.batch_first is not False:
            s += ', batch_first={batch_first}'
        if self.dropout != 0:
            s += ', dropout={dropout}'
        if self.bidirectional is not False:
            s += ', bidirectional={bidirectional}'
        return s.format(**self.__dict__)

    @property
    def all_weights(self):
        return [[getattr(self, weight) for weight in weights] for weights in self._all_weights]

    def __setstate__(self, d):
        super(RNNBase, self).__setstate__(d)
        if 'all_weights' in d:
            self._all_weights = d['all_weights']
        # In PyTorch 1.8 we added a proj_size member variable to LSTM.
        # LSTMs that were serialized via torch.save(module) before PyTorch 1.8
        # don't have it, so to preserve compatibility we set proj_size here.
        if 'proj_size' not in d:
            self.proj_size = 0

        if isinstance(self._all_weights[0][0], str):
            return
        num_layers = self.num_layers
        num_directions = 2 if self.bidirectional else 1
        self._flat_weights_names = []
        self._all_weights = []
        for layer in range(num_layers):
            for direction in range(num_directions):
                suffix = '_reverse' if direction == 1 else ''
                weights = ['weight_ih_l{}{}', 'weight_hh_l{}{}', 'bias_ih_l{}{}',
                           'bias_hh_l{}{}', 'weight_hr_l{}{}']
                weights = [x.format(layer, suffix) for x in weights]
                if self.bias:
                    if self.proj_size > 0:
                        self._all_weights += [weights]
                        self._flat_weights_names.extend(weights)
                    else:
                        self._all_weights += [weights[:4]]
                        self._flat_weights_names.extend(weights[:4])
                else:
                    if self.proj_size > 0:
                        self._all_weights += [weights[:2]] + [weights[-1:]]
                        self._flat_weights_names.extend(weights[:2] + [weights[-1:]])
                    else:
                        self._all_weights += [weights[:2]]
                        self._flat_weights_names.extend(weights[:2])
        self._flat_weights = \
            [(lambda wn: getattr(self, wn) if hasattr(self, wn) else None)(wn) for wn in self._flat_weights_names]

    def _get_weight_and_bias(self, num_directions, layer, bias):
        _param_nums_per_directions = 4 if bias else 2
        _param_nums_per_layer = num_directions * _param_nums_per_directions
        offset = _param_nums_per_layer * layer

        param = ()

        for _ in range(num_directions):
            if bias:
                param += tuple(self._flat_weights[offset:offset + _param_nums_per_directions])
            else:
                param += tuple(self._flat_weights[offset:offset + _param_nums_per_directions])
                param += (None, None)
            offset = offset + _param_nums_per_directions
        # cast parameter to ms.Tensor before call ms function.
        return cast_to_ms_tensor(param)

    def permute_hidden(self, hx, permutation):
        if permutation is None:
            return hx
        return _apply_permutation(hx, permutation)

    def _run_recurrent(self, input, hx, length=None):
        num_directions = 2 if self.bidirectional else 1

        pre_layer = input
        h_n = ()
        # For jit
        output = None

        if num_directions == 1:
            for i in range(self.num_layers):
                layer_params = self._get_weight_and_bias(num_directions, i, self.bias)
                output, h_t = self.rnn_cell(pre_layer, hx[i], length, *layer_params)
                h_n += (h_t,)

                pre_layer = ms.ops.dropout(output, self.dropout) \
                    if (self.dropout != 0 and i < self.num_layers - 1) else output
        else:
            for i in range(self.num_layers):
                layer_params = \
                    self._get_weight_and_bias(num_directions, i, self.bias)

                if length is None:
                    x_b = ms.ops.reverse(pre_layer, [0])
                else:
                    x_b = ms.ops.reverse_sequence(pre_layer, length, 0, 1)
                output, h_t = self.rnn_cell(pre_layer, hx[2 * i], length, *layer_params[0:4])
                output_b, h_t_b = self.rnn_cell(x_b, hx[2 * i + 1], length, *layer_params[4:])

                if length is None:
                    output_b = ms.ops.reverse(output_b, [0])
                else:
                    output_b = ms.ops.reverse_sequence(output_b, length, 0, 1)
                output = ms.ops.concat((output, output_b), 2)
                h_n += (h_t,)
                h_n += (h_t_b,)

                pre_layer = ms.ops.dropout(output, self.dropout) \
                    if (self.dropout != 0 and i < self.num_layers - 1) else output

        h_n = ms.ops.concat(h_n, 0)
        h_n = h_n.view(hx.shape)

        return output, h_n

    def _get_hx(self, input, hx, max_batch_size, is_batched, dtype, *, from_packed=False):
        num_directions = 2 if self.bidirectional else 1
        if hx is not None:
            hx = cast_to_ms_tensor(hx)
            if is_batched:
                if hx.ndim != 3:
                    raise RuntimeError(
                        f"For batched 3-D input, hx should also be 3-D but got {hx.ndim}-D tensor")
            else:
                if hx.ndim != 2:
                    raise RuntimeError(
                        f"For unbatched 2-D input, hx should also be 2-D but got {hx.ndim}-D tensor")
                hx = ms.ops.unsqueeze(hx, 1)
        else:
            hx = ms.ops.zeros((self.num_layers * num_directions,
                              max_batch_size, self.hidden_size),
                              dtype=dtype)
        self.check_forward_args(input, hx, None, from_packed=from_packed, is_batched=is_batched)
        return hx

    def _get_sequence_output(self, output, batch_sizes):
        num_directions = 2 if self.bidirectional else 1
        batch_sizes_tensor = ms.Tensor(batch_sizes)
        _masked = ms.ops.arange(output.shape[1])
        _masked = ms.ops.tile(_masked, (output.shape[0], 1))
        masked = _masked < batch_sizes_tensor[:, None]
        for _ in range(masked.ndim, output.ndim):
            masked = masked.unsqueeze(-1)
        masked = masked.broadcast_to(output.shape)
        output = ms.ops.masked_select(output, masked)
        _out_size = self.hidden_size if self.proj_size <= 0 else self.proj_size
        output = output.reshape(-1, _out_size * num_directions)
        return output

    def forward(self, input, hx=None):
        orig_input = input
        length = None
        # For jit
        sorted_indices = None
        unsorted_indices = None
        is_batched = None

        if isinstance(orig_input, PackedSequence):
            _, batch_sizes, sorted_indices, unsorted_indices = orig_input
            # mindspore can not process packed_sequence, should recover to normal tensor type
            input, length = pad_packed_sequence(orig_input, batch_first=False)
            input_ms = cast_to_ms_tensor(input)
            x_dtype = input_ms.dtype
            length = cast_to_ms_tensor(length)
            if sorted_indices is not None:
                input_ms = input_ms.index_select(1, ms.Tensor(sorted_indices))
                length = length.index_select(0, ms.Tensor(sorted_indices))

            if hx is None:
                hx = self._get_hx(input_ms, hx, input_ms.shape[1], True, x_dtype, from_packed=True)
            else:
                # Each batch of the hidden state should match the input sequence that
                # the user believes he/she is passing in.
                hx = cast_to_ms_tensor(hx)
                hx = self.permute_hidden(hx, sorted_indices)
                self.check_forward_args(input_ms, hx, None, from_packed=True)

            output, h_n = self._run_recurrent(input_ms, hx, length)

            output = self._get_sequence_output(output, batch_sizes)
            output = cast_to_adapter_tensor(output.astype(x_dtype))
            h_n = cast_to_adapter_tensor(h_n.astype(x_dtype))

            output_packed = PackedSequence(output, batch_sizes, sorted_indices, unsorted_indices)
            return output_packed, self.permute_hidden(h_n, unsorted_indices)

        batch_sizes = None
        input_ms = cast_to_ms_tensor(orig_input)
        x_dtype = input_ms.dtype

        if input_ms.ndim not in (2, 3):
            raise ValueError(f"Expected input to be 2-D or 3-D but received {input_ms.ndim}-D tensor")
        is_batched = input_ms.ndim == 3

        if not is_batched:
            # self.rnn_cell do not support batch-first, so can only unsuqeeze at second dimention.
            input_ms = ms.ops.unsqueeze(input_ms, 1)
            hx = self._get_hx(input_ms, hx, 1, is_batched, input_ms.dtype)
            output, h_n = self._run_recurrent(input_ms, hx)
            output = ms.ops.squeeze(output, 1)
            h_n = ms.ops.squeeze(h_n, 1)
        else:
            max_batch_size = input_ms.shape[0] if self.batch_first else input_ms.shape[1]
            hx = self._get_hx(input_ms, hx, max_batch_size, is_batched, input_ms.dtype)
            if self.batch_first:
                # self.rnn_cell do not support batch-first input, so need to transpose.
                input_ms = ms.ops.transpose(input_ms, (1, 0, 2))
                output, h_n = self._run_recurrent(input_ms, hx)
                output = ms.ops.transpose(output, (1, 0, 2))
            else:
                output, h_n = self._run_recurrent(input_ms, hx)

        return cast_to_adapter_tensor(output.astype(x_dtype)), cast_to_adapter_tensor(h_n.astype(x_dtype))

class RNN(RNNBase):
    def __init__(self, *args, **kwargs):
        if 'proj_size' in kwargs:
            raise ValueError("proj_size argument is only supported for LSTM, not RNN or GRU")
        self.nonlinearity = kwargs.pop('nonlinearity', 'tanh')
        if self.nonlinearity == 'tanh':
            mode = 'RNN_TANH'
        elif self.nonlinearity == 'relu':
            mode = 'RNN_RELU'
        else:
            raise ValueError("Unknown nonlinearity '{}'".format(self.nonlinearity))
        super(RNN, self).__init__(mode, *args, **kwargs)

        if mode == 'RNN_TANH':
            self.rnn_cell = _DynamicRNNTanh()
        elif mode == 'RNN_RELU':
            self.rnn_cell = _DynamicRNNRelu()

class GRU(RNNBase):
    def __init__(self, *args, **kwargs):
        if 'proj_size' in kwargs:
            raise ValueError("proj_size argument is only supported for LSTM, not RNN or GRU")

        super(GRU, self).__init__('GRU', *args, **kwargs)

        if is_under_ascend_context():
            self.rnn_cell = _DynamicGRUAscend()
        else:
            self.rnn_cell = _DynamicGRUCPUGPU()

def _lstm_proj_unit(inputs, hidden, w_ih, w_hh, b_ih, b_hh, w_hr):
    # ms.ops.matmul not support transpose input, and ms.ops.split do not support spilt to certain number.
    # so, here use ms.ops.MatMul and ms.ops.Split
    _matmul = _get_cache_prim(ms.ops.MatMul)(False, True)
    _spilt = _get_cache_prim(ms.ops.Split)(1, 4)
    hx, cx = hidden
    if b_ih is None:
        gates = _matmul(inputs, w_ih) + _matmul(hx, w_hh)
    else:
        gates = _matmul(inputs, w_ih) + _matmul(hx, w_hh) + b_ih + b_hh
    ingate, forgetgate, cellgate, outgate = _spilt(gates)

    ingate = ms.ops.sigmoid(ingate)
    forgetgate = ms.ops.sigmoid(forgetgate)
    cellgate = ms.ops.tanh(cellgate)
    outgate = ms.ops.sigmoid(outgate)

    cy = (forgetgate * cx) + (ingate * cellgate)
    hy = outgate * ms.ops.tanh(cy)

    hy = _matmul(hy, w_hr)

    return hy, cy

def _lstm_proj_recurrent(x, h_0, w_ih, w_hh, b_ih, b_hh, w_hr):
    time_step = x.shape[0]
    outputs = []
    t = 0
    h = h_0
    while t < time_step:
        x_t = x[t:t + 1:1]
        x_t = ms.ops.squeeze(x_t, 0)
        h = _lstm_proj_unit(x_t, h, w_ih, w_hh, b_ih, b_hh, w_hr)
        outputs.append(h[0])
        t += 1
    outputs = ms.ops.stack(outputs, 0)
    return outputs, h

def _lstm_proj_variable_recurrent(x, h, seq_length, w_ih, w_hh, b_ih, b_hh, w_hr):
    '''recurrent steps with sequence length'''
    time_step = x.shape[0]
    h_t = h
    proj_size = h[0].shape[-1]
    hidden_size = h[1].shape[-1]
    zero_output = ms.ops.zeros_like(h_t[0])

    h_seq_length = ms.ops.cast(seq_length, ms.float32)
    h_seq_length = ms.ops.broadcast_to(h_seq_length, (proj_size, -1))
    h_seq_length = ms.ops.cast(h_seq_length, ms.int32)
    h_seq_length = ms.ops.transpose(h_seq_length, (1, 0))

    c_seq_length = ms.ops.cast(seq_length, ms.float32)
    c_seq_length = ms.ops.broadcast_to(c_seq_length, (hidden_size, -1))
    c_seq_length = ms.ops.cast(c_seq_length, ms.int32)
    c_seq_length = ms.ops.transpose(c_seq_length, (1, 0))

    outputs = []
    state_t = h_t
    t = 0
    while t < time_step:
        x_t = x[t:t + 1:1]
        x_t = ms.ops.squeeze(x_t, 0)
        h_t = _lstm_proj_unit(x_t, state_t, w_ih, w_hh, b_ih, b_hh, w_hr)
        h_seq_cond = h_seq_length > t
        c_seq_cond = c_seq_length > t

        state_t_0 = ms.ops.select(h_seq_cond, h_t[0], state_t[0])
        state_t_1 = ms.ops.select(c_seq_cond, h_t[1], state_t[1])
        output = ms.ops.select(h_seq_cond, h_t[0], zero_output)
        state_t = (state_t_0, state_t_1)

        outputs.append(output)
        t += 1
    outputs = ms.ops.stack(outputs)
    return outputs, state_t

def _lstm_proj(x, h, seq_length, w_ih, w_hh, b_ih, b_hh, w_hr):
    x_dtype = x.dtype
    w_ih = w_ih.astype(x_dtype)
    w_hh = w_hh.astype(x_dtype)
    w_hr = w_hr.astype(x_dtype)
    if b_ih is not None:
        b_ih = b_ih.astype(x_dtype)
        b_hh = b_hh.astype(x_dtype)
    if seq_length is None:
        return _lstm_proj_recurrent(x, h, w_ih, w_hh, b_ih, b_hh, w_hr)
    return _lstm_proj_variable_recurrent(x, h, seq_length, w_ih, w_hh, b_ih, b_hh, w_hr)

class LSTM(RNNBase):
    def __init__(self, *args, **kwargs):
        super(LSTM, self).__init__('LSTM', *args, **kwargs)
        if is_under_ascend_context():
            self.lstm_cell = _DynamicLSTMAscend()
        else:
            self.lstm_cell = _DynamicLSTMCPUGPU()

        self.lstm_cell_proj= _lstm_proj

    def get_expected_cell_size(self, input, batch_sizes, *, from_packed=False, is_batched=True):
        if batch_sizes is not None:
            mini_batch = int(batch_sizes[0])
        else:
            if not from_packed:
                if not is_batched:
                    # if not is_batched, it means mindtorch has expand dim on dim-1 as batch dim.
                    mini_batch = input.shape[1]
                else:
                    mini_batch = input.shape[0] if self.batch_first else input.shape[1]
            else:
                # if input is from packed_sequence, the input batch dim is always 1.
                mini_batch = input.shape[1]
        num_directions = 2 if self.bidirectional else 1
        expected_hidden_size = (self.num_layers * num_directions,
                                mini_batch, self.hidden_size)
        return expected_hidden_size

    def check_forward_args(self, input, hidden, batch_sizes, *, from_packed=False, is_batched=True):
        self.check_input(input, batch_sizes)
        self.check_hidden_size(hidden[0], self.get_expected_hidden_size(input, batch_sizes, from_packed=from_packed,
                               is_batched=is_batched), 'Expected hidden[0] size {}, got {}')
        self.check_hidden_size(hidden[1], self.get_expected_cell_size(input, batch_sizes, from_packed=from_packed,
                               is_batched=is_batched), 'Expected hidden[1] size {}, got {}')

    def permute_hidden(self, hx, permutation):
        if permutation is None:
            return hx
        return _apply_permutation(hx[0], permutation), _apply_permutation(hx[1], permutation)

    def _get_weight_and_bias(self, num_directions, layer, bias, proj_size):
        if proj_size:
            _param_nums_per_directions = 5 if bias else 3
        else:
            _param_nums_per_directions = 4 if bias else 2
        _param_nums_per_layer = num_directions * _param_nums_per_directions
        offset = _param_nums_per_layer * layer

        param = ()

        for _ in range(num_directions):
            if bias:
                param += tuple(self._flat_weights[offset:offset + _param_nums_per_directions])
            else:
                param += tuple(self._flat_weights[offset:offset + 2])
                param += (None, None)
                param += tuple(self._flat_weights[offset + 2:offset+_param_nums_per_directions])
            offset = offset + _param_nums_per_directions

        # cast parameter to ms.Tensor before call ms function.
        return cast_to_ms_tensor(param)

    def _run_recurrent(self, input, hx, length=None):
        num_directions = 2 if self.bidirectional else 1

        pre_layer = input
        h_n = ()
        c_n = ()
        # For jit
        output = None

        if num_directions == 1:
            for i in range(self.num_layers):
                if self.proj_size:
                    layer_params = self._get_weight_and_bias(num_directions, i, self.bias, True)
                else:
                    layer_params = self._get_weight_and_bias(num_directions, i, self.bias, False)

                h_i = (hx[0][i], hx[1][i])

                if self.proj_size:
                    output, hc_t = self.lstm_cell_proj(pre_layer, h_i, length, *layer_params)
                else:
                    output, hc_t = self.lstm_cell(pre_layer, h_i, length, *layer_params)

                h_t, c_t = hc_t
                h_n += (h_t,)
                c_n += (c_t,)

                pre_layer = ms.ops.dropout(output, self.dropout) \
                    if (self.dropout != 0 and i < self.num_layers - 1) else output
        else:
            for i in range(self.num_layers):
                if self.proj_size > 0:
                    layer_params = self._get_weight_and_bias(num_directions, i, self.bias, True)
                else:
                    layer_params = self._get_weight_and_bias(num_directions, i, self.bias, False)

                x_b = ms.ops.reverse(pre_layer, [0])
                h_i = (hx[0][2 * i], hx[1][2 * i])
                h_b_i = (hx[0][2 * i + 1], hx[1][2 * i + 1])

                if length is None:
                    x_b = ms.ops.reverse(pre_layer, [0])
                else:
                    x_b = ms.ops.reverse_sequence(pre_layer, length, 0, 1)

                if self.proj_size > 0:
                    output, hc_t = self.lstm_cell_proj(
                        pre_layer, h_i, length, *layer_params[:5])
                    output_b, hc_t_b = self.lstm_cell_proj(
                        x_b, h_b_i, length, *layer_params[5:])
                else:
                    output, hc_t = self.lstm_cell(pre_layer, h_i, length, *layer_params[:4])
                    output_b, hc_t_b = self.lstm_cell(x_b, h_b_i, length, *layer_params[4:])

                if length is None:
                    output_b = ms.ops.reverse(output_b, [0])
                else:
                    output_b = ms.ops.reverse_sequence(output_b, length, 0, 1)

                output = ms.ops.concat((output, output_b), 2)
                h_t, c_t = hc_t
                h_t_b, c_t_b = hc_t_b
                h_n += (h_t,)
                h_n += (h_t_b,)
                c_n += (c_t,)
                c_n += (c_t_b,)

                pre_layer = ms.ops.dropout(output, self.dropout) \
                    if (self.dropout != 0 and i < self.num_layers - 1) else output

        h_n = ms.ops.concat(h_n, 0)
        h_n = h_n.view(hx[0].shape)
        c_n = ms.ops.concat(c_n, 0)
        c_n = c_n.view(hx[1].shape)

        return output, h_n, c_n

    def _get_hx(self, input, hx, max_batch_size,real_hidden_size, is_batched, dtype, *, from_packed=False):
        num_directions = 2 if self.bidirectional else 1
        if hx is None:
            h_zeros = ms.ops.zeros((self.num_layers * num_directions,
                                   max_batch_size, real_hidden_size),
                                   dtype=dtype)
            c_zeros = ms.ops.zeros((self.num_layers * num_directions,
                                   max_batch_size, self.hidden_size),
                                   dtype=dtype)
            hx = (h_zeros, c_zeros)
        else:
            hx = cast_to_ms_tensor(hx)
            if is_batched:
                if (hx[0].ndim != 3 or hx[1].ndim != 3):
                    msg = ("For batched 3-D input, hx and cx should "
                            f"also be 3-D but got ({hx[0].ndim}-D, {hx[1].ndim}-D) tensors")
                    raise RuntimeError(msg)
            else:
                if hx[0].ndim != 2 or hx[1].ndim != 2:
                    msg = ("For unbatched 2-D input, hx and cx should "
                            f"also be 2-D but got ({hx[0].ndim}-D, {hx[1].ndim}-D) tensors")
                    raise RuntimeError(msg)
                hx = (hx[0].unsqueeze(1), hx[1].unsqueeze(1))
        self.check_forward_args(input, hx, None, from_packed=from_packed, is_batched=is_batched)
        return hx

    def forward(self, input, hx=None):
        orig_input = input

        real_hidden_size = self.proj_size if self.proj_size > 0 else self.hidden_size

        length = None
        # for jit
        sorted_indices = None
        unsorted_indices = None
        is_batched = None

        if isinstance(orig_input, PackedSequence):
            _, batch_sizes, sorted_indices, unsorted_indices = orig_input
            # mindspore can not process packed_sequence, should recover to normal tensor type
            input, length = pad_packed_sequence(orig_input, batch_first=False)
            input_ms = cast_to_ms_tensor(input)
            x_dtype = input_ms.dtype
            length = cast_to_ms_tensor(length)
            if sorted_indices is not None:
                input_ms = input_ms.index_select(1, ms.Tensor(sorted_indices))
                length = length.index_select(0, ms.Tensor(sorted_indices))

            if hx is None:
                hx = self._get_hx(input_ms, hx, input_ms.shape[1], real_hidden_size, True, x_dtype, from_packed=True)
            else:
                # Each batch of the hidden state should match the input sequence that
                # the user believes he/she is passing in.
                hx = cast_to_ms_tensor(hx)
                hx = self.permute_hidden(hx, sorted_indices)
                self.check_forward_args(input_ms, hx, None, from_packed=True)

            output, h_n, c_n = self._run_recurrent(input_ms, hx, length)

            output = self._get_sequence_output(output, batch_sizes)
            output = cast_to_adapter_tensor(output.astype(x_dtype))
            h_n = cast_to_adapter_tensor(h_n.astype(x_dtype))
            c_n = cast_to_adapter_tensor(c_n.astype(x_dtype))
            output_packed = PackedSequence(output, batch_sizes, sorted_indices, unsorted_indices)
            return output_packed, self.permute_hidden((h_n, c_n), unsorted_indices)

        batch_sizes = None
        input_ms = cast_to_ms_tensor(orig_input)
        x_dtype = input_ms.dtype
        if input_ms.ndim not in (2, 3):
            raise ValueError(f"Expected input to be 2-D or 3-D but received {input_ms.ndim}-D tensor")
        is_batched = input_ms.ndim == 3

        if not is_batched:
            input_ms = input_ms.unsqueeze(1)
            hx = self._get_hx(input_ms, hx, 1, real_hidden_size, False, input_ms.dtype)
            output, h_n, c_n = self._run_recurrent(input_ms, hx)
            output = ms.ops.squeeze(output, 1)
            h_n = ms.ops.squeeze(h_n, 1)
            c_n = ms.ops.squeeze(c_n, 1)
        else:
            max_batch_size = input_ms.shape[0] if self.batch_first else input_ms.shape[1]
            hx = self._get_hx(input_ms, hx, max_batch_size, real_hidden_size, True, input_ms.dtype)
            if self.batch_first:
                input_ms = ms.ops.transpose(input_ms, (1, 0, 2))
                output, h_n, c_n = self._run_recurrent(input_ms, hx)
                output = ms.ops.transpose(output, (1, 0, 2))
            else:
                output, h_n, c_n = self._run_recurrent(input_ms, hx)

        return cast_to_adapter_tensor(output.astype(x_dtype)), \
                cast_to_adapter_tensor((h_n.astype(x_dtype), c_n.astype(x_dtype)))


class RNNCellBase(Module):
    def __init__(self, input_size, hidden_size, bias, num_chunks, device=None, dtype=None):
        unsupported_attr(device)
        super(RNNCellBase, self).__init__()
        self.input_size = input_size
        self.hidden_size = hidden_size
        self.bias = bias
        self.weight_ih = Parameter(empty((num_chunks * hidden_size, input_size), dtype=dtype))
        self.weight_hh = Parameter(empty((num_chunks * hidden_size, hidden_size), dtype=dtype))
        if bias:
            self.bias_ih = Parameter(empty(num_chunks * hidden_size, dtype=dtype))
            self.bias_hh = Parameter(empty(num_chunks * hidden_size, dtype=dtype))
        else:
            # can not use register_parameter('bias_ih', None),
            # because GRAPH_MODE not support Parameter with None value.
            self.bias_ih = None
            self.bias_hh = None

        self._rnn_cell = None
        self.reset_parameters()

    def extra_repr(self) -> str:
        s = '{input_size}, {hidden_size}'
        if 'bias' in self.__dict__ and self.bias is not True:
            s += ', bias={bias}'
        if 'nonlinearity' in self.__dict__ and self.nonlinearity != "tanh":
            s += ', nonlinearity={nonlinearity}'
        return s.format(**self.__dict__)

    def reset_parameters(self) -> None:
        stdv = 1.0 / math.sqrt(self.hidden_size) if self.hidden_size > 0 else 0
        for weight in self.parameters():
            init.uniform_(weight, -stdv, stdv)

    def forward(self, input, hx=None):
        input_ms = cast_to_ms_tensor(input)

        if len(input_ms.shape) not in (1, 2):
            raise RuntimeError(f"RNNCell: Expected input to be 1-D or 2-D but received {len(input_ms.shape)}-D tensor")
        is_batched = len(input_ms.shape) == 2
        if not is_batched:
            input_ms = ms.ops.unsqueeze(input_ms, 0)

        if hx is None:
            hx = zeros(input_ms.shape[0], self.hidden_size, dtype=input_ms.dtype)
            hx = cast_to_ms_tensor(hx)
        else:
            hx = cast_to_ms_tensor(hx)
            hx = ms.ops.unsqueeze(hx, 0) if not is_batched else hx

        ret = self._rnn_cell(input_ms, hx, self.weight_ih, self.weight_hh, self.bias_ih, self.bias_hh)
        if not is_batched:
            ret = ms.ops.squeeze(ret, 0)
        return cast_to_adapter_tensor(ret)

class RNNCell(RNNCellBase):
    def __init__(self, input_size, hidden_size, bias=True, nonlinearity="tanh",
                 device=None, dtype=None):
        super(RNNCell, self).__init__(input_size, hidden_size, bias, num_chunks=1, device=device, dtype=dtype)
        self.nonlinearity = nonlinearity
        if self.nonlinearity == "tanh":
            self._rnn_cell = _rnn_tanh_cell
        elif self.nonlinearity == "relu":
            self._rnn_cell = _rnn_relu_cell
        else:
            raise RuntimeError(
                "Unknown nonlinearity: {}".format(self.nonlinearity))

class LSTMCell(RNNCellBase):
    def __init__(self, input_size, hidden_size, bias=True, device=None, dtype=None):
        super(LSTMCell, self).__init__(input_size, hidden_size, bias, num_chunks=4, device=device, dtype=dtype)

    def forward(self, input, hx=None):
        input_ms = cast_to_ms_tensor(input)
        if len(input_ms.shape) not in (1, 2):
            raise RuntimeError(f"LSTMCell: Expected input to be 1-D or 2-D but received {len(input_ms.shape)}-D tensor")
        is_batched = len(input_ms.shape) == 2
        if not is_batched:
            input_ms = ms.ops.unsqueeze(input_ms, 0)

        if hx is None:
            _zeros = zeros(input_ms.shape[0], self.hidden_size, dtype=input_ms.dtype)
            hx = (_zeros, _zeros)
            hx = cast_to_ms_tensor(hx)
        else:
            hx = cast_to_ms_tensor(hx)
            hx = (ms.ops.unsqueeze(hx[0], 0), ms.ops.unsqueeze(hx[1], 0)) if not is_batched else hx

        hx = cast_to_ms_tensor(hx)

        ret = _lstm_cell(input_ms, hx, self.weight_ih, self.weight_hh, self.bias_ih, self.bias_hh)

        if not is_batched:
            ret = (ms.ops.squeeze(ret[0], 0), ms.ops.squeeze(ret[1], 0))
        return cast_to_adapter_tensor(ret)


class GRUCell(RNNCellBase):
    def __init__(self, input_size, hidden_size, bias=True, device=None, dtype=None):
        super(GRUCell, self).__init__(input_size, hidden_size, bias, num_chunks=3, device=device, dtype=dtype)
        self._rnn_cell = _gru_cell
