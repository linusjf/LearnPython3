#!/usr/bin/env python
"""
Conditionals.

######################################################################
# @author      : Linus Fernandes (linusfernandes at gmail dot com)
# @file        : conditionals
# @created     : Saturday Mar 04, 2023 12:13:34 IST
# @description :
# -*- coding: utf-8 -*-'
######################################################################
"""
import regex

numbered_capture = regex.compile(r"^(START)?\d+(?(1)END|\b)")
S1 = "START134END"
S2 = "456"
print(numbered_capture.sub("", S1))
print(numbered_capture.sub("", S2))
print(numbered_capture.findall(S1))
print(numbered_capture.findall(S2))
numbered_capture = regex.compile(r"^(?:START\d+END|\d+\b)")
print(numbered_capture.sub("", S1))
print(numbered_capture.sub("", S2))
print(numbered_capture.findall(S1))
print(numbered_capture.findall(S2))

named_capture = regex.compile(r"^(?<UC>[A-Z])?\d+(?(UC)_END)$")
S1 = "A55_END"
S2 = "456"
print(named_capture.sub("", S1))
print(named_capture.sub("", S2))
print(named_capture.findall(S1))
print(named_capture.findall(S2))

PAT = r"^(?(?=.*_FRUIT$)(?:apple|banana)|(?:carrot|pumpkin))\b"
lookaround = regex.compile(PAT)
S1 = "apple _FRUIT"
S2 = "carrot"
print(lookaround.sub("", S1))
print(lookaround.sub("", S2))
print(lookaround.findall(S1))
print(lookaround.findall(S2))

subroutine = regex.compile(r"(A(?(1)B|C))(?1)")
S1 = "ACAB"
print(subroutine.sub("", S1))
print(subroutine.findall(S1))

named_subroutine = regex.compile(r"(?P<foo>A(?(foo)B|C))(?P>foo)")
S1 = "ACAB"
print(named_subroutine.sub("", S1))
print(named_subroutine.findall(S1))

nested_subroutine = regex.compile(r"(A(?(1)C))(B(?1))(?2)")
S1 = "ABACBAC"
print(nested_subroutine.sub("", S1))
print(nested_subroutine.findall(S1))

nested_subroutine = regex.compile(r"(A(?(2)C))(B(?1))(?2)")
S1 = "ABABA"
S2 = "ABABAC"
S3 = "ABABACD"
print(nested_subroutine.sub("", S1))
print(nested_subroutine.findall(S1))
print(nested_subroutine.sub("", S2))
print(nested_subroutine.findall(S2))
print(nested_subroutine.sub("", S3))
print(nested_subroutine.findall(S3))

recursive = regex.compile(r"(A(?(R))B)(?R)?C")
S1 = "AABCC"
S2 = "ACABC"
print(recursive.sub("", S1))
print(recursive.findall(S1))
print(recursive.sub("", S2))
print(recursive.findall(S2))

delimiters = regex.compile(r"^(?:(BEGIN:)|({{)).*?(?(1):END)(?(2)}})$")
alternate = regex.compile(r"^(BEGIN:.*?:END)|({{.*?}})$")
S1 = "{{foo}}"
S2 = "BEGIN:bar:END"
print(delimiters.sub("", S1))
print(delimiters.findall(S1))
print(delimiters.sub("", S2))
print(delimiters.findall(S2))
print(alternate.sub("", S1))
print(alternate.findall(S1))
print(alternate.sub("", S2))
print(alternate.findall(S2))
