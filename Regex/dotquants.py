#!/usr/bin/env python
"""
######################################################################
# @author      : Linus Fernandes (linusfernandes at gmail dot com)
# @file        : dotquants
# @created     : Monday Feb 06, 2023 16:05:00 IST
# @description :
# -*- coding: utf-8 -*-'
######################################################################
"""
import re

# matches character 'c', any character and then character 't'
print(re.sub(r'c.t', r'X', 'tac tin cat abc;tuv acute'))
# matches character 'r', any two characters and then character 'd'
print(re.sub(r'r..d', r'X', 'breadth markedly reported overrides'))
# matches character '2', any character and then character '3'
print(re.sub(r'2.3', r'8', '42\t35'))

# same as: r'ear|ar'
print(re.sub(r'e?ar', r'X', 'far feat flare fear'))
# same as: r'\bpar(t|)\b'
print(re.sub(r'\bpart?\b', r'X', 'par spare part party'))
# same as: r'\b(re.d|red)\b'
words = ['red', 'read', 'ready', 're;d', 'redo', 'reed']
print([w for w in words if re.search(r'\bre.?d\b', w)])
# same as: r'part|parrot'
print(re.sub(r'par(ro)?t', r'X', 'par part parrot parent'))
# same as: r'part|parrot|parent'
print(re.sub(r'par(en|ro)?t', r'X', 'par part parrot parent'))
# The * metacharacter quantifies a character or group to match 0 or more times. There is
# no upper bound, more details will be discussed at the end of this section.
# match 't' followed by zero or more of 'a' followed by 'r'
print(re.sub(r'ta*r', r'X', 'tr tear tare steer sitaara'))
# match 't' followed by zero or more of 'e' or 'a' followed by 'r'
print(re.sub(r't(e|a)*r', r'X', 'tr tear tare steer sitaara'))
# match zero or more of '1' followed by '2'
print(re.sub(r'1*2', r'X', '3111111111125111142'))
#Time to introduce re.split function:
# last element is empty because there is nothing between 511114 and 2
print(re.split(r'1*2', '3111111111125111142'))
# optional argument maxsplit specifies how many times to split
# later, you'll see how to get behavior like the str.partition method
print(re.split(r'1*2', '3111111111125111142', maxsplit=1))
# empty string matches at start and end of string
# it matches between every character
# and, there is an empty match after the split at u
print(re.split(r'u*', 'cloudy'))
#The + metacharacter quantifies a character or group to match 1 or more times. Similar
#to * quantifier, there is no upper bound. More importantly, this doesn’t have surprises like
#matching empty string in between patterns or at start/end of string.
print(re.sub(r'ta+r', r'X', 'tr tear tare steer sitaara'))
print(re.sub(r't(e|a)+r', r'X', 'tr tear tare steer sitaara'))
print(re.sub(r'1+2', r'X', '3111111111125111142'))
print(re.split(r'1+', '3111111111125111142'))
print(re.split(r'u+', 'cloudy'))
demo = ['abc', 'ac', 'adc', 'abbc', 'xabbbcz', 'bbb', 'bc', 'abbbbbc']
print([w for w in demo if re.search(r'ab{1,4}c', w)])
print([w for w in demo if re.search(r'ab{3,}c', w)])
print([w for w in demo if re.search(r'ab{,2}c', w)])
print([w for w in demo if re.search(r'ab{3}c', w)])
# match 'Error' followed by zero or more characters followed by 'valid'
print(bool(re.search(r'Error.*valid', 'Error: not a valid input')))
print(bool(re.search(r'Error.*valid', 'Error: key not found')))
#To allow matching in any order, you’ll have to bring in alternation as well. That is somewhat
#manageable for 2 or 3 patterns. In a later chapter, you’ll learn how to use lookarounds for a
#comparatively easier approach.
SEQ1 = 'cat and dog'
SEQ2 = 'dog and cat'
print(bool(re.search(r'cat.*dog|dog.*cat', SEQ1)))
print(bool(re.search(r'cat.*dog|dog.*cat', SEQ2)))

# if you just need True/False result, this would be a scalable approach
patterns = (r'cat', r'dog')
print(all(re.search(p, SEQ1) for p in patterns))
print(all(re.search(p, SEQ2) for p in patterns))
print(re.sub(r'f.?o', r'X', 'foot'))
# a more practical example
# prefix '<' with '\' if it is not already prefixed
print(re.sub(r'\\?<', r'\<', r'blah \< foo < bar \< blah < baz'))
# say goodbye to r'handful|handy|hand' shenanigans
print(re.sub(r'hand(y|ful)?', r'X', 'hand handy handful'))
SENTENCE = 'that is quite a fabricated tale'
# r't.*a' will always match from first 't' to last 'a'
# also, note that count argument is set to 1 for illustration purposes
print(re.sub(r't.*a', r'X', SENTENCE, count=1))
print(re.sub(r't.*a', r'X', 'star', count=1))
# matching first 't' to last 'a' for t.*a won't work for these cases
# the engine backtracks until .*q matches and so on
print(re.sub(r't.*a.*q.*f', r'X', SENTENCE, count=1))
print(re.sub(r't.*a.*u', r'X', SENTENCE, count=1))

print(re.sub(r'f.??o', r'X', 'foot', count=1))
print(re.sub(r'f.??o', r'X', 'frost', count=1))
print(re.sub(r'.{2,5}?', r'X', '123456789', count=1))

# r't.*?a' will always match from first 't' to first 'a'
print(re.sub(r't.*?a', r'X', SENTENCE, count=1))
# matching first 't' to first 'a' for t.*?a won't work for this case
# so, engine will move forward until .*?f matches and so on
print(re.sub(r't.*?a.*?f', r'X', SENTENCE, count=1))

demo = ['abc', 'ac', 'adc', 'abbc', 'xabbbcz', 'bbb', 'bc', 'abbbbbc']
# functionally equivalent greedy and possessive versions
print([w for w in demo if re.search(r'ab*c', w)])
print([w for w in demo if re.search(r'ab*+c', w)])
# different results
print(re.sub(r'f(a|e)*at', r'X', 'feat ft feaeat'))
IP = 'fig:mango:pineapple:guava:apples:orange'
print(re.search(r':.*+', IP)[0])
print(bool(re.search(r':.*+apple', IP)))
# Suppose you want to match integer numbers greater than or equal
# to 100 where these numbers can optionally have leading zeros.

NUMBERS = '42 314 001 12 00984'

# this solution fails because 0* and \d{3,} can both match leading zeros
# and greedy quantifiers will give up characters to help overall regex succeed
print(re.findall(r'0*\d{3,}', NUMBERS))
# here 0*+ will not give back leading zeros after they are consumed
print(re.findall(r'0*+\d{3,}', NUMBERS))
# workaround if possessive quantifiers are not supported
print(re.findall(r'0*[1-9]\d{2,}', NUMBERS))
# (a|e)*+ would match 'a' or 'e' as much as possible
# no backtracking, so another 'a' can never match
print(re.sub(r'f(a|e)*+at', r'X', 'feat ft feaeat'))
lines = ['#comment', 'c = "#"', '\t #comment', 'abc', '', ' \t ']
# The goal is to match lines whose first non-whitespace character is not a # character.
# A matching line should have at least one non-# character,
# so empty lines and those with only whitespace characters should not match.
# this solution fails because \s* can backtrack
# and [^#] can match a whitespace character as well
print([e for e in lines if re.match(r'\s*[^#]', e)])

# this works because \s*+ will not give back any whitespace characters
print([e for e in lines if re.match(r'\s*+[^#]', e)])

# workaround if possessive quantifiers are not supported
print([e for e in lines if re.match(r'\s*[^#\s]', e)])
# same as: r'(b|o)++'
print(re.sub(r'(?>(b|o)+)', r'X', 'abbbc foooooot'))
# same as: r'f(a|e)*+at'
print(re.sub(r'f(?>(a|e)*)at', r'X', 'feat ft feaeat'))

NUMBERS = '42 314 001 12 00984'
# 0* is greedy and the (?>) grouping prevents backtracking
# same as: re.findall(r'0*+\d{3,}', numbers)
print(re.findall(r'(?>0*)\d{3,}', NUMBERS))

IP = 'fig::mango::pineapple::guava::apples::orange'

# this matches from the first '::' to the first occurrence of '::apple'
print(re.search(r'::.*?::apple', IP)[0])

# '(?>::.*?::)' will match only from '::' to the very next '::'
# '::mango::' fails because 'apple' isn't found afterwards
# similarly '::pineapple::' fails
# '::guava::' succeeds because it is followed by 'apple'
print(re.search(r'(?>::.*?::)apple', IP)[0])
