| Note | Description |
| ---- | ----------- |
| \. | match any character except the newline character |
| greedy | match as much as possible |
| \? | greedy quantifier, match 0 or 1 times |
| \* | greedy quantifier, match 0 or more times |
| \+ | greedy quantifier, match 1 or more times |
| {m,n} | greedy quantifier, match m to n times |
| {m,}  | greedy quantifier, match at least m times |
| {,n} | greedy quantifier, match up to n times (including 0 times) |
| {n}  | greedy quantifier, match exactly n times |
| pat1\.\*pat2  | any number of characters between pat1 and pat2 |
| pat1\.\*pat2\|pat2.*pat1  | match both pat1 and pat2 in any order |
| non-greedy | append \? to greedy quantifier |
||match as minimally as possible |
| possessive | append + to greedy quantifier ( regex module) |
|| like greedy, but no backtracking |
| \(\?>pat) | atomic grouping, similar to possessive quantifier |
| re.split(r'pat', s) | split a string based on RE |
||maxsplit and flags are optional argument |
