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
Rashida Jones: actress
Peter Sellers: comedian
Indiana Jones: movie character
Jerry Seinfeld: comedian
Bill Burr: comedian
Eddie Murphy: actor-comedian
"""
PAT = r"(?ms)(^(?>\w{6,}) Jones:[^\r\n]+)+"
regexx = regex.compile(PAT)
m = regexx.search(S1)
if m:
    print(m[0])
print(regexx.findall(S1))
PAT = r"(?ms)(^\w{6,}+ Jones:[^\r\n]+)+"
regexx = regex.compile(PAT)
m = regexx.search(S1)
if m:
    print(m[0])
print(regexx.findall(S1))
PAT = r"(?ms)(^\w{6,}(*PRUNE) Jones:[^\r\n]+)+"
regexx = regex.compile(PAT)
m = regexx.search(S1)
if m:
    print(m[0])
print(regexx.findall(S1))
