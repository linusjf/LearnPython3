#!/usr/bin/env python
# -*- coding: utf-8 -*-
from sympy.abc import x, y
from sympy import Matrix, pprint, exp, symbols

f = Matrix([2 * x * y, x**2 * y])
variables = Matrix([x, y])
pprint(f.jacobian(variables))

p, q, r, s, t, u = symbols("p q r s t u", real=True, constant=True)
f = Matrix([1 + exp(-(p * x + q * y)), 1 + exp(-(r * x + s * y)), 1 + exp(-(t * x + u * y))])
pprint(f.jacobian(variables))
