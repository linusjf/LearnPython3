#!/usr/bin/env python
# -*- coding: utf-8 -*-

from price_parser import Price
from price_parser import parse_price

price = Price.fromstring("22,90 €")
print(price)
# numeric price amount
print(price.amount)
# currency symbol, as appears in the string
print(price.currency)
# price amount, as appears in the string
print(price.amount_text)
# price amount as float, not Decimal
print(price.amount_float)

print(parse_price("22,90 €"))

print(Price.fromstring("Price: $119.00"))
print(Price.fromstring("15 130 Р"))
print(Price.fromstring("151,200 تومان"))
print(Price.fromstring("Rp 1.550.000"))
print(Price.fromstring("Běžná cena 75 990,00 Kč"))

print(Price.fromstring("1,235€ 99"))
print(Price.fromstring("24€99"))
print(Price.fromstring("99 € 95 €"))
print(Price.fromstring("35€ 999"))
print(Price.fromstring("€35,999"))
print(Price.fromstring("€35,999", currency_hint="€", decimal_separator=","))

print(Price.fromstring(""))
print(Price.fromstring("Foo"))
print(Price.fromstring("50% OFF"))
print(Price.fromstring("50"))
print(Price.fromstring("R$"))

print(Price.fromstring("34.99", currency_hint="руб. (шт)"))

price = Price.fromstring("1 000")
price.currency = "EUR"
print(price)

print(Price.fromstring("Price: $140.600", decimal_separator="."))
print(Price.fromstring("Price: $140.600", decimal_separator=","))
