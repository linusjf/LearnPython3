#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""PDFEncrypt."""
from PyPDF2 import PdfWriter, PdfReader

with open("diveintopython.pdf", "rb", encoding="utf-8") as fp:
    reader = PdfReader(fp)
    writer = PdfWriter()
    for _, page in enumerate(reader.pages):
        writer.add_page(page)
    writer.encrypt("P@$$w0rd")
    with open("EncryptExercise.pdf", "wb", encoding="utf-8") as newfp:
        writer.write(newfp)
