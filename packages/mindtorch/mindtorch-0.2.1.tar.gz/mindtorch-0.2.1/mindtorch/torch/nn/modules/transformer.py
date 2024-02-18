#!/usr/bin/env python
# -*- coding: utf-8 -*-
import copy
import mindspore as ms
import mindspore.ops as ops
from mindtorch.utils import unsupported_attr
from mindtorch.torch.tensor import cast_to_ms_tensor, cast_to_adapter_tensor

from .module import Module
from .activation import MultiheadAttention
from .container import ModuleList
from .dropout import Dropout
from .linear import Linear
from .normalization import LayerNorm
from .. import functional as F
from ..init import xavier_uniform_

__all__ = ['TransformerEncoderLayer', 'TransformerDecoderLayer', 'TransformerEncoder', 'TransformerDecoder',
           'Transformer']

class Transformer(Module):
    def __init__(self, d_model=512, nhead=8, num_encoder_layers=6, num_decoder_layers=6, dim_feedforward=2048,
                 dropout=0.1, activation='relu', custom_encoder=None, custom_decoder=None, layer_norm_eps=1e-5,
                 batch_first=False, norm_first=False, device=None, dtype=None):
        unsupported_attr(device)
        super(Transformer, self).__init__()

        if custom_encoder is not None:
            self.encoder = custom_encoder
        else:
            encoder_layer = TransformerEncoderLayer(d_model, nhead, dim_feedforward, dropout, activation,
                                                    layer_norm_eps, batch_first, norm_first, dtype=dtype)
            encoder_norm = LayerNorm(d_model, eps=layer_norm_eps, dtype=dtype)
            self.encoder = TransformerEncoder(encoder_layer, num_encoder_layers, encoder_norm)

        if custom_decoder is not None:
            self.decoder = custom_decoder
        else:
            decoder_layer = TransformerDecoderLayer(d_model, nhead, dim_feedforward, dropout, activation,
                                                    layer_norm_eps, batch_first, norm_first, dtype=dtype)
            decoder_norm = LayerNorm(d_model, eps=layer_norm_eps, dtype=dtype)
            self.decoder = TransformerDecoder(decoder_layer, num_decoder_layers, decoder_norm)

        self._reset_parameters()

        self.d_model = d_model
        self.nhead = nhead

        self.batch_first = batch_first

    def forward(self, src, tgt, src_mask=None, tgt_mask=None, memory_mask=None, src_key_padding_mask=None,
                tgt_key_padding_mask=None, memory_key_padding_mask=None):
        src = cast_to_ms_tensor(src)
        tgt = cast_to_ms_tensor(tgt)
        src_mask = cast_to_ms_tensor(src_mask)
        tgt_mask = cast_to_ms_tensor(tgt_mask)
        memory_mask = cast_to_ms_tensor(memory_mask)
        src_key_padding_mask = cast_to_ms_tensor(src_key_padding_mask)
        tgt_key_padding_mask = cast_to_ms_tensor(tgt_key_padding_mask)
        memory_key_padding_mask = cast_to_ms_tensor(memory_key_padding_mask)

        is_batched = src.dim() == 3
        if not self.batch_first and src.shape[1] != tgt.shape[1] and is_batched:
            raise ValueError("the batch number of src and tgt must be equal")
        elif self.batch_first and src.shape[0] != tgt.shape[0] and is_batched:
            raise ValueError("the batch number of src and tgt must be equal")

        if src.shape[-1] != self.d_model or tgt.shape[-1] != self.d_model:
            raise ValueError("the feature number of src and tgt must be equal to d_model")

        memory = self.encoder(src, mask=src_mask, src_key_padding_mask=src_key_padding_mask)
        output = self.decoder(tgt, memory, tgt_mask=tgt_mask, memory_mask=memory_mask,
                              tgt_key_padding_mask=tgt_key_padding_mask,
                              memory_key_padding_mask=memory_key_padding_mask)
        return cast_to_adapter_tensor(output)

    @staticmethod
    def generate_square_subsequent_mask(sz):
        #TODO: replace with ms.ops.triu and ms.ops.full
        # does not support ascend now
        return ms.numpy.full((sz, sz), float('-inf')).triu(diagonal=1)

    def _reset_parameters(self):
        for p in self.parameters():
            if p.dim() > 1:
                xavier_uniform_(p)

class TransformerEncoder(Module):
    def __init__(self, encoder_layer, num_layers, norm=None, enable_nested_tensor=False):
        unsupported_attr(enable_nested_tensor)
        super(TransformerEncoder, self).__init__()
        self.layers = _get_clones(encoder_layer, num_layers)
        self.num_layers = num_layers
        self.norm = norm

    def forward(self, src, mask=None, src_key_padding_mask=None):
        src = cast_to_ms_tensor(src)
        mask = cast_to_ms_tensor(mask)
        src_key_padding_mask = cast_to_ms_tensor(src_key_padding_mask)

        if src_key_padding_mask is not None:
            _skpm_dtype = src_key_padding_mask.dtype
            if _skpm_dtype != ms.bool_ and not ops.is_floating_point(src_key_padding_mask):
                raise AssertionError("only bool and floating types of key_padding_mask are supported")

        output = src
        for mod in self.layers:
            output = mod(output, src_mask=mask, src_key_padding_mask=src_key_padding_mask)

        if self.norm is not None:
            output = self.norm(output)

        return cast_to_adapter_tensor(output)


class TransformerDecoder(Module):
    def __init__(self, decoder_layer, num_layers, norm=None):
        super(TransformerDecoder, self).__init__()
        self.layers = _get_clones(decoder_layer, num_layers)
        self.num_layers = num_layers
        self.norm = norm

    def forward(self, tgt, memory, tgt_mask=None, memory_mask=None, tgt_key_padding_mask=None,
                memory_key_padding_mask=None):
        tgt = cast_to_ms_tensor(tgt)
        memory = cast_to_ms_tensor(memory)
        tgt_mask = cast_to_ms_tensor(tgt_mask)
        memory_mask = cast_to_ms_tensor(memory_mask)
        tgt_key_padding_mask = cast_to_ms_tensor(tgt_key_padding_mask)
        memory_key_padding_mask = cast_to_ms_tensor(memory_key_padding_mask)

        output = tgt
        for mod in self.layers:
            output = mod(output, memory, tgt_mask=tgt_mask, memory_mask=memory_mask,
                         tgt_key_padding_mask=tgt_key_padding_mask, memory_key_padding_mask=memory_key_padding_mask)

        if self.norm is not None:
            output = self.norm(output)

        return cast_to_adapter_tensor(output)

class TransformerEncoderLayer(Module):
    def __init__(self, d_model, nhead, dim_feedforward=2048, dropout=0.1, activation='relu', layer_norm_eps=1e-5,
                 batch_first=False, norm_first=False, device=None, dtype=None):
        unsupported_attr(device)
        super(TransformerEncoderLayer, self).__init__()
        self.self_attn = MultiheadAttention(d_model, nhead, dropout=dropout, batch_first=batch_first, dtype=dtype)
        # Implementation of Feedforward model
        self.linear1 = Linear(d_model, dim_feedforward, dtype=dtype)
        self.dropout = Dropout(dropout)
        self.linear2 = Linear(dim_feedforward, d_model, dtype=dtype)

        self.norm_first = norm_first
        self.norm1 = LayerNorm(d_model, eps=layer_norm_eps, dtype=dtype)
        self.norm2 = LayerNorm(d_model, eps=layer_norm_eps, dtype=dtype)
        self.dropout1 = Dropout(dropout)
        self.dropout2 = Dropout(dropout)

        #TODO: other types of activation should be considered
        if isinstance(activation, str):
            activation = _get_activation_fn(activation)

        if activation is F.relu:
            self.activation_relu_or_gelu = 1
        elif activation is F.gelu:
            self.activation_relu_or_gelu = 2
        else:
            self.activation_relu_or_gelu = 0
        self.activation = activation

    def __setstate__(self, state):
        if 'activation' not in state[1]:
            state[1]['activation'] = F.relu
        super(TransformerEncoderLayer, self).__setstate__(state)

    def forward(self, src, src_mask=None, src_key_padding_mask=None):
        src = cast_to_ms_tensor(src)
        src_mask = cast_to_ms_tensor(src_mask)
        src_key_padding_mask = cast_to_ms_tensor(src_key_padding_mask)

        if src_key_padding_mask is not None:
            _skpm_dtype = src_key_padding_mask.dtype
            if _skpm_dtype != ms.bool_ and not ops.is_floating_point(src_key_padding_mask):
                raise AssertionError("only bool and floating types of key_padding_mask are supported")

        x = src
        if self.norm_first:
            x = x + self._sa_block(self.norm1(x), src_mask, src_key_padding_mask)
            x = x + self._ff_block(self.norm2(x))
        else:
            x = self.norm1(x + self._sa_block(x, src_mask, src_key_padding_mask))
            x = self.norm2(x + self._ff_block(x))
        return cast_to_adapter_tensor(x)

    # self-attention block
    def _sa_block(self, x, attn_mask=None, key_padding_mask=None):
        x = self.self_attn(x, x, x, attn_mask=attn_mask, key_padding_mask=key_padding_mask, need_weights=False)[0]
        return self.dropout1(x)

    # feed forward block
    def _ff_block(self, x):
        x = self.linear2(self.dropout(self.activation(self.linear1(x))))
        return self.dropout2(x)


class TransformerDecoderLayer(Module):
    def __init__(self, d_model, nhead, dim_feedforward=2048, dropout=0.1, activation='relu', layer_norm_eps=1e-5,
                 batch_first=False, norm_first=False, device=None, dtype=None):
        unsupported_attr(device)

        super(TransformerDecoderLayer, self).__init__()
        self.self_attn = MultiheadAttention(d_model, nhead, dropout=dropout, batch_first=batch_first, dtype=dtype)
        self.multihead_attn = MultiheadAttention(d_model, nhead, dropout=dropout, batch_first=batch_first, dtype=dtype)
        # Implementation of Feedforward model
        self.linear1 = Linear(d_model, dim_feedforward, dtype=dtype)
        self.dropout = Dropout(dropout)
        self.linear2 = Linear(dim_feedforward, d_model, dtype=dtype)

        self.norm_first = norm_first
        self.norm1 = LayerNorm(d_model, eps=layer_norm_eps, dtype=dtype)
        self.norm2 = LayerNorm(d_model, eps=layer_norm_eps, dtype=dtype)
        self.norm3 = LayerNorm(d_model, eps=layer_norm_eps, dtype=dtype)
        self.dropout1 = Dropout(dropout)
        self.dropout2 = Dropout(dropout)
        self.dropout3 = Dropout(dropout)

        #TODO: other types of activation should be considered
        # Legacy string support for activation function.
        if isinstance(activation, str):
            self.activation = _get_activation_fn(activation)
        else:
            self.activation = activation

    def __setstate__(self, state):
        if 'activation' not in state[1]:
            state[1]['activation'] = F.relu
        super(TransformerDecoderLayer, self).__setstate__(state)

    def forward(self, tgt, memory, tgt_mask=None, memory_mask=None, tgt_key_padding_mask=None,
                memory_key_padding_mask=None):
        tgt = cast_to_ms_tensor(tgt)
        memory = cast_to_ms_tensor(memory)
        tgt_mask = cast_to_ms_tensor(tgt_mask)
        memory_mask = cast_to_ms_tensor(memory_mask)
        tgt_key_padding_mask = cast_to_ms_tensor(tgt_key_padding_mask)
        memory_key_padding_mask = cast_to_ms_tensor(memory_key_padding_mask)

        x = tgt
        if self.norm_first:
            x = x + self._sa_block(self.norm1(x), tgt_mask, tgt_key_padding_mask)
            x = x + self._mha_block(self.norm2(x), memory, memory_mask, memory_key_padding_mask)
            x = x + self._ff_block(self.norm3(x))
        else:
            x = self.norm1(x + self._sa_block(x, tgt_mask, tgt_key_padding_mask))
            x = self.norm2(x + self._mha_block(x, memory, memory_mask, memory_key_padding_mask))
            x = self.norm3(x + self._ff_block(x))

        return cast_to_adapter_tensor(x)

    # self-attention block
    def _sa_block(self, x, attn_mask=None, key_padding_mask=None):
        x = self.self_attn(x, x, x, attn_mask=attn_mask, key_padding_mask=key_padding_mask, need_weights=False)[0]
        return self.dropout1(x)

    # multihead attention block
    def _mha_block(self, x, mem, attn_mask=None, key_padding_mask=None):
        x = self.multihead_attn(x, mem, mem, attn_mask=attn_mask, key_padding_mask=key_padding_mask,
                                need_weights=False)[0]
        return self.dropout2(x)

    # feed forward block
    def _ff_block(self, x):
        x = self.linear2(self.dropout(self.activation(self.linear1(x))))
        return self.dropout3(x)


def _get_clones(module, N):
    #TODO: CellList?
    return ModuleList([copy.deepcopy(module) for i in range(N)])


def _get_activation_fn(activation):
    if activation == "relu":
        return F.relu
    elif activation == "gelu":
        return F.gelu

    raise RuntimeError("activation should be relu/gelu, not {}".format(activation))
