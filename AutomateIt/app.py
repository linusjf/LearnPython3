#!/usr/bin/env python

"""
######################################################################
# @author      : Linus Fernandes (linusfernandes at gmail dot com)
# @file        : app
# @created     : Tuesday Jan 10, 2023 17:54:10 IST
# @description : 
# -*- coding: utf-8 -*-'
######################################################################
"""
from flask import Flask
app = Flask(__name__)
@app.route('/')
def index():
    return "Hello, Python!"
if __name__ == '__main__':
    app.run(debug=True)
