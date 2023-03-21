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
from functools import lru_cache
import math

# Given two integers a and b. The task is to
# print sum of all the digits appearing in the
# integers between a and b
# Memoization for the state results
dp = [[[-1] * 1 for _ in range(180)] for _ in range(20)]


# Function to computer sum of digits in
# numbers from 1 to n
def sum_digits_formula(num):
    """Sum of digits formula."""
    dig_cnt = int(math.log(num, 10))
    if dig_cnt == 0:
        return num
    array = [0] * (dig_cnt + 1)
    array[0] = 0
    array[1] = 45
    for i in range(2, dig_cnt + 1):
        array[i] = array[i - 1] * 10 + 45 * int(math.ceil(pow(10, i - 1)))
    return sum_digits_util(num, array)


def sum_digits_util(num, array):
    """Sum digits utility."""
    if num < 10:
        return (num * (num + 1)) // 2
    d = int(math.log(num, 10))  # pylint: disable=invalid-name
    p = int(math.ceil(pow(10, d)))  # pylint: disable=invalid-name

    msd = num // p
    return (
        msd * array[d]
        + (msd * (msd - 1) // 2) * p
        + msd * (1 + num % p)
        + sum_digits_util(num % p, array)
    )


# Stores the digits in x in a list digit
def get_digits(num):
    """Get digits."""
    digits = []
    while num:
        digits.append(num % 10)
        num //= 10
    return digits


# Return sum of digits from 1 to integer in digit list
def digit_sum(index, sumof, tight, digit):
    """Sum digits."""
    print(f"index = {index}, sumof = {sumof}, tight = {tight}, digit = {digit}")
    # Base case
    if index == -1:
        return sumof
    if not tight:
        print(f"dp[{index}][{sumof}][{tight}] = {dp[index][sumof][tight]}")
    # Checking if already calculated this state
    if not tight and dp[index][sumof][tight] != -1:
        return dp[index][sumof][tight]
    # Check if the range of integers is restricted
    # Calculating range value
    # restrict the range if tight
    print(f"digit[{index}] = {digit[index]}")
    k = digit[index] if tight else 9
    print(f"k = {k}")
    ret = 0
    for i in range(0, k + 1):
        print(f"i = {i}")
        # Calculating new_tight value for next state
        new_tight = tight if digit[index] == i else 0
        # Fetching answer from next state
        print(f"new_tight = {new_tight}")
        print(f"calling recursively with index = {index - 1} and adding {i}")
        ret += digit_sum(index - 1, sumof + i, new_tight, digit)
    if not tight:
        dp[index][sumof][tight] = ret
    return ret


# Returns sum of digits in numbers from a to b
def range_digit_sum(numa, numb):
    """Sum over range."""
    # Storing digits of numa-1 in digits
    digits = get_digits(numa - 1)
    print(f"digits for {numa} = {digits}")
    # Finding sum of digits from 1 to "numa-1" which is passed as digitA
    ans1 = digit_sum(len(digits) - 1, 0, 1, digits)
    print(f"ans1 = {ans1}")
    print()
    print("-----------------------------")
    # Storing digits of b in digitB
    digits = get_digits(numb)
    print(f"digits for {numb} = {digits}")
    # Finding sum of digits from 1 to "numb" which is passed as digitB
    ans2 = digit_sum(len(digits) - 1, 0, 1, digits)
    print(f"ans2 = {ans2}")
    return ans2 - ans1


# Returns sum of all digits in numbers
# from 1 to n
def sum_of_digits(num):
    """Sum up digits."""
    result = 0  # initialize result
    # One by one compute sum of digits
    # in every number from 1 to n
    for x in range(0, num + 1):  # pylint: disable=invalid-name
        result = result + sum_up_digits(x)
    return result


# A utility function to compute sum of
# digits in a given number x
def sum_up_digits(numx):
    """Sum digits in number."""
    digits = get_digits(numx)
    return sum_digits(tuple(sorted(digits)))


# A utility function to compute sum of
# digits in a given number x
@lru_cache
def sum_digits(digits):
    """Sum digits in number."""
    return sum(digits)


a, b = 123, 1024
print("digit sum for given range: ", range_digit_sum(a, b))
a, b = 122, 1024
print("digit sum for given range: ", range_digit_sum(a, b))
a, b = 2, 30
print("digit sum for given range: ", range_digit_sum(a, b))
a, b = 2, 35
print("digit sum for given range: ", range_digit_sum(a, b))
a, b = 2, 35
print("digit sum for given range: ", sum_of_digits(b) - sum_of_digits(a - 1))
a, b = 2, 35
print("digit sum for given range: ", sum_digits_formula(b) - sum_digits_formula(a - 1))
