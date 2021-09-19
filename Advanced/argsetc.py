#!/usr/bin/env python

def adder(*args):
    result = 0
    for arg in args:
        result+=arg
    return result

print(adder(1,2))
print(adder(1,2,3))
print(adder(1,2,5,7,8,9,100))

def myprint(**kwargs):
    for k,v in kwargs.items():
        print(f'{k} is {v} years old')

myprint(Sansa=20,Tyrion=40,Arya=17)
