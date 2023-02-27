| Note | Description |
| ----- | ---------- |
| docs.python: | Unicode tutorial on Unicode support in Python |
| re.ASCII or re.A | match only ASCII characters for \b , \w , \d , \s |
| | and their opposites, only for Unicode patterns |
| re.LOCALE or re.L | use locale settings for byte patterns and 8-bit locales |
| İıſK | characters that can match if re.I is used but not re.A |
| \p{} | Unicode character sets provided by regex module |
| | see regular-expressions: Unicode for details |
| \P{L} or \p{ˆL} | match characters other than \p{L} set |
| hex(ord(c)) | get codepoint for ASCII character c |
| c.encode('unicode_escape') | get codepoint for Unicode character c |
| \uXXXX | codepoint defined using 4-hexdigits |
| \UXXXXXXXX | codepoint defined using 8-hexdigits |
