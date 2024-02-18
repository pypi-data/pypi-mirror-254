import mindtorch.torch.nn.functional as Adapter_F
from mindtorch.torch.functional import empty
from mindtorch.torch.nn.parameter import Parameter
from mindtorch.utils import unsupported_attr
from mindtorch.torch.nn.modules.module import Module
from mindtorch.torch.nn.init import normal_

__all__ = ['Embedding']

class Embedding(Module):
    def __init__(self, num_embeddings, embedding_dim, padding_idx=None,
                 max_norm=None, norm_type=2., scale_grad_by_freq=False,
                 sparse=False, _weight=None, device=None, dtype=None):
        unsupported_attr(scale_grad_by_freq)
        unsupported_attr(sparse)
        unsupported_attr(device)

        super(Embedding, self).__init__()
        self.num_embeddings = num_embeddings
        self.embedding_dim = embedding_dim
        if padding_idx is not None:
            if padding_idx > 0:
                if padding_idx >= self.num_embeddings:
                    raise ValueError('Padding_idx must be within num_embeddings')
            elif padding_idx < 0:
                if padding_idx < -self.num_embeddings:
                    raise ValueError('Padding_idx must be within num_embeddings')
                padding_idx = self.num_embeddings + padding_idx
        self.padding_idx = padding_idx
        self.max_norm = max_norm
        self.norm_type = norm_type
        self.scale_grad_by_freq = scale_grad_by_freq
        if _weight is None:
            self.weight = Parameter(empty((num_embeddings, embedding_dim), dtype=dtype))
            self.reset_parameters()
        else:
            if list(_weight.shape) != [num_embeddings, embedding_dim]:
                raise ValueError('Shape of weight does not match num_embeddings and embedding_dim')
            self.weight = Parameter(_weight)

        self.sparse = sparse

    def reset_parameters(self):
        normal_(self.weight)
        self._fill_padding_idx_with_zero()

    def _fill_padding_idx_with_zero(self):
        if self.padding_idx is not None:
            self.weight[self.padding_idx] = 0

    def forward(self, input):
        return Adapter_F.embedding(
            input, self.weight, self.padding_idx, self.max_norm,
            self.norm_type, self.scale_grad_by_freq, self.sparse)

    def extra_repr(self):
        s = '{num_embeddings}, {embedding_dim}'
        if self.padding_idx is not None:
            s += ', padding_idx={padding_idx}'
        if self.max_norm is not None:
            s += ', max_norm={max_norm}'
        if self.norm_type != 2:
            s += ', norm_type={norm_type}'
        if self.scale_grad_by_freq is not False:
            s += ', scale_grad_by_freq={scale_grad_by_freq}'
        if self.sparse is not False:
            s += ', sparse=True'
        return s.format(**self.__dict__)

    @classmethod
    def from_pretrained(cls, embeddings, freeze=True, padding_idx=None,
                        max_norm=None, norm_type=2., scale_grad_by_freq=False,
                        sparse=False):
        embeddings_rank = len(embeddings.shape)
        if embeddings_rank != 2:
            raise ValueError(f"dim of embedding must be 2, but got {embeddings_rank}")

        rows, cols = embeddings.shape
        embedding = cls(
            num_embeddings=rows,
            embedding_dim=cols,
            _weight=embeddings,
            padding_idx=padding_idx,
            max_norm=max_norm,
            norm_type=norm_type,
            scale_grad_by_freq=scale_grad_by_freq,
            sparse=sparse)
        embedding.weight.requires_grad = not freeze
        return embedding
