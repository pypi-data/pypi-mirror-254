from typing import Callable
import logging
import re
from .file_handlers import get_format_string, get_rotating_file_handler
from .stream_handlers import get_stdout_handler, get_stderr_handler
from .formaters import ErrorCriticalFormatter
from .config import Config


class DMLogger:
    def __init__(self, logger):
        self.__logger = logger

    def debug(self, message: any = None, **kwargs) -> None:
        self.__log(self.__logger.debug, message, **kwargs)

    def info(self, message: any = None, **kwargs) -> None:
        self.__log(self.__logger.info, message, **kwargs)

    def warning(self, message: any = None, **kwargs) -> None:
        self.__log(self.__logger.warning, message, **kwargs)

    def error(self, message: any = None, **kwargs) -> None:
        self.__log(self.__logger.error, message, **kwargs)

    def critical(self, message: any = None, **kwargs) -> None:
        self.__log(self.__logger.critical, message, **kwargs)

    @staticmethod
    def __log(level_func: Callable, message: any, **kwargs) -> None:
        message = "-- " + str(message) if not (message is None) else ""
        if kwargs:
            dict_string = re.sub(r"'(\w+)':", r"\1:", str(kwargs))
            message = f"{dict_string} {message}"
        level_func(message, stacklevel=3)


class DMLoggerBuilder:
    config: Config = Config
    __loggers: dict = {}
    __file_handlers: dict = {}

    @classmethod
    def create(
        cls,
        name: str,
        level: str = "DEBUG",
        *,
        write_logs: bool = True,
        print_logs: bool = True,
        file_name: str = None
    ) -> DMLogger:
        if name not in cls.__loggers:
            logger = logging.getLogger(name)
            level = logging.getLevelName(level.upper())
            logger.setLevel(level)
            formatter_instance = ErrorCriticalFormatter if cls.config.show_location_label == "auto" else logging.Formatter
            formatter = formatter_instance(get_format_string(cls.config), datefmt='%d-%m-%Y %H:%M:%S')

            if write_logs:
                file_name = file_name or cls.config.file_name
                if file_name not in cls.__file_handlers:
                    cls.__file_handlers[file_name] = get_rotating_file_handler(file_name, cls.config, formatter)
                logger.addHandler(cls.__file_handlers[file_name])

            if print_logs:
                logger.addHandler(get_stdout_handler(formatter))
                logger.addHandler(get_stderr_handler(formatter))

            cls.__loggers[name] = DMLogger(logger)
        return cls.__loggers[name]

