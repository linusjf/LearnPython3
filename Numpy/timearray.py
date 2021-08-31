#!/usr/bin/env python
# -*- coding: utf-8 -*-

from timeit import timeit

print(timeit(setup="L = range(1000)",
             stmt="[i**2 for i in L]",
             number = 1))

print(timeit(setup="import numpy as np\na = np.arange(1000)",
             stmt="a**2",
             number=1))
