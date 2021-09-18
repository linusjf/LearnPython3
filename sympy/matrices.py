#!/usr/bin/env python
from sympy import *
init_printing(use_unicode=True)

print(Matrix([[1, -1], [3, 4], [0, 2]]))
print(Matrix([1, 2, 3]))
M = Matrix([[1, 2, 3], [3, 2, 1]])
N = Matrix([0, 1, 1])
print(M*N)
M = Matrix([[1, 2, 3], [-2, 0, 4]])
print(M)
print(shape(M))
print(M.row(0))

print(M.col(-1))

M.col_del(0)
print(M)
M.row_del(1)
print(M)

M = M.row_insert(1, Matrix([[0, 4]]))
print(M)
M = M.col_insert(0, Matrix([1, -2]))
print(M)
M = Matrix([[1, 3], [-2, 3]])
N = Matrix([[0, 3], [0, 7]])
print(M + N)
print(M*N)
print(3*M)
print(M**2)
print(M**-1)
#print(N**-1)
