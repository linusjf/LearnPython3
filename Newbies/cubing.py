#!/usr/bin/env python3
"""Cubing special."""
# pylint: disable=no-name-in-module
from scipy.special import cbrt
# Find cubic root of 27 & 64 using cbrt() function
CB = cbrt([27, 64, 125])
# print value of cb
print(CB)
# pylint: enable=no-name-in-module
