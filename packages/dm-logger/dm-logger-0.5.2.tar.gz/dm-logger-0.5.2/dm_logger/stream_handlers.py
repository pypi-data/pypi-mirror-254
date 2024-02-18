import logging
import sys
from .filters import DebugInfoFilter, WarningErrorCriticalFilter


def get_stdout_handler(formatter: logging.Formatter) -> logging.StreamHandler:
    stdout_handler = logging.StreamHandler(sys.stdout)
    stdout_handler.setLevel(logging.DEBUG)
    stdout_handler.addFilter(DebugInfoFilter())
    stdout_handler.setFormatter(formatter)
    return stdout_handler


def get_stderr_handler(formatter: logging.Formatter) -> logging.StreamHandler:
    stdout_handler = logging.StreamHandler(sys.stderr)
    stdout_handler.setLevel(logging.WARNING)
    stdout_handler.addFilter(WarningErrorCriticalFilter())
    stdout_handler.setFormatter(formatter)
    return stdout_handler
