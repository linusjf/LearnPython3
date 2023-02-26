#!/usr/bin/env python
"""
Flags.

######################################################################
# @author      : Linus Fernandes (linusfernandes at gmail dot com)
# @file        : flags
# @created     : Monday Feb 20, 2023 04:21:06 IST
# @description :
# -*- coding: utf-8 -*-'
######################################################################
"""
import re

print(bool(re.search(r"cat", "Cat")))
print(bool(re.search(r"cat", "Cat", flags=re.IGNORECASE)))
print(re.findall(r"c.t", "Cat cot CATER ScUtTLe", flags=re.I))
# without flag, you need to use: r'[a-zA-Z]+'
# with flag, can also use: r'[A-Z]+'
print(re.findall(r"[a-z]+", "Sample123string42with777numbers", flags=re.I))
# by default, the . metacharacter doesn't match newline
print(re.sub(r"the.*ice", r"X", "Hi there\nHave a Nice Day"))
# re.S flag will allow newline character to be matched as well
print(re.sub(r"the.*ice", r"X", "Hi there\nHave a Nice Day", flags=re.S))
# multiple flags can be combined using bitwise OR operator
print(re.sub(r"the.*day", r"Bye", "Hi there\nHave a Nice Day", flags=re.S | re.I))
# check if any line in the string starts with 'top'
print(bool(re.search(r"^top", "hi hello\ntop spot", flags=re.M)))
# check if any line in the string ends with 'ar'
print(bool(re.search(r"ar$", "spare\npar\ndare", flags=re.M)))

# same as: rex = re.compile(r'\A((?:[^,]+,){3})([^,]+)')
# note the use of triple quoted string
rex = re.compile(
    r"""
\A( # group-1, captures first 3 columns
(?:[^,]+,){3} # non-capturing group to get the 3 columns
)
([^,]+) # group-2, captures 4th column
""",
    flags=re.X,
)
print(rex.sub(r"\1(\2)", "1,2,3,4,5,6,7", count=1))
