#!/usr/bin/env python
# -*- coding: utf-8 -*-

name = 'Andy'
age = 20
print("I am " + name + ". I am " + str(age) + " years old")

print("I am %s. I am %s years old" % (name, age))

print("I am {}. I am {} years old".format(name, age))

print("I am {name}. I am {age} years old".format(name
= name, age = age))

data = {'name':'Andy','age':20}
print("I am {name}. I am {age} years old".format(**data))

print(f"I am {name}. I am {age} years old")

num1 = 4
num2 = 5
print(f"The sum of {num1} and {num2} is {num1+num2}.")

def totalFruits(apples,oranges):
    return apples+oranges

data = {'name':'Andy','age':20}
apples = 20
oranges = 30
print(f"{data['name']} has {totalFruits(apples,oranges)} fruits")
num1 = 4
num2 = 5
print(f'''The sum of {num1} and {num2} is {num1+num2}.''')
numFloat = 10.23456678
print(f'Printing Float with 2 decimals: {numFloat:.2f}')
