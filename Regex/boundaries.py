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