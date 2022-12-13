#!/usr/bin/env python
# -*- coding: utf-8 -*-
token = ""
try:
    with open('.gisttoken','r') as file:
        token = file.read()
except Exception as exc:
    print(exc)
    exit(1)

import requests
import json
 
BASE_URL = 'https://api.github.com'
Link_URL = 'https://gist.github.com'
## Fill in your github username
username = 'fernal73' 
## Fill in your token
api_token = token.rstrip() 
header = {
    'X-Github-Username': '%s' % username,
    'Content-Type': 'application/json',
    'Authorization': 'Token %s' % api_token}
print("Header:")
print("------------------------------")
print(header)
url = "/gists"
data = {
    "description": "the description for this gist",
    "public": True,
    "files": {
        "file1.txt": {
            "content": "String file contents"
        }
    }
}
print("Files:")
print("------------------------------")
print(data)
gisturl = ""
try:
    r = requests.post('%s%s' % (BASE_URL, url),
                  headers=header,
                  data=json.dumps(data))
    gisturl = r.json()['url']
    print(gisturl)
except Exception as exc:
    print(exc)
    exit(1)

try:
    r = requests.get('%s' %gisturl,
                     headers=header)
    print(r.json())
except Exception as exc:
    print(exc)
    exit(1)

data = { 
    "description": "Updating the description for this gist",
    "files":{ 
        "file1.txt": {
            "content": "Updating file contents...",
            "filename": "file.txt"
        }
    }
}
try:
    r = requests.patch('%s' %gisturl,
                       headers=header,
                       data=json.dumps(data))
    print("Patch result:")
    print("------------------------------")
    print(r.json())
except Exception as exc:
    print(exc)
    exit(1)

try:
    r = requests.delete('%s' %gisturl,
                    headers=header)
except Exception as exc:
    print(exc)
    exit(1)

url = "/users/%s/gists" % username
try:
    r = requests.get('%s%s' % (BASE_URL, url),headers=header)
except Exception as exc:
    print(exc)
    exit(1)
gists = r.json()
print("List gists result:")
print("------------------------------")
for gist in gists:
    data = gist['files'].values()
    data = list(data)[0] 
    print(data['filename'],data['raw_url'], data['language'])
