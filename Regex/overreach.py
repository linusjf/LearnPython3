#!/usr/bin/env python
"""
Notmutex.

######################################################################
# @author      : Linus Fernandes (linusfernandes at gmail dot com)
# @file        : overreach
# @created     : Saturday Mar 04, 2023 08:33:57 IST
# @description :
# -*- coding: utf-8 -*-'
######################################################################
"""
from timeit import timeit
import re

remote = re.compile(r"^.*A.*AB")
S1 = "AAAAAAAAAAAAAAAAAAAAB"  # noqa
S2 = "AAAAAAAAAAAAAAAAAAAA@"  # noqa
print(f"remote: {remote.pattern}")
print(S1)
print(timeit("remote.search(S1)", number=10000, globals=globals()))
print()
print(f"remote: {remote.pattern}")
print(S2)
print(timeit("remote.search(S2)", number=10000, globals=globals()))

print()
remote = re.compile(r"^\d*?1\d*?1B")
S1 = "11111111111111111111B"  # noqa
S2 = "11111111111111111111@"  # noqa
print(f"remote: {remote.pattern}")
print(S1)
print(timeit("remote.search(S1)", number=10000, globals=globals()))
print()
print(f"remote: {remote.pattern}")
print(S2)
print(timeit("remote.search(S2)", number=10000, globals=globals()))

remote = re.compile(r".*{START}.*")
S1 = "{START} Mary Ate A Little Lamb {END}"
print(f"remote: {remote.pattern}")
print(S1)
print(timeit("remote.search(S1)", number=10000, globals=globals()))
print()
atomic = re.compile(r"(?>.*?{START}).*")
print(f"atomic: {atomic.pattern}")
print(S1)
print(timeit("atomic.search(S1)", number=10000, globals=globals()))
print()
tempered = re.compile(r"(?:(?!{START}).)*{START}.*")
print(f"tempered: {tempered.pattern}")
print(S1)
print(timeit("tempered.search(S1)", number=10000, globals=globals()))
print()
explicit_greedy = re.compile(r"(?:[^{]++|{(?!START}))*+{START}.*")  # noqa
print(f"explicit_greedy: {explicit_greedy.pattern}")
print(S1)
print(timeit("explicit_greedy.search(S1)", number=10000, globals=globals()))
print()
unrolled_star = re.compile(r"[^{]*(?:(?:{(?!START}))+[^{]*)*{START}")  # noqa
print(f"unrolled_star: {unrolled_star.pattern}")
print(S1)
print(timeit("unrolled_star.search(S1)", number=10000, globals=globals()))
print()
