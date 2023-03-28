#!/usr/bin/env python
"""
Minbits.

######################################################################
# @author      : Linus Fernandes (linusfernandes at gmail dot com)
# @file        : minbits
# @created     : Wednesday Mar 29, 2023 05:24:03 IST
# @description :
# An efficient Python3 program to find minimum number formed by bits of a given
# number.
# -*- coding: utf-8 -*-'
######################################################################
"""


# Returns minimum number formed by
# bits of a given number.
def minimize(num):
    """Minimize."""
    # _popcnt32(a) gives number of 1's
    # present in binary representation
    # of a.
    bits = bin(num).count("1")
    return pow(2, bits) - 1


# Driver Code
NUM = 11
print(minimize(NUM))
