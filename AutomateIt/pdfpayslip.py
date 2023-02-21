#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""PDFPaySlip."""
from datetime import datetime
from fpdf import FPDF, HTMLMixin
from fpdf.enums import XPos, YPos, Align

employee_data = [
    {"id": 123, "name": "John Sally", "payment": 10000, "tax": 3000, "total": 7000},
    {"id": 245, "name": "Robert Langford", "payment": 12000, "tax": 4000, "total": 8000},
]


class PaySlip(FPDF, HTMLMixin):
    """PaySlip."""

    def footer(self):
        """Draw footer."""
        self.set_y(-15)
        self.set_font("Courier", "I", 8)
        self.cell(0, 10, f"Page {self.page_no()}", 0, new_x=XPos.RIGHT, new_y=YPos.TOP, align="C")

    def header(self):
        """Draw header."""
        self.set_font("Courier", "B", 15)
        self.cell(80)
        self.cell(30, 10, "Google", 0, new_x=XPos.RIGHT, new_y=YPos.TOP, align=Align.C)
        self.ln(20)


def generate_payslip(data):
    """Generate payslip."""
    month = datetime.now().strftime("%B")
    year = datetime.now().strftime("%Y")
    pdf = PaySlip(format="letter")
    pdf.add_page()
    pdf.set_font("Times", size=12)
    pdf.cell(200, 10, txt=f"Pay Slip for {month}, {year}", align=Align.C)
    pdf.cell(50)
    pdf.cell(
        100,
        10,
        txt=f"Employeed Id: {data['id']}",
        new_x=XPos.LMARGIN,
        new_y=YPos.NEXT,
        align="L",
    )
    pdf.cell(50)
    pdf.cell(100, 10, txt=f"Employee Name: {data['name']}", align="L")
    html = (
        """
<table border="0" align="center" width="50%">
<thead><tr><th align="left" width="50%">
Pay Slip Details</th><th align="right" width="50%">
Amount in USD</th></tr></thead>
<tbody>
<tr><td>Payments</td><td align="right">"""
        + str(data["payment"])
        + """</td></tr>
<tr><td>Tax</td><td align="right">"""
        + str(data["tax"])
        + """</td></tr>
<tr><td>Total</td><td align="right">"""
        + str(data["total"])
        + """</td></tr>
</tbody>
</table>
"""
    )
    pdf.write_html(html)
    pdf.output("payslip_{data['id']}.pdf")


for emp in employee_data:
    generate_payslip(emp)
