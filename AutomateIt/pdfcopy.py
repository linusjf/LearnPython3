#!/usr/bin/env python
# -*- coding: utf-8 -*-
from PyPDF2 import PdfReader, PdfWriter

infile = PdfReader(open("diveintopython.pdf", "rb"))
outfile = PdfWriter()
outfile.add_blank_page(612, 792)
p = infile.pages[0]
outfile.add_page(p)
with open("myPdf.pdf", "wb") as f:
    outfile.write(f)
f.close()
