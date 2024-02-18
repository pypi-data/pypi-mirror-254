import logging
from .fs_config import location_fs, message_fs


class ErrorCriticalFormatter(logging.Formatter):
    def format(self, record):
        original_format = str(self._style._fmt)
        if record.levelno >= logging.ERROR and location_fs not in self._style._fmt:
            self._style._fmt = self._style._fmt.split(message_fs)[0] + location_fs + message_fs
        result = super().format(record)
        self._style._fmt = original_format
        return result
