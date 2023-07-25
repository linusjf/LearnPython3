#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""PDFMeta."""
from pypdf import PdfMerger, PdfReader

merger = PdfMerger()
with open("myPdf.pdf", "wb") as fp:
    metadata = {
        "/edited": "ByPdfMerger",
    }
    merger.add_metadata(metadata)
    merger.write(fp)
with open("myPdf.pdf", "rb") as pdf:
    reader = PdfReader(pdf)
    print("Document Info:", reader.metadata)
