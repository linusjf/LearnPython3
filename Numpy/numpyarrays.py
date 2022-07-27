#!/usr/bin/env python
# -*- coding: utf-8 -*-
import numpy 
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
