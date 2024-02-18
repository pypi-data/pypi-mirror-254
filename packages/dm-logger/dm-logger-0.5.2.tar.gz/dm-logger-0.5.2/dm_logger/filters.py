import logging


class DebugInfoFilter(logging.Filter):
    def filter(self, record):
        return record.levelno in (logging.DEBUG, logging.INFO)


class WarningErrorCriticalFilter(logging.Filter):
    def filter(self, record):
        return record.levelno in (logging.WARNING, logging.ERROR, logging.CRITICAL)
