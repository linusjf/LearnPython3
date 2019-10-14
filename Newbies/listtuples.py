#!/usr/bin/env python3
"""Lists and tuples."""
MONTHS_TUPLE = ('January', 'February', 'March',
                'April', 'May', 'June', 'July',
                'August', 'September', 'October', 'November', 'December')
MONTHS_LIST = list(MONTHS_TUPLE)
print('MONTHS_TUPLE is {}.'.format(type(MONTHS_TUPLE)))
print('MONTHS_LIST is {}.'.format(type(MONTHS_LIST)))
ANIMALS_LIST = ['toad', 'lion', 'seal']
ANIMALS_TUPLE = tuple(ANIMALS_LIST)
print('ANIMALS_LIST is {}.'.format(type(ANIMALS_LIST)))
print('ANIMALS_TUPLE is {}.'.format(type(ANIMALS_TUPLE)))
