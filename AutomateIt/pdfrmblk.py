#!/usr/bin/env python
# -*- coding: utf-8 -*-

from PyPDF2 import PdfReader, PdfWriter

infile = PdfReader("myPdf.pdf", "rb")
output = PdfWriter()
for i in range(len(infile.pages)):
    p = infile.pages[i]
    if p.get_contents():
        output.add_page(p)
with open("myPdf_wo_blank.pdf", "wb") as f:
    output.write(f)
