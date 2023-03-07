#!/usr/bin/env python
"""
Recursion.

######################################################################
# @author      : Linus Fernandes (linusfernandes at gmail dot com)
# @file        : recursion
# @created     : Tuesday Mar 07, 2023 09:57:43 IST
# @description :
# -*- coding: utf-8 -*-'
######################################################################
"""
import regex

PAT = r"a(?R)?z"
regexx = regex.compile(PAT)
S1 = "aaazzz"
S2 = "aaazzzz"
m = regexx.search(S1)
if m:
    print(m[0])
m = regexx.search(S2)
if m:
    print(m[0])
PAT = r"^(a(?1)?z)$"
regexx = regex.compile(PAT)
m = regexx.search(S1)
if m:
    print(m[0])
m = regexx.search(S2)
if m:
    print(m[0])

PAT = r"\((?>[^()]|(?R))*\)"
regexx = regex.compile(PAT)
S1 = "((3+4))(4-5)"
S2 = ")(3+7)("
m = regexx.search(S1)
if m:
    print(m[0])
print(regexx.findall(S1))
m = regexx.search(S2)
if m:
    print(m[0])

PAT = r"\((?R)*\)|[^()]+"
regexx = regex.compile(PAT)
m = regexx.search(S1)
if m:
    print(m[0])
print(regexx.findall(S1))
m = regexx.search(S2)
if m:
    print(m[0])
S3 = "3+7()"
m = regexx.search(S3)
if m:
    print(m[0])

PAT = r"(?:\((?R)*\)|[^()]+)"
regexx = regex.compile(PAT)
m = regexx.search(S1)
if m:
    print(m[0])
print(regexx.findall(S1))

PAT = r"^((.)(?1)\2|.?)$"
regexx = regex.compile(PAT)
S1 = "kayak"
m = regexx.search(S1)
if m:
    print(m[0])
print(regexx.findall(S1))
