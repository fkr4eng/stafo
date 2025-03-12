import os
import sys
import logging  # logging module from python std lib


# initialize logging with default loglevel (might be overwritten by command line option)
# see https://docs.python.org/3/howto/logging-cookbook.html

defaul_loglevel = logging.INFO
FORMAT = "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
DATEFORMAT = "%H:%M:%S"
logging.basicConfig(
    level=defaul_loglevel,
    format=FORMAT,
    datefmt=DATEFORMAT,
    handlers=[
        logging.FileHandler("stafo.log"),
        logging.StreamHandler(sys.stdout)
    ],
)


logger = logging.getLogger("stafo")