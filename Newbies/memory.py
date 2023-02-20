#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Variable 1: peanut_butter
peanut_butter = 6
print("The memory location of variable peanut_butter is: ", id(peanut_butter))
# Variable 2: sandwich
sandwich = 6
print("The memory location of variable sandwich is: ", id(sandwich))
print(
    " We can see that the memory location of both the variables is the same because they were assigned the same value"
)
# Setting value of sandwich variable to a new number
sandwich = 7
# Setting both the variables equal to each other:
peanut_butter = sandwich
print("After setting the values of both variables equal to each other, we have: ")
print("The value of variable sandwich is now set to:  ", sandwich)
print("The value of variable peanut_butter is now set to: ", peanut_butter)
print(
    "The value of sandwich variable was changed to 10, let's see whether it affects the value of peanut_butter"
)
# Setting value of sandwich variable to a new number
sandwich = 10
print("The value of variable peanut_butter: ", peanut_butter)
print("The value of peanut_butter did NOT change even though we changed the value of sandwich")
print("The memory location of variable peanut_butter is: ", id(peanut_butter))

import time

number = 1000000
# Check the current time
startTime = time.time()
# Create an empty list
list = []
# Add items to the list one by one
for counter in range(number):
    list.append(counter)
# Display the run time
print(time.time() - startTime)

# Check the current time
startTime = time.time()
# Create a list of 1000000 zeros
list = [None] * number
# Add items to the list one by one
for counter in range(number):
    list[counter] = counter
# Display the run time
print(time.time() - startTime)
