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
import regex

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

WORD = "coffining"
print(WORD)
# recursively delete 'fin'
while True:
    WORD, cnt = re.subn(r"fin", r"", WORD)
    if cnt == 0:
        break
    print(WORD)
print(WORD)

ROW = "421,foo,2425,42,5,foo,6,6,42"
# lookarounds used to ensure start/end of column matching
# possessive quantifier used to ensure partial column is not captured
# if a column has same text as another column, the latter column is deleted
print(ROW)
while True:
    ROW, cnt = regex.subn(r"(?<=\A|,)([^,]++).*\K,\1(?=,|\Z)", r"", ROW)
    if cnt == 0:
        break
    print(ROW)
print(ROW)
print()
ROW = "421,foo,2425,42,5,foo,6,6,42"
print()
print(ROW)
while True:
    ROW, cnt = regex.subn(r"(?<=\A|,)([^,]+).*\K,\1(?=,|\Z)", r"", ROW)
    if cnt == 0:
        break
    print(ROW)
print(ROW)

STR = "123-87-593 42 foo"
print(STR)
# all non-whitespace characters from start of string
print(regex.findall(r"\G\S", STR))
print(regex.sub(r"\G\S", r"*", STR))
# all digits and optional hyphen combo from start of string
print(regex.findall(r"\G\d+-?", STR))
print(regex.sub(r"\G(\d+)(-?)", r"(\1)\2", STR))

# all word characters from start of string
# only if it is followed by word character
print(regex.findall(r"\G\w(?=\w)", "cat12 bat pin"))
print(regex.sub(r"\G\w(?=\w)", r"\g<0>:", "cat12 bat pin"))
# all lowercase alphabets or space from start of string
print(regex.sub(r"\G[a-z ]", r"(\g<0>)", "par tar-den hen-food mood"))
