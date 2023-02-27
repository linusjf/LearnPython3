#!/usr/bin/env python
"""
Unicode.

######################################################################
# @author      : Linus Fernandes (linusfernandes at gmail dot com)
# @file        : unicode
# @created     : Monday Feb 27, 2023 11:47:17 IST
# @description :
# -*- coding: utf-8 -*-'
######################################################################
"""
import re
import regex

# \w is Unicode aware
print(re.findall(r"\w+", "fox:αλεπού"))
print(re.findall(r"\w+", "fox:αλεπού", flags=re.A))
print(re.findall(r"[a-zA-Z0-9_]+", "fox:αλεπού"))
print(bool(re.search(r"[a-zA-Z]", "İıſK")))
m = re.search(r"[a-z]+", "İıſK", flags=re.I)
if m:
    print(m[0])
print(bool(re.search(r"[a-z]", "İıſK", flags=re.I | re.A)))

# extract all consecutive letters
print(regex.findall(r"\p{L}+", "fox:αλεπού,eagle:αετός"))
# extract all consecutive Greek letters
print(regex.findall(r"\p{Greek}+", "fox:αλεπού,eagle:αετός"))
# extract all words
print(regex.findall(r"\p{Word}+", "φοο12,βτ_4,foo"))
# delete all characters other than letters
# \p{^L} can also be used instead of \P{L}
print(regex.sub(r"\P{L}+", r"", "φοο12,βτ_4,foo"))
# to get codepoints for ASCII characters
print([hex(ord(c)) for c in "fox"])
# to get codepoints for Unicode characters
print([c.encode("unicode_escape") for c in "αλεπού"])
print([c.encode("unicode_escape") for c in "İıſK"])
# character range example using \u
# all english lowercase letters
print(re.findall(r"[\u0061-\u007a]+", "fox:αλεπού,eagle:αετός"))

print()
print("Exercises")
print()

# Exercises
# a) Output True or False depending on input string
# made up of ASCII characters or not.
# Consider the input to be non-empty strings and any
# character that isn’t part of 7-bit ASCII set
# should give False
STR1 = "123—456"
STR2 = "good fοοd"
STR3 = "happy learning!"
STR4 = "İıſK"
STR5 = "àpple"
print(not bool(re.search(r"[^\x00-\x7f]", STR1)))
print(not bool(re.search(r"[^\x00-\x7f]", STR2)))
print(not bool(re.search(r"[^\x00-\x7f]", STR3)))
print(not bool(re.search(r"[^\x00-\x7f]", STR4)))
print(not bool(re.search(r"[^\x00-\x7f]", STR5)))
print(STR1.isascii())
print(STR2.isascii())
print(STR3.isascii())
print(STR4.isascii())
print(STR5.isascii())
print([c.encode("unicode_escape") for c in STR1])
print([c.encode("unicode_escape") for c in STR2])
print([c.encode("unicode_escape") for c in STR3])
print([c.encode("unicode_escape") for c in STR4])
print([c.encode("unicode_escape") for c in STR5])

# b) Does the . quantifier match non-ASCII characters even with
# the re.ASCII flag enabled?
m = re.search(r".+", "fox:αλεπού")
if m:
    print(m[0])

m = re.search(r"(?a).+", "fox:αλεπού")
if m:
    print(m[0])

subscripts = re.compile(r"[₁₂₃₄₅₆₇₈₉₀]")
STR = "a₅b₁₀"
print(subscripts.findall(STR))
subscripts = re.compile(r"[₁₂₃₄₅₆₇₈₉₀]+")
print(subscripts.findall(STR))
superscripts = re.compile(r"\d+[²³¹⁰ⁱ⁴⁵⁶⁷⁸⁹⁺⁻⁼⁽⁾ⁿ]+")
STR = "N = 2¹⁰"
print(superscripts.findall(STR))
