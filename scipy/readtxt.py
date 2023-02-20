#!/usr/bin/env python
# -*- coding: utf-8 -*-

import numpy as np
from io import StringIO

# StringIO behaves like a file object
c = StringIO("0 1\n2 3")
print(np.loadtxt(c))
d = StringIO("M 21 72\nF 35 58")
np.loadtxt(d, dtype={"names": ("gender", "age", "weight"), "formats": ("S1", "i4", "f4")})
c = StringIO("1,0,2\n3,0,4")
x, y = np.loadtxt(c, delimiter=",", usecols=(0, 2), unpack=True)
print(x)
print(y)

s = StringIO("10.01 31.25-\n19.22 64.31\n17.57- 63.94")


def conv(fld):
    return -float(fld[:-1]) if fld.endswith(b"-") else float(fld)


print(np.loadtxt(s, converters={0: conv, 1: conv}))

x = y = z = np.arange(0.0, 5.0, 1.0)
np.savetxt("test.out", x, delimiter=",")  # X is an array
np.savetxt("test1.out", (x, y, z))  # x,y,z equal sized 1D arrays
np.savetxt("test2.out", x, fmt="%1.4e")  # use exponential notation
