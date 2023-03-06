#!/usr/bin/env python
"""
Controlverbs.

######################################################################
# @author      : Linus Fernandes (linusfernandes at gmail dot com)
# @file        : controlverbs
# @created     : Monday Mar 06, 2023 12:44:01 IST
# @description :
# -*- coding: utf-8 -*-'
######################################################################
"""
import regex

PAT = r"Comedian: (?:B\w+ Murray|E\w+ Murphy|P\w+ Sellers)"
regexx = regex.compile(PAT)
S1 = "Comedian: Bill Burr -- Comedian: Peter Sellers"
m = regexx.search(S1)
if m:
    print(m[0])
S1 = """
Quincy Jones: music producer
Peter Sellers: comedian
Rashida Jones: actress
Jerry Seinfeld: comedian
Indiana Jones: movie character
Bill Burr: comedian
Eddie Murphy: actor-comedian
"""
S2 = """Quincy Jones: music producer
Peter Sellers: comedian
Rashida Jones: actress
Jerry Seinfeld: comedian
Indiana Jones: movie character
Bill Burr: comedian
Eddie Murphy: actor-comedian"""
S3 = """Peter Sellers: comedian
Quincy Jones: music producer
Rashida Jones: actress
Jerry Seinfeld: comedian
Indiana Jones: movie character
Bill Burr: comedian
Eddie Murphy: actor-comedian"""
PAT = r"(?ms)(^(?>\w{6,}) Jones:[^\r\n]+)+"
regexx = regex.compile(PAT)
m = regexx.search(S1)
if m:
    print(m[0])
print(regexx.findall(S1))
m = regexx.search(S2)
if m:
    print(m[0])
print(regexx.findall(S2))
PAT = r"(?ms)(^\w{6,}+ Jones:[^\r\n]+)+"
regexx = regex.compile(PAT)
m = regexx.search(S1)
if m:
    print(m[0])
print(regexx.findall(S1))
m = regexx.search(S2)
if m:
    print(m[0])
print(regexx.findall(S2))
PAT = r"(?ms)(^\w{6,}(*PRUNE) Jones:[^\r\n]+)+"
regexx = regex.compile(PAT)
m = regexx.search(S1)
if m:
    print(m[0])
print(regexx.findall(S1))
m = regexx.search(S2)
if m:
    print(m[0])
print(regexx.findall(S2))

ATOMIC = r"(?>\w{2,4} )Murray|Bill Burr|Peter Sellers"
print(regex.search(ATOMIC, "Bill Burr -- Peter Sellers"))
ACTOR_REGEX = r"\w{2,4} (*PRUNE)Murray|Bill Burr|Peter Sellers"
print(regex.search(ACTOR_REGEX, "Bill Burr -- Peter Sellers"))
PAT = r"(?ms)((?:(?!^\w{6,} Jones:)[^\r\n]+\r?\n)(*SKIP)(*FAIL)|[^\r\n]+\r?\n)"
regexx = regex.compile(PAT)
m = regexx.search(S1)
if m:
    print(m[0])
print(regexx.findall(S1))
m = regexx.search(S2)
if m:
    print(m[0])
print(regexx.findall(S2))
PAT = r"(?ms)(?:(?:(?=^\w{6,} Jones:)[^\r\n]+\r?\n?)(*SKIP)(*FAIL)|([^\r\n]+)\r?\n?)"
regexx = regex.compile(PAT)
m = regexx.search(S1)
if m:
    print(m.groups(0))
print(regexx.findall(S1))
print(regexx.sub("", S1))
m = regexx.search(S2)
if m:
    print(m.groups(0))
print(regexx.findall(S2))
print(regexx.sub("", S2))
m = regexx.search(S3)
if m:
    print(m.groups(0))
print(regexx.findall(S3))
print(regexx.sub("", S3))
