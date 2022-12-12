#!/usr/bin/env python
# -*- coding: utf-8 -*-
from bs4 import BeautifulSoup
import re
import urllib.request as req
import os
## Download paramters
image_type = "Project"
movie = "Avatar"
url = "https://www.google.com/search?q="+movie+"&source=lnms&tbm=isch"
header = {'User-Agent': 'Mozilla/5.0'}
soup = BeautifulSoup(req.urlopen(req.Request(url,headers=header)),"lxml")
images = [a['src'] for a in soup.find_all("img", {"src":re.compile("gstatic.com")})][:5]
for img in images:
    print("Image Source:", img)
