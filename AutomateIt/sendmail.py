#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""SendMail."""

import smtplib
import config

server = smtplib.SMTP("smtp.gmail.com", 587)
server.starttls()
server.login(config.fromaddr, config.password)
MSG = "Some nice msg"
server.sendmail(config.fromaddr, config.toaddr, MSG)
server.quit()
