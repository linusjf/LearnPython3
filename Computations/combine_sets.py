#!/usr/bin/env python
# -*- coding: utf-8 -*-

dice = []
for d1 in range(1, 7):
    for d2 in range(1, 7):
        dice.append((d1, d2))

n = 0
comb = []
for d1, d2 in dice:
    if d1 + d2 == 7:
        n += 1
        comb.append((d1,d2))
print('%d combinations results in the sum 7' % n)
print(comb)
