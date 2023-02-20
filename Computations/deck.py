#!/usr/bin/env python
# -*- coding: utf-8 -*-

ranks = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]
suits = ["C", "D", "H", "S"]
deck = []
for s in suits:
    for r in ranks:
        deck.append(s + r)
print(deck)
