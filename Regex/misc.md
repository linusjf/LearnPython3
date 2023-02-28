| Note | Description |
| ---- | ------------- |
| using dict | replacement string based on the matched text as dictionary key |
| | ex: re.sub(r'pat', lambda m: d.get(m[0], default), s) |
| re.subn() | gives tuple of modified string and number of substitutions |
| \G | regex module, restricts matching from start of string like \A |
| | continues matching from end of match as new anchor until it fails |
| | ex: regex.findall(r'\G\d+-?', '12-34 42') gives ['12-', '34'] |
| subexpression call | regex module, helps to define recursive matching |
| | ex: r'\((?:[ˆ()]++|(?0))++\)' matches nested sets of parentheses |
| [[:digit:]] | regex module, named character set for \d |
| [[:ˆdigit:]] | to indicate \D |
| | See regular-expressions: POSIX Bracket for full list |
| (?V1)  | inline flag to enable version 1 for regex module |
| | regex.DEFAULT_VERSION=regex.VERSION1 can also be used |
| | (?V0) or regex.VERSION0 to get back default version |
| set operations | V1 enables this feature for character classes, nested [] allowed |
| \|\| | union |
| \~\~ | symmetric difference |
| && | intersection |
| \-\- | difference |
| | ex: (?V1)[[:punct:]--[.!?]] punctuation except . ! and ? |
| pat(*SKIP)(*F) | regex module, ignore text matched by pat |
| | ex: "[ˆ"]++"(*SKIP)(*F)|, will match , but not inside |
| | double quoted pairs |
