#!/usr/bin/env python
# -*- coding: utf-8 -*-

import string
letters = string.ascii_uppercase
digits = range(10)
registration_numbers = []
for place1 in letters:
    for place2 in letters:
        for place3 in digits:
            for place4 in digits:
                for place5 in digits:
                    registration_numbers.append(
                        '%s%s%s%s%s' %
                        (place1, place2, place3, place4, place5))
print(registration_numbers)
print(len(registration_numbers))
