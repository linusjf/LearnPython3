#!/usr/bin/env python
"""
Backreferences.

######################################################################
# @author      : Linus Fernandes (linusfernandes at gmail dot com)
# @file        : backreferences
# @created     : Tuesday Feb 14, 2023 15:56:54 IST
# @description :
# -*- coding: utf-8 -*-'
######################################################################
"""
import re
import urllib.request

import regex

# remove square brackets that surround digit characters
print(re.sub(r"\[(\d+)\]", r"\1", "[52] apples and [31] mangoes"))
# replace __ with _ and delete _ if it is alone
print(re.sub(r"(_)?_", r"\1", "_foo_ __123__ _baz_"))
# add something around the matched strings
print(re.sub(r"\d+", r"(\g<0>0)", "52 apples and 31 mangoes"))
# note the use of count flag
# otherwise empty string matching with * will come into play
print(re.sub(r".*", r"Hi,\g<0>. Have a nice day!", "Linus Fernandes", count=1))
# swap words that are separated by a comma
print(re.sub(r"(\w+),(\w+)", r"\2,\1", "good,bad 42,24"))

# whole words that have at least one consecutive repeated character
words = ["effort", "flee", "facade", "oddball", "rat", "tool"]
print([w for w in words if re.search(r"\b\w*(\w)\1\w*\b", w)])
# remove any number of consecutive duplicate words separated by space
# quantifiers can be applied to backreferences too!
print(re.sub(r"\b(\w+)( \1)+\b", r"\1", "aa a a a 42 f_1 f_1 f_13.14"))

# without capture group
print(re.split(r"\d+", "Sample123string42with777numbers"))
# to include the matching delimiter strings as well in the output
print(re.split(r"(\d+)", "Sample123string42with777numbers"))
# optional argument maxsplit can be used to specify no. of splits
# setting to 1 gives behavior like partition string method
print(re.split(r"(1*2)", "3111111111125111142", maxsplit=1))
# normal capture group will hinder ability to get whole match
# non-capturing group to the rescue
print(re.findall(r"\b\w*(?:st|in)\b", "cost akin more east run against"))
# capturing wasn't needed here, only common grouping and quantifier
print(re.split(r"hand(?:y|ful)?", "123hand42handy777handful500"))
# with normal grouping, need to keep track of all the groups
print(re.sub(r"\A(([^,]+,){3})([^,]+)", r"\1(\3)", "1,2,3,4,5,6,7", count=1))
# using non-capturing groups, only relevant groups have to be tracked
print(re.sub(r"\A((?:[^,]+,){3})([^,]+)", r"\1(\2)", "1,2,3,4,5,6,7", count=1))
WORDS = "effort flee facade oddball rat tool"
# whole words containing at least one consecutive repeated character
repeat_char = re.compile(r"\b\w*(\w)\1\w*\b")
# () in findall will only return text matched by capture groups
print(repeat_char.findall(WORDS))

WORDS = "effort flee facade oddball rat tool"
# whole words containing at least one consecutive repeated character
repeat_char = re.compile(r"\b\w*(\w)\1\w*\b")
# () in findall will only return text matched by capture groups
print(repeat_char.findall(WORDS))
m_iter = repeat_char.finditer(WORDS)
print([m[0] for m in m_iter])

# giving names to first and second captured words
re.sub(r"(?P<fw>\w+),(?P<sw>\w+)", r"\g<sw>,\g<fw>", "good,bad 42,24")
SENTENCE = "I bought an apple"
m = re.search(r"(?P<fruit>\w+)\Z", SENTENCE)
print(m[1])
print(m["fruit"])
print(m.group("fruit"))

ROW = "today,2008-03-24,food,2012-08-12,nice,5632"
# with re module and manually repeating the pattern
print(re.search(r"\d{4}-\d{2}-\d{2}.*\d{4}-\d{2}-\d{2}", ROW)[0])
# with regex module and subexpression calling
print(regex.search(r"(\d{4}-\d{2}-\d{2}).*(?1)", ROW)[0])
print(regex.search(r"(?P<date>\d{4}-\d{2}-\d{2}).*(?&date)", ROW)[0])

print("\n--------------")
print("Exercises")
print("--------------\n")

ROW = "3.14,hi:42.5,bye:1056.1,cool:00.9,fool"
regex = regex.compile(r"(\d+\.\d),(\w+)")
print(regex.sub(r"\2,\g<1>0", ROW))

SCARLET_PIMPERNEL_LINK = r"https://www.gutenberg.org/cache/epub/60/pg60.txt"
word_expr = re.compile(rb"\b\w+(\w)\1\w*(\w)\2\w*\b")  # add your solution here
COUNT = 0
with urllib.request.urlopen(SCARLET_PIMPERNEL_LINK) as ip_file:
    for line in ip_file:
        for word in re.findall(rb"\w+", line):
            if word_expr.search(word):
                COUNT += 1
print(COUNT)

# Convert the given markdown headers to corresponding anchor tag. Consider the
# input
# to start with one or more # characters followed by
# space and word characters. The name
# attribute is constructed by converting the header to lowercase and replacing
# spaces with hyphens. Can you do it without using a capture group?
HEADER1 = "# Regular Expressions"
HEADER2 = "## Compiling regular expressions"


# add your solution here for header1
def anchor(_):
    """Anchor."""
    match = _[0].replace(" ", "-")
    _anchor = match.split("-")[0]
    _name = match[match.find("-") + 1:].lower()
    _label = _[0][_[0].find(" ") + 1:]
    return _anchor + " " + '<a name="' + _name + '"></a>' + _label


regex = re.compile(r"\#+[A-Za-z0-9 ]+")
print(regex.findall(HEADER1))
print(regex.findall(HEADER2))
print(regex.sub(anchor, HEADER1))
print(regex.sub(anchor, HEADER2))

# Convert the given markdown anchors to corresponding hyperlinks.
ANCHOR1 = '# <a name="regular-expressions"></a>Regular Expressions'
ANCHOR2 = '## <a name="subexpression-calls"></a>Subexpression calls'
regex = re.compile(r'\#+ \<a name="([\w-]+)"></a>([A-Za-z ]+)')
print(regex.findall(ANCHOR1))
print(regex.findall(ANCHOR2))
print(regex.sub(r"[\2](#\1)", ANCHOR1))
print(regex.sub(r"[\2](#\1)", ANCHOR2))

# Use appropriate regular expression function to get the expected output
# for the given string.
STR1 = "price_42 roast:\t\n:-ice==cat\neast"
print(re.findall(r"\w+|[\s:-]+|=+", STR1))
