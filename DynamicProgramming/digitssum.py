#!/usr/bin/env python
"""
Digits Sum.

######################################################################
# @author      : Linus Fernandes (linusfernandes at gmail dot com)
# @file        : digitssum
# @created     : Monday Mar 20, 2023 22:42:34 IST
# @description :
# -*- coding: utf-8 -*-'
######################################################################
"""
# Given two integers a and b. The task is to
# print sum of all the digits appearing in the
# integers between a and b
# Memoization for the state results
dp = [[[-1] * 2 for _ in range(180)] for _ in range(20)]


# Stores the digits in x in a list digit
def get_digits(num, digit):
    """Get digits."""
    while num:
        digit.append(num % 10)
        num //= 10


# Return sum of digits from 1 to integer in digit list
def digit_sum(index, sumof, tight, digit):
    """Sum digits."""
    # Base case
    if index == -1:
        return sumof
    # Checking if already calculated this state
    if dp[index][sumof][tight] != -1 and tight != 1:
        return dp[index][sumof][tight]
    ret = 0
    # Calculating range value
    k = digit[index] if tight else 9
    for i in range(0, k + 1):
        # Calculating newTight value for nextstate
        new_tight = tight if digit[index] == i else 0
        # Fetching answer from next state
        ret += digit_sum(index - 1, sumof + i, new_tight, digit)
    if not tight:
        dp[index][sumof][tight] = ret
    return ret


# Returns sum of digits in numbers from a to b
def range_digit_sum(numa, numb):
    """Sum over range."""
    digits = []
    # Storing digits of numa-1 in digits
    get_digits(numa - 1, digits)
    # Finding sum of digits from 1 to "numa-1" which is passed as digitA
    ans1 = digit_sum(len(digits) - 1, 0, 1, digits)
    digits = []
    # Storing digits of b in digitB
    get_digits(numb, digits)
    # Finding sum of digits from 1 to "numb" which is passed as digitB
    ans2 = digit_sum(len(digits) - 1, 0, 1, digits)
    return ans2 - ans1


a, b = 123, 1024
print("digit sum for given range: ", range_digit_sum(a, b))
