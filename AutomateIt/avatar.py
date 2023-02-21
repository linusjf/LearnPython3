#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Avatar."""
import re
import urllib.request as req
import os
from bs4 import BeautifulSoup

# Download paramters
IMAGE_TYPE = "Project"
MOVIE = "Avatar"
URL = "https://www.google.com/search?q=" + MOVIE + "&source=lnms&tbm=isch"
HEADER = {"User-Agent": "Mozilla/5.0"}
with req.urlopen(req.Request(URL, headers=HEADER)) as doc:  # nosec
    soup = BeautifulSoup(doc, "lxml")
    imglines = soup.find_all("img", {"src": re.compile("gstatic.com")})[:5]
    images = [a["src"] for a in imglines]
    for img in images:
        print("Image Source:", img)
        with req.urlopen(img).read() as raw_img:
            cntr = len([i for i in os.listdir(".") if IMAGE_TYPE in i]) + 1
            with open(IMAGE_TYPE + "_" + str(cntr) + ".jpg", "wb") as f:
                f.write(raw_img)
