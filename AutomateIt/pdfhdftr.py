#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""PDFHeaderFooter."""
from fpdf import FPDF


class PDF(FPDF):
    """PDF Class."""

    def footer(self):
        """Create footer."""
        self.set_y(-15)
        self.set_font("Arial", "I", 8)
        self.cell(0, 10, f"Page {self.page_no()}", 0, 0, "C")

    def header(self):
        """Create header."""
        self.set_font("Arial", "B", 15)
        self.cell(80)
        self.cell(30, 10, "Automate It!", 1, 0, "C")
        self.ln(20)


pdf = PDF(format="A5")
pdf.add_page()
pdf.set_font("Times", size=12)
for i in range(1, 50):
    pdf.cell(0, 10, f"This my new line. Line number is: {i}", ln=1, align="C")
pdf.output("header_footer.pdf")
