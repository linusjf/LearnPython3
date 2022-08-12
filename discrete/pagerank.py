#!/usr/bin/env python
# -*- coding: utf-8 -*-
# import the NumPy library
import numpy
# transition probability matrix
A = numpy.array([[0, 0.25, 0.25, 0.25, 0.25],
 [0.5, 0, 0, 0.5, 0],
 [0.33, 0, 0, 0.33, 0.33],
 [1, 0, 0, 0, 0],
 [0, 0, 0, 1, 0]])

# initialize the PageRank vector
v = numpy.array([[0.2], [0.2], [0.2], [0.2], [0.2]])
# the damping factor
d = 0.85
# the size of the "Internet"
N = 5
# compute the update matrix
U = d * A.T + (1 - d) / N
# compute the new PageRank vector
v = numpy.dot(U, v)
# print the new PageRank vector
print(v)

# initialize the PageRank vector
v = numpy.array([[0.2], [0.2], [0.2], [0.2], [0.2]])
# print the initial vector
print('PageRank vector', 0, 'is', v.T)

# compute the PageRank vector for 15 iterations
for i in range(15):
    # compute the next PageRank vector
    v = numpy.dot(U, v)
    # round the PageRank vector to 3 places
    v = numpy.round(v, 3)
    # print the PageRank vector
    print('PageRank vector', i + 1, 'is', v.T)
