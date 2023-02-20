#!/usr/bin/env python
# -*- coding: utf-8 -*-
from bs4 import BeautifulSoup
from threading import Thread
import urllib.request as req
import json
import xml.sax.saxutils as saxutils

# Location of restaurants
home_url = "https://www.yelp.com"
find_what = "Restaurants"
location = "London%2C+United+Kingdom"
# Get all restaurants that match the search criteria
search_url = "https://www.yelp.com/search?find_desc=" + find_what + "&find_loc=" + location
s_html = req.urlopen(search_url).read()
soup_s = BeautifulSoup(s_html, "lxml")
# Get URLs of top 10 Restaurants in London
url = []
for a in soup_s.find_all("a", href=True):
    href = a["href"]
    index = href.find("?")
    if index >= 0:
        href = href[0:index]

    if href.startswith("/biz") and not home_url + href in url:
        url.append(home_url + href)

url = url[0:10]


# Function that will do actual scraping job
def scrape(ur):
    html = req.urlopen(ur).read()
    soup = BeautifulSoup(html, "lxml")
    jsonstring = ""
    for script in soup.findAll("script", {"type": "application/ld+json"}):
        jsondata = json.loads(script.text)
        if jsondata["@type"] == "Restaurant":
            jsonstring = jsondata
            break

    title = jsonstring["name"]
    saddress = jsonstring["address"]
    phone = jsonstring["telephone"]
    if title:
        print("Title: ", saxutils.unescape(title, {"&apos;": "'"}))
    if saddress:
        print("Address: ")
        print("Street address: ", saxutils.unescape(saddress["streetAddress"], {"&apos;": "'"}))
        print("Locality: ", saddress["addressLocality"])
        print("Country: ", saddress["addressCountry"])
        print("Region: ", saddress["addressRegion"])
        print("Postal code: ", saddress["postalCode"])
    if phone:
        print("Phone Number: ", phone)
    print("-------------------")


threadlist = []
i = 0
# Making threads to perform scraping
while i < len(url):
    t = Thread(target=scrape, args=(url[i],))
    t.start()
    threadlist.append(t)
    i = i + 1

for t in threadlist:
    t.join()
