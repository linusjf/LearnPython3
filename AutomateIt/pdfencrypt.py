#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""PDFEncrypt."""
from pypdf import PdfWriter, PdfReader

with open("diveintopython.pdf", "rb") as fp:
    reader = PdfReader(fp)
    writer = PdfWriter()
    for _, page in enumerate(reader.pages):
        writer.add_page(page)
    writer.encrypt("P@$$w0rd")
    with open("EncryptExercise.pdf", "wb") as newfp:
        writer.write(newfp)
