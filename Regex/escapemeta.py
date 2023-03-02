#!/usr/bin/env python
"""
EscapeMeta.

######################################################################
# @author      : Linus Fernandes (linusfernandes at gmail dot com)
# @file        : escapemeta
# @created     : Monday Feb 06, 2023 14:30:22 IST
# @description :
# -*- coding: utf-8 -*-'
######################################################################
"""
import re

# even though ^ is not being used as anchor, it won't be matched literally
print(bool(re.search(r"b^2", "a^2 + b^2 - C*3")))
# escaping will work
print(bool(re.search(r"b\^2", "a^2 + b^2 - C*3")))
# match ( or ) literally
print(re.sub(r"\(|\)", r"", "(a*b) + c"))
# note that here input string is also a raw string
print(re.sub(r"\\", r"/", r"\learn\by\example"))
EQN = "f*(a^b) - 3*(a^b)"
# straightforward search and replace, no need RE shenanigans
print(EQN.replace("(a^b)", "c"))
EXPR = "(a^b)"
# print used here to show results similar to raw string
print(re.escape(EXPR))
# replace only at end of string
print(re.sub(re.escape(EXPR) + r"\Z", r"c", EQN))
# if strings are to be matched literally,
# need to use re.escape for each string when creating alternations
terms = ["foo_baz", EXPR]
print("|".join(re.escape(w) for w in terms))

STR1 = "(9-2)*5+qty/3"
STR2 = "(qty+4)/2-(9-2)*5+pq/4"
EXPR = r"(9-2)*5"
print(re.sub(re.escape(EXPR), r"35", STR1))
print(re.sub(re.escape(EXPR), r"35", STR2))

items = ["a.b", "3+n", r"x\y\z", "qty||price", "{n}"]
alt_re = re.compile(r"a\.b|3\+n|x\\y\\z|qty\|\|price|\{n\}")
print(alt_re)
items = [re.escape(e) for e in items]
alt_re2 = re.compile("|".join(items))
print(alt_re2)
print(alt_re.sub(r"X", "0a.bcd"))
print(alt_re.sub(r"X", "E{n}AMPLE"))
print(alt_re.sub(r"X", r"43+n2 ax\y\ze"))
print(alt_re2.sub(r"X", "0a.bcd"))
print(alt_re2.sub(r"X", "E{n}AMPLE"))
print(alt_re2.sub(r"X", r"43+n2 ax\y\ze"))

# iterable of strings, assume alternation precedence sorting isn't needed
terms = ["a_42", "(a^b)", "2|3"]
print(terms)
# using 're.escape' and 'join' to construct the pattern
pat1 = re.compile("|".join(re.escape(s) for s in terms))
# using only 'join' to construct the pattern
pat2 = re.compile("|".join(terms))

print(pat1.pattern)
print(pat2.pattern)
S = "ba_423 (a^b)c 2|3 a^b"
print(S)
print(pat1.sub("X", S))
print(pat2.sub("X", S))

print(re.sub(r"\t", ":", "a\tb\tc"))
print(re.sub(r"\n", " ", "1\n2\n3"))

try:
    re.search(r"\e", "hello")
except re.error as e:
    print(str(e))

# \x20 is space character
print(re.sub(r"\x20", "", "h e l l o"))

# \x7c is '|' character
print(re.sub(r"2\x7c3", "5", "12|30"))
print(re.sub(r"2|3", "5", "12|30"))
