#!/usr/bin/env python
# -*- coding: utf-8 -*-
#!/usr/bin/env python
# -*- coding: utf-8 -*-
# eigendecomposition
import numpy as np
from numpy import array
from numpy import trace
from numpy import prod
from numpy import sum
from numpy.linalg import eigvals
from numpy.linalg import det
from numpy.linalg import slogdet
from numpy import log

def verify(A):
    print(A)
    # factorize
    values = eigvals(A)
    print(values)
    determinant = det(A)
    print(determinant)
    if (abs(determinant) < 1e-10):
        print("Singular Matrix")
    else:
        print("Non-Singular matrix")
    print(prod(values))
    print(slogdet(A))
    print(sum(log(values)))
    print(trace(A))
    print(sum(values))
    print()


# define matrix
A = array([
[1, 2, 3],
[4, 5, 6],
[7, 8, 9]])
verify(A)

A = array([
    [2,-1,0],
    [-1,2,-1],
    [0,-1,2]])
verify(A)
