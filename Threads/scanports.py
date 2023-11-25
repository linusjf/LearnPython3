#!/usr/bin/env python
"""
Scanports.

######################################################################
# @author      : Linus Fernandes (linusfernandes at gmail dot com)
# @file        : scanports
# @created     : Saturday Nov 25, 2023 14:31:28 IST
# @description :
# -*- coding: utf-8 -*-'
######################################################################
"""
# SuperFastPython.com
# scan a range of port numbers on a host concurrently
from socket import AF_INET
from socket import SOCK_STREAM
from socket import socket
from multiprocessing.pool import ThreadPool


def test_port_number(_host, port):
    """returns True if a connection can be made, False otherwise"""
    # create and configure the socket
    with socket(AF_INET, SOCK_STREAM) as sock:
        # set a timeout of a few seconds
        sock.settimeout(3)
        # connecting may fail
        try:
            # attempt to connect
            sock.connect((_host, port))
            # a successful connection was made
            return True
        except OSError:
            # ignore the failure
            return False


def port_scan(_host, _ports):
    """scan port numbers on a host"""
    print(f'Scanning {_host}...')
    # create the thread pool
    with ThreadPool(len(_ports)) as pool:
        # prepare the arguments
        args = [(_host, port) for port in _ports]
        # dispatch all tasks
        results = pool.starmap(test_port_number, args)
        # report results in order
        for port, is_open in zip(ports, results):
            if is_open:
                print(f'> {_host}:{port} open')


# protect the entry point
if __name__ == '__main__':
    # define host and port numbers to scan
    HOST = 'python.org'
    ports = range(1024)
    # test the ports
    port_scan(HOST, ports)
