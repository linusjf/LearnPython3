#!/usr/bin/env python
# -*- coding: utf-8 -*-
import numpy

# Create A and b matrices
A = numpy.array([[2, -6, 6], [2, 3, -1], [4, -3, -1]])
b = numpy.array([-8, 15, 19])
# Solve Ax = b
sol = numpy.linalg.solve(A, b)
print(sol)

# inconsistent system
A = numpy.array([[2, 1], [6, 3]])
b = numpy.array([3, 3])
print(numpy.linalg.solve(A, b))

# dependent system
A = numpy.array([[2, 1], [6, 3]])
b = numpy.array([1, 3])
print(numpy.linalg.solve(A, b))
# A good practice is to verify that the
# determinant of A is nonzero with the numpy.linalg.det function before proceeding
# further.
# In the following code, we create a NumPy array A, compute the determinant, and
# print it.
A = numpy.array([[2, 1], [6, 3]])
print(numpy.linalg.det(A))

numpy.random.seed(1)
# Create A and b matrices with random
A = 10 * numpy.random.rand(10, 10) - 5
b = 10 * numpy.random.rand(10) - 5
# Solve Ax = b
solution = numpy.linalg.solve(A, b)
print(solution)
# To verify the solution works, show Ax - b is near 0
rem = sum(abs(numpy.dot(A, solution) - b))
print(rem)
