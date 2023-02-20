#!/usr/bin/env python
"""
######################################################################
# @author      : Linus Fernandes (linusfernandes at gmail dot com)
# @file        : gettweets
# @created     : Thursday Jan 12, 2023 18:58:56 IST
# @description :
# -*- coding: utf-8 -*-'
######################################################################
"""
import json
import requests
import config

bearer_token = config.twitterbearertoken


def create_url():
    """create url"""
    tweet_fields = "tweet.fields=lang,author_id"
    # Tweet fields are adjustable.
    # Options include:
    # attachments, author_id, context_annotations,
    # conversation_id, created_at, entities, geo, id,
    # in_reply_to_user_id, lang, non_public_metrics, organic_metrics,
    # possibly_sensitive, promoted_metrics, public_metrics, referenced_tweets,
    # source, text, and withheld
    ids = "ids=1278747501642657792,1255542774432063488,1613516569828630529,1570685356110147585"
    # You can adjust ids to include a single Tweets.
    # Or you can add to up to 100 comma-separated IDs
    url = f"https://api.twitter.com/2/tweets?{ids}&{tweet_fields}"
    return url


def bearer_oauth(request):
    """
    Method required by bearer token authentication.
    """

    request.headers["Authorization"] = f"Bearer {bearer_token}"
    request.headers["User-Agent"] = "v2TweetLookupPython"
    return request


def connect_to_endpoint(url):
    """connect to endpoint"""
    response = requests.request("GET", url, auth=bearer_oauth, timeout=10)
    print(response.status_code)
    if response.status_code != 200:
        raise Exception(f"Request returned an error: {response.status_code} {response.text}")
    return response.json()


def main():
    """main"""
    url = create_url()
    json_response = connect_to_endpoint(url)
    print(json.dumps(json_response, indent=4, sort_keys=True))


if __name__ == "__main__":
    main()
