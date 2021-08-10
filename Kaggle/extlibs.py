#!/usr/bin/env python
# -*- coding: utf-8 -*-

import math

print("It's math! It has type {}".format(type(math)))

print(dir(math))

print("pi to 4 significant digits = {:.4}".format(math.pi))

print(math.log(32, 2))

import math as mt
print(mt.pi)

import math
mt = math
print(mt.pi)

from math import *
print(pi, log(32, 2))

from math import log, pi
from numpy import asarray

import numpy
print("numpy.random is a", type(numpy.random))
print("it contains names such as...",
      dir(numpy.random)[-15:]
     )

# Roll 10 dice
rolls = numpy.random.randint(low=1, high=6, size=10)
print(rolls)
print(type(rolls))
print(dir(rolls))
# If I want the average roll, the "mean" method looks promising...
print(rolls.mean())
# Or maybe I just want to turn the array into a list, in which case I can use "tolist"
print(rolls.tolist())
print(rolls + 10)
# At which indices are the dice less than or equal to 3?
print(rolls <= 3)

xlist = [[1,2,3],[2,4,6],]
# Create a 2-dimensional array
x = numpy.asarray(xlist)
print("xlist = {}\nx =\n{}".format(xlist, x))

# Get the last element of the second row of our numpy array
print(x[1,-1])
print(xlist[1][-1])

print(dir(list))

