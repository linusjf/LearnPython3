#!/usr/bin/env python
"""
Catastrophe.

######################################################################
# @author      : Linus Fernandes (linusfernandes at gmail dot com)
# @file        : catastrophe
# @created     : Friday Mar 03, 2023 09:00:08 IST
# @description :
# -*- coding: utf-8 -*-'
######################################################################
"""
import re
from timeit import timeit
import regex

_greedy = re.compile(r"(a+|\w+)*:")
_possessive = re.compile(r"(a+|\w+)*+:")

# string that'll match the above patterns
_S1 = "aaaaaaaaaaaaaaaa:123"
# string that does NOT match the above patterns
_S2 = "aaaaaaaaaaaaaaaa-123"

# no issues when input string has a match
print(timeit("_greedy.search(S1)", number=10000, globals=globals()))
print(timeit("_possessive.search(S1)", number=10000, globals=globals()))

# if input doesn't match, greedy version suffers from catastrophic backtracking
# note that 'number' parameter is reduced to 10 since it takes a long time
print(timeit("_greedy.search(S2)", number=10, globals=globals()))
print(timeit("_possessive.search(S2)", number=10, globals=globals()))

_greedyr = regex.compile(r"(a+|\w+)*:")
_possessiver = regex.compile(r"(a+|\w+)*+:")

# no issues when input string has a match
print(timeit("_greedyr.search(S1)", number=10000, globals=globals()))
print(timeit("_possessiver.search(S1)", number=10000, globals=globals()))

# if input doesn't match, greedy version suffers from catastrophic backtracking
# note that 'number' parameter is reduced to 10 since it takes a long time
print(timeit("_greedyr.search(S2)", number=10, globals=globals()))
print(timeit("_possessiver.search(S2)", number=10, globals=globals()))
