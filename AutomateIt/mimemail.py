#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""MimeMail."""
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import email.utils
import config

fromaddr = config.fromaddr
toaddr = config.toaddr
msg = MIMEMultipart()
msg["Subject"] = "Hello from the Reader of Automate It!"
msg["To"] = email.utils.formataddr(("Recipient", toaddr))
msg["From"] = email.utils.formataddr(("Author", fromaddr))
BODY = "What a wonderful world!"
msg_body = MIMEText(BODY, "plain")
msg.attach(msg_body)
server = smtplib.SMTP("smtp.gmail.com", 587)
server.starttls()
server.login(fromaddr, config.password)
text = msg.as_string()
print("Text is:", text)
server.sendmail(fromaddr, toaddr, text)
server.quit()
