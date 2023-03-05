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

palindrome = regex.compile(r"(\w)(?:(?R)|\w?)\1")
S1 = "dontmatchme"
S2 = "kook"
S3 = "book"
S4 = "paper"
S5 = "kayak"
S6 = "okonoko"
S7 = "aaaaa"
S8 = "bbbb"
print(palindrome.sub("", S1))
print(palindrome.sub("", S2))
print(palindrome.sub("", S3))
print(palindrome.sub("", S4))
print(palindrome.sub("", S5))
print(palindrome.sub("", S6))
print(palindrome.sub("", S7))
print(palindrome.sub("", S8))
print(palindrome.findall(S1))
print(palindrome.findall(S2))
print(palindrome.findall(S3))
print(palindrome.findall(S4))
print(palindrome.findall(S5))
print(palindrome.findall(S6))
print(palindrome.findall(S7))
print(palindrome.findall(S8))

palindrome = regex.compile(r"^((\w)(?:(?1)|\w?)\2)$")
S1 = "dontmatchme"
S2 = "kook"
S3 = "book"
S4 = "paper"
S5 = "kayak"
S6 = "okonoko"
S7 = "aaaaa"
S8 = "bbbb"
print(palindrome.sub("", S1))
print(palindrome.sub("", S2))
print(palindrome.sub("", S3))
print(palindrome.sub("", S4))
print(palindrome.sub("", S5))
print(palindrome.sub("", S6))
print(palindrome.sub("", S7))
print(palindrome.sub("", S8))
print(palindrome.findall(S1))
print(palindrome.findall(S2))
print(palindrome.findall(S3))
print(palindrome.findall(S4))
print(palindrome.findall(S5))
print(palindrome.findall(S6))
print(palindrome.findall(S7))
print(palindrome.findall(S8))
