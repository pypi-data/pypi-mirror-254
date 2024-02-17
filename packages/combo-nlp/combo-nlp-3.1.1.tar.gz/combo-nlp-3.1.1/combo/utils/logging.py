import logging
from overrides import overrides
from datetime import datetime


class ComboLogger(logging.Logger):
    def __init__(self, name: str, prefix: str = None, display_date: bool = True):
        super().__init__(name)
        self.__prefix = prefix or ''
        self.__display_date = display_date

    @overrides(check_signature=False)
    def log(self, level: int, msg: str, prefix: str = None):
        prefix = prefix or self.__prefix
        super().log(level, '[{date} UTC {prefix}] {msg}'.format(
            date=datetime.utcnow().strftime('%Y-%m-%d %H:%M:%S'),
            prefix=prefix,
            msg=msg
        ))

    @overrides(check_signature=False)
    def debug(self, msg: str, prefix: str = None):
        self.log(level=logging.DEBUG, msg=msg, prefix=prefix)

    @overrides(check_signature=False)
    def info(self, msg: str, prefix: str = None):
        self.log(level=logging.INFO, msg=msg, prefix=prefix)

    @overrides(check_signature=False)
    def warning(self, msg: str, prefix: str = None):
        self.log(level=logging.WARN, msg=msg, prefix=prefix)

    @overrides(check_signature=False)
    def error(self, msg: str, prefix: str = None):
        self.log(level=logging.ERROR, msg=msg, prefix=prefix)

    @overrides(check_signature=False)
    def fatal(self, msg: str, prefix: str = None):
        self.log(level=logging.FATAL, msg=msg, prefix=prefix)

    @overrides(check_signature=False)
    def critical(self, msg: str, prefix: str = None):
        self.log(level=logging.CRITICAL, msg=msg, prefix=prefix)
