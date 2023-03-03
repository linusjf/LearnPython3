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

greedy = re.compile(r"(a+|\w+)*:")  # noqa
possessive = re.compile(r"(a+|\w+)*+:")  # noqa

# string that'll match the above patterns
S1 = "aaaaaaaaaaaaaaaa:123"  # noqa
# string that does NOT match the above patterns
S2 = "aaaaaaaaaaaaaaaa-123"  # noqa

# no issues when input string has a match
print(timeit("greedy.search(S1)", number=10000, globals=globals()))
print(timeit("possessive.search(S1)", number=10000, globals=globals()))

# if input doesn't match, greedy version suffers from catastrophic backtracking
# note that 'number' parameter is reduced to 10 since it takes a long time
print(timeit("greedy.search(S2)", number=10, globals=globals()))
print(timeit("possessive.search(S2)", number=10, globals=globals()))

greedyr = regex.compile(r"(a+|\w+)*:")  # noqa
possessiver = regex.compile(r"(a+|\w+)*+:")  # noqa

# no issues when input string has a match
print(timeit("greedyr.search(S1)", number=10000, globals=globals()))
print(timeit("possessiver.search(S1)", number=10000, globals=globals()))

# if input doesn't match, greedy version suffers from catastrophic backtracking
# note that 'number' parameter is reduced to 10 since it takes a long time
print(timeit("greedyr.search(S2)", number=10, globals=globals()))
print(timeit("possessiver.search(S2)", number=10, globals=globals()))
