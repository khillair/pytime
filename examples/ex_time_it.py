# -*- coding: utf-8 -*-
import logging
import time

from pytime import time_it

logger = logging.getLogger("my_custom_logger")


@time_it()
def default():
    time.sleep(0.42)


@time_it(level=logging.INFO)
def level_info():
    time.sleep(0.42)


@time_it(logger=logger)
def custom_logger():
    time.sleep(0.42)


if __name__ == "__main__":
    logging.basicConfig(level=logging.DEBUG)

    default()
    level_info()
    custom_logger()
