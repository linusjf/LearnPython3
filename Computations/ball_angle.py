#!/usr/bin/env python
# -*- coding: utf-8 -*-

from math import atan, pi

# Horizontal position
x = 10
# Vertical position
y = 10

angle = atan(y / x)

print((angle / pi) * 180)
