#!/usr/bin/env python
# -*- coding: utf-8 -*-
from lxml import html
import requests
page = requests.get('https://github.com/pricing/')
tree = html.fromstring(page.content)
print("Page Object:", tree)
plans = tree.xpath('//h2[@class="mb-2 h5-mktg"]/text()')
pricing = tree.xpath('//span[@data-plan="free" and @class="js-computed-value"]/text()')[0]
print("Plan:", plans[0], "\nPricing:", pricing)
pricing = tree.xpath('//span[@data-plan="business" and @class="js-computed-value"][1]/text()')[0]
print("Plan:", plans[1], "\nPricing:", pricing)
pricing = tree.xpath('//span[@data-plan="business_plus" and @class="js-computed-value"][1]/text()')[0]
print("Plan:", plans[2], "\nPricing:", pricing)