#!/usr/bin/env python
"""
Unpickled.

######################################################################
# @author      : Linus Fernandes (linusfernandes at gmail dot com)
# @file        : unpickled
# @created     : Monday Nov 20, 2023 03:27:51 IST
# @description :
# -*- coding: utf-8 -*-'
######################################################################
"""
# SuperFastPython.com
# example of an argument that does not pickle
from concurrent.futures import ProcessPoolExecutor


def work(file):
    """write to a file"""
    file.write("hi there")
    return "All done!"


def main():
    """entry point"""
    # submit the task
    with open("tmp.txt", "w", encoding="UTF-8") as file:
        # start the process pool
        with ProcessPoolExecutor() as executor:
            # submit the task
            future = executor.submit(work, file)
            # get the result
            result = future.result()
            print(result)


if __name__ == "__main__":
    main()
