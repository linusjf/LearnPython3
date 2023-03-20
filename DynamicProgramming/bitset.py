#!/usr/bin/env python
"""
Bitset.

######################################################################
# @author      : Linus Fernandes (linusfernandes at gmail dot com)
# @file        : bitset
# @created     : Friday Mar 17, 2023 20:59:25 IST
# @description :
# -*- coding: utf-8 -*-'
######################################################################
"""
import math


def unsetbit(bit, data):  # noqa
    """Unset bit."""
    return data & ~(1 << bit)


def setbit(bit, data):  # noqa
    """Set bit."""
    return data | (1 << bit)


def isbitset(bit, data):  # noqa
    """Check if bit is set."""
    return data & (1 << bit)


def count_set_bits(value, bitcount):  # noqa
    """Count set bits."""
    count = 0
    for i in range(bitcount):
        if isbitset(i, value):
            count += 1
    return count


def get_bit(bit, data):  # noqa
    """Get bit."""
    return (data >> bit) & 1


def first_bit_index(data):  # noqa
    """Get first set bit index."""
    return int(math.log(data, 2))
