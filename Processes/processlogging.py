#!/usr/bin/env python
"""
Logging.

######################################################################
# @author      : Linus Fernandes (linusfernandes at gmail dot com)
# @file        : logging
# @created     : Friday Nov 24, 2023 13:44:12 IST
# @description :
# -*- coding: utf-8 -*-'
######################################################################
"""
# SuperFastPython.com
# example of logging from multiple processes in a process-safe manner
from secrets import randbelow
from time import sleep
from multiprocessing import current_process
from multiprocessing import Process
from multiprocessing import Queue
from logging.handlers import QueueHandler
import logging


def logger_process(que):
    """executed in a process that performs logging"""
    # create a logger
    _logger = logging.getLogger('app')
    # configure a stream handler
    _logger.addHandler(logging.StreamHandler())
    # log all messages, debug and up
    _logger.setLevel(logging.DEBUG)
    # run forever
    while True:
        # consume a log message, block until one arrives
        message = que.get()
        # check for shutdown
        if message is None:
            break
        # log the message
        _logger.handle(message)


def task(que):
    """task to be executed in child processes"""
    # create a logger
    _logger = logging.getLogger('app')
    # add a handler that uses the shared queue
    _logger.addHandler(QueueHandler(que))
    # log all messages, debug and up
    _logger.setLevel(logging.DEBUG)
    # get the current process
    _process = current_process()
    # report initial message
    _logger.info('Child %s starting.', _process.name)
    # simulate doing work
    for i in range(5):
        # report a message
        _logger.debug('Child %s step %d.', _process.name, i)
        # block
        sleep(randbelow(100) / 100.0)
    # report final message
    _logger.info('Child %s done.', _process.name)


# protect the entry point
if __name__ == '__main__':
    # create the shared queue
    queue = Queue()
    # create a logger
    logger = logging.getLogger('app')
    # add a handler that uses the shared queue
    logger.addHandler(QueueHandler(queue))
    # log all messages, debug and up
    logger.setLevel(logging.DEBUG)
    # start the logger process
    logger_p = Process(target=logger_process, args=(queue,))
    logger_p.start()
    # report initial message
    logger.info('Main process started.')
    # configure child processes
    processes = [Process(target=task, args=(queue,)) for _ in range(5)]
    # start child processes
    for process in processes:
        process.start()
    # wait for child processes to finish
    for process in processes:
        process.join()
    # report final message
    logger.info('Main process done.')
    # shutdown the queue correctly
    queue.put(None)
