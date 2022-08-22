#!/usr/bin/env python
# -*- coding: utf-8 -*-
import numpy 
from numpy import array
from numpy import vstack
from numpy import hstack
# initialize matrices 
A = numpy.array([[3, 2, 1], [9, 0, 1], [3, 4, 1]]) 
B = numpy.array([[1, 1, 2], [8, 4, 1], [0, 0, 3]])
# print the entry in the first row and first column of A
print(A[0,0])
# print the entry in the second row and third column of B
print(B[1,2])
# Add A and B
print(numpy.add(A,B))
# Subtract A and B
print(numpy.subtract(A,B))
# Multiply A by a scalar 5
print(numpy.multiply(5,A))
# Find the transpose of A
print(numpy.transpose(A))
# Multiply A and B
print(numpy.dot(A,B))

# create array with vstack
# create first array
a1 = array([1,2,3])
print(a1)
# create second array
a2 = array([4,5,6])
print(a2)
# vertical stack
a3 = vstack((a1, a2))
print(a3)
print(a3.shape)

# create array with hstack
# create first array
a1 = array([1,2,3])
print(a1)
# create second array
a2 = array([4,5,6])
print(a2)
# create horizontal stack
a3 = hstack((a1, a2))
print(a3)
print(a3.shape)
