#!/usr/bin/env python
# -*- coding: utf-8 -*-

from timeit import Timer

print(min(Timer(setup="L = range(1000)",
             stmt="[i**2 for i in L]").repeat(10,1000)), " ms per invocation")

print(min(Timer(setup="import numpy as np\na = np.arange(1000)",
             stmt="a**2").repeat(10,1000)), " ms per invocation")
