#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
from dotenv import load_dotenv

load_dotenv()

fromaddr = os.getenv('fromaddr')
password = os.getenv('password')
toaddr = os.getenv('toaddr')
