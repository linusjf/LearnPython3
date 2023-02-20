#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Configuration setup."""
import os
from dotenv import load_dotenv

load_dotenv()

fromaddr = os.getenv("fromaddr")
password = os.getenv("password")
toaddr = os.getenv("toaddr")
serviceaccount = os.getenv("serviceaccount")
twitterapikey = os.getenv("TWITTER_API_KEY")
twitterapikeysecret = os.getenv("TWITTER_API_KEY_SECRET")
twitterbearertoken = os.getenv("TWITTER_BEARER_TOKEN")
