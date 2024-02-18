from logging.handlers import RotatingFileHandler
import logging
import os
from .config import Config
from .fs_config import *


def get_rotating_file_handler(file_name: str, options: Config, formatter: logging.Formatter) -> RotatingFileHandler:
    logs_dir_path = options.logs_dir_path or "logs"
    logs_dir_path = os.path.normpath(logs_dir_path)
    if not os.path.exists(logs_dir_path):
        os.makedirs(logs_dir_path)
    log_path = os.path.join(logs_dir_path, file_name)
    file_handler = RotatingFileHandler(log_path, maxBytes=options.max_MB * 1024 * 1024,
                                       backupCount=options.max_count, encoding="utf-8")
    if options.write_mode == "w" and os.path.exists(log_path):
        file_handler.doRollover()
    file_handler.setFormatter(formatter)
    return file_handler


def get_format_string(options: Config) -> str:
    format_string = options.format_string or default_format_string
    if format_string != default_format_string:
        return format_string
    if options.show_name_label is False:
        format_string = format_string.replace(name_fs, "")
    if options.show_location_label is not True:
        format_string = format_string.replace(location_fs, "")
    return format_string
