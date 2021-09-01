#!/usr/bin/env python
# -*- coding: utf-8 -*-

import numpy as np
from timeit import Timer
a = np.array([1, 2, 3, 4])
print(a + 1)
2**a
b = np.ones(4) + 1
a - b
a * b
j = np.arange(5)
2**(j + 1) - j


print(min(Timer(setup="import numpy as np\na = np.arange(10000)",
      stmt="a + 1").repeat(5,1000)))

print(min(Timer(setup="l = range(10000)",
      stmt="[i+1 for i in l]").repeat(5,1000)))
