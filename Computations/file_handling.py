#!/usr/bin/env python
# -*- coding: utf-8 -*-

filename = 'tmp.dat'
# Open file for reading
infile = open(filename, 'r')  
# Read first line
line = infile.readline()      
# Read x and y coordinates from the file and store in lists
x = []
y = []
for line in infile:
    # Split line into words
    words = line.split()    
    x.append(float(words[0]))
    y.append(float(words[1]))
infile.close()

# Transform y coordinates
from math import log

def f(y):
    return log(y)

for i in range(len(y)):
    y[i] = f(y[i])

# Write out x and y to a two-column file
filename = 'tmp_out.dat'
outfile = open(filename, 'w')  
# Open file for writing
outfile.write('# x and y coordinates\n')
for xi, yi in zip(x, y):
    outfile.write('%10.5f %10.5f\n' % (xi, yi))
outfile.close()
