| Note | Description |
| —--- | —---------- |
| [ae;o] | match any of these characters once |
| quantifiers are applicable to character classes too |
| [3-7] | range of characters from 3 to 7 |
| [ˆ=b2] | match other than = or b or 2 |
| [a-z-] | - should be first/last or escaped using \ to match literally |
| [+ˆ] | ˆ shouldn’t be first character or escaped using \ |
| [a\[\]] | [ can be escaped with \ or placed as last character |
| [a\[\]] | ] can be escaped with \ or placed as first character |
| [a\\b] | \ should be escaped using \ |
| \w | similar to [a-zA-Z0-9_] for matching word characters |
| \d | similar to [0-9] for matching digit characters |
| \s | similar to [ \t\n\r\f\v] for matching whitespace characters |
| | \W , \D , and \S for their opposites respectively |
