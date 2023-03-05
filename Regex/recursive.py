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

S1 = """
Paint it white
Paint it black
Why not blue?
Or red or brown?
~1~2~3~4~5~6~7~8~9~10
"""
S2 = """Paint it blue
Paint it green
Paint it black
Why not white?
Or red or brown?
~1~2~3~4~5~6~7~8~9~10
"""

PAT = r"""
(?xsm)             # free-spacing mode, DOTALL, multi-line
(?=.*?blue)        # if blue isn't there, fail without delay

######    Recursive Section     ######
# This section aims to balance empty lines with digits, i.e.
# emptyLine,emptyLine,emptyLine ... ~1~2~3
# The last digit block is captured to Group 2, e.g. ~3
(?=                # lookahead
(                  # Group 1
(?:               # skip one line that doesn't contain blue
      ^              # start of line
      (?:(?!blue)[^\r\n])*  # zero or more chars
                            # that do not start blue
      (?:\r?\n)      # newline
    )
    (?:(?1)|[^~]+)   # recurse Group 1 OR match all non-tilde chars
    (~\d+)           # match a sequence of digits
)?                 # End Group 1
)                  # End lookahead.

# Group 2, if set, now contains the number of lines skipped
.*?               # lazily match chars up to...
blue              # match blue
.*?               # lazily match chars up to..
(?(2)\2)          # if Group 2 is set, match Group 2
~                 # Match the next tilde
\K                # drop what was matched so far
\d+               # match the next digits: this is the match
"""
print(S1)
recursive = regex.compile(PAT)
print(recursive.findall(S1))
print(bool(recursive.search(S1)))
print(S2)
print(recursive.findall(S2))
print(bool(recursive.search(S2)))

PAT2 = r"(?xsm)(?=.*?blue)(?=(^[^\r\n]*\r?\n)(?(?=^.*blue)[^~]+|(?1)))"
recursive = regex.compile(PAT2)
print(S1)
print(f"Line number : {len(recursive.findall(S1))}")
print(bool(recursive.search(S1)))
print(S2)
print(f"Line number : {len(recursive.findall(S2))}")
print(bool(recursive.search(S2)))
