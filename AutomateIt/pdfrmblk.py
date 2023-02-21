#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""PDFRmBlk."""

from PyPDF2 import PdfReader, PdfWriter

infile = PdfReader("myPdf.pdf")
output = PdfWriter()
for _, p in enumerate(infile.pages):
    if p.get_contents():
        output.add_page(p)
with open("myPdf_wo_blank.pdf", "wb") as f:
    output.write(f)
