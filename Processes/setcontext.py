#!/usr/bin/env python
"""
Setcontext.

######################################################################
# @author      : Linus Fernandes (linusfernandes at gmail dot com)
# @file        : setcontext
# @created     : Sunday Nov 19, 2023 20:19:44 IST
# @description :
# -*- coding: utf-8 -*-'
######################################################################
"""
# SuperFastPython.com
# example of setting the process start context
from multiprocessing import get_context
from concurrent.futures import ProcessPoolExecutor


def main():
    """entry point"""
    # create a start process context
    context = get_context('spawn')
    # create a process pool
    with ProcessPoolExecutor(mp_context=context) as executor:
        # report the context used
        print(executor._mp_context)  # pylint: disable=protected-access


if __name__ == '__main__':
    main()
