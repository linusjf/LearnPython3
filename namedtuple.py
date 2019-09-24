#!/usr/bin/env python3
""" Named tuple example """
from collections import namedtuple

Car = namedtuple('Car', 'color mileage')

# Our new "Car" class works as expected:
MY_CAR = Car('red', 3812.4)
print(MY_CAR.color)
print(MY_CAR.mileage)

# We get a nice string repr for free:
print(MY_CAR)

try:
    MY_CAR.color = 'blue'
except AttributeError as inst:
    print(type(inst))     # the exception instance
    print(inst.args)      # arguments stored in .args
    print(inst)
finally:
    print("Into finally")
