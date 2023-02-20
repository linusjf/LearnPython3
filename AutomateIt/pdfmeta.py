#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""PDFMeta."""
from PyPDF2 import PdfMerger, PdfReader

merger = PdfMerger()
with open("myPdf.pdf", "wb", encoding="utf-8") as fp:
    metadata = {
        "/edited": "ByPdfMerger",
    }
merger.add_metadata(metadata)
merger.write(fp)
fp.close()
with open("myPdf.pdf", "rb", encoding="utf-8") as pdf:
    reader = PdfReader(pdf)
    print("Document Info:", reader.metadata)
