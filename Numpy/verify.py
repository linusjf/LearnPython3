#!/usr/bin/env python
# -*- coding: utf-8 -*-
#!/usr/bin/env python
# -*- coding: utf-8 -*-
# eigendecomposition
from numpy import array
from numpy import trace
from numpy import prod
from numpy import sum
from numpy.linalg import eigvals
from numpy.linalg import det
# define matrix
A = array([
[1, 2, 3],
[4, 5, 6],
[7, 8, 9]])
print(A)
# factorize
values = eigvals(A)
print(values)
print(det(A))
print(prod(values))
print(trace(A))
print(sum(values))
