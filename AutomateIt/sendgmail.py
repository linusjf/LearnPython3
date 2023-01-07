#!/usr/bin/env python

######################################################################
# @author      : Linus Fernandes (linusfernandes at gmail dot com)
# @file        : sendgmail
# @created     : Saturday Jan 07, 2023 15:22:15 IST
# @description :
# -*- coding: utf-8 -*-'
######################################################################
from simplegmail import Gmail
import config

gmail = Gmail(
    "client_secret.json"
)  # will open a browser window to ask you to log in and authenticate

params = {
    "to": config.toaddr,
    "sender": config.fromaddr,
    "subject": "My first email",
    "msg_html": "<h1>Woah, my first email!</h1><br />This is an HTML email.",
    "msg_plain": "Hi\nThis is a plain text email.",
    "signature": True  # use my account signature
}
message = gmail.send_message(**params)  #
