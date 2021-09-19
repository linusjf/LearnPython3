#!/usr/bin/env python

######################################################################
# @author      : Linus Fernandes (linusfernandes at gmail dot com)
# @file        : primes
# @created     : Sunday Sep 19, 2021 19:07:50 IST
# @description : 
# -*- coding: utf-8 -*-'
######################################################################

def check_prime(number):
    for divisor in range(2, int(number ** 0.5) + 1):
        if number % divisor == 0:
            return False
    return True

class PrimesIter:
    def __init__(self, max):
        # the maximum number of primes we want generated
        self.max = max
        # start with this number to check if it is a prime.
        self.number = 1
        # No of primes generated yet. We want to StopIteration when it reaches max
        self.primes_generated = 0

    def __iter__(self):
        return self

    def __next__(self):
        self.number += 1
        if self.primes_generated >= self.max:
            raise StopIteration
        elif check_prime(self.number):
            self.primes_generated+=1
            return self.number
        else:
            return self.__next__()

prime_generator = PrimesIter(50)

for x in prime_generator:
    print(x)

def PrimesGen(max):
    number = 1
    generated = 0
    while generated < max:
        number += 1
        if check_prime(number):
            generated+=1
            yield number

prime_generator = PrimesGen(10)

for x in prime_generator:
    print(x)

primes = (i for i in range(1,100) if check_prime(i))
for x in primes:
    print(x)
