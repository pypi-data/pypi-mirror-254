import os
import io
import struct
import sys
import importlib
import pickle
import pathlib
from collections.abc import Mapping, Sequence
from typing import Any, BinaryIO, Union, IO
from pickle import UnpicklingError
from typing_extensions import TypeAlias
from mindtorch.torch.tensor import msdapter_dtype, tensor
from mindtorch.torch.nn.modules.module import Module
from mindtorch.utils import unsupported_attr
from mindtorch.torch.logging import warning

DEFAULT_PROTOCOL = 2

LONG_SIZE = struct.Struct('=l').size
INT_SIZE = struct.Struct('=i').size
SHORT_SIZE = struct.Struct('=h').size

MAGIC_NUMBER = 0x1950a86a20f9469cfc6c
PROTOCOL_VERSION = 1001

string_classes = (str, bytes)

FILE_LIKE: TypeAlias = Union[str, os.PathLike, BinaryIO, IO[bytes]]

__all__ = [
    'save',
    'load',
]

def dict_convert(state_dict):

    pt = try_import("torch")

    _dtypeConvertor = {
        pt.float16: msdapter_dtype.float16,
        pt.float32: msdapter_dtype.float32,
        pt.float64: msdapter_dtype.float64,
        pt.int8: msdapter_dtype.int8,
        pt.int16: msdapter_dtype.int16,
        pt.int32: msdapter_dtype.int32,
        pt.int64: msdapter_dtype.int64,
        pt.uint8: msdapter_dtype.uint8,
        pt.bool: msdapter_dtype.bool,
        pt.complex64: msdapter_dtype.complex64,
        pt.complex128: msdapter_dtype.complex128,
        pt.long: msdapter_dtype.int64,
    }

    elem_type = type(state_dict)
    if isinstance(state_dict, pt.Tensor):
        origin_dtype = state_dict.dtype
        origin_dtype = _dtypeConvertor[origin_dtype]
        data = state_dict.detach().numpy()
        if not data.flags.owndata:
            data = data.copy()
        return tensor(data, dtype=origin_dtype)
    elif isinstance(state_dict, Mapping):
        try:
            return elem_type({key: dict_convert(state_dict[key]) for key in state_dict})
        except TypeError:
            return {key: dict_convert(state_dict[key]) for key in state_dict}
    elif isinstance(state_dict, tuple) and hasattr(state_dict, '_fields'):
        return elem_type(*(dict_convert(d) for d in state_dict))
    elif isinstance(state_dict, (tuple, list)):
        return [dict_convert(d) for d in state_dict]
    elif isinstance(state_dict, Sequence) and not isinstance(state_dict, string_classes):
        try:
            return elem_type([dict_convert(d) for d in state_dict])
        except TypeError:
            return [dict_convert(d) for d in state_dict]
    else:
        return state_dict


def try_import(module_name):
    """Try importing a module, with an informative error message on failure."""
    install_name = module_name

    if module_name.find('.') > -1:
        install_name = module_name.split('.')[0]

    try:
        mod = importlib.import_module(module_name)
        return mod
    except (Exception,) as error:
        err_msg = (
            "Failed importing {}. This likely means that some torch modules "
            "require additional dependencies that have to be "
            "manually installed (usually with `pip install {}`). ").format(
                module_name, install_name)
        raise ImportError(err_msg) from error

def check_module_version_greater_or_equal(module, req_version_tuple, error_if_malformed=True):
    '''
    Check if a module's version satisfies requirements

    Usually, a module's version string will be like 'x.y.z', which would be represented
    as a tuple (x, y, z), but sometimes it could be an unexpected format. If the version
    string does not match the given tuple's format up to the length of the tuple, then
    error and exit or emit a warning.

    Args:
        module: the module to check the version of
        req_version_tuple: tuple (usually of ints) representing the required version
        error_if_malformed: whether we should exit if module version string is malformed

    Returns:
        requirement_is_met: bool
    '''

    version_strs = module.__version__.split('.')
    # Cast module version fields to match the types of the required version
    module_version = tuple(
        type(req_field)(version_strs[idx]) for idx, req_field in enumerate(req_version_tuple)
    )
    try:
        requirement_is_met = module_version >= req_version_tuple

    except RuntimeError as e:
        message = (
            "'%s' module version string is malformed '%s' and cannot be compared"
            " with tuple %s"
        ) % (
            module.__name__, module.__version__, str(req_version_tuple)
        )
        if error_if_malformed:
            raise RuntimeError(message) from e
        else:
            warning(message + ', but continuing assuming that requirement is met')
            requirement_is_met = True

    return requirement_is_met


def _is_path(name_or_buffer):
    return isinstance(name_or_buffer, (str, pathlib.Path))


class _opener():
    def __init__(self, file_like):
        self.file_like = file_like

    def __enter__(self):
        return self.file_like

    def __exit__(self, *args):
        pass


class _open_file(_opener):
    def __init__(self, name, mode):
        super(_open_file, self).__init__(open(name, mode))

    def __exit__(self, *args):
        self.file_like.close()


class _open_buffer_reader(_opener):
    def __init__(self, buffer):
        super(_open_buffer_reader, self).__init__(buffer)
        _check_seekable(buffer)


class _open_buffer_writer(_opener):
    def __exit__(self, *args):
        self.file_like.flush()


def _open_file_like(name_or_buffer, mode):
    if _is_path(name_or_buffer):
        return _open_file(name_or_buffer, mode)
    else:
        if 'w' in mode:
            return _open_buffer_writer(name_or_buffer)
        elif 'r' in mode:
            return _open_buffer_reader(name_or_buffer)
        else:
            raise RuntimeError(f"Expected 'r' or 'w' in mode but got {mode}")

def _check_seekable(f) -> bool:

    def raise_err_msg(patterns, e):
        for p in patterns:
            if p in str(e):
                msg = (str(e) + ". You can only torch.load from a file that is seekable."
                                + " Please pre-load the data into a buffer like io.BytesIO and"
                                + " try to load from it instead.")
                raise type(e)(msg)
        raise e

    try:
        f.seek(f.tell())
        return True
    except (io.UnsupportedOperation, AttributeError) as e:
        raise_err_msg(["seek", "tell"], e)
    return False

def _check_dill_version(pickle_module) -> None:
    '''Checks if using dill as the pickle module, and if so, checks if it is the correct version.
    If dill version is lower than 0.3.1, a ValueError is raised.

    Args:
        pickle_module: module used for pickling metadata and objects

    '''
    if pickle_module is not None and pickle_module.__name__ == 'dill':
        required_dill_version = (0, 3, 1)
        if not check_module_version_greater_or_equal(pickle_module, required_dill_version, False):
            raise ValueError((
                "'torch' supports dill >= %s, but you have dill %s."
                " Please upgrade dill or switch to 'pickle'"
            ) % (
                '.'.join([str(num) for num in required_dill_version]),
                pickle_module.__version__
            ))

def save(
    obj: object,
    f: FILE_LIKE,
    pickle_module: Any = pickle,
    pickle_protocol: int = DEFAULT_PROTOCOL,
    _use_new_zipfile_serialization: bool = False
) -> None:
    # The first line of this docstring overrides the one Sphinx generates for the
    # documentation. We need it so that Sphinx doesn't leak `pickle`s path from
    # the build environment (e.g. `<module 'pickle' from '/leaked/path').

    """save(obj, f, pickle_module=pickle, pickle_protocol=DEFAULT_PROTOCOL, _use_new_zipfile_serialization=True)

    Saves an object to a disk file.

    See also: :ref:`saving-loading-tensors`

    Args:
        obj: saved object
        f: a file-like object (has to implement write and flush) or a string or
           os.PathLike object containing a file name
        pickle_module: module used for pickling metadata and objects
        pickle_protocol: can be specified to override the default protocol

    Example:
        >>> # Save to file
        >>> x = torch.tensor([0, 1, 2, 3, 4])
        >>> torch.save(x, 'tensor.pt')
        >>> # Save to io.BytesIO buffer
        >>> buffer = io.BytesIO()
        >>> torch.save(x, buffer)
    """
    _check_dill_version(pickle_module)

    if _use_new_zipfile_serialization:
        unsupported_attr(_use_new_zipfile_serialization)

    with _open_file_like(f, 'wb') as opened_file:
        _legacy_save(obj, opened_file, pickle_module, pickle_protocol)


def _legacy_save(obj, f, pickle_module, pickle_protocol) -> None:
    sys_info = dict(
        protocol_version=PROTOCOL_VERSION,
        little_endian=sys.byteorder == 'little',
        type_sizes=dict(
            short=SHORT_SIZE,
            int=INT_SIZE,
            long=LONG_SIZE,
        ),
    )

    if isinstance(obj, Module):
        raise ValueError(
            'Currently, saving model structure (modules) is not supported. If you want to save module\'s parameters, '
            'please using module.state_dict() to replace.'
        )
    elif isinstance(obj, dict):
        for key, value in obj.items():
            if isinstance(value, Module):
                raise ValueError(
                    f'Currently, saving model structure (modules) is not supported, but got a module object '
                    f'[\'{key}\']. If you want to save module\'s parameters, please using \'{key}\':'
                    f'module.state_dict() to replace.'
                )
    elif isinstance(obj, (list, tuple)):
        for i, item in enumerate(obj):
            if isinstance(item, Module):
                raise ValueError(
                    f'Currently, saving model structure (modules) is not supported, but got a module object '
                    f'inputs[{i}]. If you want to save module\'s parameters, please using module.state_dict() '
                    f'to replace.'
                )

    pickle_module.dump(MAGIC_NUMBER, f, protocol=pickle_protocol)
    pickle_module.dump(PROTOCOL_VERSION, f, protocol=pickle_protocol)
    pickle_module.dump(sys_info, f, protocol=pickle_protocol)
    pickler = pickle_module.Pickler(f, protocol=pickle_protocol)
    pickler.dump(obj)
    f.flush()


def load(
    f: FILE_LIKE,
    map_location = None,
    pickle_module: Any = pickle,
    **pickle_load_args: Any
) -> Any:

    """load(f, from_torch : Optional = False, map_location=None, pickle_module=pickle, **pickle_load_args)

    Loads an object saved with :func:`torch.save` from a file.

    :func:`torch.load` uses Python's unpickling facilities but treats storages,
    which underlie tensors, specially. They are first deserialized on the
    CPU and are then moved to the device they were saved from. If this fails
    (e.g. because the run time system doesn't have certain devices), an exception
    is raised. However, storages can be dynamically remapped to an alternative
    set of devices using the :attr:`map_location` argument.

    If :attr:`map_location` is a callable, it will be called once for each serialized
    storage with two arguments: storage and location. The storage argument
    will be the initial deserialization of the storage, residing on the CPU.
    Each serialized storage has a location tag associated with it which
    identifies the device it was saved from, and this tag is the second
    argument passed to :attr:`map_location`. The builtin location tags are ``'cpu'``
    for CPU tensors and ``'cuda:device_id'`` (e.g. ``'cuda:2'``) for CUDA tensors.
    :attr:`map_location` should return either ``None`` or a storage. If
    :attr:`map_location` returns a storage, it will be used as the final deserialized
    object, already moved to the right device. Otherwise, :func:`torch.load` will
    fall back to the default behavior, as if :attr:`map_location` wasn't specified.

    If :attr:`map_location` is a :class:`torch.device` object or a string containing
    a device tag, it indicates the location where all tensors should be loaded.

    Otherwise, if :attr:`map_location` is a dict, it will be used to remap location tags
    appearing in the file (keys), to ones that specify where to put the
    storages (values).

    User extensions can register their own location tags and tagging and
    deserialization methods using :func:`torch.serialization.register_package`.

    Args:
        f: a file-like object (has to implement :meth:`read`, :meth:`readline`, :meth:`tell`, and :meth:`seek`),
            or a string or os.PathLike object containing a file name
        map_location: a function, :class:`torch.device`, string or a dict specifying how to remap storage
            locations
        pickle_module: module used for unpickling metadata and objects (has to
            match the :attr:`pickle_module` used to serialize file)
        pickle_load_args: (Python 3 only) optional keyword arguments passed over to
            :func:`pickle_module.load` and :func:`pickle_module.Unpickler`, e.g.,
            :attr:`errors=...`.

    Example:
        >>> # xdoctest: +SKIP("undefined filepaths")
        >>> torch.load('tensors.pt')
    """

    try:
        _check_dill_version(pickle_module)

        if map_location:
            unsupported_attr(map_location)

        if 'encoding' not in pickle_load_args.keys():
            pickle_load_args['encoding'] = 'utf-8'

        with _open_file_like(f, 'rb') as opened_file:
            # The zipfile reader is going to advance the current file position.
            # If we want to actually tail call to torch.jit.load, we need to
            # reset back to the original position.
            return _legacy_load(opened_file, pickle_module, **pickle_load_args)

    except UnpicklingError:
        pt = try_import('torch')
        state = pt.load(
            f, map_location ='cpu', pickle_module=pickle_module, **pickle_load_args
        )
        if isinstance(state, pt.nn.Module):
            print("Importing torch model file into MindTorch is not supported now.")
        return dict_convert(state)

    except Exception as e: # pylint: disable=broad-except
        template = "An exception of type {0} occurred. Arguments:\n{1!r}"
        message = template.format(type(e).__name__, e.args)
        print(message)
        print("The load function currently only supports Torch model files and MindTorch model files now.")

    return None

def _legacy_load(f, pickle_module, **pickle_load_args):

    _check_seekable(f)

    if not hasattr(f, 'readinto') and (3, 8, 0) <= sys.version_info < (3, 8, 2):
        raise RuntimeError(
            "torch.load does not work with file-like objects that do not implement readinto on Python 3.8.0 and 3.8.1. "
            f"Received object of type \"{type(f)}\". Please update to Python 3.8.2 or newer to restore this "
            "functionality.")

    magic_number = pickle_module.load(f, **pickle_load_args)
    if magic_number != MAGIC_NUMBER:
        raise RuntimeError("Invalid magic number; corrupt file?")
    protocol_version = pickle_module.load(f, **pickle_load_args)
    if protocol_version != PROTOCOL_VERSION:
        raise RuntimeError("Invalid protocol version: %s" % protocol_version)

    _sys_info = pickle_module.load(f, **pickle_load_args)
    unpickler = pickle_module.Unpickler(f, **pickle_load_args)
    result = unpickler.load()
    return result
