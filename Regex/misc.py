#!/usr/bin/env python
"""
Misc.

######################################################################
# @author      : Linus Fernandes (linusfernandes at gmail dot com)
# @file        : misc
# @created     : Monday Feb 27, 2023 21:32:31 IST
# @description :
# -*- coding: utf-8 -*-'
######################################################################
"""
import re
import regex

# one to one mappings
d = {"1": "one", "2": "two", "4": "four"}
print(re.sub(r"[124]", lambda m: d[str(m[0])], "9234012"))
# if the matched text doesn't exist as a key, default value will be used
print(re.sub(r"\d", lambda m: d.get(str(m[0]), "X"), "9234012"))
# For swapping two or more portions without using intermediate
# result, using a dict is rec-
# ommended.
swap = {"cat": "tiger", "tiger": "cat"}
WORDS = "cat tiger dog tiger cat"
# replace word if it exists as key, else leave it as is
print(re.sub(r"\w+", lambda m: swap.get(str(m[0]), str(m[0])), WORDS))
# or, build the alternation list manually for simple cases
print(re.sub(r"cat|tiger", lambda m: swap[str(m[0])], WORDS))
# For dict that have many entries and likely
# to undergo changes during development, building
# alternation list manually is not a good choice.
# Also, recall that as per precedence rules, longest
# length string should come first.
d = {"hand": "1", "handy": "2", "handful": "3", "a^b": "4"}
# take care of metacharacter escaping first
LIST = [re.escape(k) for k in d]
# build alternation list
# add anchors and flags as needed to construct the final RE
print("|".join(sorted(LIST, key=len, reverse=True)))

WORD = "coffining"
print(WORD)
# recursively delete 'fin'
while True:
    WORD, cnt = re.subn(r"fin", r"", WORD)
    if cnt == 0:
        break
    print(WORD)
print(WORD)

ROW = "421,foo,2425,42,5,foo,6,6,42"
# lookarounds used to ensure start/end of column matching
# possessive quantifier used to ensure partial column is not captured
# if a column has same text as another column, the latter column is deleted
print(ROW)
while True:
    ROW, cnt = regex.subn(r"(?<=\A|,)([^,]++).*\K,\1(?=,|\Z)", r"", ROW)
    if cnt == 0:
        break
    print(ROW)
print(ROW)
print()
ROW = "421,foo,2425,42,5,foo,6,6,42"
print()
print(ROW)
while True:
    ROW, cnt = regex.subn(r"(?<=\A|,)([^,]+).*\K,\1(?=,|\Z)", r"", ROW)
    if cnt == 0:
        break
    print(ROW)
print(ROW)

STR = "123-87-593 42 foo"
print(STR)
# all non-whitespace characters from start of string
print(regex.findall(r"\G\S", STR))
print(regex.sub(r"\G\S", r"*", STR))
# all digits and optional hyphen combo from start of string
print(regex.findall(r"\G\d+-?", STR))
print(regex.sub(r"\G(\d+)(-?)", r"(\1)\2", STR))

# all word characters from start of string
# only if it is followed by word character
print(regex.findall(r"\G\w(?=\w)", "cat12 bat pin"))
print(regex.sub(r"\G\w(?=\w)", r"\g<0>:", "cat12 bat pin"))
# all lowercase alphabets or space from start of string
print(regex.sub(r"\G[a-z ]", r"(\g<0>)", "par tar-den hen-food mood"))

# note the use of possessive quantifier
EQN0 = "a + (b * c) - (d / e)"
print(regex.findall(r"\([^()]++\)", EQN0))
EQN1 = "((f+x)^y-42)*((3-g)^z+2)"
print(regex.findall(r"\([^()]++\)", EQN1))
# Next, matching a set of parentheses which may optionally
# contain any
# number of non-nested
# sets of parentheses (termed as level-two RE for reference).
# See debuggex for a railroad
# diagram, notice the recursive nature of this RE.
EQN1 = "((f+x)^y-42)*((3-g)^z+2)"
# note the use of non-capturing group
print(regex.findall(r"\((?:[^()]++|\([^()]++\))++\)", EQN1))
EQN2 = "a + (b) + ((c)) + (((d)))"
print(regex.findall(r"\((?:[^()]++|\([^()]++\))++\)", EQN2))

lvl2 = regex.compile(
    """\\( #literal (
(?: #start of non-capturing group
[^()]++ #non-parentheses characters
| #OR
\\([^()]++\\) #level-one RE
)++ #end of non-capturing group, 1 or more times
\\) #literal )
""",
    flags=regex.X,
)
print(lvl2.findall(EQN1))
print(lvl2.findall(EQN2))

lvln = regex.compile(
    """
\\( #literal (
(?: #start of non-capturing group
[^()]++ #non-parentheses characters
| #OR
(?0) #recursive call
)++ #end of non-capturing group, 1 or more times
\\) #literal )
""",
    flags=regex.X,
)
print(lvln.findall(EQN0))
print(lvln.findall(EQN1))
print(lvln.findall(EQN2))
EQN3 = "(3+a) * ((r-2)*(t+2)/6) + 42 * (a(b(c(d(e)))))"
print(lvln.findall(EQN3))

# similar to: r'\d+' or r'[0-9]+'
print(regex.split(r"[[:digit:]]+", "Sample123string42with777numbers"))
# similar to: r'[a-zA-Z]+'
print(regex.sub(r"[[:alpha:]]+", r":", "Sample123string42with777numbers"))
# similar to: r'[\w\s]+'
print(regex.findall(r"[[:word:][:space:]]+", "tea sea-pit sit-lean\tbean"))
# similar to: r'\S+'
print(regex.findall(r"[[:^space:]]+", "tea sea-pit sit-lean\tbean"))
# words not surrounded by punctuation characters
STR = "tie. ink eat;"
print(regex.findall(r"(?<![[:punct:]])\b\w+\b(?![[:punct:]])", STR))

# [^aeiou] will match any non-vowel character
# which means space is also a v
print(re.findall(r"\b[^aeiou]+\b", "tryst glyph pity why"))
# intersection or difference can be used here
# to get a positive definition of characters to match
print(regex.findall(r"(?V1)\b[a-z&&[^aeiou]]+\b", "tryst glyph pity why"))
# [[a-l]~~[g-z]] is same as [a-fm-z]
print(regex.findall(r"(?V1)\b[[a-l]~~[g-z]]+\b", "gets eat top sigh"))
# remove all punctuation characters except . ! and ?
PARA = '"Hi", there! How *are* you? All fine here.'
print(regex.sub(r"(?V1)[[:punct:]--[.!?]]+", r"", PARA))

# change lowercase words other than imp or rat
WORDS = "tiger imp goat eagle rat"
regex.sub(r"\b(?:imp|rat)\b(*SKIP)(*F)|[a-z]++", r"(\g<0>)", WORDS)
# change all commas other than those inside double quotes
ROW = '1,"cat,12",nice,two,"dog,5"'
regex.sub(r'"[^"]++"(*SKIP)(*F)|,', r"|", ROW)

# a) Count the maximum depth of nested braces for the given string.
# Unbalanced or wrongly ordered braces should return -1


def max_nested_braces(word):
    """Max_nested_braces."""
    print(word)
    count = 0
    while True:
        word, no_of_subs = re.subn(r"\{[^{}]*\}", "", word)
        print(word)
        if no_of_subs == 0:
            break
        count += 1
    if re.search(r"[{}]", word):
        return -1
    return count


print(max_nested_braces("a*b"))
print(max_nested_braces("}a+b{"))
print(max_nested_braces("a*b+{}"))
print(max_nested_braces("{{a+2}*{b+c}+e}"))
print(max_nested_braces("{{a+2}*{b+{c*d}}+e}"))
print(max_nested_braces("{{a+2}*{\n{b+{c*d}}+e*d}}"))
print(max_nested_braces("a*{b+c*{e*3.14}}}"))


def max_nested_brackets(expr):
    """Max_nested_brackets."""
    count = 0
    while (_op := re.subn(r"\{[^{}]*\}", "", expr)) and _op[1]:
        expr = _op[0]
        count += 1

    if re.search(r"[{}]", expr):
        return -1
    return count


print(max_nested_brackets("a*b"))
print(max_nested_brackets("}a+b{"))
print(max_nested_brackets("a*b+{}"))
print(max_nested_brackets("{{a+2}*{b+c}+e}"))
print(max_nested_brackets("{{a+2}*{b+{c*d}}+e}"))
print(max_nested_brackets("{{a+2}*{\n{b+{c*d}}+e*d}}"))
print(max_nested_brackets("a*{b+c*{e*3.14}}}"))

# b) Replace the string par with spar , spare with extra and park with garden
d = {"par": "spar", "spare": "extra", "park": "garden"}
# take care of metacharacter escaping first
LIST = [re.escape(k) for k in d]
# build alternation list
# add anchors and flags as needed to construct the final RE
PAT = "|".join(sorted(LIST, key=len, reverse=True))
print(PAT)
STR1 = "apartment has a park"
STR2 = "do you have a spare cable"
STR3 = "write a parser"
print(re.sub(PAT, lambda m: d[str(m[0])], STR1))
print(re.sub(PAT, lambda m: d[str(m[0])], STR2))
print(re.sub(PAT, lambda m: d[str(m[0])], STR3))
