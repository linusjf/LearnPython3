#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""PDFCreate."""
from fpdf import FPDF

pdf = FPDF(format="letter")
pdf.add_page()
pdf.set_font("Arial", size=12)
pdf.cell(200, 10, txt="Welcome to Automate It!", ln=1, align="C")
pdf.cell(200, 10, "Created by Linus", 0, 1, "C")
pdf.output("automateit.pdf")
