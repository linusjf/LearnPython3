#!/usr/bin/env python3
"""Unpacking function parameters."""


def myfunc(_x, _y, _z):
    """Print function parameters."""
    print(_x, _y, _z)


TUPLE_VEC = (1, 0, 1)
DICT_VEC = {"_x": 1, "_y": 0, "_z": 1}

myfunc(*TUPLE_VEC)
myfunc(**DICT_VEC)
