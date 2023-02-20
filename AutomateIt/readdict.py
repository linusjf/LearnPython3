#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""ReadDict."""
import csv

with open("mylist.csv", "rt", encoding="utf-8") as f:
    print("File Contents:")
    reader = csv.DictReader(f)
    for row in reader:
        print(row["first_name"], row["last_name"], row["email"])

with open("mylist.csv", "rt", encoding="utf-8") as f:
    reader = csv.DictReader(f)
    print("Columns in CSV file:", reader.fieldnames)
    print("Dialect used in CSV file:", reader.dialect)
    print("Current line number in CSV file:", reader.line_num)
    print("Moving the reader to next line with reader.__next__()")
    next(reader)
    print("Reading line number:", reader.line_num)
