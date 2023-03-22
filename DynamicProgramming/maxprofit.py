#!/usr/bin/env python
"""
Maximize profit.

######################################################################
# @author      : Linus Fernandes (linusfernandes at gmail dot com)
# @file        : maxprofit
# @created     : Tuesday Mar 21, 2023 20:12:56 IST
# @description :
# -*- coding: utf-8 -*-'
######################################################################
"""
import sys


def maxtwobuysell(arr):
    """Maximize profit for two pairs of transactions."""
    size = len(arr)
    first_buy = -sys.maxsize
    first_sell = 0
    second_buy = -sys.maxsize
    second_sell = 0
    for i in range(size):
        first_buy = max(first_buy, -arr[i])
        first_sell = max(first_sell, first_buy + arr[i])
        second_buy = max(second_buy, first_sell - arr[i])
        second_sell = max(second_sell, second_buy + arr[i])
    return second_sell


# two transactions on a given
# two transactions on a given
# list of stock prices price[0..n-1]
def max_profit(price):
    """Maximize profit."""
    num = len(price)
    # Create profit array and initialize it as 0
    profit = [0] * num

    # Get the maximum profit
    # with only one transaction
    # allowed. After this loop,
    # profit[i] contains maximum
    # profit from price[i..n-1]
    # using at most one trans.
    max_price = price[num - 1]
    for i in range(num - 2, 0, -1):
        if price[i] > max_price:
            max_price = price[i]

        # we can get profit[i] by
        # taking maximum of:
        # a) previous maximum,
        # i.e., profit[i+1]
        # b) profit by buying at
        # price[i] and selling at
        # max_price
        profit[i] = max(profit[i + 1], max_price - price[i])

    print(profit)
    # Get the maximum profit
    # with two transactions allowed
    # After this loop, profit[n-1]
    # contains the result
    min_price = price[0]
    for i in range(1, num):
        if price[i] < min_price:
            min_price = price[i]
        # Maximum profit is maximum of:
        # a) previous maximum,
        # i.e., profit[i-1]
        # b) (Buy, Sell) at
        # (min_price, A[i]) and add
        #  profit of other trans.
        # stored in profit[i]
        profit[i] = max(profit[i - 1], profit[i] + (price[i] - min_price))
    result = profit[num - 1]
    print(profit)
    return result


# list of stock prices price[0..n-1]
def max_profit2(price):
    """Maximize profit."""
    print(price)
    num = len(price)
    # Create profit array and initialize it as 0
    profit = [0] * num

    min_price = price[0]
    for i in range(1, num - 1):
        if price[i] < min_price:
            min_price = price[i]
        # Maximum profit is maximum of:
        # a) previous maximum,
        # i.e., profit[i-1]
        # b) (Buy, Sell) at
        # (min_price, A[i]) and add
        #  profit of other trans.
        # stored in profit[i]
        profit[i] = max(profit[i - 1], price[i] - min_price)
    print(profit)
    # Get the maximum profit
    # with only one transaction
    # allowed. After this loop,
    # profit[i] contains maximum
    # profit from price[i..n-1]
    # using at most one trans.
    max_price = price[num - 1]
    for i in range(num - 2, 0, -1):
        if price[i] > max_price:
            max_price = price[i]

        # we can get profit[i] by
        # taking maximum of:
        # a) previous maximum,
        # i.e., profit[i+1]
        # b) profit by buying at
        # price[i] and selling at
        # max_price
        profit[i] = max(profit[i + 1], profit[i] + max_price - price[i])

    print(profit)
    result = profit[1]
    return result


# Driver function
PRICE = [2, 30, 15, 10, 8, 25, 80]
print(f"Maximum profit is {max_profit(PRICE)}")
PRICE = [2, 30, 15, 10, 8, 25, 80]
print(f"Maximum profit is {max_profit2(PRICE)}")
PRICE = [2, 30, 15, 15, 8, 25, 80]
print(f"Maximum profit is {max_profit(PRICE)}")
PRICE = [2, 30, 15, 15, 8, 25, 80]
print(f"Maximum profit is {max_profit2(PRICE)}")
PRICE = [2, 30, 15, 10, 8, 25, 80]
print(f"Maximum profit is {maxtwobuysell(PRICE)}")
