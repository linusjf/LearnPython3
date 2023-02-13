| Note | Description |
| ---- | ----------- |
| re.Match | object get details like matched portions, location, etc |
| m[0] or m.group(0) | entire matched portion of re.Match object m |
| m[1] or m.group(1) | matched portion of first capture group |
| m[2] or m.group(2) | matched portion of second capture group and so on |
| m.groups() | tuple of all the capture groups’ matched portions |
| m.span() | start and end+1 index of entire matched portion |
| | pass a number to get span of that particular capture group |
| re.sub(r'pat', f, s)  | function f will get re.Match object as argument |
| re.findall(r'pat', s) | returns all the matches as a list |
| | if 1 capture group is used, only its matches are returned |
| | 1+, each element will be tuple of capture groups |
| re.finditer(r'pat', s) | iterator with re.Match object for each match |
