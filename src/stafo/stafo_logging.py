import os
import sys
import logging  # logging module from python std lib


# initialize logging with default loglevel (might be overwritten by command line option)
# see https://docs.python.org/3/howto/logging-cookbook.html


class ExtraFormatter(logging.Formatter):
    def format(self, record: logging.LogRecord) -> str:
        if "line" in record.__dict__.keys():
            line = f' - FNL l.{record.__dict__["line"]}'
        else:
            line = ""
        s = f"{self.formatTime(record, self.datefmt)} - {record.name} - {record.levelname}{line} - {record.getMessage()}"
        return s


defaul_loglevel = logging.INFO
DATEFORMAT = "%H:%M:%S"
h1 = logging.StreamHandler(sys.stdout)
h2 = logging.FileHandler("stafo.log", encoding="utf-8")
h3 = logging.FileHandler("sparql.log", encoding="utf-8")
formatter = ExtraFormatter(None, DATEFORMAT)
for handler in [h1, h2, h3]:
    handler.setFormatter(formatter)
logging.basicConfig(
    level=defaul_loglevel,
    handlers=[h1],
)


logger = logging.getLogger("stafo")
logger.addHandler(h2)

sparql_logger = logging.getLogger("sparql")
sparql_logger.addHandler(h3)
