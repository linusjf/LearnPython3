#!/usr/bin/env python
"""
Parentheses.

######################################################################
# @author      : Linus Fernandes (linusfernandes at gmail dot com)
# @file        : parentheses
# @created     : Tuesday Mar 07, 2023 08:43:56 IST
# @description :
# -*- coding: utf-8 -*-'
######################################################################
"""
from timeit import timeit
import regex


def check(val):  # noqa
    """Check."""
    counter = 0
    for character in val:
        if character == "(":
            counter += 1
        elif character == ")":
            counter -= 1
        else:
            raise AttributeError("invalid character in the argument")
        if counter < 0:
            return False
    return counter == 0


def regexcheck(val):  # noqa
    """Regex Check."""
    return bool(regex.search(r"^(\((?1)*\))(?1)*$", val))


print(timeit('check("(((()))())")', number=100000, globals=globals()))
print(timeit('regexcheck("(((()))())")', number=100000, globals=globals()))
print(timeit('check("(((())())")', number=100000, globals=globals()))
print(timeit('regexcheck("(((())())")', number=100000, globals=globals()))
