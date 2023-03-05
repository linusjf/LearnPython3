#!/usr/bin/env python
"""
Recursive.

######################################################################
# @author      : Linus Fernandes (linusfernandes at gmail dot com)
# @file        : recursive
# @created     : Sunday Mar 05, 2023 11:04:10 IST
# @description :
# -*- coding: utf-8 -*-'
######################################################################
"""
import regex

recursive = regex.compile(r"\w{3}\d{3}(?R)?")
S1 = "aaa111bbb222"
S2 = "aaa111bbb222ccc333ddd444"
print(recursive.sub("", S1))
print(recursive.findall(S1))
print(recursive.sub("", S2))
print(recursive.findall(S2))

alternative = regex.compile(r"\w{3}\d{3}(?R)?")
print(alternative.sub("", S1))
print(alternative.findall(S1))
print(alternative.sub("", S2))
print(alternative.findall(S2))

recursive = regex.compile(r"abc(?:$|(?R))")
S1 = "abc"
S2 = "abcabc"
S3 = "abc123"
print(recursive.sub("", S1))
print(recursive.findall(S1))
print(recursive.sub("", S2))
print(recursive.findall(S2))
print(recursive.sub("", S3))
print(recursive.findall(S3))
