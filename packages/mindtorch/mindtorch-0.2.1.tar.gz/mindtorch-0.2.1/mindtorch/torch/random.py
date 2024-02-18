import mindspore as ms
import numpy as np


def manual_seed(seed):
    return ms.set_seed(seed)


def seed():
    value = np.floor(np.random.random(1) * 2**32 - 1)
    return ms.set_seed(int(value))


def initial_seed():
    return ms.get_seed()
