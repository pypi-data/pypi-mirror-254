import typing
from typing import Optional

from ddtrace.span import Span

def init(
    env: Optional[str],
    service: Optional[str],
    version: Optional[str],
    tags: Optional[typing.Dict[str, str]],
    max_nframes: Optional[int],
    url: Optional[str],
) -> None: ...
def start_sample(nframes: int) -> None: ...
def push_cputime(value: int, count: int) -> None: ...
def push_walltime(value: int, count: int) -> None: ...
def push_acquire(value: int, count: int) -> None: ...
def push_release(value: int, count: int) -> None: ...
def push_alloc(value: int, count: int) -> None: ...
def push_heap(value: int) -> None: ...
def push_lock_name(lock_name: str) -> None: ...
def push_frame(name: str, filename: str, address: int, line: int) -> None: ...
def push_threadinfo(thread_id: int, thread_native_id: int, thread_name: Optional[str]) -> None: ...
def push_taskinfo(task_id: int, task_name: str) -> None: ...
def push_exceptioninfo(exc_type: type, count: int) -> None: ...
def push_class_name(class_name: str) -> None: ...
def push_span(span: typing.Optional[Span], endpoint_collection_enabled: bool) -> None: ...
def flush_sample() -> None: ...
def upload() -> None: ...
