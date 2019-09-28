#!/usr/bin/env python3
"""Formatting examples."""

print('{0:9} | {1:8}'.format('Vegetable', 'Quantity'))
print('{0:9} | {1:8}'.format('Asparagus', 3))
print('{0:9} | {1:8}'.format('Onions', 10))

print('{0:9} | {1:<8}'.format('Vegetable', 'Quantity'))
print('{0:9} | {1:<8}'.format('Asparagus', 3))
print('{0:9} | {1:<8}'.format('Onions', 10))

print('{0:8} | {1:<8}'.format('Vegetable', 'Quantity'))
print('{0:9} | {1:<8.2f}'.format('Asparagus', 2.33333))
print('{0:9} | {1:<8.2f}'.format('Onions', 10))

print('{0:^9} | {1:^8}'.format('Vegetable', 'Quantity'))
print('{0:^9} | {1:^8}'.format('Asparagus', 3))
print('{0:^9} | {1:^8}'.format('Onions', 10))

print('{0:>8} | {1:>8}'.format('Vegetable', 'Quantity'))
print('{0:>9} | {1:>8.2f}'.format('Asparagus', 2.33333))
print('{0:>9} | {1:>8.2f}'.format('Onions', 10))
