from collections import namedtuple
from typing import Iterable
import numpy as np
import mindspore as ms
from mindtorch.utils import is_under_gpu_context
import mindtorch.torch.functional as adapter_F
from mindtorch.torch.conflict_functional import arange
from mindtorch.torch.tensor import Tensor as adapter_tensor
from mindtorch.torch.tensor import cast_to_ms_tensor, cast_to_adapter_tensor

PackedSequence_ = namedtuple('PackedSequence_', ['data', 'batch_sizes', 'sorted_indices', 'unsorted_indices'])

def pad_sequence(sequences, batch_first=False, padding_value=0.0):
    if not isinstance(sequences, Iterable):
        msg = ('pad_sequence: Expected iterable for input sequences, but got arg of type: '
               f'{type(sequences)}')
        raise RuntimeError(msg)
    if len(sequences) == 0:
        raise RuntimeError("pad_sequence: received an empty list of sequences")
    if isinstance(sequences[0], adapter_tensor):
        sequences = cast_to_ms_tensor(sequences)
        num_samples = len(sequences)
        lengths = []
        sample_shape = ()
        flag = True

        # take the sample shape from the first non empty sequence
        # checking for consistency in the main loop below.
        for x in sequences:
            lengths.append(len(x))
            if flag and len(x):
                sample_shape = np.asarray(x).shape[1:]
                flag = False

        maxlen = max(lengths)

        x_shape = (num_samples, maxlen) + sample_shape if batch_first else (maxlen, num_samples) + sample_shape
        x = ms.ops.full(x_shape, padding_value, dtype=sequences[0].dtype)
        for idx, s in enumerate(sequences):
            if batch_first:
                trunc = s[:maxlen]
                x[idx, :len(trunc)] = trunc
            else:
                trunc = s[:maxlen]
                x[:len(trunc), idx] = trunc
        return cast_to_adapter_tensor(x)

    elif isinstance(sequences[0], np.ndarray):
        num_samples = len(sequences)

        lengths = []
        sample_shape = ()
        flag = True

        # take the sample shape from the first non empty sequence
        # checking for consistency in the main loop below.

        for x in sequences:
            lengths.append(len(x))
            if flag and len(x):
                sample_shape = np.asarray(x).shape[1:]
                flag = False

        maxlen = np.max(lengths)

        x_shape = (num_samples, maxlen) + sample_shape if batch_first else (maxlen, num_samples) + sample_shape
        output = np.full(x_shape, padding_value, dtype=sequences[0].dtype)
        for idx, s in enumerate(sequences):
            if batch_first:
                trunc = s[:maxlen]
                output[idx, :len(trunc)] = trunc
            else:
                trunc = s[:maxlen]
                output[:len(trunc), idx] = trunc
        return output

    raise TypeError("pad_sequence: sequences must contain tensors or numpy arrays; found {}".format(type(sequences[0])))

def _invert_permutation(permutation):
    if permutation is None:
        return None
    output = adapter_F.empty_like(permutation).astype(ms.int64)
    # TODO: ms_torch.scatter needs to be improved
    output = output.scatter(0, permutation, arange(0, permutation.numel()))
    return output

# TorchScript doesn't support constructors on named tuples, so we use this helper
# method to construct PackedSequence
def _packed_sequence_init_args(data, batch_sizes=None, sorted_indices=None, unsorted_indices=None):
    # NB: if unsorted_indices is provided, it should be the inverse permutation
    # to sorted_indices. Don't assert it here because the PackedSequence ctor
    # should only be used internally.

    if unsorted_indices is None:
        unsorted_indices = _invert_permutation(sorted_indices)

    # support being called as `PackedSequence(data, batch_sizes, sorted_indices)`
    if batch_sizes is not None:
        # TODO: device related
        # if batch_sizes.device.type != 'cpu':
        #     raise ValueError(
        #         "batch_sizes should always be on CPU. "
        #         "Instances of PackedSequence should never be created manually. "
        #         "They should be instantiated by functions like pack_sequence "
        #         "and pack_padded_sequences in nn.utils.rnn. ")
        return data, batch_sizes, sorted_indices, unsorted_indices

    # support being called as `PackedSequence((data, batch_sizes), *, sorted_indices)`
    else:
        assert isinstance(data, (list, tuple)) and len(data) == 2
        return data[0], data[1], sorted_indices, unsorted_indices

class PackedSequence(PackedSequence_):
    def __new__(cls, data, batch_sizes=None, sorted_indices=None, unsorted_indices=None):
        return super(PackedSequence, cls).__new__(
            cls,
            *_packed_sequence_init_args(data, batch_sizes, sorted_indices,
                                        unsorted_indices))
    # pin memory not supported
    def pin_memory(self):
        return self

    def is_pinned(self):
        return False

    def cuda(self, *args, **kwargs):
        return self.to(*args, **kwargs)

    def cpu(self, *args, **kwargs):
        return self.to(*args, **kwargs)

    @property
    def is_cuda(self):
        return is_under_gpu_context()

    def double(self):
        return self.to(dtype=ms.double)

    def float(self):
        return self.to(dtype=ms.float32)

    def half(self):
        return self.to(dtype=ms.half)

    def long(self):
        return self.to(dtype=ms.int64)

    def int(self):
        return self.to(dtype=ms.int32)

    def short(self):
        return self.to(dtype=ms.short)

    def char(self):
        return self.to(dtype=ms.int8)

    def byte(self):
        return self.to(dtype=ms.uint8)

    def to(self, *args, **kwargs):
        data = self.data.to(*args, **kwargs)
        if data is self.data:
            return self
        else:
            return type(self)(data, self.batch_sizes, self.sorted_indices, self.unsorted_indices)

# This method returns `(data, batch_sizes)`, which are then passed into a
# `PackedSequence` constructor.
# `data` can be on arbitrary device and of arbitrary dtype, but `batch_sizes`
# must be a CPU int64 tensor.
def _pack_padded_sequence(_input, _lengths, batch_first):
    input = _input.transpose(0, 1) if batch_first else _input
    lengths = _lengths.asnumpy().tolist()
    batch_size = input.size(1)

    if input.numel() <= 0:
        raise RuntimeError("Cannot pack empty tensors.")
    if len(lengths) != batch_size:
        raise RuntimeError(f"Expected `len(lengths)` to be equal to batch_size, but got {len(lengths)}"
                           f"(batch_size={batch_size})")
    if lengths[-1] <= 0:
        raise RuntimeError("Length of all samples has to be greater than 0, but found an element "
                           "in 'lengths' that is <= 0")

    if any(lengths[-1 - i] > lengths[-2 - i] for i in range(batch_size - 1)):
        msg = ("`lengths` array must be sorted in decreasing order when "
                "`enforce_sorted` is True. You can pass `enforce_sorted=False` "
                "to pack_padded_sequence and/or pack_sequence to sidestep this "
                "requirement if you do not need ONNX exportability.")
        raise RuntimeError(msg)

    steps = []
    prev_l = 0
    batch_sizes_i = 0
    batch_sizes_t = adapter_F.empty(lengths[0], dtype=_lengths.dtype)

    for i in range(batch_size):
        l = lengths[batch_size - 1 - i]
        if l > prev_l:
            current_batch_size = batch_size - i
            for _ in range(0, l - prev_l):
                batch_sizes_t[batch_sizes_i] = current_batch_size
                sliced = input[batch_sizes_i][:current_batch_size]
                steps.append(sliced)
                batch_sizes_i = batch_sizes_i + 1
            prev_l = l

    return cast_to_adapter_tensor(ms.ops.cat(steps)), batch_sizes_t

def _packed_sequence_init(data, batch_sizes=None, sorted_indices=None, unsorted_indices=None):
    data, batch_sizes, sorted_indices, unsorted_indices = _packed_sequence_init_args(
        data, batch_sizes, sorted_indices, unsorted_indices)
    return PackedSequence(data, batch_sizes, sorted_indices, unsorted_indices)

def pack_padded_sequence(input, lengths, batch_first=False, enforce_sorted=True):
    if not isinstance(lengths, adapter_tensor):
        lengths = adapter_F.as_tensor(lengths, dtype=ms.int64)
    if enforce_sorted:
        sorted_indices = None
    else:
        lengths, sorted_indices = adapter_F.sort(lengths, descending=True)
        # TODO: adapter sort need to be improved, indices returned dtype wrong
        sorted_indices = sorted_indices.astype(lengths.dtype)
        batch_dim = 0 if batch_first else 1
        input = input.index_select(batch_dim, sorted_indices)

    data, batch_sizes = _pack_padded_sequence(input, lengths, batch_first)
    return _packed_sequence_init(data, batch_sizes, sorted_indices, None)

def pack_sequence(sequences, enforce_sorted=True):
    lengths = adapter_F.as_tensor([v.size(0) for v in sequences])
    return pack_padded_sequence(pad_sequence(sequences), lengths, enforce_sorted=enforce_sorted)

def _pad_packed_sequence(data, _batch_sizes, batch_first, padding_value, total_length):
    max_batch_size = _batch_sizes[0].item()
    max_real_seq_length = _batch_sizes.size(0)
    max_seq_length = max_real_seq_length
    if total_length > 0:
        if total_length < max_seq_length:
            msg = ("Expected total_length to be at least the length of the longest "
                   f"sequence in input, but got total_length={total_length} and "
                   f"max sequence length being {max_seq_length}")
            raise RuntimeError(msg)
        max_seq_length = total_length

    s_data_size = data.shape[1:]
    output_size = (max_seq_length, max_batch_size) + s_data_size

    output = adapter_F.full(output_size, padding_value, dtype=data.dtype)

    lengths_t = adapter_F.empty(max_batch_size, dtype=_batch_sizes.dtype)
    data_offset = 0
    prev_batch_size = max_batch_size
    prev_i = 0
    lengths_i = max_batch_size - 1
    for i in range(0, max_real_seq_length + 1):
        batch_size = _batch_sizes[i].item() if i != max_real_seq_length else 0
        if batch_size != prev_batch_size:
            l = prev_batch_size * (i - prev_i)
            tmp = data[data_offset:data_offset + l]
            tmp_shape = (i - prev_i, prev_batch_size) + output_size[2:]
            output[prev_i:i, :prev_batch_size] = tmp.view(tmp_shape)
            data_offset += l
            prev_i = i

        dec = prev_batch_size - batch_size
        if dec > 0:
            for _ in range(dec):
                lengths_t[lengths_i] = i
                lengths_i -= 1
        prev_batch_size = batch_size

    if batch_first:
        output = output.transpose(0, 1)

    return (output, lengths_t)

def pad_packed_sequence(sequence, batch_first=False, padding_value=0.0, total_length=None):
    max_seq_length = sequence.batch_sizes.size(0)
    if total_length is not None:
        if total_length < max_seq_length:
            raise ValueError("Expected total_length to be at least the length "
                             "of the longest sequence in input, but got "
                             "total_length={} and max sequence length being {}"
                             .format(total_length, max_seq_length))
        max_seq_length = total_length
    padded_output, lengths = _pad_packed_sequence(
        sequence.data, sequence.batch_sizes, batch_first, padding_value, max_seq_length)
    unsorted_indices = sequence.unsorted_indices
    if unsorted_indices is not None:
        batch_dim = 0 if batch_first else 1
        return padded_output.index_select(batch_dim, unsorted_indices), lengths[unsorted_indices]
    return padded_output, lengths
