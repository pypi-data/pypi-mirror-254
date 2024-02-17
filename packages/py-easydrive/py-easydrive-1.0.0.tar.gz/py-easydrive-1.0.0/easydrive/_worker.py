from threading import Thread, Event
from concurrent.futures import Future as ConcurrentFuture, ThreadPoolExecutor
from typing import Any, Optional, Callable, ParamSpec, TypeVar
from asyncio import new_event_loop, run_coroutine_threadsafe
from collections.abc import Awaitable

__all__ = (
    "AsyncWorker",
    "get_single_worker"
)
T = TypeVar('T')
P = ParamSpec('P')
POOL = ThreadPoolExecutor()

class AsyncWorker(Thread):
    def __init__(self):
        self._setup_complete_event = Event()

        super().__init__(daemon=True)
        pass

    def run(self):
        self._loop = new_event_loop()
        self._setup_complete_event.set()

        self._loop.run_forever()
        pass

    def run_future(self, 
        future: Awaitable[T], 
        blocking: bool=True, 
        completion_callback: Callable[
            [ConcurrentFuture],
            None
        ]|None= None,
        timeout: Optional[float]=None
        ) -> T:
        con_future: ConcurrentFuture = run_coroutine_threadsafe(future, self._loop)
        
        if completion_callback is not None:
            con_future.add_done_callback(completion_callback)
            pass
        
        if blocking: 
            res = con_future.result(timeout)
            return res
            pass
        else:
            return con_future
            pass
        pass

    @property
    def setup_complete(self) -> bool:
        return self._setup_complete_event.is_set()
        pass

    def wait_for_setup_completion(self, timeout: Optional[float]=None):
        self._setup_complete_event.wait()
        pass

    def stop(self):
        self._loop.stop()
        pass
    pass


_SINGLE: AsyncWorker|None = None
def get_single_worker():
    global _SINGLE

    if _SINGLE is None:
        _SINGLE= AsyncWorker()
        _SINGLE.start()
        _SINGLE.wait_for_setup_completion()
        pass

    return _SINGLE
    pass


def make_concurrent(func: Callable[P, Any]) -> Callable[P, None]:
    # Decorator wrapping a callback to be run concurrently using a thread pool
    def wrapper(*args: P.args, **kwargs: P.kwargs) -> None:
        POOL.submit(func, *args, **kwargs)
    
    return wrapper
    pass