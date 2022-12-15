#!/usr/bin/env python
# -*- coding: utf-8 -*-
import csv
fh = open("mylist.csv", 'r')
try:
    reader = csv.reader(fh)
    print("Data from the CSV:")
    print(list(reader))
except Exception as e:
    print("Exception is:", e)
finally:
    fh.close()
