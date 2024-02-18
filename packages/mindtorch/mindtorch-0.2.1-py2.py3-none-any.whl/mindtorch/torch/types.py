#!/usr/bin/env python
import builtins
from typing import Any,  Union
import mindspore as ms
from mindtorch.utils import unsupported_attr, get_backend

@ms.jit_class
class device():
    def __init__(self, type=None, index=None):
        if type is not None:
            if isinstance(type, str):
                if ':' in type:
                    if index is not None:
                        raise ValueError("`type` must not include an index because index was "
                                         f"passed explicitly: {type}")
                    _target, _id = type.split(':')
                    _id = int(_id)
                else:
                    _target = type
                    _id = index
            elif isinstance(type, int):
                _target = get_backend()
                _id = type
            elif isinstance(type, device):
                if index is not None:
                    raise ValueError("torch.device(): When input is torch.device, `index` can not be set.")
                _target = type.type()
                _id = type.index
            else:
                raise TypeError("torch.device(): `type` must be type of 'str' or 'torch.device'.")
        else:
            raise ValueError("torch.device(): `type` can not be None")

        self.type = _target
        self.index = _id

    def __repr__(self):
        if self.index is None:
            return str(self.type)
        return f"{self.type}:{self.index}"

    def __eq__(self, __value):
        if not isinstance(__value, device):
            return False
        return hash(self) == hash(__value)

    def __hash__(self):
        return hash(str(self))


_int = builtins.int
_float = builtins.float
_bool = builtins.bool

_device = device


class SymInt:
    pass

# Meta-type for "numeric" things; matches our docs
Number = Union[_int, _float, _bool]

# Meta-type for "device-like" things.  Not to be confused with 'device' (a
# literal device object).  This nomenclature is consistent with PythonArgParser.
# None means use the default device (typically CPU)
Device = Union[_device, str, _int, None]

# Storage protocol implemented by ${Type}StorageBase classes

@ms.jit_class
class Storage():
    def _print(self):
        raise NotImplementedError("`Storage` is not currently supported, please delete it, "
                                  "and that will not affect the calculation results.")

    def __deepcopy__(self, memo) -> 'Storage':
        unsupported_attr(memo)
        self._print()

    def _new_shared(self, int) -> 'Storage':
        unsupported_attr(int)
        self._print()

    def _write_file(self, f: Any, is_real_file: _bool, save_size: _bool, element_size: int) -> None:
        unsupported_attr(f, is_real_file, save_size, element_size)
        self._print()

    def element_size(self) -> int:
        self._print()

    def is_shared(self) -> bool:
        self._print()

    def share_memory_(self) -> 'Storage':
        self._print()

    def nbytes(self) -> int:
        self._print()

    def cpu(self) -> 'Storage':
        self._print()

    def data_ptr(self) -> int:
        self._print()

    def from_file(self, filename: str, shared: bool = False, nbytes: int = 0) -> 'Storage':
        unsupported_attr(filename, shared, nbytes)
        self._print()

    def _new_with_file(self, f: Any, element_size: int) -> 'Storage':
        unsupported_attr(f, element_size)
        self._print()
