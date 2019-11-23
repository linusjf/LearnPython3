#!/usr/bin/env python3
"""Read CSV file using generator."""
import sys
from random import randint
from threading import Timer
from locked import LockedIterator


def csv_reader(file_name):
    """Read file."""
    for line in open(file_name, "r"):
        yield line


def finite_sequence(limit):
    """Generate finite sequence."""
    num = 0
    while num < limit:
        _x = yield num
        if _x is not None:
            print("Ending iterator...")
            return
        num += 1


def is_palindrome(num):
    """Check if palindrome."""
    # Skip single-digit inputs
    if num // 10 == 0:
        return False
    temp = num
    reversed_num = 0

    while temp != 0:
        reversed_num = (reversed_num * 10) + (temp % 10)
        temp = temp // 10

    if num == reversed_num:
        return num


def run_finite_seq(rand):
    """Run finite sequence."""
    for i in finite_sequence(rand):
        print(i, end=" ")


def run_finite_palindromes_sixdigits(rand):
    """Run finite sequence of palindromes."""
    sequencer = LockedIterator(finite_sequence(rand))
    _timer = Timer(1, sequencer.send, ['anything'])
    _timer.start()
    for i in sequencer:
        pal = is_palindrome(i)
        if pal:
            if len(str(pal)) <= 6:
                print(pal)
            else:
                return


CSV_GEN = csv_reader("techcrunch.csv")
ROW_COUNT = 0

for row in CSV_GEN:
    ROW_COUNT += 1

print(f"Row count is {ROW_COUNT}")

CSV_GEN = (row for row in open("techcrunch.csv"))
ROW_COUNT = 0

for row in CSV_GEN:
    ROW_COUNT += 1

print(f"Row count is {ROW_COUNT}")

RAND = randint(0, sys.maxsize)

run_finite_palindromes_sixdigits(RAND)
