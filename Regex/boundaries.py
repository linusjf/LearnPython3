#!/usr/bin/env python
"""
Boundaries.

######################################################################
# @author      : Linus Fernandes (linusfernandes at gmail dot com)
# @file        : boundaries
# @created     : Saturday Feb 25, 2023 11:59:56 IST
# @description :
# -*- coding: utf-8 -*-'
######################################################################
"""
import regex

LINE = "START start of line END"
regexx = regex.compile(r"(?<=START).*")
print(regexx.sub("", LINE))
regexx = regex.compile(r".*?(?=END)")
print(regexx.sub("", LINE))
EMAILLINE = "> and then she told him \
she wouldn't settle for less than a Hawaiian pizza, and"
EMAIL2 = "> >>>"
regexx = regex.compile(r"(?<=^> )\w+")
print(regexx.sub("AND", EMAILLINE))
print(regexx.sub("AND", EMAIL2))
regexx = regex.compile("(?<=^> )(?=[a-zA-Z]).")
print(regexx.sub("", EMAILLINE))
regexx = regex.compile("(?=[a-zA-Z])(?<=^> ).")
print(regexx.sub("", EMAILLINE))
regexx = regex.compile(r"(?:(?=\w)(?<!\w)|(?<=\w)(?!\w))")
print(regexx.sub("|", EMAILLINE))
regexx = regex.compile(r"\b")
print(regexx.sub("|", EMAILLINE))

# A "real word boundary" that detects the edge between
# an ASCII letter and a non-letter
regexx = regex.compile(r"(?i)(?<=^|[^a-z])(?=[a-z])|(?<=[a-z])(?=$|[^a-z])")
print(regexx.sub("|", EMAILLINE))
EMAILLINE = "> and then she told him \
she wouldn't settle for less than 1000 Hawaiian pizzas, \
and 500 cokes."
print(regexx.sub("|", EMAILLINE))
regexx = regex.compile("(?:(?i)(?<=^|\\d)(?=[a-z])|(?<=[a-z])(?=$|\\d))")
EMAILLINE = "> and then she told him \
she wouldn't settle for less than 1000 Hawaiian pizzas, \
and 500 cokes and she wouldn't pay more than 100Rs."
print(regexx.sub("|", EMAILLINE))

STRING = "0# 1 #2 #3# 4# #5"
regexx = regex.compile(r"(?:(?:^|#| )*?)(\d)(?:$|#| )")
print(",".join(regexx.findall(STRING)))
