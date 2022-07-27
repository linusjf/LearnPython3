#!/usr/bin/env python
# -*- coding: utf-8 -*-
import numpy
# Create A and b matrices
A = numpy.array([[2, -6, 6], [2, 3, -1], [4, -3, -1]])
b = numpy.array([-8, 15, 19])
# Solve Ax = b
sol = numpy.linalg.solve(A,b)
print(sol)
