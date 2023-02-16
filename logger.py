import datetime
import logging
from logging.handlers import TimedRotatingFileHandler
from tglogging import TelegramLogHandler #disinstall if you ever get around doing your own
import sys

DATE_FORMAT = "%Y-%m-%dT%H:%M:%S%z" #ISO-8601 format in UTC
HUMAN_FORMAT = logging.Formatter("%(name)-8s: [%(asctime)-24s %(msecs)dms] <%(levelname)-8s> %(filename)-10s: %(funcName)-10s #%(message)s", datefmt=DATE_FORMAT)
MACHINE_FORMAT = ...

class LucaFileHandler(logging.FileHandler):
    def __init__(self,file) -> None:
        super().__init__(file)
        self.setFormatter(HUMAN_FORMAT)
        self.setLevel(logging.INFO)

class LucaTimeRotator(TimedRotatingFileHandler):
    def __init__(self, filename: str, when: str = "D", interval: int = 1, backupCount: int = 7, encoding: str | None = None, delay: bool = False, utc: bool = False, atTime: datetime.time | None = datetime.time(2,0,0), errors: str | None = None) -> None:
        super().__init__(filename, when, interval, backupCount, encoding, delay, utc, atTime, errors)
        self.setFormatter(HUMAN_FORMAT)
        self.setLevel(logging.DEBUG)

class LucaTelegramStream(TelegramLogHandler):
    def __init__(self,token,chat_id) -> None:
        super().__init__(token,chat_id,update_interval = 2)
        self.setFormatter(HUMAN_FORMAT)
        self.setLevel(logging.WARNING)

class LucaLogger(logging.Logger):
    def __init__(self,name) -> None:
        super().__init__(name,logging.DEBUG)

    def new_stream(self) -> None:
        handle = logging.StreamHandler(sys.stdout)
        handle.setFormatter(HUMAN_FORMAT)
        self.addHandler(handle)
        
    def new_file(self, file) -> None:
        handle = LucaFileHandler(file)
        self.addHandler(handle)

    def new_time_rotator(self,file, **kwargs) -> None:
        handle = LucaTimeRotator(file, **kwargs)
        self.addHandler(handle)

    def telegram_bot(self,token,chat_id,):
        handle = LucaTelegramStream(token,chat_id)
        self.addHandler(handle)






# https://pypi.org/project/colorlog/


# https://docs.python.org/3/howto/logging-cookbook.html#implementing-structured-logging
# https://github.com/madzak/python-json-logger
# https://docs.python.org/3/library/logging.html#logging.Formatter
# https://docs.python.org/3/library/logging.handlers.html