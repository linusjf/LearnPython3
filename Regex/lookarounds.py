#!/usr/bin/env python
"""
Lookarounds.

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
print(re.sub(r"foo(?!\d)", r"baz", "hey food! foo42 foot5 foofoo"))
# change 'foo' only if it is not preceded by _
# note how 'foo' at start of string is matched as well
print(re.sub(r"(?<!_)foo", r"baz", "foo _foo 42foofoo"))
# overlap example
# the final _ was replaced as well as played a part in the assertion
print(re.sub(r"(?<!_)foo.", r"baz", "food _fool 42foo_foot"))

# change whole word only if it is not preceded by : or -
print(re.sub(r"(?<![:-])\b\w+\b", r"X", ":cart <apple -rest ;tea"))
# add space to word boundaries, but not at start or end of string
# similar to: re.sub(r'\b', r' ', 'foo_baz=num1+35*42/num2').strip()
print(re.sub(r"(?<!\A)\b(?!\Z)", r" ", "foo_baz=num1+35*42/num2"))

# extract digits only if it is followed by ,
# note that end of string doesn't qualify as this is positive assertion
print(re.findall(r"\d+(?=,)", "42 foo-5, baz3; x-83, y-20: f12"))
# extract digits only if it is preceded by - and followed by ; or :
print(re.findall(r"(?<=-)\d+(?=[:;])", "42 foo-5, baz3; x-83, y-20: f12"))
# except first and last fields
print(re.findall(r"(?<=,)[^,]+(?=,)", "1,two,3,four,5"))
# replace empty fields with NA
# note that in this case, order of lookbehind and lookahead doesn't matter
print(re.sub(r"(?<![^,])(?![^,])", r"NA", ",1,,,two,3,,,"))
print(re.sub(r"(\S+\s+)(?=(\S+)\s)", r"\1\2\n", "a b c d e"))
# and of course, use non-capturing group where needed
print(re.findall(r"(?<=(po|ca)re)\d+", "pore42 car3 pare7 care5"))
print(re.findall(r"(?<=(?:po|ca)re)\d+", "pore42 car3 pare7 care5"))

words = ["sequoia", "subtle", "questionable", "exhibit", "equation"]
# words containing 'b' and 'e' and 't' in any order
# same as: r'b.*e.*t|b.*t.*e|e.*b.*t|e.*t.*b|t.*b.*e|t.*e.*b'
print([w for w in words if re.search(r"(?=.*b)(?=.*e).*t", w)])
# words containing all lowercase vowels in any order
print([w for w in words if re.search(r"(?=.*a)(?=.*e)(?=.*i)(?=.*o).*u", w)])

# allowed
print(re.findall(r"(?<=(?:po|ca)re)\d+", "pore42 car3 pare7 care5"))
print(re.findall(r"(?<=\b[a-z]{4})\d+", "pore42 car3 pare7 care5"))
# not allowed
try:
    re.findall(r"(?<!car|pare)\d+", "pore42 car3 pare7 care5")
except re.error as e:
    print(e)
try:
    re.findall(r"(?<=\b[a-z]+)\d+", "pore42 car3 pare7 care5")
except re.error as e:
    print(e)
try:
    re.sub(r"(?<=\A|,)(?=,|\Z)", r"NA", ",1,,,two,3,,,")
except re.error as e:
    print(e)

# similar to: r'(?<=\b\w)\w*\W*'
# text matched before \K won't be replaced
print(regex.sub(r"\b\w\K\w*\W*", r"", "sea eat car rat eel tea"))
# replace only 3rd occurrence of 'cat'
print(regex.sub(r"(cat.*?){2}\Kcat", r"X", "cat scatter cater scat", count=1))
# The regex module allows using variable length lookbehind without needing
# any change.
print(regex.findall(r"(?<=\b[a-z]+)\d+", "pore42 car3 pare7 care5"))
print(regex.sub(r"(?<=\A|,)(?=,|\Z)", r"NA", ",1,,,two,3,,,"))
print(regex.sub(r"(?<=(cat.*?){2})cat", r"X", "cat scatter cater scat", count=1))
print(regex.findall(r"(?<!car|pare)\d+", "pore42 car3 pare7 care5"))
# match 'dog' only if it is not preceded by 'cat'
print(bool(regex.search(r"(?<!cat.*)dog", "fox,cat,dog,parrot")))
# match 'dog' only if it is not preceded by 'parrot'
print(bool(regex.search(r"(?<!parrot.*)dog", "fox,cat,dog,parrot")))

# note the use of \A anchor to force matching all characters up to 'dog'
print(bool(re.search(r"\A((?!cat).)*dog", "fox,cat,dog,parrot")))
print(bool(re.search(r"\A((?!parrot).)*dog", "fox,cat,dog,parrot")))
# easier to understand by checking matched portion
m = re.search(r"\A((?!cat).)*", "fox,cat,dog,parrot")
if m:
    print(m[0])
m = re.search(r"\A((?!parrot).)*", "fox,cat,dog,parrot")
if m:
    print(m[0])
m = re.search(r"\A((?!(.)\2).)*", "fox,cat,dog,parrot")
if m:
    print(m[0])
# match if 'do' is not there between 'at' and 'par'
print(bool(re.search(r"at((?!do).)*par", "fox,cat,dog,parrot")))
# match if 'go' is not there between 'at' and 'par'
print(bool(re.search(r"at((?!go).)*par", "fox,cat,dog,parrot")))
m = re.search(r"at((?!go).)*par", "fox,cat,dog,parrot")
if m:
    print(m[0])
# use non-capturing group if required
print(re.findall(r"a(?:(?!\d).)*z", "at,baz,a2z,bad-zoo"))

items = ["1,2,3,4", "a,b,c,d", "#apple 123"]
# filter elements containing digit and '#' characters
print([s for s in items if "#" in s and re.search(r"\d", s)])
# modify elements only if it doesn't start with '#'
for s in items:
    if s[0] != "#":
        print(re.sub(r",.+,", " ", s))

# change 'cat' only if it is not followed by a digit character
# note that the end of string satisfies the given assertion
# 'catcat' has two matches as the assertion doesn't consume characters
print(re.sub(r"cat(?!\d)", "dog", "hey cats! cat42 cat_5 catcat"))

# change 'cat' only if it is not preceded by _
# note how 'cat' at the start of string is matched as well
print(re.sub(r"(?<!_)cat", "dog", "cat _cat 42catcat"))

# overlap example
# the final _ was replaced as well as played a part in the assertion
print(re.sub(r"(?<!_)cat.", "dog", "cats _cater 42cat_cats"))

# change whole word only if it is not preceded by : or -
print(re.sub(r"(?<![:-])\b\w+\b", "X", ":cart <apple: -rest ;tea"))
# add space to word boundaries, but not at the start or end of string
# similar to: re.sub(r'\b', ' ', 'output=num1+35*42/num2').strip()
print(re.sub(r"(?<!\A)\b(?!\Z)", " ", "output=num1+35*42/num2"))
# replace a character as long as it is not preceded by 'p' or 'r
print(re.sub(r"(?<![pr]).", "*", "spare"))
print(re.sub(r".(?<![pr].)", "*", "spare"))

# replace 'par' as long as 's' is not present later in the input
# this assumes that the lookaround doesn't conflict with search pattern
# i.e. 's' will not conflict 'par' but would affect if it was 'r' and 'par'
print(re.sub(r"par(?!.*s)", "[\\g<0>]", "par spare part party"))
print(re.sub(r"(?!.*s)par", "[\\g<0>]", "par spare part party"))

# since the three assertions used here are all zero-width,
# all of the 6 possible combinations will be equivalent
print(re.sub(r"(?!\Z)\b(?<!\A)", " ", "output=num1+35*42/num2"))

# extract digits only if it is followed by ,
# note that end of string doesn't qualify as this is a positive assertion
print(re.findall(r"\d+(?=,)", "42 apple-5, fig3; x-83, y-20: f12"))

# extract digits only if it is preceded by - and followed by ; or :
print(re.findall(r"(?<=-)\d+(?=[:;])", "42 apple-5, fig3; x-83, y-20: f12"))

# replace 'par' as long as 'part' occurs as a whole word later in the line
print(re.sub(r"par(?=.*\bpart\b)", "[\\g<0>]", "par spare part party"))

# replace 'par' as long as 'part' occurs as a starting  later in the line
print(re.sub(r"par(?=.*\bpart)", "[\\g<0>]", "par spare part party"))

# except first and last fields
print(re.findall(r"(?<=,)[^,]+(?=,)", "1,two,3,four,5"))

# replace empty fields with NA
# note that in this case, order of lookbehind and lookahead doesn't matter
print(re.sub(r"(?<![^,])(?![^,])", "NA", ",1,,,two,3,,,"))
print(regex.sub(r"(?<=\A|,)(?=,|\Z)", "NA", ",1,,,two,3,,,"))

print(re.sub(r"(\S+\s+)(?=(\S+)\s)", r"\1\2\n", "a b c d e"))

# and of course, use non-capturing group where needed
print(re.findall(r"(?<=(po|ca)re)\d+", "pore42 car3 pare7 care5"))
print(re.findall(r"(?<=(?:po|ca)re)\d+", "pore42 car3 pare7 care5"))

words = ["sequoia", "subtle", "questionable", "exhibit", "equation"]

# words containing 'b' and 'e' and 't' in any order
# same as: r'b.*e.*t|b.*t.*e|e.*b.*t|e.*t.*b|t.*b.*e|t.*e.*b'
print([w for w in words if re.search(r"(?=.*b)(?=.*e).*t", w)])

# words containing all lowercase vowels in any order
print([w for w in words if re.search(r"(?=.*a)(?=.*e)(?=.*i)(?=.*o).*u", w)])

# words containing ('ab' or 'at') and 'q' but not 'n' at the end of the element
print([w for w in words if re.search(r"(?!.*n\Z)(?=.*a[bt]).*q", w)])

S = "pore42 tar3 dare7 care5"

# allowed
print(re.findall(r"(?<=(?:po|da)re)\d+", S))
print(re.findall(r"(?<=\b[a-z]{4})\d+", S))

# not allowed
try:
    re.findall(r"(?<!tar|dare)\d+", S)
except re.error as e:
    # look-behind requires fixed-width pattern
    print(e)

try:
    re.findall(r"(?<=\b[pd][a-z]*)\d+", S)
except re.error as e:
    print(e)
# look-behind requires fixed-width pattern
try:
    re.sub(r"(?<=\A|,)(?=,|\Z)", "NA", ",1,,,two,3,,,")
except re.error as e:
    print(e)
    # look-behind requires fixed-width pattern

S = "pore42 tar3 dare7 care5"

# workaround for r'(?<!tar|dare)\d+'
print(re.findall(r"(?<!tar)(?<!dare)\d+", S))

# workaround for r'(?<=tar|dare)\d+'
print(re.findall(r"(?:(?<=tar)|(?<=dare))\d+", S))

# workaround for r'(?<=\A|,)(?=,|\Z)'
print(re.sub(r"((?<=\A)|(?<=,))(?=,|\Z)", "NA", ",1,,,two,3,,,"))

S = "pore42 tar3 dare7 care5"

# same as: re.findall(r'(?:(?<=tar)|(?<=dare))\d+', s)
print(re.findall(r"(?:tar|dare)(\d+)", S))

# delete digits only if they are preceded by 'tar' or 'dare'
print(re.sub(r"(tar|dare)\d+", r"\1", S))

# workaround for r'(?<=\b[pd][a-z]*)\d+'
# get digits only if they are preceded by a word starting with 'p' or 'd'
print(re.findall(r"\b[pd][a-z]*(\d+)", S))

# delete digits only if they are preceded by a word starting with 'p' or 'd'
print(re.sub(r"(\b[pd][a-z]*)\d+", r"\1", S))

# note the use of \A anchor to force matching all the characters up to 'dog'
print(bool(re.search(r"\A((?!cat).)*dog", "fox,cat,dog,parrot")))
print(re.search(r"\A((?!cat).)*dog", "fox,cat,dog,parrot"))
m = re.search(r"\A((?!cat).)*", "fox,cat,dog,parrot")
if m:
    print(m[0])
# easier to understand by checking the matched portion
print(bool(re.search(r"\A((?!parrot).)*dog", "fox,cat,dog,parrot")))
m = re.search(r"\A((?!parrot).)*", "fox,cat,dog,parrot")
if m:
    print(m[0])
# without the anchor, you'll get false matches
print(bool(re.search(r"((?!cat).)*dog", "fox,cat,dog,parrot")))
m = re.search(r"\A(?:(?!(.)\1).)*", "fox,cat,dog,parrot")
if m:
    print(m[0])

# match if 'do' is not there between 'at' and 'par'
print(bool(re.search(r"at((?!do).)*par", "fox,cat,dog,parrot")))
# match if 'go' is not there between 'at' and 'par'
print(bool(re.search(r"at((?!go).)*par", "fox,cat,dog,parrot")))
m = re.search(r"at((?!go).)*par", "fox,cat,dog,parrot")
if m:
    print(m[0])

# use non-capturing group if required
WORDS = "apple banana 12_bananas cherry fig mango cake42"
print(re.findall(r"\b[a-z](?:(?!pp|rr)[a-z])*\b", WORDS))

# Our password must meet four conditions:

# 1. The password must have between six and ten word characters \w
# 2. It must include at least one lowercase character [a-z]
# 3. It must include at least three uppercase characters [A-Z]
# 4. It must include at least one digit \d
regexpwd = re.compile(r"\A(?=[^a-z]*[a-z])(?=(?:[^A-Z]*[A-Z]){3})(?=\D*\d)\w{6,10}\Z")  # noqa
print(regexpwd.findall("fivec"))
print(regexpwd.findall("ALLCAPS"))
print(regexpwd.findall("NOtallcaps"))
print(regexpwd.findall("NODigits"))
print(regexpwd.findall("NODigits1"))

noqregex = regex.compile(r"[^\WQ]")
print(noqregex.findall("noqueue"))
print(noqregex.findall("Queue"))
noqregex = regex.compile(r"[_0-9a-zA-PR-Z]")
print(noqregex.findall("noqueue"))
print(noqregex.findall("Queue"))
noqregex = regex.compile(r"(?!Q)\w")
print(noqregex.findall("noqueue"))
print(noqregex.findall("Queue"))
noqregex = regex.compile(r"\w(?<!Q)")
print(noqregex.findall("noqueue"))
print(noqregex.findall("Queue"))

# suppose we want to match any character as long as it is not followed by
# {END}.
noendregex = regex.compile(r"(?:(?!{END}).)*")
print(noendregex.findall("THE{END}"))
print(noendregex.findall("NoEnd"))
noendregex = regex.compile(r"(?:(?!{END}).)+")
print(noendregex.findall("THE{END}"))
print(noendregex.findall("NoEnd"))
noendregex = regex.compile(r"(?:[^{]++|{(?!END}))*+")
print(noendregex.findall("THE{END}"))
print(noendregex.findall("NoEnd"))
noendregex = regex.compile(r"(?:[^{]++|{(?!END}))+")
print(noendregex.findall("THE{END}"))
print(noendregex.findall("NoEnd"))

startregex = regex.compile(r"(?<=#START#).*")
print(startregex.findall("#START#stringstartshere#START#"))
startregex = regex.compile(r"(?<=#START#).+")
print(startregex.findall("#START#stringstartshere#START#"))
endregex = regex.compile(r".*(?=#END#)")
print(endregex.findall("#END#stringendsshere#END#"))
endregex = regex.compile(r".+(?=#END#)")
print(endregex.findall("#END#stringendsshere#END#"))
startendregex = regex.compile(r"(?<=#START#).+?(?=#END#)")
print(startendregex.findall("#START#stringendsshere#END#"))
startendregex = regex.compile(r"(?<=#START#).*?(?=#END#)")
print(startendregex.findall("#START#stringendsshere#END#"))

insertregex = regex.compile(r"(?<=[a-z])(?=[A-Z])")
print(insertregex.sub(" ", "HaroldAndKumarGoToWhiteCastle"))
print(insertregex.split("AppleOrangeBananaStrawberryPeach"))

overlapregex = regex.compile(r"(?=(\w+))")
print(overlapregex.findall("ABCDE"))
overlapregex = regex.compile(r"(?<=(\w+))")
print(overlapregex.findall("ABCDE"))

multiregex = regex.compile(r"(?m)^")
LINES = """This is
a multline
string. We will regex
the start of each
line.
"""
print(multiregex.sub("// ", LINES))

efficientregex = regex.compile(r"\d+(?= dollars)")
inefficientregex = regex.compile(r"(?=\d+ dollars)\d+")
TEXT = "100 dollars"
print(efficientregex.findall(TEXT))
print(inefficientregex.findall(TEXT))
efficientregex = regex.compile(r"\d+(?! dollars)")
inefficientregex = regex.compile(r"(?!\d+ dollars)\d+")
TEXT = "100 pesos"
print(efficientregex.findall(TEXT))
print(inefficientregex.findall(TEXT))
efficientregex = regex.compile(r"(?<=USD)\d{3}")
inefficientregex = regex.compile(r"\d{3}(?<=USD\d{3})")
TEXT = "USD100"
print(efficientregex.findall(TEXT))
print(inefficientregex.findall(TEXT))
efficientregex = regex.compile(r"(?<!USD)\d{3}")
inefficientregex = regex.compile(r"\d{3}(?<!USD\d{3})")
TEXT = "JPY100"
print(efficientregex.findall(TEXT))
print(inefficientregex.findall(TEXT))

# Suppose you want to match a two-digit
# number surrounded by underscores as in _12_ but not the underscores.
regexone = regex.compile(r"_(\d{2})_")
regextwo = regex.compile(r"(?<=_)\d{2}(?=_)")
regexthree = regex.compile(r"_\K\d{2}(?=_)")
NUMBERS = "23 _45_ _67_ 78 89 67 _56_"
print(regexone.findall(NUMBERS))
print(regextwo.findall(NUMBERS))
print(regexthree.findall(NUMBERS))
regexbtf = regex.compile(r"(?<=_(?=\d{2}_))\d+")
print(regexbtf.findall(NUMBERS))
regexbtf = regex.compile(r"\d+(?<=_\d{2}(?=_))")
print(regexbtf.findall(NUMBERS))

# matches a number that is precede by an underscore that is not
# preceded by an underscore unless that underscore is preceded by an X.
NUMBERS = "23 _45_ __67_ X__78 89 67 _56_"
regexbtf = regex.compile(r"(?<=(?<!(?<!X)_)_)\d+")
print(regexbtf.findall(NUMBERS))
regexbtf = regex.compile(r"(?:(?<=(?<!_)_)|(?<=X__))\d+")
print(regexbtf.findall(NUMBERS))

ANIMALS = "_rabbit _dog _mouse DIC:cat:dog:mouse"
animalregex = regex.compile(r"_(\w+)\b(?=.*:\1\b)")
print(animalregex.findall(ANIMALS))
animalregex = regex.compile(r"_(?=.*:(\w+)\b)\1\b")
print(animalregex.findall(ANIMALS))
animalregex = regex.compile(r"_(?=.*:(\w+)\b)\1\b")
print(animalregex.findall(ANIMALS))

expr = regex.compile(r"(?<=\b\d+_)[A-Z]+")
print(expr.findall("123456_ORANGE"))
print(expr.findall("abc12_APPLE"))

variablelb = regex.compile(r"(?<=(\d{1,5}))Z")
print(variablelb.findall("123Z"))
cgregex = regex.compile(r"\b\d+_([A-Z]+)")
print(cgregex.findall("123456_ORANGE"))
print(cgregex.findall("abc12_APPLE"))
keepoutregex = regex.compile(r"\b\d+_\K[A-Z]+")
print(keepoutregex.findall("123456_ORANGE"))
print(keepoutregex.findall("abc12_APPLE"))

numsregex = regex.compile(r"(?<=\d)\d")
print(numsregex.findall("123"))
numsregex = regex.compile(r"\d\K\d")
print(numsregex.findall("123"))
numsregex = regex.compile(r"\d(\d)")
print(numsregex.findall("123"))

# Replace all whole words with X unless it is preceded by a ( character.

IP = "(apple) guava berry) apple (mango) (grape"
regexx = regex.compile(r"(?<!\()\b\w+\b")
print(regexx.sub("X", IP))
regexx = regex.compile(r"\b\w+\b(?![)])")
print(regexx.sub("X", IP))
regexx = regex.compile(r"(?<![(])\b\w+\b(?![)])")
print(regexx.sub("X", IP))

IP = "a_t row on Urn e note Dust n end a2-e|u"
print(IP)
regexx = regex.compile(r"(?!\b\w*[en]\b)\b\w+\b")
print(regexx.findall(IP))

regexx = regex.compile(r"(?!\b[adn]\w*\b)\b\w+\b")
print(regexx.findall(IP))

IP = "Poke,on=-=so_good:ink.to/is(vast)ever2-sit"
print(IP)
regexx = regex.compile(r"(?=\b\w+\b[:,-])\b\w+\b")
print(regexx.findall(IP))

regexx = regex.compile(r"(?<=[=/-])\b\w+\b")
print(regexx.findall(IP))

regexx = regex.compile(r"(?<=[=:])(?=\b\w+\b[:\.])\b\w+\b")
print(regexx.findall(IP))
regexx = regex.compile(r"(?<=[\(:=\.-])(?=\b\w+\b(?:[^\./]|$))\b\w+\b")
print(regexx.findall(IP))
# Suppose you want to match one word character \w as
# long as it is not the letter Q.
# a) Remove leading and trailing whitespaces from all the individual
# fields of these csv strings.
CSV1 = " comma ,separated ,values "
print(CSV1)
CSV2 = "good bad,nice ice , 42 , , stall small"
print(CSV2)
remove_whitespace = regex.compile(r"(?<=(\A|(\b\w+\b)|,))(?<!\b\w+\b(?!\s+,))\s+")
print(remove_whitespace.sub("", CSV1))
print(remove_whitespace.sub("", CSV2))

# Filter all elements that satisfy all of these rules:

# should have at least two alphabets
# should have at least three digits
# should have at least one special character among % or * or # or $
# should not end with a whitespace character
pwds = ["hunter2", "F2H3u%9", "*X3Yz3.14\t", "r2_d2_42", "A $B C1234"]
print(pwds)
COMP = r"\A(?=([^A-Za-z]*[A-Za-z]){2,})"
COMP += r"(?=(\D*\d){3,})"
COMP += r"(?=([^\*%\#\$]*[\*%\#\$]){1,})"
COMP += r".+[^\s]\Z"
regexx = regex.compile(COMP)

print([w for w in pwds if regex.search(regexx, w)])
# ['F2H3u%9', 'A $B C1234']

# For the given string, surround all whole words with {} except for whole words par
# and cat and apple.

IP = "part; cat {super} rest_42 par scatter apple spar"
print(IP)
regexx = regex.compile(r"(?!(\bpar\b)|(\bcat\b)|(\bapple\b))(\b\w+\b)")
print(regexx.sub(r"{\4}", IP))
# '{part}; cat {{super}} {rest_42} par {scatter} apple {spar}'

# Extract integer portion of floating-point numbers for the given string.
# Integers and numbers ending with . and no further digits should
# not be considered.
IP = "12 ab32.4 go 5 2. 46.42 5"
print(IP)
regexx = regex.compile(r"(?=[A-Za-z]*\d+\.\d*)[A-Za-z]*(\d+)\.[^\s]")
print(regexx.findall(IP))
# ['32', '46']

# For the given input strings, extract all overlapping two character sequences.
S1 = "apple"
S2 = "1.2-3:4"
PAT = regex.compile(r"(?=(\S\S)\S*)")
print(PAT.findall(S1))
print(PAT.findall(S2))
# ['ap', 'pp', 'pl', 'le']
# ['1.', '.2', '2-', '-3', '3:', ':4']

# Extract all whole words unless they are preceded by
# : or <=> or ---- or #.

IP = "::very--at<=>row|in.a_b#b2c=>lion----east"
PAT = regex.compile(r"(?<!(?::|<=>|-{4}|#))\b\w+\b")
print(PAT.findall(IP))
# ['at', 'in', 'a_b', 'lion']

# Match strings if it contains qty
# followed by price but not if there is any whitespace character or the string
# error between them

STR1 = "23,qty,price,42"
STR2 = "qty price,oh"
STR3 = "3.14,qty,6,errors,9,price,3"
STR4 = "42\nqty-6,apple-56,price-234,error"
STR5 = "4,price,3.14,qty,4"
STR6 = "(qtyprice) (hi-there)"

neg = re.compile(r"(?!qty.*(\s|error)+.*price)qty.*price")
print(bool(neg.search(STR1)))
# True
print(bool(neg.search(STR2)))
# False
print(bool(neg.search(STR3)))
# False
print(bool(neg.search(STR4)))
# True
print(bool(neg.search(STR5)))
# False
print(bool(neg.search(STR6)))
# True

# Can you reason out why the following regular expressions behave differently?
IP = "I have 12, he has 2!"
print(regex.sub(r"\b..\b", "{\\g<0>}", IP))
# '{I }have {12}{, }{he} has{ 2}!'
print(regex.sub(r"(?<!\w)..(?!\w)", "{\\g<0>}", IP))
# 'I have {12}, {he} has {2!}'

# The given input string has comma separated fields and some of
# them can occur more than once. For the duplicated fields,
# retain only the rightmost one. Assume that there are no empty fields.
ROW = "421,cat,2425,42,5,cat,6,6,42,61,6,6,scat,6,6,4,Cat,425,4"
print(ROW)
regexx = regex.compile(r"(\b\w+\b)(?:,\1)*(?!(?:.*?\1.*?){2,})")
print(regexx.findall(ROW))
print(",".join(regexx.findall(ROW)))
ROW = "6,7,6,6"
print(ROW)
print(regexx.findall(ROW))
print(",".join(regexx.findall(ROW)))
regexx = regex.compile(r"(?<=\A|\b)([\b\w]+),(?=.*(?<=\b)\1(?=\Z|,))")
print(regexx.sub("", ROW))
ROW = "421,cat,2425,42,5,cat,6,6,42,61,6,6,scat,6,6,4,Cat,425,4"
print(regexx.sub("", ROW))
# '421,2425,5,cat,42,61,scat,6,Cat,425,4'

# The given input strings contain fields separated by the :
# character. Delete : and the last field if there is a digit
# character anywhere before the last field.

S1 = "42:cat"
S2 = "twelve:a2b"
S3 = "we:be:he:0:a:b:bother"
S4 = "apple:banana-42:cherry:"
S5 = "dragon:unicorn:centaur"

pat = regex.compile(r"(?<=\d.*)(:[^:]*)\Z")
print(S1)
print(pat.findall(S1))
print(pat.sub(r"", S1))
print(S2)
print(pat.findall(S2))
print(pat.sub(r"", S2))
print(S3)
print(pat.findall(S3))
print(pat.sub(r"", S3))
print(S4)
print(pat.findall(S4))
print(pat.sub(r"", S4))
print(S5)
