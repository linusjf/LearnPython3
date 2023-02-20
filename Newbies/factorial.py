#!/usr/bin/env python
# -*- coding: utf-8 -*-
import math
import scipy.special

print("20! = {}".format(math.factorial(20)))
print("100! = {}".format(math.factorial(100)))
print("²⁰P₁₀ = {}".format(math.factorial(20) / math.factorial(10)))
print("²⁰C₁₀ = {}".format(math.factorial(20) / (math.factorial(10) * math.factorial(10))))
print(
    "²⁰C₄ ways of selecting 4 candidates out of 20: {}".format(
        math.factorial(20) / math.factorial(4) / math.factorial(20 - 4)
    )
)
print("²⁰C₄ ways of selecting 4 candidates out of 20: {}".format(scipy.special.binom(20, 4)))
