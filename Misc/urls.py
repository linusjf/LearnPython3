#!/usr/bin/env python
import can_ada
urlstring = "https://www.GOoglé.com/./path/../path2/"
url = can_ada.parse(urlstring)
# prints www.xn--googl-fsa.com, the correctly parsed domain name according
# to WHATWG
print(url.hostname)
# prints /path2/, which is the correctly parsed pathname according to WHATWG
print(url.pathname)

import urllib.parse
urlstring = "https://www.GOoglé.com/./path/../path2/"
url = urllib.parse.urlparse(urlstring)
# prints www.googlé.com
print(url.hostname)
# prints /./path/../path2/
print(url.path)
