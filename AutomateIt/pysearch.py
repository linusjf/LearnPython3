#!/usr/bin/env python
"""
PySearch.

######################################################################
# @author      : Linus Fernandes (linusfernandes at gmail dot com)
# @file        : pysearch
# @created     : Thursday Jan 12, 2023 21:11:48 IST
# @description :
# -*- coding: utf-8 -*-'
######################################################################
"""
from twython import Twython  # type: ignore

import config

APP_KEY = config.twitterapikey
APP_SECRET = config.twitterapikeysecret

twitter = Twython(APP_KEY, APP_SECRET, oauth_version=1)

auth = twitter.get_authentication_tokens()

print(auth)

OAUTH_TOKEN = auth["oauth_token"]
OAUTH_TOKEN_SECRET = auth["oauth_token_secret"]

auth_url = auth["auth_url"]

print("Use the following url to obtain the oauth_verifier")
print(auth_url)

verifier = input("Enter oauth verifier: ")

twitter = Twython(APP_KEY, APP_SECRET, OAUTH_TOKEN, OAUTH_TOKEN_SECRET)

final_step = twitter.get_authorized_tokens(verifier)

print(final_step)
OAUTH_TOKEN = final_step["oauth_token"]
OAUTH_TOKEN_SECRET = final_step["oauth_token_secret"]

twitter = Twython(APP_KEY, APP_SECRET, OAUTH_TOKEN, OAUTH_TOKEN_SECRET)
twitter.get_home_timeline()
print(twitter.search(q="python"))
