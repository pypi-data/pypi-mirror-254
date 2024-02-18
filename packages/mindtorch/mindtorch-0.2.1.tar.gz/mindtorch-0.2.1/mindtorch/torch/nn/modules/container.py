#!/usr/bin/env python
# -*- coding: utf-8 -*-
from abc import abstractmethod
import operator
from itertools import chain
from typing import Dict
from collections import OrderedDict, abc as container_abcs
from mindspore.nn.layer.container import _get_prefix_and_index, _valid_index, _valid_cell

from mindtorch.torch.tensor import Tensor, cast_to_adapter_tensor
from mindtorch.torch.nn.parameter import Parameter
from mindtorch.torch._ref import typename
from .module import Module


class Sequential(Module):
    """
    Sequential Module container. For more details about Module, please refer to

    A list of Cells will be added to it in the order they are passed in the constructor.
    Alternatively, an ordered dict of cells can also be passed in.

    Note:
        Sequential and nn.ModuleList are different, ModuleList is a list for storing modules. However,
        the layers in a Sequential are connected in a cascading way.

    Args:
        args (list, OrderedDict): List or OrderedDict of subclass of Module.

    Inputs:
        - **x** (Tensor) - Tensor with shape according to the first Module in the sequence.

    Outputs:
        Tensor, the output Tensor with shape depending on the input `x` and defined sequence of Cells.

    Raises:
        TypeError: If the type of the `args` is not list or OrderedDict.

    Supported Platforms:
        ``Ascend`` ``GPU`` ``CPU``

    Examples:
        >>> conv = nn.Conv2d(3, 2, 3, pad_mode='valid', weight_init="ones")
        >>> relu = nn.ReLU()
        >>> seq = nn.Sequential([conv, relu])
        >>> x = Tensor(np.ones([1, 3, 4, 4]), dtype=mindspore.float32)
        >>> output = seq(x)
        >>> print(output)
        [[[[27. 27.]
           [27. 27.]]
          [[27. 27.]
           [27. 27.]]]]
        >>> from collections import OrderedDict
        >>> d = OrderedDict()
        >>> d["conv"] = conv
        >>> d["relu"] = relu
        >>> seq = nn.Sequential(d)
        >>> x = Tensor(np.ones([1, 3, 4, 4]), dtype=mindspore.float32)
        >>> output = seq(x)
        >>> print(output)
        [[[[27. 27.]
           [27. 27.]]
          [[27. 27.]
           [27. 27.]]]]
    """
    def __init__(self, *args):
        """Initialize Sequential."""
        super(Sequential, self).__init__()
        self._is_dynamic_name = []
        if len(args) == 1:
            cells = args[0]
            if isinstance(cells, list):
                for index, cell in enumerate(cells):
                    self.insert_child_to_cell(str(index), cell)
                    cell.update_parameters_name(str(index) + ".")
                    self._is_dynamic_name.append(True)
            elif isinstance(cells, OrderedDict):
                for name, cell in cells.items():
                    self.insert_child_to_cell(name, cell)
                    cell.update_parameters_name(name + ".")
                    self._is_dynamic_name.append(False)
            elif isinstance(cells, Module):
                for index, cell in enumerate(args):
                    self.insert_child_to_cell(str(index), cell)
                    cell.update_parameters_name(str(index) + ".")
                    self._is_dynamic_name.append(True)
            else:
                raise TypeError(f"For '{self.__class__.__name__}', the 'args[0]' must be list or orderedDict, "
                                f"but got {type(cells).__name__}")
        else:
            for index, cell in enumerate(args):
                self.insert_child_to_cell(str(index), cell)
                cell.update_parameters_name(str(index) + ".")
                self._is_dynamic_name.append(True)
        self.cell_list = list(self._cells.values())

    def __getitem__(self, index):
        if isinstance(index, slice):
            return self.__class__(
                OrderedDict(list(self._cells.items())[index]))
        if isinstance(index, Tensor):
            index = int(index)
        index = _valid_index(len(self), index, self.__class__.__name__)
        return list(self._cells.values())[index]

    def __setitem__(self, index, module):
        if isinstance(index, Tensor):
            index = int(index)
        cls_name = self.__class__.__name__
        if _valid_cell(module, cls_name):
            prefix, _ = _get_prefix_and_index(self._cells)
            index = _valid_index(len(self), index, cls_name)
            key = list(self._cells.keys())[index]
            self._cells[key] = module
            module.update_parameters_name(prefix + key + ".")
            self.cell_list = list(self._cells.values())

    def __delitem__(self, index):
        cls_name = self.__class__.__name__
        if isinstance(index, int):
            index = _valid_index(len(self), index, cls_name)
            key = list(self._cells.keys())[index]
            del self._cells[key]
            del self._is_dynamic_name[index]
        elif isinstance(index, slice):
            keys = list(self._cells.keys())[index]
            for key in keys:
                del self._cells[key]
            del self._is_dynamic_name[index]
        else:
            raise TypeError(f"For '{cls_name}', the type of index must be int type or slice type, "
                            f"but got {type(index).__name__}")
        prefix, key_index = _get_prefix_and_index(self._cells)
        temp_dict = OrderedDict()
        for idx, key in enumerate(self._cells.keys()):
            cell = self._cells[key]
            if self._is_dynamic_name[idx]:
                for _, param in cell.parameters_and_names():
                    param.name = prefix + str(idx) + "." + ".".join(param.name.split(".")[key_index+1:])
                temp_dict[str(idx)] = cell
            else:
                temp_dict[key] = cell
        self._cells = temp_dict
        self.cell_list = list(self._cells.values())

    def __len__(self):
        return len(self._cells)

    def __bool__(self):
        return len(self._cells) != 0

    def __add__(self, other):
        if isinstance(other, Sequential):
            ret = Sequential()
            for layer in self:
                self.append(ret, layer)
            for layer in other:
                self.append(ret, layer)
            return ret
        else:
            raise ValueError('add operator supports only objects '
                             'of Sequential class, but {} is given.'.format(
                             str(type(other))))

    def __iadd__(self, other):
        if isinstance(other, Sequential):
            offset = len(self)
            for i, module in enumerate(other):
                self.add_module(str(i + offset), module)
            return self
        else:
            raise ValueError('add operator supports only objects '
                             'of Sequential class, but {} is given.'.format(
                             str(type(other))))

    def __mul__(self, other):
        if not isinstance(other, int):
            raise TypeError(f"unsupported operand type(s) for *: {type(self)} and {type(other)}")
        elif other <= 0:
            raise ValueError(f"Non-positive multiplication factor {other} for {type(self)}")
        else:
            combined = Sequential()
            offset = 0
            for _ in range(other):
                for module in self:
                    combined.add_module(str(offset), module)
                    offset += 1
            return combined

    def __rmul__(self, other):
        return self.__mul__(other)

    def __imul__(self, other):
        if not isinstance(other, int):
            raise TypeError(f"unsupported operand type(s) for *: {type(self)} and {type(other)}")
        elif other <= 0:
            raise ValueError(f"Non-positive multiplication factor {other} for {type(self)}")
        else:
            len_original = len(self)
            offset = len(self)
            for _ in range(other - 1):
                for i in range(len_original):
                    self.add_module(str(i + offset), self._cells[str(i)])
                offset += len_original
            return self

    def __dir__(self):
        keys = Module.__dir__(self)
        keys = [key for key in keys if not key.isdigit()]
        return keys

    def __iter__(self):
        return iter(self._cells.values())

    @property
    def _modules(self):
        return self._cells

    def set_grad(self, flag=True):
        self.requires_grad = flag
        for cell in self._cells.values():
            cell.set_grad(flag)

    def append(self, module):
        """
        Appends a given Module to the end of the list.

        Args:
            module(Module): The Module to be appended.

        Examples:
            >>> conv = nn.Conv2d(3, 2, 3, pad_mode='valid', weight_init="ones")
            >>> bn = nn.BatchNorm2d(2)
            >>> relu = nn.ReLU()
            >>> seq = nn.Sequential([conv, bn])
            >>> seq.append(relu)
            >>> x = Tensor(np.ones([1, 3, 4, 4]), dtype=mindspore.float32)
            >>> output = seq(x)
            >>> print(output)
            [[[[26.999863 26.999863]
               [26.999863 26.999863]]
              [[26.999863 26.999863]
               [26.999863 26.999863]]]]
        """
        if _valid_cell(module, self.__class__.__name__):
            prefix, _ = _get_prefix_and_index(self._cells)
            module.update_parameters_name(prefix + str(len(self)) + ".")
            self._is_dynamic_name.append(True)
            self._cells[str(len(self))] = module
        self.cell_list = list(self._cells.values())
        return self

    def add_module(self, name, module):
        if not isinstance(module, Module) and module is not None:
            raise TypeError("{} is not a Module subclass".format(
                module.__name__))
        elif hasattr(self, name) and name not in self._cells:
            raise KeyError("attribute '{}' already exists".format(name))
        elif '.' in name:
            raise KeyError("module name can't contain \".\", got: {}".format(name))
        elif name == '':
            raise KeyError("module name can't be empty string \"\"")

        if _valid_cell(module, self.__class__.__name__):
            module.update_parameters_name(name + ".")
            self._is_dynamic_name.append(False)

        self._cells[name] = module
        self.cell_list = list(self._cells.values())

    def forward(self, input):
        for cell in self.cell_list:
            input = cell(input)
        return cast_to_adapter_tensor(input)

    def pop(self, key):
        v = self[key]
        del self[key]
        return v

    def extend(self, sequential):
        for layer in sequential:
            self.append(layer)
        return self

    def insert(self, index, module):
        """
        Inserts a given Cell before a given index in the list.

        Args:
            index(int): The Insert index in the CellList.
            cell(Cell): The Cell to be inserted.
        """
        cls_name = self.__class__.__name__
        idx = _valid_index(len(self), index, cls_name)
        _valid_cell(module, cls_name)
        length = len(self)
        prefix, key_index = _get_prefix_and_index(self._cells)
        while length > idx:
            if self._auto_prefix:
                tmp_cell = self._cells[str(length-1)]
                for _, param in tmp_cell.parameters_and_names():
                    param.name = f'{prefix}{str(length)}{"."}{".".join(param.name.split(".")[key_index+1:])}'
            self._cells[str(length)] = self._cells[str(length - 1)]
            length -= 1
        self._cells[str(idx)] = module
        if self._auto_prefix:
            module.update_parameters_name(prefix + str(idx) + ".")
        self.cell_list = list(self._cells.values())
        self._is_dynamic_name.insert(index, True)

#_ModuleListBase is similar to ms.nn._CellListBase
class _ModuleListBase:
    """
    An interface for base the Module as list.

    The sequential Module may be iterated using the construct method using for-in statement.
    But there are some scenarios that the construct method built-in does not fit.
    For convenience, we provide an interface that indicates the sequential
    Module may be interpreted as list of Cells, so it can be accessed using
    iterator or subscript when a sequential Module instantiate is accessed
    by iterator or subscript, it will be interpreted as a list of Cells.
    """
    def __init__(self):
        """Initialize _ModuleListBase."""
        self.__cell_as_list__ = True  #for ms jit parse

    @abstractmethod
    def __len__(self):
        pass

    @abstractmethod
    def __getitem__(self, index):
        pass

class ModuleList(_ModuleListBase, Module):
    """
    Holds Cells in a list.
    ModuleList can be used like a regular Python list, the Cells it contains have been initialized.

    Args:
    modules (iterable, optional): an iterable of modules to add

    Examples:
        class MyModule(nn.Module):
            def __init__(self):
                super(MyModule, self).__init__()
                self.linears = nn.ModuleList([nn.Linear(10, 10) for i in range(10)])

            def forward(self, x):
                # ModuleList can act as an iterable, or be indexed using ints
                for i, l in enumerate(self.linears):
                    x = self.linears[i // 2](x) + l(x)
                return x
    """
    def __init__(self, modules=None):
        """Initialize ModuleList."""
        _ModuleListBase.__init__(self)
        Module.__init__(self)
        if modules is not None:
            self.extend(modules)

    def __getitem__(self, idx):
        if isinstance(idx, Tensor):
            idx = int(idx)
        cls_name = self.__class__.__name__
        if isinstance(idx, slice):
            return self.__class__(list(self._cells.values())[idx])
        if isinstance(idx, int):
            idx = _valid_index(len(self), idx, cls_name)
            return self._cells[str(idx)]
        raise TypeError(f"For '{cls_name}', the type of 'idx' must be int or slice, "
                        f"but got {type(idx).__name__}.")

    def __setitem__(self, idx, module):
        if isinstance(idx, Tensor):
            idx = int(idx)
        cls_name = self.__class__.__name__
        if not isinstance(idx, int) and _valid_cell(module, cls_name):
            raise TypeError(f"For '{cls_name}', the type of 'idx' must be int, "
                            f"but got {type(idx).__name__}.")
        idx = _valid_index(len(self), idx, cls_name)
        if self._auto_prefix:
            prefix, _ = _get_prefix_and_index(self._cells)
            module.update_parameters_name(prefix + str(idx) + ".")
        self._cells[str(idx)] = module

    def __delitem__(self, idx):
        if isinstance(idx, Tensor):
            idx = int(idx)
        cls_name = self.__class__.__name__
        if isinstance(idx, int):
            idx = _valid_index(len(self), idx, cls_name)
            del self._cells[str(idx)]
        elif isinstance(idx, slice):
            keys = list(self._cells.keys())[idx]
            for key in keys:
                del self._cells[key]
        else:
            raise TypeError(f"For '{cls_name}', the type of 'index' must be int or slice, "
                            f"but got {type(idx).__name__}.")
        # adjust orderedDict
        prefix, key_index = _get_prefix_and_index(self._cells)
        temp_dict = OrderedDict()
        for id, cell in enumerate(self._cells.values()):
            if self._auto_prefix:
                for _, param in cell.parameters_and_names():
                    param.name = prefix + str(id) + "." + ".".join(param.name.split(".")[key_index+1:])
            temp_dict[str(id)] = cell
        self._cells = temp_dict

    def __len__(self):
        return len(self._cells)

    def __iter__(self):
        return iter(self._cells.values())

    def __iadd__(self, modules):
        return self.extend(modules)

    def __add__(self, other):
        combined = ModuleList()
        for _, module in enumerate(chain(self, other)):
            combined.append(module)
        return combined

    def __dir__(self):
        keys = super(ModuleList, self).__dir__()
        keys = [key for key in keys if not key.isdigit()]
        return keys

    def pop(self, key):
        v = self[key]
        del self[key]
        return v

    def insert(self, index, module):
        """
        Inserts a given Module before a given index in the list.

        Args:
            index(int): The Insert index in the ModuleList.
            module(Module): The Module to be inserted.
        """
        cls_name = self.__class__.__name__
        #TODO: after _valid_index fixed, below code can be remove
        if len(self) == 0 and index == 0:
            idx = index
        else:
            idx = _valid_index(len(self), index, cls_name)
        _valid_cell(module, cls_name)
        length = len(self)
        prefix, key_index = _get_prefix_and_index(self._cells)
        while length > idx:
            if self._auto_prefix:
                tmp_cell = self._cells[str(length-1)]
                for _, param in tmp_cell.parameters_and_names():
                    param.name = prefix + str(length) + "." + ".".join(param.name.split(".")[key_index+1:])
            self._cells[str(length)] = self._cells[str(length - 1)]
            length -= 1
        self._cells[str(idx)] = module
        if self._auto_prefix:
            module.update_parameters_name(prefix + str(idx) + ".")

    def extend(self, modules):
        """
        Appends Cells from a Python iterable to the end of the list.

        Args:
            cells(list): The Cells to be extended.

        Raises:
            TypeError: If the argument cells are not a list of Cells.
        """
        cls_name = self.__class__.__name__
        if not isinstance(modules, container_abcs.Iterable):
            raise TypeError("ModuleList.extend should be called with an "
                            "iterable, but got " + type(modules).__name__)
        prefix, _ = _get_prefix_and_index(self._cells)
        for module in modules:
            if _valid_cell(module, cls_name):
                if self._auto_prefix:
                    module.update_parameters_name(prefix + str(len(self)) + ".")
                self._cells[str(len(self))] = module
        return self

    def append(self, module):
        """
        Appends a given Module to the end of the list.

        Args:
            module(Module): The subcell to be appended.
        """
        if _valid_cell(module, self.__class__.__name__):
            if self._auto_prefix:
                prefix, _ = _get_prefix_and_index(self._cells)
                module.update_parameters_name(prefix + str(len(self)) + ".")
            self._cells[str(len(self))] = module

    def set_grad(self, flag=True):
        self.requires_grad = flag
        for cell in self._cells.values():
            cell.set_grad(flag)

class ModuleDict(Module):
    r"""Holds submodules in a dictionary.

    :class:`nn.ModuleDict` can be indexed like a regular Python dictionary,
    but modules it contains are properly registered, and will be visible by all
    :class:`nn.Module` methods.

    :class:`nn.ModuleDict` is an **ordered** dictionary that respects

    * the order of insertion, and

    * in :meth:`nn.ModuleDict.update`, the order of the merged
      ``OrderedDict``, ``dict`` (started from Python 3.6) or another
      :class:`nn.ModuleDict` (the argument to
      :meth:`nn.ModuleDict.update`).

    Note that :meth:`nn.ModuleDict.update` with other unordered mapping
    types (e.g., Python's plain ``dict`` before Python version 3.6) does not
    preserve the order of the merged mapping.

    Args:
        modules (iterable, optional): a mapping (dictionary) of (string: module)
            or an iterable of key-value pairs of type (string, module)

    Example::

        class MyModule(nn.Module):
            def __init__(self):
                super(MyModule, self).__init__()
                self.choices = nn.ModuleDict({
                        'conv': nn.Conv2d(10, 10, 3),
                        'pool': nn.MaxPool2d(3)
                })
                self.activations = nn.ModuleDict([
                        ['lrelu', nn.LeakyReLU()],
                        ['prelu', nn.PReLU()]
                ])

            def forward(self, x, choice, act):
                x = self.choices[choice](x)
                x = self.activations[act](x)
                return x
    """

    def __init__(self, modules=None):
        super(ModuleDict, self).__init__()
        self.__cell_as_dict__ = True
        if modules is not None:
            self.update(modules)

    def __getitem__(self, key):
        return self._cells[key]

    def __setitem__(self, key, module):
        self._update_cell_para_name(key, module)
        self.add_module(key, module)

    def __delitem__(self, key):
        del self._cells[key]

    def __len__(self):
        return len(self._cells)

    def __iter__(self):
        return iter(self._cells)

    def __contains__(self, key):
        return key in self._cells

    def _update_cell_para_name(self, key, cell):
        if self._auto_prefix:
            prefix, _ = _get_prefix_and_index(self._cells)
            cell.update_parameters_name(prefix + key + ".")

    def clear(self):
        """Remove all items from the ModuleDict.
        """
        self._cells.clear()

    def pop(self, key):
        r"""Remove key from the ModuleDict and return its module.

        Args:
            key (str): key to pop from the ModuleDict
        """
        v = self[key]
        del self[key]
        return v

    def keys(self):
        r"""Return an iterable of the ModuleDict keys.
        """
        return self._cells.keys()

    def items(self):
        r"""Return an iterable of the ModuleDict key/value pairs.
        """
        return self._cells.items()

    def values(self):
        r"""Return an iterable of the ModuleDict values.
        """
        return self._cells.values()

    def update(self, modules):
        r"""Update the :class:`nn.ModuleDict` with the key-value pairs from a
        mapping or an iterable, overwriting existing keys.

        .. note::
            If :attr:`modules` is an ``OrderedDict``, a :class:`nn.ModuleDict`, or
            an iterable of key-value pairs, the order of new elements in it is preserved.

        Args:
            modules (iterable): a mapping (dictionary) from string to :class:`nn.Module`,
                or an iterable of key-value pairs of type (string, :class:`nn.Module`)
        """
        if not isinstance(modules, container_abcs.Iterable):
            raise TypeError("ModuleDict.update should be called with an "
                            "iterable of key/value pairs, but got " +
                            type(modules).__name__)

        if isinstance(modules, (OrderedDict, ModuleDict, container_abcs.Mapping)):
            for key, module in modules.items():
                self[key] = module
        else:
            # modules here can be a list with two items
            for j, m in enumerate(modules):
                if not isinstance(m, container_abcs.Iterable):
                    raise TypeError("ModuleDict update sequence element "
                                    "#" + str(j) + " should be Iterable; is" +
                                    type(m).__name__)
                if not len(m) == 2:
                    raise ValueError("ModuleDict update sequence element "
                                     "#" + str(j) + " has length " + str(len(m)) +
                                     "; 2 is required")
                # modules can be Mapping (what it's typed at), or a list: [(name1, module1), (name2, module2)]
                # that's too cumbersome to type correctly with overloads, so we add an ignore here
                self[m[0]] = m[1]  # type: ignore[assignment]

    # remove forward alltogether to fallback on Module's _forward_unimplemented


class ParameterList(Module):
    """Holds parameters in a list.

    :class:`nn.ParameterList` can be used like a regular Python
    list, but Tensors that are :class:`nn.Parameter` are properly registered,
    and will be visible by all :class:`nn.Module` methods.

    Note that the constructor, assigning an element of the list, the
    :meth:`nn.ParameterDict.append` method and the :meth:`nn.ParameterDict.extend`
    method will convert any :class:`Tensor` into :class:`nn.Parameter`.

    Args:
        parameters (iterable, optional): an iterable of elements to add to the list.

    Example::

        class MyModule(nn.Module):
            def __init__(self):
                super(MyModule, self).__init__()
                self.params = nn.ParameterList([nn.Parameter(ms_torch.randn(10, 10)) for i in range(10)])

            def forward(self, x):
                # ParameterList can act as an iterable, or be indexed using ints
                for i, p in enumerate(self.params):
                    x = self.params[i // 2].mm(x) + p.mm(x)
                return x
    """

    def __init__(self, values=None):
        super(ParameterList, self).__init__()
        self._size = 0
        if values is not None:
            self += values

    def _get_abs_string_index(self, idx):
        """Get the absolute index for the list of modules"""
        idx = operator.index(idx)
        if not -len(self) <= idx < len(self):
            raise IndexError('index {} is out of range'.format(idx))
        if idx < 0:
            idx += len(self)
        return str(idx)

    def __getitem__(self, idx):
        if isinstance(idx, slice):
            start, stop, step = idx.indices(len(self))
            out = self.__class__()
            for i in range(start, stop, step):
                out.append(self[i])
            return out
        else:
            idx = self._get_abs_string_index(idx)
            return getattr(self, str(idx))

    def __setitem__(self, idx, param):
        # Note that all other function that add an entry to the list part of
        # the ParameterList end up here. So this is the only place where we need
        # to wrap things into Parameter if needed.
        # Objects added via setattr() are not in the list part and thus won't
        # call into this function.
        idx = self._get_abs_string_index(idx)
        if isinstance(param, Tensor) and not isinstance(param, Parameter):
            param = Parameter(param)
        return setattr(self, str(idx), param)

    def __len__(self):
        return self._size

    def __iter__(self):
        return iter(self[i] for i in range(len(self)))

    def __iadd__(self, parameters):
        return self.extend(parameters)

    def __dir__(self):
        keys = super(ParameterList, self).__dir__()
        keys = [key for key in keys if not key.isdigit()]
        return keys

    def append(self, value):
        """Appends a given value at the end of the list.

        Args:
            value (Any): value to append
        """
        new_idx = len(self)
        self._size += 1
        self[new_idx] = value
        return self

    def extend(self, values):
        """Appends values from a Python iterable to the end of the list.

        Args:
            values (iterable): iterable of values to append
        """
        # Tensor is an iterable but we never want to unpack it here
        if not isinstance(values, container_abcs.Iterable) or isinstance(values, Tensor):
            raise TypeError("ParameterList.extend should be called with an "
                            "iterable, but got " + type(values).__name__)
        for value in values:
            self.append(value)
        return self

    def extra_repr(self):
        child_lines = []
        for k, p in enumerate(self):
            if isinstance(p, Tensor):
                size_str = 'x'.join(str(size) for size in p.size())
                device_str = '' if not p.is_cuda else ' (GPU {})'.format(p.get_device())
                parastr = '{} containing: [{} of size {}{}]'.format(
                    "Parameter" if isinstance(p, Parameter) else "Tensor",
                    p.dtype, size_str, device_str)
                child_lines.append('  (' + str(k) + '): ' + parastr)
            else:
                child_lines.append('  (' + str(k) + '): Object of type: ' + type(p).__name__)

        tmpstr = '\n'.join(child_lines)
        return tmpstr

    def __call__(self, *args, **kwargs):
        raise RuntimeError('ParameterList should not be called.')

    # adpater api, to convert ParameterList to list[Parameter]
    def to_list(self):
        list_params = []
        for i, p in enumerate(self):
            p.name = str(i) + "." + p.name
            list_params.append(p)
        return list_params


class ParameterDict(Module):
    """Holds parameters in a dictionary.

    ParameterDict can be indexed like a regular Python dictionary, but Parameters it
    contains are properly registered, and will be visible by all Module methods.
    Other objects are treated as would be done by a regular Python dictionary

    :class:`nn.ParameterDict` is an **ordered** dictionary.
    :meth:`nn.ParameterDict.update` with other unordered mapping
    types (e.g., Python's plain ``dict``) does not preserve the order of the
    merged mapping. On the other hand, ``OrderedDict`` or another :class:`nn.ParameterDict`
    will preserve their ordering.

    Note that the constructor, assigning an element of the dictionary and the
    :meth:`nn.ParameterDict.update` method will convert any :class:`Tensor` into
    :class:`nn.Parameter`.

    Args:
        values (iterable, optional): a mapping (dictionary) of
            (string : Any) or an iterable of key-value pairs
            of type (string, Any)

    Example::

        class MyModule(nn.Module):
            def __init__(self):
                super(MyModule, self).__init__()
                self.params = nn.ParameterDict({
                        'left': nn.Parameter(ms_torch.randn(5, 10)),
                        'right': nn.Parameter(ms_torch.randn(5, 10))
                })

            def forward(self, x, choice):
                x = self.params[choice].mm(x)
                return x
    """

    def __init__(self, parameters = None):
        super(ParameterDict, self).__init__()
        self._keys: Dict[str, None] = {}
        if parameters is not None:
            self.update(parameters)

    def _key_to_attr(self, key):
        if not isinstance(key, str):
            raise TypeError("Index given to ParameterDict cannot be used as a key as it is "
                            f"not a string (type is '{type(key).__name__}'). Open an issue on "
                            "github if you need non-string keys.")
        else:
            # Use the key as-is so that `.named_parameters()` returns the right thing
            return key

    def __getitem__(self, key):
        attr = self._key_to_attr(key)
        return getattr(self, attr)

    def __setitem__(self, key, value):
        # Note that all other function that add an entry to the dictionary part of
        # the ParameterDict end up here. So this is the only place where we need
        # to wrap things into Parameter if needed.
        # Objects added via setattr() are not in the dictionary part and thus won't
        # call into this function.
        self._keys[key] = None
        attr = self._key_to_attr(key)
        if isinstance(value, Tensor) and not isinstance(value, Parameter):
            value = Parameter(value)
        setattr(self, attr, value)

    def __delitem__(self, key):
        del self._keys[key]
        attr = self._key_to_attr(key)
        delattr(self, attr)

    def __len__(self):
        return len(self._keys)

    def __iter__(self):
        return iter(self._keys)

    def __reversed__(self):
        return reversed(list(self._keys))

    def copy(self):
        """Returns a copy of this :class:`nn.ParameterDict` instance.
        """
        # We have to use an OrderedDict because the ParameterDict constructor
        # behaves differently on plain dict vs OrderedDict
        return ParameterDict(OrderedDict((k, self[k]) for k in self._keys))

    def __contains__(self, key):
        return key in self._keys

    def setdefault(self, key, default = None):
        """If key is in the ParameterDict, return its value.
        If not, insert `key` with a parameter `default` and return `default`.
        `default` defaults to `None`.

        Args:
            key (str): key to set default for
            default (Any): the parameter set to the key
        """

        if key not in self:
            self[key] = default
        return self[key]

    def clear(self):
        """Remove all items from the ParameterDict.
        """
        for k in self._keys.copy():
            del self[k]

    def pop(self, key):
        r"""Remove key from the ParameterDict and return its parameter.

        Args:
            key (str): key to pop from the ParameterDict
        """
        v = self[key]
        del self[key]
        return v

    def popitem(self):
        """Remove and return the last inserted `(key, parameter)` pair
        from the ParameterDict
        """
        k, _ = self._keys.popitem()
        # We need the key in the _keys to be able to access/del
        self._keys[k] = None
        val = self[k]
        del self[k]
        return k, val

    def get(self, key, default = None):
        r"""Return the parameter associated with key if present.
        Otherwise return default if provided, None if not.

        Args:
            key (str): key to get from the ParameterDict
            default (Parameter, optional): value to return if key not present
        """
        return self[key] if key in self else default

    def fromkeys(self, keys, default = None):
        r"""Return a new ParameterDict with the keys provided

        Args:
            keys (iterable, string): keys to make the new ParameterDict from
            default (Parameter, optional): value to set for all keys
        """
        return ParameterDict(((k, default) for k in keys))

    def keys(self):
        r"""Return an iterable of the ParameterDict keys.
        """
        return self._keys.keys()

    def items(self):
        r"""Return an iterable of the ParameterDict key/value pairs.
        """
        return ((k, self[k]) for k in self._keys)

    def values(self):
        r"""Return an iterable of the ParameterDict values.
        """
        return (self[k] for k in self._keys)

    def update(self, parameters):
        r"""Update the :class:`~nn.ParameterDict` with the key-value pairs from a
        mapping or an iterable, overwriting existing keys.

        .. note::
            If :attr:`parameters` is an ``OrderedDict``, a :class:`~nn.ParameterDict`, or
            an iterable of key-value pairs, the order of new elements in it is preserved.

        Args:
            parameters (iterable): a mapping (dictionary) from string to
                :class:`~nn.Parameter`, or an iterable of
                key-value pairs of type (string, :class:`~nn.Parameter`)
        """
        if not isinstance(parameters, container_abcs.Iterable):
            raise TypeError("ParametersDict.update should be called with an "
                            "iterable of key/value pairs, but got " +
                            type(parameters).__name__)

        if isinstance(parameters, (OrderedDict, ParameterDict)):
            for key, parameter in parameters.items():
                self[key] = parameter
        elif isinstance(parameters, container_abcs.Mapping):
            for key, parameter in sorted(parameters.items()):
                self[key] = parameter
        else:
            for j, p in enumerate(parameters):
                if not isinstance(p, container_abcs.Iterable):
                    raise TypeError("ParameterDict update sequence element "
                                    "#" + str(j) + " should be Iterable; is" +
                                    type(p).__name__)
                if not len(p) == 2:
                    raise ValueError("ParameterDict update sequence element "
                                     "#" + str(j) + " has length " + str(len(p)) +
                                     "; 2 is required")
                # parameters as length-2 list too cumbersome to type, see ModuleDict.update comment
                self[p[0]] = p[1]  # type: ignore[assignment]

    def extra_repr(self):
        child_lines = []
        for k, p in self.items():
            if isinstance(p, Tensor):
                size_str = 'x'.join(str(size) for size in p.size())
                device_str = '' if not p.is_cuda else ' (GPU {})'.format(p.get_device())
                parastr = '{} containing: [{} of size {}{}]'.format(
                    "Parameter" if isinstance(p, Parameter) else "Tensor",
                    typename(p), size_str, device_str)
                child_lines.append('  (' + str(k) + '): ' + parastr)
            else:
                child_lines.append('  (' + str(k) + '): Object of type: ' + type(p).__name__)
        tmpstr = '\n'.join(child_lines)
        return tmpstr

    def __call__(self, input):
        raise RuntimeError('ParameterDict should not be called.')

    def __or__(self, other):
        copy = self.copy()
        copy.update(other)
        return copy

    def __ror__(self, other):
        copy = other.copy()
        copy.update(self)
        return copy

    def __ior__(self, other):
        self.update(other)
        return self

    def to_dict(self):
        new_dict = {}
        for key in self._keys:
            new_dict[key] = self[key]
        return new_dict
