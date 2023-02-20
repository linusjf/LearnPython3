#!/usr/bin/env python
"""
Characters.

######################################################################
# @author      : Linus Fernandes (linusfernandes at gmail dot com)
# @file        : characters
# @created     : Monday Feb 13, 2023 13:18:03 IST
# @description :
# -*- coding: utf-8 -*-'
######################################################################
"""
import re

words = ["cute", "cat", "cot", "coat", "cost", "scuttle"]
print([w for w in words if re.search(r"c[ou]t", w)])
# same as: r'(a|e|o)+t'
print(re.sub(r"[aeo]+t", r"X", "meeting cute boat site foot"))
# all digits
print(re.findall(r"[0-9]+", "Sample123string42with777numbers"))
# whole words made up of lowercase alphabets and digits only
print(re.findall(r"\b[a-z0-9]+\b", "coat Bin food tar12 best"))
# whole words made up of lowercase alphabets, but starting with 'p' to 'z'
print(re.findall(r"\b[p-z][a-z]*\b", "coat tin food put stoop best"))
# whole words made up of only 'a' to 'f' and 'p' to 't' lowercase alphabets
print(re.findall(r"\b[a-fp-t]+\b", "coat tin food put stoop best"))

print(re.findall(r"[0-9]+", "Sample123string42with777numbers"))
# whole words made up of lowercase alphabets and digits only
print(re.findall(r"\b[a-z0-9]+\b", "coat Bin food tar12 best"))
# whole words made up of lowercase alphabets, but starting with 'p' to 'z'
print(re.findall(r"\b[p-z][a-z]*\b", "coat tin food put stoop best"))
# whole words made up of only 'a' to 'f' and 'p' to 't' lowercase alphabets
print(re.findall(r"\b[a-fp-t]+\b", "coat tin food put stoop best"))

print(re.findall(r"\b[12][0-9]\b", "23 154 12 26 98234"))
# numbers >= 100
print(re.findall(r"\b[0-9]{3,}\b", "23 154 12 26 98234"))
# numbers >= 100 if there are leading zeros
print(re.findall(r"\b0*[1-9][0-9]{2,}\b", "0501 035 154 12 26 98234"))
# numbers < 350
m_iter = re.finditer(r"[0-9]+", "45 349 651 593 4 204")
print([m[0] for m in m_iter if int(m[0]) < 350])


# note that return value is string and s[0] is used to get matched portion
def num_range(_):
    """Num-Range."""
    return "1" if 200 <= int(_[0]) <= 650 else "0"


# numbers between 200 and 650
# note that only function name is supplied, () is not used
# Match object is automatically passed as argument
print(re.sub(r"[0-9]+", num_range, "45 349 651 593 4 204"))
# all non-digits
print(re.findall(r"[^0-9]+", "Sample123string42with777numbers"))
# remove first two columns where : is delimiter
print(re.sub(r"\A([^:]+:){2}", r"", "foo:123:bar:baz", count=1))
# deleting characters at end of string based on a delimiter
print(re.sub(r"=[^=]+\Z", r"", "foo=42; baz=123", count=1))

words = ["tryst", "fun", "glyph", "pity", "why"]
# words not containing vowel characters
print([w for w in words if re.search(r"\A[^aeiou]+\Z", w)])
# easier to write and maintain
print([w for w in words if not re.search(r"[aeiou]", w)])
# - should be first or last character or escaped using \
print(re.findall(r"\b[a-z-]{2,}\b", "ab-cd gh-c 12-423"))
print(re.findall(r"\b[a-z\-0-9]{2,}\b", "ab-cd gh-c 12-423"))
# ^ should be other than first character or escaped using \
print(re.findall(r"a[+^]b", "f*(a^b) - 3*(a+b)"))
print(re.findall(r"a[\^+]b", "f*(a^b) - 3*(a+b)"))
# [ can be escaped with \ or placed as last character
# ] can be escaped with \ or placed as first character
print(re.search(r'[a-z\[\]0-9]+', 'words[5] = tea')[0])
# \ should be escaped using \
print(re.search(r'[a\\b]+', r'5ba\babc2')[0])

print(re.split(r"\d+", "Sample123string42with777numbers"))
print(re.findall(r"\d+", "foo=5, bar=3; x=83, y=120"))
print("".join(re.findall(r"\b\w", "sea eat car rat eel tea")))
print(re.findall(r"[\w\s]+", "tea sea-pit sit-lean\tbean"))
print(re.sub(r"\D+", r"-", "Sample123string42with777numbers"))
print(re.sub(r"\W+", r"", "foo=5, bar=3; x=83, y=120"))
print(re.findall(r"\S+", " 1..3 \v\f foo_baz 42\tzzz \r\n1-2-3 "))

print("\n-----------")
print("Exercises")
print("-----------\n")
# Delete all pair of parentheses, unless they contain a parentheses character.
STR1 = "def factorial()"
STR2 = "a/b(division) + c%d(#modulo) - (e+(j/k-3)*4)"
STR3 = "Hi there(greeting). Nice day(a(b)"
remove_parentheses = re.compile(r"\([#/\w-]*\)")  # add your solution here
print(remove_parentheses.sub("", STR1))
print(remove_parentheses.sub("", STR2))
print(remove_parentheses.sub("", STR3))

# Extract all hex character sequences, with optional prefix.
# Match the characters case insen-
# sitively, and the sequences shouldn’t be surrounded by other word characters.
hex_seq = re.compile(r"\b(?:0x)?[a-f0-9]+\b", flags=re.IGNORECASE)
STR1 = "128A foo 0xfe32 34 0xbar"
STR2 = "0XDEADBEEF place 0x0ff1ce bad"
print(hex_seq.findall(STR1))
print(hex_seq.findall(STR2))

# Check if input string contains any number sequence that is greater than 624.
STR1 = "hi0000432abcd"
STR2 = "42_624 0512"
STR3 = "3.14 96 2 foo1234baz"
REGEX = r"0*[1-9][0-9]+"
m_iter = re.finditer(REGEX, STR1)
print([m[0] for m in m_iter if int(m[0]) > 624])
m_iter = re.finditer(REGEX, STR2)
print([m[0] for m in m_iter if int(m[0]) > 624])
m_iter = re.finditer(REGEX, STR3)
print([m[0] for m in m_iter if int(m[0]) > 624])

# Split the given strings based on consecutive sequence of digit or
# whitespace characters.
STR1 = "lion \t Ink32onion Nice"
STR2 = "**1\f2\n3star\t7 77\r**"
expr = re.compile(r"[\s0-9]+")  # add your solution here
print(expr.split(STR1))
print(expr.split(STR2))
