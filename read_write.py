#!/usr/bin/env python3
"""Read and write files."""


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


if __name__ == "__main__":
    main()
