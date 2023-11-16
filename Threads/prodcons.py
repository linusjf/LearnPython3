#!/usr/bin/env python
"""
Prodcons.

######################################################################
# @author      : Linus Fernandes (linusfernandes at gmail dot com)
# @file        : prodcons
# @created     : Thursday Nov 16, 2023 16:18:48 IST
# @description :
# -*- coding: utf-8 -*-'
######################################################################
"""
# SuperFastPython.com
# example of using the queue
from time import sleep
from secrets import randbelow
from threading import Thread
from queue import Queue


def producer(_queue):
    """generate work"""
    print('Producer: Running')
    # generate work
    for _ in range(10):
        # generate a value
        value = randbelow(10)
        # block
        sleep(value)
        # add to the queue
        _queue.put(value)
    # all done
    _queue.put(None)
    print('Producer: Done')


def consumer(_queue):
    """consume work"""
    print('Consumer: Running')
    # consume work
    while True:
        # get a unit of work
        item = _queue.get()
        # check for stop
        if item is None:
            break
        # report
        print(f'>got {item}')
    # all done
    print('Consumer: Done')


# create the shared queue
queue = Queue()
# start the consumer
consumer = Thread(target=consumer, args=(queue,))
consumer.start()
# start the producer
producer = Thread(target=producer, args=(queue,))
producer.start()
# wait for all threads to finish
producer.join()
consumer.join()
