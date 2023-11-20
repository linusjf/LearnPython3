#!/usr/bin/env python
"""
Pipe.

######################################################################
# @author      : Linus Fernandes (linusfernandes at gmail dot com)
# @file        : pipe
# @created     : Monday Nov 20, 2023 18:17:52 IST
# @description :
# -*- coding: utf-8 -*-'
######################################################################
"""
# SuperFastPython.com
# example of using a pipe between processes
from time import sleep
from secrets import randbelow
from multiprocessing import Process
from multiprocessing import Pipe
from colorama import init
from termcolor import colored


def sender(connection):
    """Generate work."""
    print(colored('Sender: Running', 'green'), flush=True)
    # generate work
    for _ in range(10):
        # generate a value
        value = randbelow(100) / 100.0
        # block
        sleep(value)
        print(colored(f'Sending...{value}', 'green'), flush=True)
        # send data
        connection.send(value)
    # all done
    connection.send(None)
    print(colored('Sender: Done', 'green'), flush=True)


def receiver(connection):
    """Consume work."""
    print('Receiver: Running', flush=True)
    # consume work
    while True:
        value = randbelow(100) / 100.0
        sleep(value)
        # get a unit of work
        item = connection.recv()
        # report
        print(f'>receiver got {item}', flush=True)
        # check for stop
        if item is None:
            break
    # all done
    print('Receiver: Done', flush=True)


# entry point
if __name__ == '__main__':
    init()
    # create the pipe
    conn1, conn2 = Pipe()
    # start the sender
    sender_process = Process(target=sender, args=(conn2,))
    sender_process.start()
    # start the receiver
    receiver_process = Process(target=receiver, args=(conn1,))
    receiver_process.start()
    # wait for all processes to finish
    sender_process.join()
    receiver_process.join()
