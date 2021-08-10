#!/usr/bin/env python
# -*- coding: utf-8 -*-

x = 'Pluto is a planet'
y = "Pluto is a planet"
print(x == y)

print("Pluto's a planet!")
print('My dog is named "Pluto"')

hello = "hello\nworld"
print(hello)

triplequoted_hello = """hello
world"""
print(triplequoted_hello)
print(triplequoted_hello == hello)

print("hello")
print("world")
print("hello", end = '')
print("pluto", end = '')
print("")

# Indexing
planet = 'Pluto'
print(planet[0])

# Slicing
print(planet[-3:])

# How long is this string?
print(len(planet))

# Yes, we can even loop over them
print([char+'! ' for char in planet])

# ALL CAPS
claim = "Pluto is a planet!"
print(claim.upper())
# all lowercase
print(claim.lower())
# Searching for the first index of a substring
print(claim.index('plan'))
print(claim.startswith(planet))
print(claim.endswith('dwarf planet'))

words = claim.split()
print(words)
datestr = '1956-01-31'
year, month, day = datestr.split('-')
print(year, month, day)

datestr = '/'.join([month, day, year])
print(datestr)


# Yes, we can put unicode characters right in our string literals :)
outstr = ' 👏 '.join([word.upper() for word in words])
print(outstr)

print(planet + ', we miss you.')

position = 9
outstr = planet + ", you'll always be the " + str(position) + "th planet to me."
print(outstr)

print("{}, you'll always be the {}th planet to me.".format(planet, position))

pluto_mass = 1.303 * 10**22
earth_mass = 5.9722 * 10**24
population = 52910390
#         2 decimal points   3 decimal points, format as percent     separate with commas
print("{} weighs about {:.2} kilograms ({:.3%} of Earth's mass). It is home to {:,} Plutonians.".format(
    planet, pluto_mass, pluto_mass / earth_mass * 100, population)
)

# Referring to format() arguments by index, starting from 0
s = """Pluto's a {0}.
No, it's a {1}.
{0}!
{1}!""".format('planet', 'dwarf planet')
print(s)

numbers = {'one':1, 'two':2, 'three':3}
print(numbers['one'])
numbers['eleven'] = 11
print(numbers)
numbers['one'] = 'Pluto'
print(numbers)


planets = ['Mercury', 'Venus', 'Earth', 'Mars', 'Jupiter', 'Saturn', 'Uranus', 'Neptune']
planet_to_initial = {planet: planet[0] for planet in planets}
print(planet_to_initial)

print('Saturn' in planet_to_initial)

print('Betelgeuse' in planet_to_initial)

for k in numbers:
    print("{} = {}".format(k, numbers[k]))

# Get all the initials, sort them alphabetically, and put them in a space-separated string.
print(' '.join(sorted(planet_to_initial.values())))

for planet, initial in planet_to_initial.items():
    print("{} begins with \"{}\"".format(planet.rjust(7), initial))
