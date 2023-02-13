# Alternations and Precedence Cheatsheet and Summary
| Note | Description |
| ---- | ----------- |
| \| | multiple RE combined as conditional OR|
|  ||each alternative can have independent anchors |
| '\|'.join(iterable) | programmatically combine multiple RE |
| () | group pattern(s) |
| a(b\|c)d | same as abd|acd |
| Alternation precedence | pattern which matches earliest in the input gets precedence |
| || tie-breaker is left to right if patterns have same starting location |
| || robust solution: sort the alternations based on length, longest first |
| || "'|'.join(sorted(iterable, key=len, reverse=True)) |
