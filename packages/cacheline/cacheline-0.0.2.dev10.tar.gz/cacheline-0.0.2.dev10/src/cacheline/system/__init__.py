from __future__ import annotations

import asyncio
import logging
from collections import defaultdict
from pathlib import Path
from typing import IO, Callable, List, Union

import aiofiles

IOType = Union[Callable[[str], None], IO, str, Path, None]


def _io_process(io: IOType):
    """
    truncate file if it exists
    """
    if not isinstance(io, (str, Path)):
        return
    path = Path(io) if isinstance(io, str) else io
    if path.is_dir():
        raise ValueError(f"{path} is a directory")
    if path.exists():
        path.unlink(missing_ok=True)
    path.touch()


async def run_command(
    args: List[str],
    stdout: IOType = None,
    stderr: IOType = None,
    cwd: str | Path | None = None,
    env: dict[str, str] | None = None,
) -> int:
    """
    execute a command and handle the output
    if handler is a callable, it will be called with each line of output
    if handler is a file-like object, the output will be written to it and close when finished
    if handler is a file path, the output will be appended to the file
    """

    _io_process(stdout)
    _io_process(stderr)

    file_ref_count: dict[str, int] = defaultdict(int)

    async def read_stream(stream, handler):
        async_file_obj = None
        if isinstance(handler, (str, Path)):
            async_file_obj = await aiofiles.open(handler, "a+", encoding="utf-8")
            file_ref_count[str(handler)] += 1
            handler = async_file_obj

        while True:
            line = await stream.readline()
            if not line:  # End of file
                break
            try:
                if callable(handler):
                    handler(line.decode().rstrip())
                elif hasattr(handler, "write"):
                    await handler.write(line.decode())
                else:
                    raise ValueError(
                        "Handler must be a callable, a file-like object, or a file path"
                    )
            except Exception as e:  # pylint:disable=broad-except
                logging.error(
                    "An exception occurred in the stream handler: %s", e, exc_info=True
                )
            finally:
                if async_file_obj and file_ref_count[str(handler)] == 1:
                    await async_file_obj.close()
                else:
                    file_ref_count[str(handler)] -= 1

    try:
        # Create subprocess
        logging.debug(
            "Executing command: %s",
            " ".join([f"'{a}'" for a in args]),
        )
        process = await asyncio.create_subprocess_exec(
            *args,
            stdout=asyncio.subprocess.PIPE if stdout else None,
            stderr=asyncio.subprocess.PIPE if stderr else None,
            cwd=str(cwd) if cwd else None,
            env=env,
        )

        async def nop():
            ...

        await asyncio.gather(
            read_stream(process.stdout, stdout) if stdout else nop(),
            read_stream(process.stderr, stderr) if stderr else nop(),
        )

        # Wait for the subprocess to finish
        return await process.wait()

    except asyncio.CancelledError:
        process.kill()
        await process.wait()
        raise

    except Exception as e:  # pylint:disable=broad-except
        logging.error("An error occurred while executing the command: %s", e)
        return -1


if __name__ == "__main__":
    from cacheline import enable_debugger_mode

    enable_debugger_mode()

    async def main():
        await run_command(
            [
                "bash",
                "-c",
                "ls -lah",
            ],
            stdout=print,
            stderr=print,
        )

    asyncio.run(main())
