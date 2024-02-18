import logging
import sys
from typing import Optional


def _setup_debug_hook():
    from better_exceptions import hook  # pylint: disable=import-outside-toplevel

    hook()


def _setup_debug_logging(log_filepath: Optional[str] = None):
    import colorlog  # pylint:disable=import-outside-toplevel

    root = logging.getLogger()
    root.setLevel(logging.DEBUG)
    for handler in root.handlers:
        root.removeHandler(handler)

    stream_handler = colorlog.StreamHandler(sys.stdout)
    stream_handler.setLevel(logging.DEBUG)
    stream_handler.setFormatter(
        colorlog.ColoredFormatter(
            "%(asctime)s %(log_color)s%(levelname)-8s%(reset)s %(message_log_color)s%(message)s %(reset)s%(pathname)s:%(lineno)d ",
            datefmt=None,
            reset=True,
            log_colors={
                "DEBUG": "cyan",
                "INFO": "green",
                "WARNING": "yellow",
                "ERROR": "red",
                "CRITICAL": "red,bg_white",
            },
            secondary_log_colors={
                "message": {
                    "DEBUG": "cyan",
                    "INFO": "green",
                    "WARNING": "yellow",
                    "ERROR": "red",
                    "CRITICAL": "red,bg_white",
                }
            },
            style="%",
        )
    )
    root.addHandler(stream_handler)

    if log_filepath:
        file_handler = logging.FileHandler(log_filepath)
        file_handler.setLevel(logging.DEBUG)
        file_handler.setFormatter(
            logging.Formatter(
                "%(asctime)s - %(name)s - %(levelname)s - 🌟 %(message)s - %(pathname)s:%(lineno)d"
            )
        )
        root.addHandler(file_handler)


def enable_debugger_mode(
    *,
    logging_path: Optional[str] = None,
    better_exceptions: bool = True,
):
    """
    Enable debugger mode.
    Args:
        logging_path: Path to save the logs.
        better_exceptions: Use better_exceptions to print the exception.
    """
    _setup_debug_logging(logging_path)
    if better_exceptions:
        _setup_debug_hook()
