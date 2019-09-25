#!/usr/bin/env python3
"""Read and write files."""
import os
from os import path


def main():
    """Execute main."""
    _f = open("guru99.txt", "w+")
    for i in range(10):
        _f.write("This is line %d\r\n" % (i + 1))
    _f.close()
    # Open the file back and read the contents
    _f = open("guru99.txt", "r")
    if _f.mode == 'r':
        contents = _f.read()
        print(contents)
        _f.close()
    # or, readlines reads the individual line into a list
    _f = open("guru99.txt", "r")
    lines = _f.readlines()
    for _x in lines:
        print(_x, end='')

    # Print the name of the OS
    print(os.name)
    # Check for item existence and type
    print("Item exists:" + str(path.exists("guru99.txt")))
    print("Item is a file: " + str(path.isfile("guru99.txt")))
    print("Item is a directory: " + str(path.isdir("guru99.txt")))


if __name__ == "__main__":
    main()
