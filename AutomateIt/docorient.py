#!/usr/bin/env python
# -*- coding: utf-8 -*-

from docx import Document

employee_data = [
    {"id": 123, "name": "John Sally", "department": "Operations", "isDue": True},
    {"id": 245, "name": "Robert Langford", "department": "Software", "isDue": False},
    {"id": 300, "name": "Nancy Lord", "department": "Software", "isDue": True},
]
agenda = {
    "Operations": ["SAP Overview", "Inventory Management"],
    "Software": ["C/C++ Overview", "Computer Architecture"],
    "Hardware": ["Computer Aided Tools", "Hardware Design"],
}


def generate_document(employee_data, agenda):
    for emp in employee_data:
        if emp["isDue"]:
            document = Document()
            name = emp["name"]
            document.add_heading("Your New Hire Orientationn", level=1)
            document.add_paragraph("Dear %s," % name)
            document.add_paragraph(
                "Welcome to Google Inc. You have been selected for our new hire orientation."
            )
            document.add_paragraph("Based on your department you will go through below sessions:")
            department = emp["department"]
            for session in agenda[department]:
                document.add_paragraph(session, style="List Bullet")
            document.add_paragraph("Thanks,n HR Manager")
            document.save("orientation_%s.docx" % emp["id"])


generate_document(employee_data, agenda)
