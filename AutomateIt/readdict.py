#!/usr/bin/env python
# -*- coding: utf-8 -*-
import csv

f = open("mylist.csv", "rt")
print("File Contents:")
try:
    reader = csv.DictReader(f)
    for row in reader:
        print(row["first_name"], row["last_name"], row["email"])
finally:
    f.close()

f = open("mylist.csv", "rt")
reader = csv.DictReader(f)
print("Columns in CSV file:", reader.fieldnames)
print("Dialect used in CSV file:", reader.dialect)
print("Current line number in CSV file:", reader.line_num)
print("Moving the reader to next line with reader.__next__()")
reader.__next__()
print("Reading line number:", reader.line_num)
f.close()
