#!/usr/bin/env python
"""
Gotchas.

######################################################################
# @author      : Linus Fernandes (linusfernandes at gmail dot com)
# @file        : gotchas
# @created     : Thursday Mar 02, 2023 09:57:41 IST
# @description :
# -*- coding: utf-8 -*-'
######################################################################
"""
import re
import regex

print(bool(re.search(r"\t", "cat\tdog")))
try:
    print(bool(re.search(r"\c", "cat\tdog")))
except re.error as e:
    print(str(e))

# note also the use of special group for enabling multiline flag
print(re.sub(r"(?m)^", r"foo ", "1\n2\n"))
print(re.sub(r"(?m)$", r" baz", "1\n2\n"))

# How much does * or *+ match?
# there is an extra empty string match at end of matches
print(re.sub(r"[^,]*", r"{\g<0>}", ",cat,tiger"))
print(re.sub(r"[^,]*+", r"{\g<0>}", ",cat,tiger"))
print(re.sub(r"[^,]+", r"{\g<0>}", ",cat,tiger"))
print(regex.sub(r"[^,]*", r"{\g<0>}", ",cat,tiger"))
print(regex.sub(r"[^,]*+", r"{\g<0>}", ",cat,tiger"))
print(regex.sub(r"[^,]+", r"{\g<0>}", ",cat,tiger"))
# use lookarounds as a workaround
print(re.sub(r"(?<![^,])[^,]*", r"{\g<0>}", ",cat,tiger"))

# Referring to text matched by a capture group with a quantifier will give
# only the last match,
# not entire match. Use a non-capturing group
# inside a capture group to get the entire matched
# portion.
print(re.sub(r"\A([^,]+,){3}([^,]+)", r"\1(\2)", "1,2,3,4,5,6,7", count=1))
print(re.sub(r"\A((?:[^,]+,){3})([^,]+)", r"\1(\2)", "1,2,3,4,5,6,7", count=1))
# as mentioned earlier, findall can be useful for debugging purposes
print(re.findall(r"([^,]+,){3}", "1,2,3,4,5,6,7"))
print(re.findall(r"(?:[^,]+,){3}", "1,2,3,4,5,6,7"))

# When using flags options with regex module,
# the constants should also be used from
# regex module. A typical workflow shown below:
# Using re module, unsure if a feature is available
print(re.findall(r"[[:word:]]+", "fox:αλεπού,eagle:αετός", flags=re.A))
# Ok, convert re to regex
# Oops, output is still wrong
print(regex.findall(r"[[:word:]]+", "fox:αλεπού,eagle:αετός", flags=re.A))
# Finally correct solution, the constant had to be changed as well
print(regex.findall(r"[[:word:]]+", "fox:αλεπού,eagle:αετός", flags=regex.A))
