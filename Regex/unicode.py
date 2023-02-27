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

# \w is Unicode aware
print(re.findall(r"\w+", "fox:αλεπού"))
print(re.findall(r"\w+", "fox:αλεπού", flags=re.A))
print(re.findall(r"[a-zA-Z0-9_]+", "fox:αλεπού"))
print(bool(re.search(r"[a-zA-Z]", "İıſK")))
m = re.search(r"[a-z]+", "İıſK", flags=re.I)
if m:
    print(m[0])
print(bool(re.search(r"[a-z]", "İıſK", flags=re.I | re.A)))
