#!/usr/bin/env python
"""
Explosive.

######################################################################
# @author      : Linus Fernandes (linusfernandes at gmail dot com)
# @file        : explosive
# @created     : Friday Mar 03, 2023 13:32:55 IST
# @description :
# -*- coding: utf-8 -*-'
######################################################################
"""
import re
from timeit import timeit
import regex

greedy = re.compile(r"^(A+)*B")  # noqa
possessive = re.compile(r"^(A+)*+B")  # noqa
atomic = re.compile(r"^(?>(A+)*)B")  # noqa
# string that'll match the above patterns
S1 = "AAAAAAAAAAAAAAAAAAAAB"  # noqa
# string that does NOT match the above patterns
S2 = "AAAAAAAAAAAAAAAAAAAAC"  # noqa

print("re:")
print(f"greedy: {greedy.pattern}")
print(timeit("greedy.search(S1)", number=10000, globals=globals()))
print(f"possessive: {possessive.pattern}")
print(timeit("possessive.search(S1)", number=10000, globals=globals()))
print(f"atomic group: {atomic.pattern}")
print(timeit("atomic.search(S1)", number=10000, globals=globals()))

print()
# if input doesn't match, greedy version suffers from catastrophic backtracking
# note that 'number' parameter is reduced to 10 since it takes a long time
print(f"greedy: {greedy.pattern}")
print(timeit("greedy.search(S2)", number=10, globals=globals()))
print(f"possessive: {possessive.pattern}")
print(timeit("possessive.search(S2)", number=10, globals=globals()))
print(f"atomic group: {atomic.pattern}")
print(timeit("atomic.search(S2)", number=10000, globals=globals()))

print()

greedy_regex = regex.compile(r"^(A+)*B")  # noqa
possessive_regex = regex.compile(r"^(A+)*+B")  # noqa
atomic_regex = regex.compile(r"^(?>(A+)*)B")  # noqa

print("regex:")

print(f"greedy: {greedy_regex.pattern}")
print(timeit("greedy_regex.search(S1)", number=10000, globals=globals()))
print(f"possessive: {possessive_regex.pattern}")
print(timeit("possessive_regex.search(S1)", number=10000, globals=globals()))
print(f"atomic group: {atomic_regex.pattern}")
print(timeit("atomic_regex.search(S1)", number=10000, globals=globals()))

print()
# if input doesn't match, greedy version suffers from catastrophic backtracking
# note that 'number' parameter is reduced to 10 since it takes a long time
print(f"greedy: {greedy_regex.pattern}")
print(timeit("greedy_regex.search(S2)", number=10, globals=globals()))
print(f"possessive: {possessive_regex.pattern}")
print(timeit("possessive_regex.search(S2)", number=10, globals=globals()))
print(f"atomic group: {atomic_regex.pattern}")
print(timeit("atomic_regex.search(S2)", number=10000, globals=globals()))
print()
