import copy
import collections
from functools import lru_cache
from ast import literal_eval
from typing import Any
import mindtorch.torch.common.dtype as _dtype
from mindtorch.torch.common.dtype import _TypeDict
from mindtorch.torch.types import device
from mindtorch.torch.logging import warning
from mindtorch.utils import unsupported_attr
from ._utils import _type, _cuda, _element_size, classproperty
try:
    import numpy as np
    HAS_NUMPY = True
except ModuleNotFoundError:
    np = None  # type: ignore[assignment]

_default_dtype = np.float32

def typename(o):
    module = ''
    class_name = ''
    if hasattr(o, '__module__') and o.__module__ != 'builtins' \
            and o.__module__ != '__builtin__' and o.__module__ is not None:
        module = o.__module__ + '.'

    if hasattr(o, '__qualname__'):
        class_name = o.__qualname__
    elif hasattr(o, '__name__'):
        class_name = o.__name__
    else:
        class_name = o.__class__.__name__

    return module + class_name


class _StorageBase():
    _cdata: Any
    is_sparse: bool = False
    is_sparse_csr: bool = False
    device: device = 'cpu'

    def __init__(self, *args, **kwargs):
        if len(args) > 0:
            raise NotImplementedError("`args` is not currently supported.")
        self.inner_data = kwargs.get('inner_data', None)

    def __len__(self):
        return self.inner_data.nelement()

    def __getitem__(self, idx):
        return self.inner_data.flatten()[idx].item()

    def copy_(self, source, non_blocking=None):
        raise NotImplementedError("`copy_` is not currently supported.")

    def nbytes(self):
        return self.inner_data.numpy().nbytes

    def size(self):
        return self.nbytes()

    def type(self, dtype=None, non_blocking=False):
        raise NotImplementedError("`type` is not currently supported.")

    def cuda(self, device=None, non_blocking=False, **kwargs):
        raise NotImplementedError("`cuda` is not currently supported.")

    def element_size(self):
        return self.inner_data.element_size()

    def get_device(self):
        return self.device

    def data_ptr(self):
        warning("The id corresponding to the python object is currently returned, rather than a pointer from C++.")
        return id(self.inner_data)

    def _share_filename_cpu_(self, *args, **kwargs):
        raise NotImplementedError("`_share_filename_cpu_` is not currently supported.")

    def _share_fd_cpu_(self, *args, **kwargs):
        raise NotImplementedError("`_share_fd_cpu_` is not currently supported.")

    @classmethod
    def _new_using_filename_cpu(cls, size):
        raise NotImplementedError("`_new_using_filename_cpu` is not currently supported.")

    @classmethod
    def _new_using_fd_cpu(cls, size):
        raise NotImplementedError("`_new_using_fd_cpu` is not currently supported.")

    @classmethod
    def from_buffer(cls, *args, **kwargs):
        inner_data = np.frombuffer(args[0], _TypeDict.get(kwargs['dtype'], np.float32))
        return cls(inner_data=inner_data)

    @classmethod
    def _new_shared_filename_cpu(cls, manager, obj, size, *, device=None, dtype=None):
        raise NotImplementedError("`_new_shared_filename_cpu` is not currently supported.")

    @classmethod
    def _release_ipc_counter_cuda(cls, *args, **kwargs):
        raise NotImplementedError("`_release_ipc_counter_cuda` is not currently supported.")

    @classmethod
    def _new_with_weak_ptr(cls, *args, **kwargs):
        raise NotImplementedError("`_new_with_weak_ptr` is not currently supported.")

    def _shared_decref(self):
        raise NotImplementedError("`_shared_decref` is not currently supported.")

    def _write_file(self, *args, **kwargs):
        raise NotImplementedError("`_write_file` is not currently supported.")

    def resize_(self, size):
        raise NotImplementedError("`resize_` is not currently supported.")

    def _weak_ref(self, *args, **kwargs):
        raise NotImplementedError("`_weak_ref` is not currently supported.")

    def is_pinned(self):
        raise NotImplementedError("`is_pinned` is not currently supported.")

    def _set_from_file(self, *args, **kwargs):
        raise NotImplementedError("`_set_from_file` is not currently supported.")

    def _set_cdata(self, *args, **kwargs):
        raise NotImplementedError("`_set_cdata` is not currently supported.")

    def _share_cuda_(self, *args, **kwargs):
        raise NotImplementedError("`_share_cuda_` is not currently supported.")

    def is_shared(self):
        raise NotImplementedError("`is_shared` is not currently supported.")

    @classmethod
    def _new_shared_cuda(cls, *args, **kwargs):
        raise NotImplementedError("`_new_shared_cuda` is not currently supported.")

    def _shared_incref(self, *args, **kwargs):
        raise NotImplementedError("`_shared_incref` is not currently supported.")

    @classmethod
    def _free_weak_ref(cls, *args, **kwargs):
        raise NotImplementedError("`_free_weak_ref` is not currently supported.")

    @property
    def is_cuda(self):
        raise NotImplementedError("`is_cuda` is not currently supported.")

    def __str__(self):
        data_str = ' ' + '\n '.join(str(self[i]) for i in range(self.size()))
        return data_str + (
            f'\n[{typename(self)}(device={self.device}) '
            f'of size {len(self)}]')

    def __repr__(self):
        return str(self)

    def __iter__(self):
        return iter(map(lambda i: self[i], range(self.size())))

    def __copy__(self):
        return self.clone()

    def __deepcopy__(self, memo):
        unsupported_attr(memo)
        raise NotImplementedError("`__deepcopy__` is not currently supported.")

    def __reduce__(self):
        raise NotImplementedError("`__reduce__` is not currently supported.")

    def __sizeof__(self):
        return super(_StorageBase, self).__sizeof__() + self.size()

    def clone(self):
        raise NotImplementedError("`clone` is not currently supported.")

    def tolist(self):
        """Returns a list containing the elements of this storage"""
        return list(self.inner_data.flatten().numpy())

    def cpu(self):
        return self

    def _to(self, dtype):
        if not isinstance(dtype, _dtype.ms_dtype):
            raise TypeError(f"Argument 'dtype' must be torch.dtype, not {type(dtype)}")
        storage = self.inner_data.to(dtype).storage()
        return storage

    def double(self):
        """Casts this storage to double type"""
        return self._to(_dtype.double)

    def float(self):
        """Casts this storage to float type"""
        return self._to(_dtype.float)

    def half(self):
        """Casts this storage to half type"""
        return self._to(_dtype.half)

    def long(self):
        """Casts this storage to long type"""
        return self._to(_dtype.long)

    def int(self):
        """Casts this storage to int type"""
        return self._to(_dtype.int)

    def short(self):
        """Casts this storage to short type"""
        return self._to(_dtype.short)

    def char(self):
        """Casts this storage to char type"""
        return self._to(_dtype.int8)

    def byte(self):
        """Casts this storage to byte type"""
        return self._to(_dtype.uint8)

    def bool(self):
        """Casts this storage to bool type"""
        return self._to(_dtype.bool)

    def bfloat16(self):
        """Casts this storage to bfloat16 type"""
        return self._to(_dtype.bfloat16)

    def complex_double(self):
        """Casts this storage to complex double type"""
        return self._to(_dtype.cdouble)

    def complex_float(self):
        """Casts this storage to complex float type"""
        return self._to(_dtype.cfloat)

    def pin_memory(self):
        raise NotImplementedError("`pin_memory` is not currently supported.")

    def share_memory_(self):
        raise NotImplementedError("`share_memory_` is not currently supported.")

    @classmethod
    def _new_shared(cls, size, *, device='cpu'):
        unsupported_attr(size)
        unsupported_attr(device)
        raise NotImplementedError("`_new_shared` is not currently supported.")

    def _untyped(self):
        return self


class _UntypedStorage(_StorageBase):
    @property
    def is_cuda(self):
        return self.device.type == 'cuda'


_StorageBase.type = _type  # type: ignore[assignment]
_StorageBase.cuda = _cuda  # type: ignore[assignment]


@lru_cache(maxsize=None)
def _dtype_to_storage_type_map():
    return {
        _dtype.double: 'DoubleStorage',
        _dtype.float: 'FloatStorage',
        _dtype.half: 'HalfStorage',
        _dtype.long: 'LongStorage',
        _dtype.int: 'IntStorage',
        _dtype.int16: 'ShortStorage',
        _dtype.int8: 'CharStorage',
        _dtype.uint8: 'ByteStorage',
        _dtype.bool: 'BoolStorage',
        _dtype.bfloat16: 'BFloat16Storage',
        _dtype.cdouble: 'ComplexDoubleStorage',
        _dtype.cfloat: 'ComplexFloatStorage',
        # TODO:The quantized dtype is not supported
        # _dtype.qint8: 'QInt8Storage',
        # _dtype.qint32: 'QInt32Storage',
        # _dtype.quint8: 'QUInt8Storage',
        # _dtype.quint4x2: 'QUInt4x2Storage',
        # _dtype.quint2x4: 'QUInt2x4Storage',
    }

@lru_cache(maxsize=None)
def _storage_type_to_dtype_map():
    dtype_map = {
        val: key for key, val in _dtype_to_storage_type_map().items()}
    return dtype_map

def _isint(x):
    if HAS_NUMPY:
        return isinstance(x, (int, np.integer))
    else:
        return isinstance(x, int)


class _TypedStorage:
    is_sparse = False

    dtype: _dtype.ms_dtype

    def fill_(self, value):
        self[0:len(self)] = value
        return self

    def __new__(cls, *args, wrap_storage=None, dtype=None, device=None):
        if cls == _LegacyStorage:
            raise RuntimeError("Only child classes of _LegacyStorage can be instantiated")

        if cls == _TypedStorage:
            return super().__new__(cls)

        else:
            arg_error_msg = (
                f'{cls}.__new__ received an invalid combination '
                f'of arguments. Expected one of:\n'
                ' * no arguments\n'
                ' * (int size)\n'
                ' * (Sequence data)\n'
                ' * (*, _UntypedStorage wrap_storage)')

            if device is not None:
                raise RuntimeError(
                    arg_error_msg +
                    "\nKeyword argument 'device' cannot be specified")

            if dtype is not None:
                raise RuntimeError(
                    arg_error_msg +
                    "\nKeyword argument 'dtype' cannot be specified")

            if wrap_storage is None:
                if len(args) > 1:
                    raise RuntimeError(
                        arg_error_msg +
                        "\nToo many positional arguments")

                if len(args) == 1 and not _isint(args[0]) and not isinstance(args[0], collections.abc.Sequence):
                    raise TypeError(
                        arg_error_msg +
                        f"\nArgument type not recognized: {type(args[0])}")

                return _TypedStorage(
                    *args,
                    dtype=cls.dtype)

            else:
                if len(args) != 0:
                    raise RuntimeError(
                        arg_error_msg +
                        "\nNo positional arguments should be given when using "
                        "'wrap_storage'")

                if not isinstance(wrap_storage, _UntypedStorage):
                    raise TypeError(
                        arg_error_msg +
                        f"\nArgument 'wrap_storage' must be _UntypedStorage, but got {type(wrap_storage)}")

                cls_device = 'cuda' if cls.__module__ == 'mindtorch.torch.cuda' else 'cpu'

                if wrap_storage.device.type != cls_device:
                    raise RuntimeError(
                        arg_error_msg +
                        f"\nDevice of 'wrap_storage' must be {cls_device}"
                        f", but got {wrap_storage.device.type}")

                return _TypedStorage(
                    *args,
                    wrap_storage=wrap_storage,
                    dtype=cls.dtype)

    def __init__(self, *args, device=None, dtype=None, wrap_storage=None):
        arg_error_msg = (
            '_TypedStorage.__init__ received an invalid combination '
            'of arguments. Expected one of:\n'
            ' * (*, torch.device device, torch.dtype dtype)\n'
            ' * (int size, *, torch.device device, torch.dtype dtype)\n'
            ' * (Sequence data, *, torch.device device, torch.dtype dtype)\n'
            ' * (*, _UntypedStorage wrap_storage, torch.dtype dtype)')

        if wrap_storage is not None:
            if len(args) != 0:
                raise RuntimeError(
                    arg_error_msg +
                    "\nNo positional arguments should be given when using "
                    "'wrap_storage'")

            if dtype is None:
                raise RuntimeError(
                    arg_error_msg +
                    "\nArgument 'dtype' must be specified")

            if not isinstance(dtype, _dtype.ms_dtype):
                raise TypeError(
                    arg_error_msg +
                    f"\nArgument 'dtype' must be torch.dtype, not {type(dtype)}")

            if device is not None:
                raise RuntimeError(
                    arg_error_msg +
                    "\nArgument 'device' should not be specified when 'wrap_storage' is given")

            self.dtype = dtype

            if not isinstance(wrap_storage, _UntypedStorage):
                raise TypeError(
                    arg_error_msg +
                    f"\nArgument 'wrap_storage' must be _UntypedStorage, but got {type(wrap_storage)}")

            self._storage = wrap_storage

        else:
            self.dtype = _dtype.float32 if dtype is None else dtype

            if len(args) == 0:
                self._storage = _UntypedStorage(device=device)

            elif len(args) == 1:
                if _isint(args[0]):
                    self._storage = _UntypedStorage(int(args[0]) * self.element_size(), device=device)
                elif isinstance(args[0], collections.abc.Sequence):
                    raise NotImplementedError("`_get_storage_from_sequence` is not currently supported.")
                else:
                    raise TypeError(
                        arg_error_msg +
                        f"\nArgument type not recognized: {type(args[0])}")

            else:
                raise RuntimeError(
                    arg_error_msg +
                    "\nToo many positional arguments")


    @property
    def is_cuda(self):
        return self.device.type == 'cuda'

    def _untyped(self):
        return self._storage

    def _new_wrapped_storage(self, untyped_storage):
        assert isinstance(untyped_storage, _UntypedStorage)

        if isinstance(self, _TypedStorage):
            return _TypedStorage(wrap_storage=untyped_storage, dtype=self.dtype)
        else:
            return type(self)(wrap_storage=untyped_storage)

    def __len__(self):
        return self._storage.nbytes() // self.element_size()

    def _maybe_wrap_index(self, idx, is_stop=False):
        if idx is None:
            if is_stop:
                return self.size()
            else:
                return 0

        else:
            if not isinstance(idx, int):
                raise TypeError(
                    f"can't index a {type(self)} with {type(idx)}")
            if is_stop:
                if (idx > self.size()) or (idx < -self.size()):
                    raise IndexError(
                        f'index {idx} out of range for storage of size {self.size()}')
                if idx > 0:
                    return idx
                else:
                    return idx % self.size()
            else:
                if (idx >= self.size()) or (idx < -self.size()):
                    raise IndexError(
                        f'index {idx} out of range for storage of size {self.size()}')
                return idx % self.size()

    def __setitem__(self, idx, value):
        raise NotImplementedError("`__setitem__` is not currently supported.")

    def __getitem__(self, idx):
        return self._storage[idx]

    def copy_(self, source, non_blocking=None):
        self._storage.copy_(source._untyped(), non_blocking)
        return self

    def nbytes(self):
        return self._storage.nbytes()

    def type(self, dtype=None, non_blocking=False):
        if dtype is None:
            if self.dtype not in _dtype_to_storage_type_map():
                return None

            storage_name = _dtype_to_storage_type_map()[self.dtype]
            return '.'.join(['mindtorch', storage_name])

        else:
            return self._storage.type(dtype, non_blocking)

    def cuda(self, device=None, non_blocking=False, **kwargs):
        cuda_storage: _UntypedStorage = self._storage.cuda(device, non_blocking, **kwargs)
        return self._new_wrapped_storage(cuda_storage)

    def element_size(self):
        return _element_size(self.dtype)

    def get_device(self):
        return self._storage.get_device()

    def __str__(self):
        data_str = ' ' + '\n '.join(str(self[i]) for i in range(self.size()))
        return data_str + (
            f'\n[{typename(self)}(dtype={self.dtype}, '
            f'device={self.device}) of size {len(self)}]')

    def __repr__(self):
        return str(self)

    def __iter__(self):
        return iter(map(lambda i: self[i], range(self.size())))

    def __copy__(self):
        return self._new_wrapped_storage(copy.copy(self._storage))

    def __deepcopy__(self, memo):
        return self._new_wrapped_storage(copy.deepcopy(self._storage, memo))

    def __sizeof__(self):
        return super(_TypedStorage, self).__sizeof__() + self.nbytes()

    def clone(self):
        """Returns a copy of this storage"""
        return self._new_wrapped_storage(self._storage.clone())

    def tolist(self):
        """Returns a list containing the elements of this storage"""
        return self._storage.tolist()

    def cpu(self):
        """Returns a CPU copy of this storage if it's not already on the CPU"""
        return self._new_wrapped_storage(self._storage.cpu())

    def pin_memory(self):
        """Coppies the  storage to pinned memory, if it's not already pinned."""
        return self._new_wrapped_storage(self._storage.pin_memory())

    def share_memory_(self):
        self._storage.share_memory_()
        return self

    def _new_shared(self, size, *, device=None):
        unsupported_attr(size)
        unsupported_attr(device)
        raise NotImplementedError("`_new_shared` is not currently supported.")

    @property
    def _cdata(self):
        raise NotImplementedError("`_cdata` is not currently supported.")

    @property
    def device(self):
        return self._storage.device

    def size(self):
        return len(self._storage)

    def pickle_storage_type(self):
        try:
            return _dtype_to_storage_type_map()[self.dtype]
        except KeyError as e:
            raise KeyError(f'dtype {self.dtype} is not recognized') from e

    def __reduce__(self):
        raise NotImplementedError("`__reduce__` is not currently supported.")

    def data_ptr(self):
        return self._storage.data_ptr()

    def resize_(self, size):
        self._storage.resize_(size * self.element_size())

    @classmethod
    def _free_weak_ref(cls, *args, **kwargs):
        return _UntypedStorage._free_weak_ref(*args, **kwargs)

    def _weak_ref(self, *args, **kwargs):
        return self._storage._weak_ref(*args, **kwargs)

    @classmethod
    def from_buffer(cls, *args, dtype=None, device=None, **kwargs):
        if cls == _TypedStorage:
            dtype = _dtype.float32 if dtype is None else dtype
        else:
            if dtype is not None or len(args) == 5:
                raise RuntimeError((
                    "from_buffer: 'dtype' can only be specified in "
                    "_UntypedStorage.from_buffer and _TypedStorage.from_buffer"))
            if device is not None:
                raise RuntimeError((
                    "from_buffer: 'device' can only be specified in "
                    "_UntypedStorage.from_buffer and _TypedStorage.from_buffer"))

            dtype = cls.dtype
        untyped_storage = _UntypedStorage.from_buffer(*args, dtype=dtype, **kwargs)
        return _TypedStorage(wrap_storage=untyped_storage, dtype=dtype)

    def _to(self, dtype):
        if not isinstance(dtype, _dtype.ms_dtype):
            raise TypeError(f"Argument 'dtype' must be torch.dtype, not {type(dtype)}")
        storage = self._storage.inner_data.to(dtype).storage()
        return storage

    def double(self):
        """Casts this storage to double type"""
        return self._to(_dtype.double)

    def float(self):
        """Casts this storage to float type"""
        return self._to(_dtype.float)

    def half(self):
        """Casts this storage to half type"""
        return self._to(_dtype.half)

    def long(self):
        """Casts this storage to long type"""
        return self._to(_dtype.long)

    def int(self):
        """Casts this storage to int type"""
        return self._to(_dtype.int)

    def short(self):
        """Casts this storage to short type"""
        return self._to(_dtype.short)

    def char(self):
        """Casts this storage to char type"""
        return self._to(_dtype.int8)

    def byte(self):
        """Casts this storage to byte type"""
        return self._to(_dtype.uint8)

    def bool(self):
        """Casts this storage to bool type"""
        return self._to(_dtype.bool)

    def bfloat16(self):
        """Casts this storage to bfloat16 type"""
        return self._to(_dtype.bfloat16)

    def complex_double(self):
        """Casts this storage to complex double type"""
        return self._to(_dtype.cdouble)

    def complex_float(self):
        """Casts this storage to complex float type"""
        return self._to(_dtype.cfloat)

    @classmethod
    def from_file(cls, filename, shared, size):
        raise NotImplementedError("`from_file` is not currently supported.")

    @classmethod
    def _expired(cls, *args, **kwargs):
        return literal_eval(cls.__module__)._UntypedStorage._expired(*args, **kwargs)

    def is_pinned(self):
        return self._storage.is_pinned()

    def _write_file(self, *args, **kwargs):
        return self._storage._write_file(*args, **kwargs)

    def _set_from_file(self, *args, **kwargs):
        return self._storage._set_from_file(*args, **kwargs)

    def _set_cdata(self, *args, **kwargs):
        return self._storage._set_cdata(*args, **kwargs)

    def _share_cuda_(self, *args, **kwargs):
        return self._storage._share_cuda_(*args, **kwargs)

    def is_shared(self):
        return self._storage.is_shared()

    @classmethod
    def _new_shared_cuda(cls, *args, **kwargs):
        return _UntypedStorage._new_shared_cuda(*args, **kwargs)

    def _share_filename_cpu_(self, *args, **kwargs):
        manager_handle, storage_handle, size = self._storage._share_filename_cpu_(*args, **kwargs)
        return manager_handle, storage_handle, size // self.element_size()

    def _shared_decref(self):
        self._storage._shared_decref()
        return self

    @classmethod
    def _release_ipc_counter(cls, *args, device=None, **kwargs):
        unsupported_attr(device)
        return _UntypedStorage._release_ipc_counter_cuda(*args, **kwargs)

    def _shared_incref(self, *args, **kwargs):
        return self._storage._shared_incref(*args, **kwargs)

    def _share_fd_cpu_(self, *args, **kwargs):
        fd, size = self._storage._share_fd_cpu_(*args, **kwargs)
        return fd, size // self.element_size()

    def _get_legacy_storage_class(self):
        return _storage_classes_dict.get(self.dtype, None)


_TypedStorage.type.__doc__ = _type.__doc__
_TypedStorage.cuda.__doc__ = _cuda.__doc__

class _LegacyStorageMeta(type):
    def __instancecheck__(cls, instance):
        if isinstance(instance, _TypedStorage):
            cls_device = 'cuda' if cls.__module__ == 'mindtorch.torch.cuda' else 'cpu'
            return (cls_device == instance.device.type) and (cls.dtype == instance.dtype)
        return False

class _LegacyStorage(_TypedStorage, metaclass=_LegacyStorageMeta):
    @classmethod
    def _new_shared(cls, size):
        """Creates a new storage in shared memory with the same data type"""
        untyped_storage = _UntypedStorage._new_shared(size * cls().element_size())
        return cls(wrap_storage=untyped_storage)

    @classmethod
    def _release_ipc_counter(cls, *args, **kwargs):
        return _UntypedStorage._release_ipc_counter_cuda(*args, **kwargs)

    @classmethod
    def _new_shared_filename(cls, manager, obj, size):
        bytes_size = size * _element_size(cls.dtype)
        return cls(wrap_storage=_UntypedStorage._new_shared_filename_cpu(manager, obj, bytes_size))

def _get_dtype_from_pickle_storage_type(pickle_storage_type: str):
    try:
        return _storage_type_to_dtype_map()[pickle_storage_type]
    except KeyError as e:
        raise KeyError(
            f'pickle storage type "{pickle_storage_type}" is not recognized') from e

class ByteStorage(_LegacyStorage):
    @classproperty
    def dtype(self): # pylint: disable=E0202
        return _dtype.uint8

class DoubleStorage(_LegacyStorage):
    @classproperty
    def dtype(self): # pylint: disable=E0202
        return _dtype.double

class FloatStorage(_LegacyStorage):
    @classproperty
    def dtype(self): # pylint: disable=E0202
        return _dtype.float

class HalfStorage(_LegacyStorage):
    @classproperty
    def dtype(self): # pylint: disable=E0202
        return _dtype.half

class LongStorage(_LegacyStorage):
    @classproperty
    def dtype(self): # pylint: disable=E0202
        return _dtype.long

class IntStorage(_LegacyStorage):
    @classproperty
    def dtype(self): # pylint: disable=E0202
        return _dtype.int

class ShortStorage(_LegacyStorage):
    @classproperty
    def dtype(self): # pylint: disable=E0202
        return _dtype.short

class CharStorage(_LegacyStorage):
    @classproperty
    def dtype(self): # pylint: disable=E0202
        return _dtype.int8

class BoolStorage(_LegacyStorage):
    @classproperty
    def dtype(self): # pylint: disable=E0202
        return _dtype.bool

class BFloat16Storage(_LegacyStorage):
    @classproperty
    def dtype(self): # pylint: disable=E0202
        return _dtype.bfloat16

class ComplexDoubleStorage(_LegacyStorage):
    @classproperty
    def dtype(self): # pylint: disable=E0202
        return _dtype.cdouble

class ComplexFloatStorage(_LegacyStorage):
    @classproperty
    def dtype(self): # pylint: disable=E0202
        return _dtype.cfloat

_storage_classes_dict = {_dtype.double: DoubleStorage,
                         _dtype.float: FloatStorage,
                         _dtype.half: HalfStorage,
                         _dtype.long: LongStorage,
                         _dtype.int: IntStorage,
                         _dtype.int16: ShortStorage,
                         _dtype.int8: CharStorage,
                         _dtype.uint8: ByteStorage,
                         _dtype.bool: BoolStorage,
                         _dtype.bfloat16: BFloat16Storage,
                         _dtype.cdouble: ComplexDoubleStorage,
                         _dtype.cfloat: ComplexFloatStorage,
                         }
