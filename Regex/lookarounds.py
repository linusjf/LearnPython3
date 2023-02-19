#!/usr/bin/env python
"""
######################################################################
# @author      : Linus Fernandes (linusfernandes at gmail dot com)
# @file        : lookarounds
# @created     : Wednesday Feb 15, 2023 11:20:05 IST
# @description :
# -*- coding: utf-8 -*-'
######################################################################
"""
import re

import regex

# change 'foo' only if it is not followed by a digit character
# note that end of string satisfies the given assertion
# 'foofoo' has two matches as the assertion doesn't consume characters
print(re.sub(r'foo(?!\d)', r'baz', 'hey food! foo42 foot5 foofoo'))
# change 'foo' only if it is not preceded by _
# note how 'foo' at start of string is matched as well
print(re.sub(r'(?<!_)foo', r'baz', 'foo _foo 42foofoo'))
# overlap example
# the final _ was replaced as well as played a part in the assertion
print(re.sub(r'(?<!_)foo.', r'baz', 'food _fool 42foo_foot'))

# change whole word only if it is not preceded by : or -
print(re.sub(r'(?<![:-])\b\w+\b', r'X', ':cart <apple -rest ;tea'))
# add space to word boundaries, but not at start or end of string
# similar to: re.sub(r'\b', r' ', 'foo_baz=num1+35*42/num2').strip()
print(re.sub(r'(?<!\A)\b(?!\Z)', r' ', 'foo_baz=num1+35*42/num2'))

# extract digits only if it is followed by ,
# note that end of string doesn't qualify as this is positive assertion
print(re.findall(r'\d+(?=,)', '42 foo-5, baz3; x-83, y-20: f12'))
# extract digits only if it is preceded by - and followed by ; or :
print(re.findall(r'(?<=-)\d+(?=[:;])', '42 foo-5, baz3; x-83, y-20: f12'))
# except first and last fields
print(re.findall(r'(?<=,)[^,]+(?=,)', '1,two,3,four,5'))
# replace empty fields with NA
# note that in this case, order of lookbehind and lookahead doesn't matter
print(re.sub(r'(?<![^,])(?![^,])', r'NA', ',1,,,two,3,,,'))
print(re.sub(r'(\S+\s+)(?=(\S+)\s)', r'\1\2\n', 'a b c d e'))
# and of course, use non-capturing group where needed
print(re.findall(r'(?<=(po|ca)re)\d+', 'pore42 car3 pare7 care5'))
print(re.findall(r'(?<=(?:po|ca)re)\d+', 'pore42 car3 pare7 care5'))

words = ['sequoia', 'subtle', 'questionable', 'exhibit', 'equation']
# words containing 'b' and 'e' and 't' in any order
# same as: r'b.*e.*t|b.*t.*e|e.*b.*t|e.*t.*b|t.*b.*e|t.*e.*b'
print([w for w in words if re.search(r'(?=.*b)(?=.*e).*t', w)])
# words containing all lowercase vowels in any order
print([w for w in words if re.search(r'(?=.*a)(?=.*e)(?=.*i)(?=.*o).*u', w)])

# allowed
print(re.findall(r'(?<=(?:po|ca)re)\d+', 'pore42 car3 pare7 care5'))
print(re.findall(r'(?<=\b[a-z]{4})\d+', 'pore42 car3 pare7 care5'))
# not allowed
try:
    re.findall(r'(?<!car|pare)\d+', 'pore42 car3 pare7 care5')
except re.error as e:
    print(e)
try:
    re.findall(r'(?<=\b[a-z]+)\d+', 'pore42 car3 pare7 care5')
except re.error as e:
    print(e)
try:
    re.sub(r'(?<=\A|,)(?=,|\Z)', r'NA', ',1,,,two,3,,,')
except re.error as e:
    print(e)

# similar to: r'(?<=\b\w)\w*\W*'
# text matched before \K won't be replaced
print(regex.sub(r'\b\w\K\w*\W*', r'', 'sea eat car rat eel tea'))
# replace only 3rd occurrence of 'cat'
print(regex.sub(r'(cat.*?){2}\Kcat', r'X', 'cat scatter cater scat', count=1))
#The regex module allows using variable length lookbehind without needing any change.
print(regex.findall(r'(?<=\b[a-z]+)\d+', 'pore42 car3 pare7 care5'))
print(regex.sub(r'(?<=\A|,)(?=,|\Z)', r'NA', ',1,,,two,3,,,'))
print(
    regex.sub(r'(?<=(cat.*?){2})cat', r'X', 'cat scatter cater scat', count=1))

print(regex.findall(r'(?<!car|pare)\d+', 'pore42 car3 pare7 care5'))
# match 'dog' only if it is not preceded by 'cat'
print(bool(regex.search(r'(?<!cat.*)dog', 'fox,cat,dog,parrot')))
# match 'dog' only if it is not preceded by 'parrot'
print(bool(regex.search(r'(?<!parrot.*)dog', 'fox,cat,dog,parrot')))

# note the use of \A anchor to force matching all characters up to 'dog'
print(bool(re.search(r'\A((?!cat).)*dog', 'fox,cat,dog,parrot')))
print(bool(re.search(r'\A((?!parrot).)*dog', 'fox,cat,dog,parrot')))
# easier to understand by checking matched portion
print(re.search(r'\A((?!cat).)*', 'fox,cat,dog,parrot')[0])
print(re.search(r'\A((?!parrot).)*', 'fox,cat,dog,parrot')[0])
print(re.search(r'\A((?!(.)\2).)*', 'fox,cat,dog,parrot')[0])
# match if 'do' is not there between 'at' and 'par'
print(bool(re.search(r'at((?!do).)*par', 'fox,cat,dog,parrot')))
# match if 'go' is not there between 'at' and 'par'
print(bool(re.search(r'at((?!go).)*par', 'fox,cat,dog,parrot')))
print(re.search(r'at((?!go).)*par', 'fox,cat,dog,parrot')[0])
# use non-capturing group if required
print(re.findall(r'a(?:(?!\d).)*z', 'at,baz,a2z,bad-zoo'))

items = ['1,2,3,4', 'a,b,c,d', '#apple 123']
# filter elements containing digit and '#' characters
print([s for s in items if '#' in s and re.search(r'\d', s)])
# modify elements only if it doesn't start with '#'
for s in items:
    if s[0] != '#':
        print(re.sub(r',.+,', ' ', s))

# change 'cat' only if it is not followed by a digit character
# note that the end of string satisfies the given assertion
# 'catcat' has two matches as the assertion doesn't consume characters
print(re.sub(r'cat(?!\d)', 'dog', 'hey cats! cat42 cat_5 catcat'))

# change 'cat' only if it is not preceded by _
# note how 'cat' at the start of string is matched as well
print(re.sub(r'(?<!_)cat', 'dog', 'cat _cat 42catcat'))

# overlap example
# the final _ was replaced as well as played a part in the assertion
print(re.sub(r'(?<!_)cat.', 'dog', 'cats _cater 42cat_cats'))

# change whole word only if it is not preceded by : or -
print(re.sub(r'(?<![:-])\b\w+\b', 'X', ':cart <apple: -rest ;tea'))
# add space to word boundaries, but not at the start or end of string
# similar to: re.sub(r'\b', ' ', 'output=num1+35*42/num2').strip()
print(re.sub(r'(?<!\A)\b(?!\Z)', ' ', 'output=num1+35*42/num2'))
# replace a character as long as it is not preceded by 'p' or 'r
print(re.sub(r'(?<![pr]).', '*', 'spare'))
print(re.sub(r'.(?<![pr].)', '*', 'spare'))

# replace 'par' as long as 's' is not present later in the input
# this assumes that the lookaround doesn't conflict with search pattern
# i.e. 's' will not conflict 'par' but would affect if it was 'r' and 'par'
print(re.sub(r'par(?!.*s)', '[\\g<0>]', 'par spare part party'))
print(re.sub(r'(?!.*s)par', '[\\g<0>]', 'par spare part party'))

# since the three assertions used here are all zero-width,
# all of the 6 possible combinations will be equivalent
print(re.sub(r'(?!\Z)\b(?<!\A)', ' ', 'output=num1+35*42/num2'))

# extract digits only if it is followed by ,
# note that end of string doesn't qualify as this is a positive assertion
print(re.findall(r'\d+(?=,)', '42 apple-5, fig3; x-83, y-20: f12'))

# extract digits only if it is preceded by - and followed by ; or :
print(re.findall(r'(?<=-)\d+(?=[:;])', '42 apple-5, fig3; x-83, y-20: f12'))

# replace 'par' as long as 'part' occurs as a whole word later in the line
print(re.sub(r'par(?=.*\bpart\b)', '[\\g<0>]', 'par spare part party'))

# replace 'par' as long as 'part' occurs as a starting  later in the line
print(re.sub(r'par(?=.*\bpart)', '[\\g<0>]', 'par spare part party'))

# except first and last fields
print(re.findall(r'(?<=,)[^,]+(?=,)', '1,two,3,four,5'))

# replace empty fields with NA
# note that in this case, order of lookbehind and lookahead doesn't matter
print(re.sub(r'(?<![^,])(?![^,])', 'NA', ',1,,,two,3,,,'))
print(regex.sub(r'(?<=\A|,)(?=,|\Z)', 'NA', ',1,,,two,3,,,'))

print(re.sub(r'(\S+\s+)(?=(\S+)\s)', r'\1\2\n', 'a b c d e'))

# and of course, use non-capturing group where needed
print(re.findall(r'(?<=(po|ca)re)\d+', 'pore42 car3 pare7 care5'))
print(re.findall(r'(?<=(?:po|ca)re)\d+', 'pore42 car3 pare7 care5'))

words = ['sequoia', 'subtle', 'questionable', 'exhibit', 'equation']

# words containing 'b' and 'e' and 't' in any order
# same as: r'b.*e.*t|b.*t.*e|e.*b.*t|e.*t.*b|t.*b.*e|t.*e.*b'
print([w for w in words if re.search(r'(?=.*b)(?=.*e).*t', w)])

# words containing all lowercase vowels in any order
print([w for w in words if re.search(r'(?=.*a)(?=.*e)(?=.*i)(?=.*o).*u', w)])

# words containing ('ab' or 'at') and 'q' but not 'n' at the end of the element
print([w for w in words if re.search(r'(?!.*n\Z)(?=.*a[bt]).*q', w)])

S = 'pore42 tar3 dare7 care5'

# allowed
print(re.findall(r'(?<=(?:po|da)re)\d+', S))
print(re.findall(r'(?<=\b[a-z]{4})\d+', S))

# not allowed
try:
    re.findall(r'(?<!tar|dare)\d+', S)
except re.error as e:
    #look-behind requires fixed-width pattern
    print(e)

try:
    re.findall(r'(?<=\b[pd][a-z]*)\d+', S)
except re.error as e:
    print(e)
#look-behind requires fixed-width pattern
try:
    re.sub(r'(?<=\A|,)(?=,|\Z)', 'NA', ',1,,,two,3,,,')
except re.error as e:
    print(e)
    #look-behind requires fixed-width pattern

S = 'pore42 tar3 dare7 care5'

# workaround for r'(?<!tar|dare)\d+'
print(re.findall(r'(?<!tar)(?<!dare)\d+', S))

# workaround for r'(?<=tar|dare)\d+'
print(re.findall(r'(?:(?<=tar)|(?<=dare))\d+', S))

# workaround for r'(?<=\A|,)(?=,|\Z)'
print(re.sub(r'((?<=\A)|(?<=,))(?=,|\Z)', 'NA', ',1,,,two,3,,,'))

S = 'pore42 tar3 dare7 care5'

# same as: re.findall(r'(?:(?<=tar)|(?<=dare))\d+', s)
print(re.findall(r'(?:tar|dare)(\d+)', S))

# delete digits only if they are preceded by 'tar' or 'dare'
print(re.sub(r'(tar|dare)\d+', r'\1', S))

# workaround for r'(?<=\b[pd][a-z]*)\d+'
# get digits only if they are preceded by a word starting with 'p' or 'd'
print(re.findall(r'\b[pd][a-z]*(\d+)', S))

# delete digits only if they are preceded by a word starting with 'p' or 'd'
print(re.sub(r'(\b[pd][a-z]*)\d+', r'\1', S))

# note the use of \A anchor to force matching all the characters up to 'dog'
print(bool(re.search(r'\A((?!cat).)*dog', 'fox,cat,dog,parrot')))
print(re.search(r'\A((?!cat).)*dog', 'fox,cat,dog,parrot'))
print(re.search(r'\A((?!cat).)*', 'fox,cat,dog,parrot')[0])
# easier to understand by checking the matched portion
print(bool(re.search(r'\A((?!parrot).)*dog', 'fox,cat,dog,parrot')))
print(re.search(r'\A((?!parrot).)*', 'fox,cat,dog,parrot')[0])
# without the anchor, you'll get false matches
print(bool(re.search(r'((?!cat).)*dog', 'fox,cat,dog,parrot')))
print(re.search(r'\A(?:(?!(.)\1).)*', 'fox,cat,dog,parrot')[0])

# match if 'do' is not there between 'at' and 'par'
print(bool(re.search(r'at((?!do).)*par', 'fox,cat,dog,parrot')))
# match if 'go' is not there between 'at' and 'par'
print(bool(re.search(r'at((?!go).)*par', 'fox,cat,dog,parrot')))
print(re.search(r'at((?!go).)*par', 'fox,cat,dog,parrot')[0])

# use non-capturing group if required
WORDS = 'apple banana 12_bananas cherry fig mango cake42'
print(re.findall(r'\b[a-z](?:(?!pp|rr)[a-z])*\b', WORDS))

#Our password must meet four conditions:

#1. The password must have between six and ten word characters \w
#2. It must include at least one lowercase character [a-z]
#3. It must include at least three uppercase characters [A-Z]
#4. It must include at least one digit \d
regexpwd = re.compile(
    r'\A(?=[^a-z]*[a-z])(?=(?:[^A-Z]*[A-Z]){3})(?=\D*\d)\w{6,10}\Z')
print(regexpwd.findall("fivec"))
print(regexpwd.findall("ALLCAPS"))
print(regexpwd.findall("NOtallcaps"))
print(regexpwd.findall("NODigits"))
print(regexpwd.findall("NODigits1"))

noQregex = regex.compile(r'[^\WQ]')
print(noQregex.findall("noqueue"))
print(noQregex.findall("Queue"))
noQregex = regex.compile(r'[_0-9a-zA-PR-Z]')
print(noQregex.findall("noqueue"))
print(noQregex.findall("Queue"))
noQregex = regex.compile(r'(?!Q)\w')
print(noQregex.findall("noqueue"))
print(noQregex.findall("Queue"))
noQregex = regex.compile(r'\w(?<!Q)')
print(noQregex.findall("noqueue"))
print(noQregex.findall("Queue"))
#Suppose you want to match one word character \w as long as it is not the letter Q.
#a) Remove leading and trailing whitespaces from all the individual fields of these csv strings.
CSV1 = ' comma ,separated ,values '
CSV2 = 'good bad,nice ice , 42 , , stall small'
remove_whitespace = regex.compile(r'(?<=^|, )|(?<=, ) | (?=$|,)|(?<=, )(?=,)')
print(remove_whitespace.sub('', CSV1))
print(remove_whitespace.sub('', CSV2))
