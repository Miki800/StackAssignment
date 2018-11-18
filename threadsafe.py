import threading
import functools

def locked(func):
    def wrapper(lockable, *args, **kws):
        try:
            lockable._lock.acquire()
            return_value = func(lockable, *args, **kws)
            return return_value
        finally:
            lockable._lock.release()
    wrapper = functools.update_wrapper(wrapper, func)
    return wrapper

class Lockable(object):
    def __init__(self):
        self._lock = threading.Lock()
