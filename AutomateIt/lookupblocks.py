#!/usr/bin/env python
"""
######################################################################
# @author      : Linus Fernandes (linusfernandes at gmail dot com)
# @file        : lookupblocks
# @created     : Thursday Jan 12, 2023 19:35:17 IST
# @description :
# -*- coding: utf-8 -*-'
######################################################################
"""
import json

from requests_oauthlib import OAuth1Session

import config

consumer_key = config.twitterapikey
consumer_secret = config.twitterapikeysecret
params = {"user.fields": "created_at,description"}
# User fields are adjustable, options include:
# created_at, description, entities, id, location, name,
# pinned_tweet_id, profile_image_url, protected,
# public_metrics, url, username, verified, and withheld

REQUEST_TOKEN_URL = "https://api.twitter.com/oauth/request_token"
oauth = OAuth1Session(consumer_key, client_secret=consumer_secret)

try:
    fetch_response = oauth.fetch_request_token(REQUEST_TOKEN_URL)
except ValueError:
    print("There may have been an issue with the consumer_key or consumer_secret you entered.")

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

# Make the request
oauth = OAuth1Session(
    consumer_key,
    client_secret=consumer_secret,
    resource_owner_key=access_token,
    resource_owner_secret=access_token_secret,
)

response = oauth.get("https://api.twitter.com/2/users/me", params=params)

if response.status_code != 200:
    raise Exception(f"Request returned an error: {response.status_code} {response.text}")

print(f"Response code: {response.status_code}")

json_response = response.json()

print(json.dumps(json_response, indent=4, sort_keys=True))

# Be sure to replace your-user-id with your own user ID or one of an authenticating user
# You can find a user ID by using the user lookup endpoint
TWIT_ID = json_response["data"]["id"]
response = oauth.get(f"https://api.twitter.com/2/users/{TWIT_ID}/blocking", params=params)

if response.status_code != 200:
    raise Exception(f"Request returned an error: {response.status_code} {response.text}")

print("Response code: {response.status_code}")
json_response = response.json()
print(json.dumps(json_response, indent=4, sort_keys=True))
