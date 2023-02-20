#!/usr/bin/env python
"""
ReadTopTweet.

######################################################################
# @author      : Linus Fernandes (linusfernandes at gmail dot com)
# @file        : readtoptweet
# @created     : Thursday Jan 12, 2023 17:25:11 IST
# @description :
# -*- coding: utf-8 -*-'
######################################################################
"""
from requests_oauthlib import OAuth1Session
import twython
from twython import Twython

import config

consumer_key = config.twitterapikey
consumer_secret = config.twitterapikeysecret

# Get request token
REQUEST_TOKEN_URL = "https://api.twitter.com/oauth/request_token?\
            oauth_callback=oob&x_auth_access_type=write"
oauth = OAuth1Session(consumer_key, client_secret=consumer_secret)

try:
    fetch_response = oauth.fetch_request_token(REQUEST_TOKEN_URL)
except ValueError:
    print(
        "There may have been an\
            issue with the consumer_key or consumer_secret you entered."
    )

resource_owner_key = fetch_response.get("oauth_token")
resource_owner_secret = fetch_response.get("oauth_token_secret")
print(f"Got OAuth token: {resource_owner_key}")

# Get authorization
BASE_AUTHORIZATION_URL = "https://api.twitter.com/oauth/authorize"
authorization_url = oauth.authorization_url(BASE_AUTHORIZATION_URL)
print(f"Please go here and authorize: {authorization_url}")
verifier = input("Paste the PIN here: ")

# Get the access token
ACCESS_TOKEN_URL = "https://api.twitter.com/oauth/access_token"
oauth = OAuth1Session(
    consumer_key,
    client_secret=consumer_secret,
    resource_owner_key=resource_owner_key,
    resource_owner_secret=resource_owner_secret,
    verifier=verifier,
)
oauth_tokens = oauth.fetch_access_token(ACCESS_TOKEN_URL)

access_token = oauth_tokens["oauth_token"]
access_token_secret = oauth_tokens["oauth_token_secret"]
twitter = Twython(consumer_key, consumer_secret, access_token, access_token_secret)
try:
    tweet = twitter.get_home_timeline()[1]
    print("Tweet text: ", tweet["text"])
    print("Tweet created at: ", tweet["created_at"])
    print("Tweeted by: ", tweet["entities"]["user_mentions"][0]["name"])
    print("Re Tweeted?: ", tweet["retweet_count"])
except twython.exceptions.TwythonError as err:
    print(str(err))
