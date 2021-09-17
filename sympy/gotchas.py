#!/usr/bin/env python
# -*- coding: utf-8 -*-

from sympy import *

x = symbols('x')
print(x + 1)

x, y, z = symbols('x y z')
a, b = symbols('b a')
print(a,b)
print(b,a)
crazy = symbols('unrelated')
print(crazy + 1)
x = symbols('x')
expr = x + 1
x = 2
print(expr)

x = 'abc'
expr = x + 'def'
print(expr)
x = 'ABC'
print(expr)
x = symbols('x')
expr = x + 1
print(expr.subs(x, 2))

print(x + 1 == 4)

print(Eq(x + 1, 4))
print((x + 1)**2 == x**2 + 2*x + 1)

a = (x + 1)**2
b = x**2 + 2*x + 1
print(simplify(a - b))
c = x**2 - 2*x + 1
print(simplify(a - c))
a = cos(x)**2 - sin(x)**2
b = cos(2*x)
print(a.equals(b))
a = 2*sin(x)*cos(x)
b = sin(2*x)
print(a.equals(b))
print(True ^ False)
print(True ^ True)
print(Xor(x, y))

print(type(Integer(1) + 1))
print(type(1 + 1))
print(Integer(1)/Integer(3))
print(type(Integer(1)/Integer(3)))

print(Rational(1, 2))
print(x + 1/2) 
print(x + Rational(1, 2))
