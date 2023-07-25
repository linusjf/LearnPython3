#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""PDFCopy."""
from pypdf import PdfReader, PdfWriter

with open("diveintopython.pdf", "rb") as infile:
    reader = PdfReader(infile)
    outfile = PdfWriter()
    outfile.add_blank_page(612, 792)
    PAGE = reader.pages[0]
    outfile.add_page(PAGE)
    with open("myPdf.pdf", "wb") as f:
        outfile.write(f)
