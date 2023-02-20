#!/usr/bin/env python3
"""URL Loading."""
#
# read the data from the URL and print it
#
import urllib.request

# open a connection to a URL using urllib
WEBURL = urllib.request.urlopen("https://www.youtube.com/user/guru99com")

# get the result code and print it
print("result code: " + str(WEBURL.getcode()))

# read the data from the URL and print it
DATA = WEBURL.read()
print(DATA)
