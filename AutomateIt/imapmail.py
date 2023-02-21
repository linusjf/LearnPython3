#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Imapmail."""
import imaplib
import config

M = imaplib.IMAP4_SSL("imap.gmail.com", 993)
if config.fromaddr and config.password:
    M.login(config.fromaddr, config.password)
    print(M.list())
    M.select("INBOX")
    print("Inbox:", M)
    typ, data = M.search(None, "SUBJECT", '"Email with an attachment"')
    print(typ)
    print(data)
    if data[0] != b"":
        typs, msg = M.fetch(data[0].split()[-1], "(RFC822)")
        if msg and msg[0]:
            print("Message is ", msg[0][1])
    M.close()
    M.logout()
