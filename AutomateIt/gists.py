#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Gists."""
import json
import sys
import requests

TOKEN = ""  # nosec
try:
    with open(".gisttoken", "r", encoding="utf-8") as file:
        TOKEN = file.read()
except OSError as exc:
    print(exc)
    sys.exit(1)


BASE_URL = "https://api.github.com"
LINK_URL = "https://gist.github.com"
# Fill in your github username
USERNAME = "fernal73"
# Fill in your token
api_token = TOKEN.rstrip()
HEADER = {
    "X-Github-Username": f"{USERNAME}",
    "Content-Type": "application/json",
    "Authorization": f"Token {api_token}",
}
print("Header:")
print("------------------------------")
print(HEADER)
URL = "/gists"
data = {
    "description": "the description for this gist",
    "public": True,
    "files": {"file1.txt": {"content": "String file contents"}},
}
print("Files:")
print("------------------------------")
print(data)
GISTURL = ""
try:
    r = requests.post(f"{BASE_URL}{URL}", headers=HEADER, data=json.dumps(data), timeout=5)
    GISTURL = r.json()["url"]
    print(GISTURL)
except OSError as exc:
    print(exc)
    sys.exit(1)

try:
    r = requests.get(f"{GISTURL}", headers=HEADER, timeout=5)
    print(r.json())
except OSError as exc:
    print(exc)
    sys.exit(1)

data = {
    "description": "Updating the description for this gist",
    "files": {"file1.txt": {"content": "Updating file contents...", "filename": "file.txt"}},
}
try:
    r = requests.patch(f"{GISTURL}", headers=HEADER, data=json.dumps(data), timeout=5)
    print("Patch result:")
    print("------------------------------")
    print(r.json())
except OSError as exc:
    print(exc)
    sys.exit(1)

try:
    r = requests.delete(f"{GISTURL}", headers=HEADER, timeout=5)
except OSError as exc:
    print(exc)
    sys.exit(1)

URL = f"/users/{USERNAME}/gists"
try:
    r = requests.get(f"{BASE_URL}{URL}", headers=HEADER, timeout=5)
except OSError as exc:
    print(exc)
    sys.exit(1)
gists = r.json()
print("List gists result:")
print("------------------------------")
for gist in gists:
    vals = gist["files"].values()
    val = list(vals)[0]
    print(data["filename"], data["raw_url"], data["language"])
