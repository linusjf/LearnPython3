#!/usr/bin/env python
"""
CreateTweet.

######################################################################
# @author      : Linus Fernandes (linusfernandes at gmail dot com)
# @file        : createtweet
# @created     : Thursday Jan 12, 2023 16:07:44 IST
# @description :
# -*- coding: utf-8 -*-'
######################################################################
"""
import json

from requests_oauthlib import OAuth1Session  # type: ignore

import config

consumer_key = config.twitterapikey
consumer_secret = config.twitterapikeysecret

# Be sure to add replace the text with the text you wish to Tweet.
# You can also add parameters to post polls, quote Tweets,
# Tweet with reply settings,
# and Tweet to Super Followers in addition to other features.
payload = {"text": "Hello world!"}

# Get request token
REQUEST_TOKEN_URL = "https://api.twitter.com/oauth/request_token?\
        oauth_callback=oob&x_auth_access_type=write"  # nosec
oauth = OAuth1Session(consumer_key, client_secret=consumer_secret)

try:
    fetch_response = oauth.fetch_request_token(REQUEST_TOKEN_URL)
except ValueError:
    print(
        "There may have been an issue with the consumer_key or \
            consumer_secret you entered."
    )  # noqa

resource_owner_key = fetch_response.get("oauth_token")
resource_owner_secret = fetch_response.get("oauth_token_secret")
print(f"Got OAuth token: {resource_owner_key}")

# Get authorization
BASE_AUTHORIZATION_URL = "https://api.twitter.com/oauth/authorize"
authorization_url = oauth.authorization_url(BASE_AUTHORIZATION_URL)
print(f"Please go here and authorize: {authorization_url}")
verifier = input("Paste the PIN here: ")

# Get the access token
ACCESS_TOKEN_URL = "https://api.twitter.com/oauth/access_token"  # nosec
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

# Make the request
oauth = OAuth1Session(
    consumer_key,
    client_secret=consumer_secret,
    resource_owner_key=access_token,
    resource_owner_secret=access_token_secret,
)

# Making the request
response = oauth.post(
    "https://api.twitter.com/2/tweets",
    json=payload,
)

if response.status_code != 201:
    raise Exception(f"Request returned an error: {response.status_code} {response.text}")  # noqa

print("Response code: {response.status_code}")

# Saving the response as JSON
json_response = response.json()
print(json.dumps(json_response, indent=4, sort_keys=True))
