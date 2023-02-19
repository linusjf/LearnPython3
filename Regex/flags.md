| Note | Description |
| --   | --          |
| re.IGNORECASE or re.I | flag to ignore case |
| re.DOTALL or re.S  | allow \. metacharacter to match newline character |
| flags=re.S\|re.I | multiple flags can be combined using \| operator |
| re.MULTILINE or re.M | allow ˆ and \$ anchors to match line wise |
| re.VERBOSE or re.X  | allows to use literal whitespaces for aligning purposes |
| | and to add comments after the \# character |
|| escape spaces and \# if needed as part of actual RE |
| (?#comment) | another way to add comments, not a flag |
| (?flags:pat) | inline flags only for this pat , overrides flags argument |
| | where flags is i for re.I , s for re.S , etc  |
||except L for re.L |
| (?-flags:pat) | negate flags only for this pat
| (?flags-flags:pat) | apply and negate particular flags only for this pat
| (?flags) | apply flags for whole RE, can be used only at start of RE
| |anchors if any, should be specified after these flags |
