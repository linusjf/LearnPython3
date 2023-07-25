#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""PDFMerge."""
import os
from pypdf import PdfReader, PdfMerger

merger = PdfMerger()
files = [x for x in os.listdir(".") if x.endswith(".pdf")]
for fname in sorted(files):
    with open(os.path.join(".", fname), "rb") as f:
        merger.append(PdfReader(f))
merger.write("output.pdf")
