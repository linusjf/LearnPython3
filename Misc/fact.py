#!/usr/bin/env python
# -*- coding: utf-8 -*-

# https://www.linkedin.com/feed/update/urn:li:activity:6849655496094302208

from functools import lru_cache
from timeit import timeit
from random import randrange

def factorial(num):
    return num * factorial(num - 1) if num > 1 else 1

@lru_cache(maxsize=1024)
def factorial_memo(num):
    return num * factorial_memo(num - 1) if num > 1 else 1

print(timeit(
    stmt="factorial(randrange(0,500))",
    globals=locals(),
    number=10**5
))

print(timeit(
    stmt="factorial_memo(randrange(0,500))",
    globals=locals(),
    number=10**5
))
