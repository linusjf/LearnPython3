#!/usr/bin/env python
# -*- coding: utf-8 -*-
from PyPDF2 import PdfReader, PdfMerger
import os
merger = PdfMerger()
files = [x for x in os.listdir('.') if x.endswith('.pdf')]
for fname in sorted(files):
    merger.append(PdfReader(open(
        os.path.join('.', fname), 'rb')))
merger.write("output.pdf")
