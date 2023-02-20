#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""ScrapeYelp."""
from xml.sax import saxutils
from threading import Thread
import urllib.request as req
import json
from bs4 import BeautifulSoup

# Location of restaurants
HOME_URL = "https://www.yelp.com"
FIND_WHAT = "Restaurants"
LOCATION = "London%2C+United+Kingdom"
# Get all restaurants that match the search criteria
SEARCH_URL = "https://www.yelp.com/search?find_desc=" + FIND_WHAT + "&find_loc=" + LOCATION

with req.urlopen(SEARCH_URL) as s:
    s_html = s.read()
    soup_s = BeautifulSoup(s_html, "lxml")
    # Get URLs of top 10 Restaurants in London
    url = []
    for a in soup_s.find_all("a", href=True):
        href = a["href"]
        index = href.find("?")
        if index >= 0:
            href = href[0:index]

        if href.startswith("/biz") and not HOME_URL + href in url:
            url.append(HOME_URL + href)

url = url[0:10]


# Function that will do actual scraping job
def scrape(url_l):
    """Scrape."""
    with req.urlopen(url_l) as site:
        html = site.read()
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
            print(
                "Street address: ", saxutils.unescape(saddress["streetAddress"], {"&apos;": "'"})
            )
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
