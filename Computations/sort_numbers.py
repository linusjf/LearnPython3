#!/usr/bin/env python
# -*- coding: utf-8 -*-

from numpy import zeros
from random import uniform

N = 6
numbers = zeros(N)

# Draw random numbers
for i in range(len(numbers)):
    numbers[i] = uniform(0, 10)
print("Unsorted: %5.3f  %5.3f %5.3f %5.3f  %5.3f %5.3f" % \
        (numbers[0], numbers[1], numbers[2],\
         numbers[3], numbers[4], numbers[5]))

for reference in range(N):
    smallest = numbers[reference]
    i_smallest = reference
    # Find the smallest number in remaining unprinted array
    for i in range(reference + 1, N, 1):
        if numbers[i] <= smallest:
            smallest = numbers[i]
            i_smallest = i
    # Switch numbers, and use an extra variable for that
    switch = numbers[reference]
    numbers[reference] = numbers[i_smallest]
    numbers[i_smallest] = switch

print("Sorted  : %5.3f  %5.3f %5.3f %5.3f  %5.3f %5.3f" % \
        (numbers[0], numbers[1], numbers[2],\
         numbers[3], numbers[4], numbers[5]))
