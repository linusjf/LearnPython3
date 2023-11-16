#!/usr/bin/env python
"""
Countdownlatch.

######################################################################
# @author      : Linus Fernandes (linusfernandes at gmail dot com)
# @file        : countdownlatch
# @created     : Thursday Nov 16, 2023 10:36:26 IST
# @description :
# -*- coding: utf-8 -*-'
######################################################################
"""
# SuperFastPython.com
from threading import Condition
from threading import Thread
from time import sleep
from secrets import randbelow


class CountDownLatch():
    """simple countdown latch, starts closed then
    opens once count is reached
    """
    def __init__(self, count):
        """# constructor"""
        # store the count
        self.count = count
        # control access to the count and notify when latch is open
        self.condition = Condition()

    def count_down(self):
        """count down the latch by one increment"""
        # acquire the lock on the condition
        with self.condition:
            # check if the latch is already open
            if self.count == 0:
                return
            # decrement the counter
            self.count -= 1
            # check if the latch is now open
            if self.count == 0:
                # notify all waiting threads that the latch is open
                self.condition.notify_all()

    def wait(self):
        """wait for the latch to open"""
        # acquire the lock on the condition
        with self.condition:
            # check if the latch is already open
            if self.count == 0:
                return
            # wait to be notified when the latch is open
            self.condition.wait()


def test_count_down_latch():
    """Test function"""
    def count_down(_latch: CountDownLatch, num: int):
        sleep(randbelow(5))
        print(f"Counting down thread {num}")
        _latch.count_down()

    count = 4
    latch = CountDownLatch(count)

    for i in range(count):
        thread = Thread(target=count_down, args=(latch, i))
        thread.start()

    print("Waiting for latch...")
    latch.wait()
    print("Latch released...")


test_count_down_latch()
