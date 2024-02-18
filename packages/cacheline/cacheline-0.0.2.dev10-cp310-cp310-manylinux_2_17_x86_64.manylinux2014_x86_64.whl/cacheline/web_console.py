import atexit
import os
import sys
from typing import List, Optional


def _start_mux(master: str, target_ip: str, target_port: int):
    pid = os.fork()
    if pid == 0:
        from cacheline._mux import create_mux

        create_mux(master, target_ip, target_port)
        exit(1)
    else:
        return pid


def start_web_console(
    master: str,
    cmd_args: List[str],
    writable: bool = True,
    once: bool = True,
    port: int = 1998,
    interface: Optional[str] = None,
    credential: Optional[str] = None,
    cwd: Optional[str] = None,
):

    if sys.platform != "linux":
        raise NotImplementedError("Web console is only supported on Linux")

    pid_console = os.fork()
    if pid_console == 0:
        from cacheline._web_console import (
            start_web_console as _start_web_console,  # type:ignore
        )

        _start_web_console(
            cmd_args,
            writable=writable,
            once=once,
            port=port,
            interface=interface,
            credential=credential,
            cwd=cwd,
        )
    else:
        mux_pid = _start_mux(master, "127.0.0.1", port)

        def kill_all():
            os.kill(mux_pid, 9)
            os.kill(pid_console, 9)

        atexit.register(kill_all)
        os.waitpid(pid_console, 0)
        os.kill(mux_pid, 9)
        atexit.unregister(kill_all)
