#!/usr/bin/env python
# -*- coding: utf-8 -*-
import config, imaplib
M = imaplib.IMAP4_SSL("imap.gmail.com", 993)
M.login(config.fromaddr, config.password)
print(M.list())
M.select('INBOX')
print("Inbox:", M)
M.logout()
