#!/usr/bin/env python3
"""Read and write files."""
import os
from os import path
import shutil
import datetime
from datetime import time


def main():
    """Execute main."""
    _f = open("guru99.txt", "w+")
    for i in range(10):
        _f.write("This is line %d\r\n" % (i + 1))
    _f.close()
    # Open the file back and read the contents
    _f = open("guru99.txt", "r")
    if _f.mode == "r":
        contents = _f.read()
        print(contents)
        _f.close()
    # or, readlines reads the individual line into a list
    _f = open("guru99.txt", "r")
    lines = _f.readlines()
    for _x in lines:
        print(_x, end="")

    # Print the name of the OS
    print(os.name)
    # Check for item existence and type
    print("Item exists:" + str(path.exists("guru99.txt")))
    print("Item is a file: " + str(path.isfile("guru99.txt")))
    print("Item is a directory: " + str(path.isdir("guru99.txt")))

    # make a duplicate of an existing file
    if path.exists("guru99.txt"):
        # get the path to the file in the current directory
        src = path.realpath("guru99.txt")
        head, tail = path.split(src)
        print("path:" + head)
        print("file:" + tail)
        # let's make a backup copy by appending "bak" to the name
        dst = src + ".bak"
        # now use the shell to make a copy of the file
        shutil.copy(src, dst)
        # copy over the permissions,modification
        shutil.copystat(src, dst)
        # Get the modification time
        _t = time.ctime(path.getmtime("guru99.txt.bak"))
        print(_t)
        print(datetime.datetime.fromtimestamp(path.getmtime("guru99.txt.bak")))
        # rename the original file
        os.rename("guru99.txt", "career.guru99.txt")


if __name__ == "__main__":
    main()
