#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""PDFCopy."""
from PyPDF2 import PdfReader, PdfWriter

with open("diveintopython.pdf", "rb", encoding="utf-8") as infile:
    reader = PdfReader(infile)
    outfile = PdfWriter()
    outfile.add_blank_page(612, 792)
    p = reader.pages[0]
    outfile.add_page(p)
    with open("myPdf.pdf", "wb") as f:
        outfile.write(f)
