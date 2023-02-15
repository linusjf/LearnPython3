| Note | Description |
| —--- | —---------- |
| lookarounds | custom assertions, zero-width like anchors |
| \(\?\!pat\) | negative lookahead assertion |
| \(\?\<\!pat\) | negative lookbehind assertion |
| \(\?\=pat\) | positive lookahead assertion |
| \(\?\<\=pat\) | positive lookbehind assertion |
| \(\?\!pat1\)\(\?\=pat2\) | multiple assertions can be specified next to each other in any order |
| as they mark a matching location without consuming characters |
| \(\(\?\!pat\)\.\)\* | Negate a grouping, similar to negated character class |
| pat\\K | regex module, pat won’t be part of matching portion |
| | regex module allows variable length lookbehinds unlike re |
