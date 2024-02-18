from typing import Iterable
from packaging.version import Version, InvalidVersion

__all__ = ['TorchVersion', 'Version', 'InvalidVersion']

class TorchVersion(str):
    def _convert_to_version(self, inp):
        if isinstance(inp, Version):
            return inp
        elif isinstance(inp, str):
            return Version(inp)
        elif isinstance(inp, Iterable):
            return Version('.'.join((str(item) for item in inp)))
        else:
            raise InvalidVersion(inp)

    def _cmp_wrapper(self, cmp, method):
        try:
            return getattr(Version(self), method)(self._convert_to_version(cmp))
        except InvalidVersion:
            return getattr(super(), method)(cmp)


for cmp_method in ["__gt__", "__lt__", "__eq__", "__ge__", "__le__"]:
    setattr(TorchVersion, cmp_method, lambda x, y, method=cmp_method: x._cmp_wrapper(y, method))

internal_version = version = "1.12.1"
__version__ = TorchVersion(internal_version)
