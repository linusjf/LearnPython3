#!/usr/bin/env python3
"""Read CSV file using generator."""
import sys
import random


def csv_reader(file_name):
    """Read file."""
    for line in open(file_name, "r"):
        yield line


def finite_sequence(limit):
    """Generate finite sequence."""
    num = 0
    while num < limit:
        yield num
        num += 1


def run_finite_seq(rand):
    """Run finite sequence."""
    for i in finite_sequence(rand):
        print(i, end=" ")


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

RAND = random.randint(0, sys.maxsize)

run_finite_seq(RAND)
