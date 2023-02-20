#!/usr/bin/env python
"""Findsoup."""
# -*- coding: utf-8 -*-
import bs4

with open("python.html", encoding="utf-8") as myfile:
    soup = bs4.BeautifulSoup(myfile, "lxml")
    # Making the soup
    print("BeautifulSoup Object:", type(soup))
    # Find Elements By tags
    print(soup.find_all("a"))
    print(soup.find_all("strong"))
    # Find Elements By id
    print(soup.find("div", {"id": "inventor"}))
    print(soup.select("#inventor"))
    # Find Elements by css print
    print(soup.select(".wow"))
    print("Facebook URL:", soup.find_all("a")[0]["href"])
    print("Inventor:", soup.find("div", {"id": "inventor"}).text)
    print("Span content:", soup.select("span")[0].getText())
