#!/usr/bin/env python
"""
Notmutex.

######################################################################
# @author      : Linus Fernandes (linusfernandes at gmail dot com)
# @file        : notmutex
# @created     : Friday Mar 03, 2023 15:29:57 IST
# @description :
# -*- coding: utf-8 -*-'
######################################################################
"""
import re
from timeit import timeit

notmutex = re.compile(r"^\d+\w*@")
S1 = "12345678901234567890@"  # noqa
S2 = "12345678901234567890"  # noqa
print(f"notmutex: {notmutex.pattern}")
print(timeit("notmutex.search(S1)", number=10000, globals=globals()))
print(f"notmutex: {notmutex.pattern}")
print(timeit("notmutex.search(S2)", number=10000, globals=globals()))

print()
notmutex = re.compile(r"^(?:\d|\w)+@")
print(f"notmutex: {notmutex.pattern}")
print(timeit("notmutex.search(S1)", number=10000, globals=globals()))
print(f"notmutex: {notmutex.pattern}")
print(timeit("notmutex.search(S2)", number=10000, globals=globals()))

print()
notmutex = re.compile(r"^[\d\w]+@")
print(f"notmutex: {notmutex.pattern}")
print(timeit("notmutex.search(S1)", number=10000, globals=globals()))
print(f"notmutex: {notmutex.pattern}")
print(timeit("notmutex.search(S2)", number=10000, globals=globals()))

print()

possessive = re.compile(r"[\d\w]++")
print(f"possessive: {possessive.pattern}")
print(timeit("possessive.search(S1)", number=10000, globals=globals()))
print(f"possessive: {possessive.pattern}")
print(timeit("possessive.search(S2)", number=10000, globals=globals()))

print()

atomic = re.compile(r"(?>[\d\w]+)")
print(f"atomic: {atomic.pattern}")
print(timeit("atomic.search(S1)", number=10000, globals=globals()))
print(f"atomic: {atomic.pattern}")
print(timeit("atomic.search(S2)", number=10000, globals=globals()))
