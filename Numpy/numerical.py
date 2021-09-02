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

c = np.ones((3, 3))
# NOT matrix multiplication!
print(c * c)
print(c.dot(c))

a = np.arange(10)
b = a[0::2]
c = a[1::2]
print(b,c)
print(b + c)

a = list(range(10))
b = a[0::2]
c = a[1::2]
print(b,c)
print([b[i] + c[i] for i in range(len(b))])

iterable = (2**x for x in range(5))
a = np.fromiter(iterable, int)
print(a)

iterable = (2^(3*x) for x in range(5))
a = np.fromiter(iterable, int)
print(a)

print(min(Timer(setup="""
import numpy as np
a = np.arange(10)
""",
stmt="""
b = a[0::2]
c = a[1::2]
b + c
""").repeat(5,1000)))

print(min(Timer(setup="""
a = list(range(10))
""",
stmt="""
b = a[0::2]
c = a[1::2]
[b[i] + c[i] for i in range(len(b))]
""").repeat(5,1000)))

print(min(Timer(setup="import numpy as np\na = np.arange(10000)",
      stmt="a + 1").repeat(5,1000)))

print(min(Timer(setup="l = range(10000)",
      stmt="[i+1 for i in l]").repeat(5,1000)))
