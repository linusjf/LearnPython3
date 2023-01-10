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

from flask import Flask, jsonify
app = Flask(__name__)
 
users = [
 {
 'id': 1,
 'username': u'cjgiridhar',
 'email': u'abc@xyz.com',
 'active': True
 },
 {
     'id': 2,
     'username': u'python',
     'email': u'py@py.org',
     'active': False
 }
]
@app.route('/v1/users/', methods=['GET'])
def get_users():
     return jsonify({'users': users})
if __name__ == '__main__':
     app.run(debug=True)
