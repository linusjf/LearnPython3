#!/usr/bin/env python
"""Httpreqs."""
import requests

r = requests.get("http://ip.jsontest.com/", timeout=5)
print("Response object:", r)
print("Response Text:", r.text)
payload = {"q": "chetan"}
r = requests.get("https://github.com/search", params=payload, timeout=5)
print("Request URL:", r.url)
payload = {"key1": "value1"}
r = requests.post("http://httpbin.org/post", data=payload, timeout=5)
print("Response text:", r.json())
try:
    r = requests.get("http://www.google.com/", timeout=5)
    print("Response object:", r)
except requests.exceptions.RequestException as e:
    print("Error Response:", str(e))
