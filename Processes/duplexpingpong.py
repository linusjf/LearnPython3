#!/usr/bin/env python
"""
Duplexpingpong.

######################################################################
# @author      : Linus Fernandes (linusfernandes at gmail dot com)
# @file        : duplexpingpong
# @created     : Monday Nov 20, 2023 18:41:57 IST
# @description :
# -*- coding: utf-8 -*-'
######################################################################
"""
# SuperFastPython.com
# example of using a duplex pipe between processes
from time import sleep
from secrets import randbelow
from multiprocessing import Process
from multiprocessing import Pipe
from colorama import init
from termcolor import colored


def generate_send(connection, value):
    """Generate and send a value."""
    if value < 10:
        # generate value
        new_value = randbelow(100) / 100.0
        # block
        sleep(new_value)
        # update value
        value = value + new_value
    # report
    print(colored(f'>sending {value}', 'green'), flush=True)
    # send value
    connection.send(value)


def pingpong(connection, send_first):
    """Ping pong between processes."""
    print(colored('Process Running', 'red'), flush=True)
    # check if this process should seed the process
    if send_first:
        generate_send(connection, 0)
    # run until limit reached
    while True:
        # read a value
        value = connection.recv()
        # report
        print(colored(f'>received {value}', 'red'), flush=True)
        # send the value back
        generate_send(connection, value)
        # check for stop
        if value > 10:
            break
    print(colored('Process Done', 'red'), flush=True)


# entry point
if __name__ == '__main__':
    init()
    # create the pipe
    conn1, conn2 = Pipe(duplex=True)
    # create players
    player1 = Process(target=pingpong, args=(conn1, True))
    player2 = Process(target=pingpong, args=(conn2, False))
    # start players
    player1.start()
    player2.start()
    # wait for players to finish
    player1.join()
    player2.join()
