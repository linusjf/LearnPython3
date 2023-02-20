#!/usr/bin/env python
"""CreateDraft."""
######################################################################
# @author      : Linus Fernandes (linusfernandes at gmail dot com)
# @file        : createdraft
# @created     : Saturday Jan 07, 2023 16:19:36 IST
# @description :
# -*- coding: utf-8 -*-'
######################################################################
from __future__ import print_function

import base64
from email.message import EmailMessage

import google.auth
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
import config


def gmail_create_draft():
    """
    Create and insert a draft email.

    Print the returned draft's message and id.
    Returns: Draft object, including draft id and message meta data.

    Load pre-authorized user credentials from the environment.
    TODO(developer) - See https://developers.google.com/identity
    for guides on implementing OAuth2 for the application.
    """
    creds, _ = google.auth.default()

    try:
        # create gmail api client
        service = build("gmail", "v1", credentials=creds)

        message = EmailMessage()

        message.set_content("This is automated draft mail")

        message["To"] = config.toaddr
        message["From"] = config.fromaddr
        message["Subject"] = "Automated draft"

        # encoded message
        encoded_message = base64.urlsafe_b64encode(message.as_bytes()).decode()

        create_message = {"message": {"raw": encoded_message}}
        # pylint: disable=no-member
        draft = service.users().drafts().create(userId="me", body=create_message).execute()  # noqa

        print(f'Draft id: {draft["id"]}\nDraft message: {draft["message"]}')

    except HttpError as error:
        print(f"An error occurred: {error}")
        draft = None

    return draft


if __name__ == "__main__":
    gmail_create_draft()
