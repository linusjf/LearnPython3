# Anchors Cheatsheet and Summary
| Note | Description |
| ---- | ----------- |
| \A   | restricts the match to start of string |
| \Z   | restricts the match to end of string |
| re.sub(r'pat', r'replace', s) | search and replace |
| \n | line separator, dos-style files need special attention |
| metacharacter characters with special meaning in RE||
| ˆ | restricts the match to start of line |
| \$ | restricts the match to end of line |
| re.MULTILINE or re.M | flag to treat input as multiline string |
| \b | restricts the match to start/end of words word characters: alphabets, digits, underscore |
| \B | matches wherever \b doesn’t match |
