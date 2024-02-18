import asyncio
from concurrent.futures import ThreadPoolExecutor
from typing import Any, Awaitable, Generator, List, TypeAlias, TypeVar, Union, cast

from ._async_control import CoroutineManager
from ._downloader import download

_T = TypeVar("_T")
_FutureLike: TypeAlias = Union[Generator[Any, None, _T], Awaitable[_T]]


__all__ = ["CoroutineManager", "download"]

if hasattr(asyncio, "run"):

    def run_gather_sync(*task: _FutureLike[_T]) -> List[_T]:
        """
        invoke asyncio.gather in synchronize context
        """

        async def _wrap() -> List[_T]:
            return await asyncio.gather(*task)

        with ThreadPoolExecutor(max_workers=1) as pool:
            return cast(List[_T], pool.submit(asyncio.run, _wrap()).result())  # type: ignore

    __all__.append("run_gather_sync")
