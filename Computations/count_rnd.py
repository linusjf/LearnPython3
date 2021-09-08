#!/usr/bin/env python
# -*- coding: utf-8 -*-

from random import randint

N = int(input('How many random numbers should be drawn? '))

# Draw random numbers
# Counter for the occurences of 6
M = 0
for i in range(N):
    drawn_number = randint(1, 6)
    print('Draw number %d gave: %d' % (i+1, drawn_number))
    if drawn_number == 6:
        M += 1

print('The fraction M/N became: %g' % (M/float(N)))

