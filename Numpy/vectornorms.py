#!/usr/bin/env python
# -*- coding: utf-8 -*-
# vector L1 norm
from numpy import array
from numpy.linalg import norm
# define vector
a = array([1, 2, 3])
print(a)
# calculate norm
l1 = norm(a, 1)
print(l1)

# vector L2 norm
# define vector
a = array([1, 2, 3])
print(a)
# calculate norm
l2 = norm(a)
print(l2)

# vector max norm
from math import inf
# define vector
a = array([1, 2, 3])
print(a)
# calculate norm
maxnorm = norm(a, inf)
print(maxnorm)
