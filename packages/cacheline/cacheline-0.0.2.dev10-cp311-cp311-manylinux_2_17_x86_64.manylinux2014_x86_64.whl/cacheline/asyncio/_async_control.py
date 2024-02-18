import asyncio
from typing import Any, Coroutine, Dict


class CoroutineManager:
    def __init__(self, max_concurrency: int):
        self.semaphore = asyncio.Semaphore(max_concurrency)
        self._tasks: Dict[int, asyncio.Task] = {}
        self.task_id_generator = 0

        self._draining_tasks = False

    async def _run(self, coroutine: Coroutine[Any, Any, Any], task_id: int):
        async with self.semaphore:
            await coroutine
        self._tasks.pop(task_id)

    async def wait(self):
        self._draining_tasks = True
        for task in list(self._tasks.values()):
            await task
        self._draining_tasks = False

    def submit(self, coroutine: Coroutine[Any, Any, Any]):
        """submit a coroutine to be executed

        Args:
            coroutine (Coroutine[Any, Any, Any]): coroutine

        Example:
        >>> from datetime import datetime
        >>> import asyncio
        >>> async def foo():
        ...     await asyncio.sleep(1)
        >>> async def test():
        ...     cm = CoroutineManager(20)
        ...     start = datetime.now()
        ...     for i in range(100):
        ...         cm.submit(foo())
        ...     await cm.wait()
        ...     end = datetime.now()
        ...     print(abs((end - start).total_seconds()-5) < 1)
        >>> asyncio.run(test())
        True
        """
        if self._draining_tasks:
            raise RuntimeError("Draining tasks")
        self.task_id_generator += 1
        self._tasks[self.task_id_generator] = asyncio.create_task(
            self._run(coroutine, self.task_id_generator)
        )
