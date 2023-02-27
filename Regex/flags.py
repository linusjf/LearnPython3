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
expr = re.compile(r"the.*day", flags=re.S | re.I)
print(expr.sub(r"Bye", "Hi there\nHave a Nice Day"))
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

print(bool(re.search(r"t a", "cat and dog", flags=re.X)))
print(bool(re.search(r"t\ a", "cat and dog", flags=re.X)))
print(bool(re.search(r"t[ ]a", "cat and dog", flags=re.X)))
print(bool(re.search(r"t\x20a", "cat and dog", flags=re.X)))
m = re.search(r"a#b", "foo a#b 123", flags=re.X)
if m:
    print(m[0])
m = re.search(r"a\#b", "foo a#b 123", flags=re.X)
if m:
    print(m[0])
rex = re.compile(r"\A((?:[^,]+,){3})(?#3-cols)([^,]+)(?#4th-col)")
print(rex.sub(r"\1(\2)", "1,2,3,4,5,6,7", count=1))

# case-sensitive for whole RE definition
print(re.findall(r"Cat[a-z]*\b", "Cat SCatTeR CATER cAts"))
# case-insensitive only for '[a-z]*' portion
print(re.findall(r"Cat(?i:[a-z]*)\b", "Cat SCatTeR CATER cAts"))
# case-insensitive for whole RE definition using flags argument
print(re.findall(r"Cat[a-z]*\b", "Cat SCatTeR CATER cAts", flags=re.I))
# case-insensitive for whole RE definition using special group
print(re.findall(r"(?i)Cat[a-z]*\b", "Cat SCatTeR CATER cAts"))
# case-sensitive only for 'Cat' portion
print(re.findall(r"(?-i:Cat)[a-z]*\b", "Cat SCatTeR CATER cAts", flags=re.I))

# a) Delete from the string start if it is at beginning of a line up to the
# next occurrence of the
# string end at end of a line. Match these keywords irrespective of case.
PARA = """\
good start
start working on that
project you always wanted
to, do not let it end
hi there
start and end the end
42
Start and try to
finish the End
bye"""
expr = re.compile(r"\nstart.*?end\n", flags=re.S | re.I)
print(expr.sub("\n\n", PARA))
# good start
# hi there
# 42
# bye

# Explore what the re.DEBUG flag does.
# Here’s some examples, check their output.
print()
print(r"\Aden|ly\Z")
expr = re.compile(r"\Aden|ly\Z", flags=re.DEBUG)
print()
print(r"\b(0x)?[\da-f]+\b")
expr = re.compile(r"\b(0x)?[\da-f]+\b", flags=re.DEBUG)
print()
print(r"\b(?:0x)?[\da-f]+\b")
expr = re.compile(r"\b(?:0x)?[\da-f]+\b", flags=re.I | re.DEBUG)

# Remove from the first occurrence of
# hat to the last occurrence of it for the given input strings. Match these
# markers case insensitively.

S1 = "But Cool THAT\nsee What okay\nwow quite"
S2 = "it this hat is sliced HIT."

PAT = re.compile(r"HAT.*IT", flags=re.I | re.S)
print(PAT.sub("", S1))
print(PAT.sub("", S2))

S1 = "This is nice and Cool"
S2 = "Nice and cool this is"
S3 = "What is so nice and cool about This?"
S4 = "nice,cool,This"
S5 = "not nice This?"
S6 = "This is not cool"
PAT = re.compile(r"(?i)(?=.*nice)(?=.*cool)(?-i:.*This)")
print(bool(PAT.search(S1)))
print(bool(PAT.search(S2)))
print(bool(PAT.search(S3)))
print(bool(PAT.search(S4)))
print(bool(PAT.search(S5)))
print(bool(PAT.search(S6)))
