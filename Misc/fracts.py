#!/usr/bin/env python
# -*- coding: utf-8 -*-

from fractions import Fraction

half = Fraction('1/2')
third = Fraction('1/3')

total = half + third

print(half, '+', third, '=', total)
print(f'{half} + {third} = {total}')
print(f'{half} + {third} = {half+third}')
