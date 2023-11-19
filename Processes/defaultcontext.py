#!/usr/bin/env python
"""
Defaultcontext.

######################################################################
# @author      : Linus Fernandes (linusfernandes at gmail dot com)
# @file        : defaultcontext
# @created     : Sunday Nov 19, 2023 20:16:37 IST
# @description :
# -*- coding: utf-8 -*-'
######################################################################
"""
# SuperFastPython.com
# example of checking the process start context
from concurrent.futures import ProcessPoolExecutor


def main():
    """entry point"""
    # create a process pool
    with ProcessPoolExecutor() as executor:
        # report the context used
        print(executor._mp_context)  # pylint: disable=protected-access


if __name__ == '__main__':
    main()
