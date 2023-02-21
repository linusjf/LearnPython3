#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""SendMail."""

import smtplib
import config

server = smtplib.SMTP("smtp.gmail.com", 587)
server.starttls()
if config.fromaddr and config.password:
    server.login(config.fromaddr, config.password)
    MSG = "Some nice msg"
    if config.fromaddr and config.toaddr:
        server.sendmail(config.fromaddr, config.toaddr, MSG)
server.quit()
