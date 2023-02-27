#!/usr/bin/env python
"""
Misc.

######################################################################
# @author      : Linus Fernandes (linusfernandes at gmail dot com)
# @file        : misc
# @created     : Monday Feb 27, 2023 21:32:31 IST
# @description :
# -*- coding: utf-8 -*-'
######################################################################
"""
import re

# one to one mappings
d = {"1": "one", "2": "two", "4": "four"}
print(re.sub(r"[124]", lambda m: d[str(m[0])], "9234012"))
# if the matched text doesn't exist as a key, default value will be used
print(re.sub(r"\d", lambda m: d.get(str(m[0]), "X"), "9234012"))
# For swapping two or more portions without using intermediate
# result, using a dict is rec-
# ommended.
swap = {"cat": "tiger", "tiger": "cat"}
WORDS = "cat tiger dog tiger cat"
# replace word if it exists as key, else leave it as is
print(re.sub(r"\w+", lambda m: swap.get(str(m[0]), str(m[0])), WORDS))
# or, build the alternation list manually for simple cases
print(re.sub(r"cat|tiger", lambda m: swap[str(m[0])], WORDS))
# For dict that have many entries and likely
# to undergo changes during development, building
# alternation list manually is not a good choice.
# Also, recall that as per precedence rules, longest
# length string should come first.
d = {"hand": "1", "handy": "2", "handful": "3", "a^b": "4"}
# take care of metacharacter escaping first
LIST = [re.escape(k) for k in d]
# build alternation list
# add anchors and flags as needed to construct the final RE
print("|".join(sorted(LIST, key=len, reverse=True)))
