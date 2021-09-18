#!/usr/bin/env python
# -*- coding: utf-8 -*-

from sympy import init_printing,Integral,latex,pretty,pprint,sqrt,symbols,srepr
init_printing(use_unicode=True)
x,y,z = symbols('x y z')
print(Integral(sqrt(1/x),x))

print(srepr(Integral(sqrt(1/x), x)))
pprint(Integral(sqrt(1/x), x), use_unicode=False)

print(pretty(Integral(sqrt(1/x), x), use_unicode=False))

print(latex(Integral(sqrt(1/x), x)))
from sympy.printing.mathml import print_mathml
print_mathml(Integral(sqrt(1/x), x))


from sympy.printing.dot import dotprint
from sympy.abc import x
print(dotprint(x+2))

