#!/usr/bin/env python
# -*- coding: utf-8 -*-

filename = "tmp.dat"
import numpy

data = numpy.loadtxt(filename, comments="#")
x = data[:, 0]
y = data[:, 1]
# insert transformed y back in array
data[:, 1] = numpy.log(y)
filename = "tmp_out.dat"
filename = "tmp_out.dat"
# open file for writing
outfile = open(filename, "w")
outfile.write("# x and y coordinates\n")
numpy.savetxt(outfile, data, fmt="%10.5f")
