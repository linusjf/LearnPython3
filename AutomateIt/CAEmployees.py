#!/usr/bin/env python
# -*- coding: utf-8 -*-

import csv

f = open("mylist.csv", "rt")
fw = open("CAEmployees.csv", "wt")
try:
    reader = csv.DictReader(f)
    csvWriter = csv.writer(fw)
    for row in reader:
        if reader.line_num == 1:
            continue
        if row["state"] == "CA":
            csvWriter.writerow([row["email"], row["phone"]])
finally:
    f.close()
    fw.close()
