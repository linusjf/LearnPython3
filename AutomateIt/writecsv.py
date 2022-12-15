#!/usr/bin/env python
# -*- coding: utf-8 -*-
import csv
names = ["John", "Eve", "Fate", "Jadon"]
 
grades = ["C", "A+", "A", "B-"]
f = open("newlist.csv", 'wt')
try:
    writer = csv.writer(f)
    writer.writerow( ('Sr.', 'Names', 'Grades') )
    for i in range(4):
        writer.writerow( (i+1, names[i], grades[i]) )
finally:
    f.close()
