#!/usr/bin/env python
# -*- coding: utf-8 -*-

import re

valid_countries = ["US", "IT", "FR"]

def extract_price(description, country):
    if country not in valid_countries:
        return

    if country == "US":
        pattern = re.compile(r'\$(\d+\.\d+)')
        match = pattern.search(description)

        if not match:
            return

        try:
            return float(match.groups()[0])
        except ValueError:
            return

    if country == "IT":
        pattern = re.compile(r'€(\d+[,]\d+)')
        match = pattern.search(description)

        if not match:
            return

        try:
            return float(match.groups()[0].replace(",","."))
        except ValueError:
            return
    
    if country == "FR":
        pattern = re.compile(r'€(\d+[,]\d+)|(\d+€\d+)')
        match = pattern.search(description)

        if not match:
            return

        try:
            val = [gr for gr in match.groups() if gr != None]
            val = val[0].replace(",",".")
            val = val.replace("€",".")
            return float(val)
        except ValueError:
            return

usdprice = "$24.99"
itprice = "€24,99"
frprice = "24€99"

print(extract_price(usdprice,"US"))
print(extract_price(itprice,"IT"))
print(extract_price(itprice,"FR"))
print(extract_price(frprice,"FR"))
