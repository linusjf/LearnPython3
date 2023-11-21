#!/usr/bin/env python
"""
Endless.

######################################################################
# @author      : Linus Fernandes (linusfernandes at gmail dot com)
# @file        : endless
# @created     : Tuesday Nov 21, 2023 13:06:26 IST
# @description :
# -*- coding: utf-8 -*-'
######################################################################
"""
from itertools import cycle


def endless():
    """Yields 9, 8, 7, 6, 9, 8, 7, 6, ... forever"""
    yield from cycle((9, 8, 7, 6))


e = endless()
TOTAL = 0
for i in e:
    if TOTAL < 30:
        print(i, end=" ")
        TOTAL += i
    else:
        print()
        # Pause execution. We can resume later.
        break


# Resume
print(next(e), next(e), next(e))
