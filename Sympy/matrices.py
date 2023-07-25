#!/usr/bin/env python
from sympy import *

init_printing(use_unicode=True)

print(Matrix([[1, -1], [3, 4], [0, 2]]))
print(Matrix([1, 2, 3]))
M = Matrix([[1, 2, 3], [3, 2, 1]])
N = Matrix([0, 1, 1])
print(M * N)
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
print(M * N)
print(3 * M)
print(M**2)
print(M**-1)
# print(N**-1)

print(eye(3))
print(eye(4))
print(zeros(2, 3))
print(ones(3, 2))
print(diag(1, 2, 3))
print(diag(-1, ones(2, 2), Matrix([5, 7, 5])))
M = Matrix([[1, 0, 1], [2, -1, 3], [4, 3, 2]])
print(M)
print(M.det())
M = Matrix([[1, 0, 1, 3], [2, 3, 4, 7], [-1, -3, -3, -4]])
print(M)
print(M.rref())
M = Matrix([[1, 2, 3, 0, 0], [4, 10, 0, 0, 1]])
print(M)
print(M.nullspace())
M = Matrix([[1, 1, 2], [2, 1, 3], [3, 1, 4]])
print(M)
print(M.columnspace())
M = Matrix([[3, -2, 4, -2], [5, 3, -3, -2], [5, -2, 2, -2], [5, -2, -3, 3]])
print(M)
print(M.eigenvals())
print(M.eigenvects())
P, D = M.diagonalize()
print(P)
print(D)
print(P * D * P**-1)
print(P * D * P**-1 == M)
lamda = symbols("lamda")
p = M.charpoly(lamda)
print(factor(p.as_expr()))