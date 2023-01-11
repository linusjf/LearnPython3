#!/usr/bin/env python
"""
######################################################################
# @author      : Linus Fernandes (linusfernandes at gmail dot com)
# @file        : app
# @created     : Tuesday Jan 10, 2023 17:54:10 IST
# @description : App to run rest api server
# -*- coding: utf-8 -*-'
######################################################################
"""

from flask import Flask, abort, jsonify, make_response

app = Flask(__name__)

users = [{
    'id': 1,
    'username': 'linus',
    'email': 'linus@xyz.com',
    'active': True
}, {
    'id': 2,
    'username': 'python',
    'email': 'py@py.org',
    'active': False
}]


@app.route('/v1/users/', methods=['GET'])
def get_users():
    """Get users"""
    return jsonify({'users': users})


@app.errorhandler(404)
def not_found(error):
    """Not found"""
    return make_response(jsonify({'error': 'Not found: ' + str(error)}), 404)


@app.route('/v1/users/<int:u_id>/', methods=['GET'])
def get_user(u_id):
    """Get user"""
    for user in users:
        if user.get("id") == u_id:
            return jsonify({'users': user})
    return abort(404)


if __name__ == '__main__':
    app.run(debug=True)
