#!/usr/bin/env python
"""
Perf.

######################################################################
# @author      : Linus Fernandes (linusfernandes at gmail dot com)
# @file        : perf
# @created     : Sunday Nov 12, 2023 14:19:02 IST
# @description :
# -*- coding: utf-8 -*-'
######################################################################
"""
import timeit
import numpy as np
numbers_array = np.linspace(-10, 10, 500)
STEP = 20 / 499
numbers_list = [-10 + STEP*interval for interval in range(500)]


def test_np():
    """Test np"""
    return (numbers_array + 2.5) ** 2


def test_list():
    """Test list"""
    return [(number + 2.5) ** 2 for number in numbers_list]


print(list(test_np()) == test_list())

print(timeit.timeit("test_np()", globals=globals(), number=100000))

print(timeit.timeit("test_list()", globals=globals(), number=100000))
