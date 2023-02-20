#!/usr/bin/env python
"""
LookupBookmarks.

######################################################################
# @author      : Linus Fernandes (linusfernandes at gmail dot com)
# @file        : lookupbookmarks
# @created     : Friday Jan 13, 2023 09:50:41 IST
# @description :
# -*- coding: utf-8 -*-'
######################################################################
"""
import base64
import hashlib
import json
import os
import re

import requests
from requests_oauthlib import OAuth2Session

import config

# First, you will need to enable OAuth 2.0 in your App’s auth settings
# in the Developer Portal to get your client ID.
# Inside your terminal you will need to set an enviornment variable
# export CLIENT_ID='your-client-id'
client_id = config.twitterapikey

# If you have selected a type of App that is a confidential client you will
# need
# to set a client secret.
# Confidential Clients securely authenticate with the authorization server.

# Inside your terminal you will need to set an enviornment variable
# export CLIENT_SECRET='your-client-secret'

# Remove the comment on the following line if you are using a
# confidential client
client_secret = config.twitterapikeysecret

# Replace the following URL with your callback URL, which can be
# obtained from your App's auth settings.
REDIRECT_URI = "https://linusfernandes.com"

# Set the scopes
scopes = ["bookmark.read", "tweet.read", "users.read", "offline.access"]

# Create a code verifier
code_verifier = base64.urlsafe_b64encode(os.urandom(30)).decode("utf-8")
code_verifier = re.sub("[^a-zA-Z0-9]+", "", code_verifier)

# Create a code challenge
CODE_CHALLENGE = hashlib.sha256(code_verifier.encode("utf-8")).digest()
CODE_CHALLENGE = base64.urlsafe_b64encode(CODE_CHALLENGE).decode("utf-8")
CODE_CHALLENGE = CODE_CHALLENGE.replace("=", "")

# Start an OAuth 2.0 session
oauth = OAuth2Session(client_id, redirect_uri=REDIRECT_URI, scope=scopes)

# Create an authorize URL
AUTH_URL = "https://twitter.com/i/oauth2/authorize"
authorization_url, state = oauth.authorization_url(
    AUTH_URL, code_challenge=CODE_CHALLENGE, code_challenge_method="S256"
)

# Visit the URL to authorize your App to make requests on behalf of a user
print(
    "Visit the following URL to authorize your App\
            on behalf of your Twitter handle in a browser:"
)
print(authorization_url)

# Paste in your authorize URL to complete the request
authorization_response = input("Paste in the full URL after you've\
        authorized your App:\n")

# Fetch your access token
TOKEN_URL = "https://api.twitter.com/2/oauth2/token"

# The following line of code will only work if you are using
# a type of App that is a public client
AUTH = False

# If you are using a confidential client you will need to pass
# in basic encoding of your client ID and client secret.

# Please remove the comment on the following line
# if you are using a type of App that is a confidential client
# auth = HTTPBasicAuth(client_id, client_secret)

token = oauth.fetch_token(
    token_url=TOKEN_URL,
    authorization_response=authorization_response,
    auth=AUTH,
    client_id=client_id,
    include_client_id=True,
    code_verifier=code_verifier,
)

# Your access token
access = token["access_token"]

# Make a request to the users/me endpoint to get your user ID
user_me = requests.request(
    "GET",
    "https://api.twitter.com/2/users/me",
    headers={"Authorization": f"Bearer {access}"},
    timeout=10,
).json()
user_id = user_me["data"]["id"]

# Make a request to the bookmarks url
url = f"https://api.twitter.com/2/users/{user_id}/bookmarks"
headers = {
    "Authorization": f"Bearer {access}",
    "User-Agent": "BookmarksSampleCode",
}
response = requests.request("GET", url, headers=headers, timeout=10)
if response.status_code != 200:
    raise Exception(f"Request returned an error:\
            {response.status_code} {response.text}")
print(f"Response code: {response.status_code}")
json_response = response.json()
print(json.dumps(json_response, indent=4, sort_keys=True))
