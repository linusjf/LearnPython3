#!/usr/bin/env python
# -*- coding: utf-8 -*-

from price_parser import parse_price

def extract_price(description):
    if description.startswith("€") == -1:
        return parse_price(description,decimal_separator=",").amount
    else:
        return parse_price(description).amount

usdprice = "$24.99"
itprice = "€24,99"
usprice2 = "$24,990"
frprice = "24€99"

print(extract_price(usdprice))
print(extract_price(itprice))
print(extract_price(frprice))
print(extract_price(usprice2))
