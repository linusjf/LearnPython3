| Note | Description |
| ----- | --------- |
| \\N  | backreference, gives matched portion of Nth capture group |
| | applies to both search and replacement sections |
| | possible values: \1 , \2 up to \99 provided no more digits |
| \g<N> | backreference, gives matched portion of Nth capture group |
| | possible values: \g<0> , \g<1> , etc (not limited to 99) |
| | \\g<0> refers to entire matched portion |
| (?:pat) | non-capturing group |
| (?P\<name\>pat) | named capture group |
| | refer as 'name' in re.Match object |
| | refer as (?P=name) in search section |
| | refer as \\g<name> in replacement section |
| (?N) | subexpression call for Nth capture group |
| (?&name) | subexpression call for named capture group |
|  | subexpression call is regex module only, recursion also possible |
