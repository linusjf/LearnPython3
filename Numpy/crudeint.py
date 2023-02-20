#!/usr/bin/env python
# -*- coding: utf-8 -*-

import numpy as np


def f(a, b, c):
    return a**b - c


x = np.ogrid[0:1:24j, 0:1:12j, 0:1:6j]

values = f(x[0], x[1], x[2])

value = np.mean(values)
print(value)

exact = np.log(2) - 0.5
print(exact)

differential = np.abs(exact - value)
print(differential)
