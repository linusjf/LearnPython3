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
