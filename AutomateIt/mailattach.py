#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""MailAttach."""
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
import config

fromaddr = config.fromaddr
toaddr = config.toaddr
msg = MIMEMultipart()
msg["From"] = fromaddr
msg["To"] = toaddr
msg["Subject"] = "Email with an attachment"
BODY = "Click to open the attachment"
msg.attach(MIMEText(BODY, "plain"))
FILENAME = "attach.txt"
with open(FILENAME, "rb", encoding="utf-8") as attachment:
    part = MIMEBase("application", "octet-stream")
    part.set_payload((attachment).read())
    encoders.encode_base64(part)
    part.add_header("Content-Disposition", f"attachment; filename= {FILENAME}")
    msg.attach(part)
    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.starttls()
    if fromaddr and config.password:
        server.login(fromaddr, config.password)
        text = msg.as_string()
        server.sendmail(fromaddr, toaddr, text)
    server.quit()
