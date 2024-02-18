import sys
import traceback
from multiprocessing import context
import multiprocessing.queues
import multiprocessing
import types
import numpy as np
import mindtorch.torch as torch
from mindtorch.torch.logging import warning

class KeyErrorParse(str):
    """re-implement repr method, which returns itself in repr"""
    def __repr__(self):
        return self

class ExceptionHandler:
    """Wraps an exception with traceback to be raised in main thread/process"""
    def __init__(self, except_info=None, where="in python function"):
        # catch system exception info, when error raised.
        if except_info is None:
            except_info = sys.exc_info()
        self.where = where
        self.except_type = except_info[0]
        self.except_msg = "".join(traceback.format_exception(*except_info))

    def reraise(self):
        """Reraise the caught exception in the main thread/process"""
        # Find the last traceback which is more useful to user.
        index = [i for i in range(len(self.except_msg)) if self.except_msg.startswith('Traceback', i)]
        err_msg = "{}".format(self.except_msg[index[-1]:]).strip()

        if self.except_type == KeyError:
            # As KeyError will call its repr() function automatically, which makes stack info hard to read.
            err_msg = KeyErrorParse(err_msg)
        elif hasattr(self.except_type, "message"):
            raise self.except_type(message=err_msg)
        raise self.except_type(err_msg)


class _SharedQueue(multiprocessing.queues.Queue):
    """
    Class to implement a queue using shared memory for better performance.
    Args:
        size: Number of elements in the queue.
        count: Shared variable to suppress log printing.
        copy_out: Flag to indidcate whether an extra copy should be done before returning.  If data will immediately be
                  copied before returning, then this can be set to False.
        max_rowsize: Maximum size of any element in the Queue in MB.
    """

    def __init__(self, size = 4, max_rowsize=128):
        super().__init__(size, ctx=multiprocessing.get_context())

        # change max_rowsize in MB into bytes
        self.seg_size = max_rowsize * 1024 * 1024
        ##pipe can hold up to 65,636 bytes at a time
        # there is less benefit for small data. To small data it can be slower as we need to pass 100 bytes of metadata
        # and then access the shared memory.
        self.min_shared_mem = 10000
        self.shm_list = []
        self.seg_pos = multiprocessing.Value('i', 0)
        # num_seg has to be 2 more than the queue size.  We can have remote worker filling a buffer, main process
        # reading a buffer and also have a full queue of buffers in the meta-data queue
        self.num_seg = size + 2
        self.data_immediate = 0
        self.data_shared = 1
        self.count = multiprocessing.Value('i', 0)
        self.print_error = True

        try:
            for _ in range(self.num_seg):
                a = multiprocessing.Array("b", self.seg_size)
                self.shm_list.append(a)
        except Exception:
            raise RuntimeError(
                "_SharedQueue: Error allocating "
                + str(self.seg_size / 1024 / 1024)
                + "MB, "
                + str(self.num_seg)
                + " elements."
                + " This might be caused by insufficient shm, and the recommended shm size is at least 5 GB."
            )

    def __getstate__(self):
        context.assert_spawning(self)
        state1 = (self._ignore_epipe, self._maxsize, self._reader, self._writer, self._rlock, self._wlock, self._sem, self._opid)
        state2 = (self.seg_size, self.min_shared_mem, self.shm_list, self.seg_pos, self.num_seg, self.data_immediate, self.data_shared, self.count, self.print_error)
        return state1, state2

    def __setstate__(self, state):
        (self.seg_size, self.min_shared_mem, self.shm_list, self.seg_pos, self.num_seg, self.data_immediate, self.data_shared, self.count, self.print_error) = state[1]
        super().__setstate__(state[0])

    def put(self, data, timeout=None, list_buffer = None):

        def shareput(data):
            bufferlist = []
            for r in data:
                if isinstance(r, (tuple, list)):
                    buf = shareput(r)
                    bufferlist.append(buf)
                else:
                    # the map:pyfunc is a yield generator which can't be serialize
                    if isinstance(r, types.GeneratorType):
                        raise TypeError("Cannot pickle {} object, please verify pyfunc return with numpy array"
                                        .format(type(r)))
                    if (isinstance(r, np.ndarray) and r.size > self.min_shared_mem
                            and self.put_start_bytes + r.nbytes < self.seg_size):
                        # need to convert start_bytes to offset in array
                        start_offset = self.put_start_bytes
                        dest = np.ndarray(r.shape, r.dtype, buffer=self.shm_list[seg_pos].get_obj(),
                                          offset=start_offset)
                        np.copyto(dest, r)
                        byte = r.nbytes
                        byte = 8 * ((byte + 7) // 8)
                        self.put_start_bytes += byte
                        bufferlist.append((self.data_shared, seg_pos, byte, r.dtype, r.shape))
                    else:
                        if isinstance(r, np.ndarray) and r.size > self.min_shared_mem:
                            # Only print out error the first time it happens
                            if self.count.value == 0 and self.print_error:
                                warning(
                                    "Using shared memory queue, but rowsize is larger than allocated memory "
                                    + "max_rowsize: "
                                    + str(self.seg_size / 1024 / 1024)
                                    + "MB, current rowsize: "
                                    + str((self.put_start_bytes + r.nbytes) / 1024 / 1024)
                                    + "MB."
                                )
                                self.print_error = False
                                self.count.value += 1
                        if isinstance(r, torch.Tensor):
                            r.asnumpy()
                        bufferlist.append((self.data_immediate, r))
            if isinstance(data, tuple):
                return tuple(bufferlist)
            return bufferlist
        if isinstance(data, ExceptionHandler):  # pylint: disable=too-many-nested-blocks
            super().put(data, timeout=timeout)
        else:
            self.seg_pos.value = (self.seg_pos.value + 1) % self.num_seg
            seg_pos = self.seg_pos.value
            self.put_start_bytes = 0
            # TODO  (idx, data) data (data,) 、(data, label)、 ((data, data), label) 、((data, data), (label, label)), ({}, label)
            name_list = shareput(data)
            super().put(name_list, timeout=timeout)
            # note above could generate a queue full exception.  It will be handled by teh caller
            # only increment seg_pos after successfully adding to metadata queue

    def get(self, timeout=None):
        result = super().get(timeout=timeout)
        if isinstance(result, ExceptionHandler):
            return result
        self.get_start_bytes = 0
        def shareget(result):
            res = []
            for x in result:
                if x[0] == self.data_shared:
                    seg_pos = x[1]
                    byte = x[2]
                    dtype = x[3]
                    shape = x[4]
                    start_offset = self.get_start_bytes
                    b = self.shm_list[seg_pos]
                    data = np.ndarray(shape, dtype, buffer=b.get_obj(), offset=start_offset)
                    self.get_start_bytes += byte
                    res.append(data)
                elif x[0] == self.data_immediate:
                    res.append(x[1])
                elif isinstance(x[0], (list, tuple)):
                    cur = shareget(x)
                    res.append(cur)
                else:
                    raise RuntimeError("SharedQueue, invalid entry in metadata.")
            if isinstance(result, tuple):
                return tuple(res)
            return res
        return shareget(result)

    def __del__(self):
        shm_list_len = len(self.shm_list)
        for idx in range(shm_list_len):
            del self.shm_list[shm_list_len - idx - 1]
        del self.shm_list

        self.close()
        