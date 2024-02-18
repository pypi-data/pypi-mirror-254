from mindtorch.utils import get_backend

def is_built():
    backend = get_backend()
    if backend in ('GPU', 'Ascend'):
        return True
    return False


class cuFFTPlanCacheAttrContextProp():
    # Like regular ContextProp, but uses the `.device_index` attribute from the
    # calling object as the first argument to the getter and setter.
    def __init__(self, getter, setter):
        self.getter = getter
        self.setter = setter

    def __get__(self, obj, objtype):
        return self.getter(obj.device_index)

    def __set__(self, obj, val):
        if isinstance(self.setter, str):
            raise RuntimeError(self.setter)
        self.setter(obj.device_index, val)
