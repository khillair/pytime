# -*- coding: utf-8 -*-
import time

from pytime import Timer


def no_context():
    timer = Timer().start()

    time.sleep(0.42)
    print(f"no_context, timer no finished, but still getting the elapsed time: {timer}")
    time.sleep(0.42)

    timer.stop()
    print(f"no_context 1, total elapsed time: {timer}")


def using_context_1():
    with Timer() as timer:
        time.sleep(0.42)
    print(f"using_context 1., elapsed time: {timer}")


def using_context_2():
    timer = Timer()

    # do things...

    with timer:
        time.sleep(0.42)
    print(f"using_context 2.1., elapsed time: {timer}")

    # do things...

    with timer:  # no need to instianciate another timer
        time.sleep(0.42)
    print(f"using_context 2.2, elapsed time: {timer}")


if __name__ == "__main__":
    no_context()
    using_context_1()
    using_context_2()
