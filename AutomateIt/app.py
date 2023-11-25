#!/usr/bin/env python
"""
App.

######################################################################
# @author      : Linus Fernandes (linusfernandes at gmail dot com)
# @file        : app
# @created     : Tuesday Jan 10, 2023 17:54:10 IST
# @description : App to run rest api server
# -*- coding: utf-8 -*-'
######################################################################
"""

import os

from flask import Flask, abort, jsonify, make_response, request

app = Flask(__name__)

users = [
    {"id": 1, "username": "linus", "email": "linus@xyz.com", "active": True},
    {"id": 2, "username": "python", "email": "py@py.org", "active": False},
]


@app.route("/v1/users/", methods=["GET"])
def get_users():
    """Get users."""
    return jsonify({"users": users})


@app.errorhandler(404)
def not_found(error):
    """Not found."""
    return make_response(jsonify({"error": "Not found: " + str(error)}), 404)


@app.route("/v1/users/<int:u_id>/", methods=["GET"])
def get_user(u_id):
    """Get user."""
    for user in users:
        if user.get("id") == u_id:
            return jsonify({"user": user})
    return abort(404)


@app.route("/v1/users/", methods=["POST"])
def create_user():
    """Create user."""
    if not request.json or "email" not in request.json:
        abort(404)
    user_id = int(users[-1].get("id")) + 1
    username = request.json.get("username")
    email = request.json.get("email")
    status = False
    user = {"id": user_id, "email": email, "username": username, "active": status}
    users.append(user)
    return jsonify({"user": user}), 201


@app.route("/v1/users/<int:u_id>/", methods=["PUT"])
def update_user(u_id):
    """Update user."""
    user = [user for user in users if user["id"] == u_id]
    user[0]["username"] = request.json.get("username", user[0]["username"])
    user[0]["email"] = request.json.get("email", user[0]["email"])
    user[0]["active"] = request.json.get("active", user[0]["active"])
    return jsonify({"user": user[0]})


@app.route("/v1/users/<int:u_id>/", methods=["DELETE"])
def delete_user(u_id):
    """Delete user."""
    user = [user for user in users if user["id"] == u_id]
    users.remove(user[0])
    return jsonify({}), 204


def write_pid_file():
    """Write pid file."""
    pid = str(os.getpid())
    with open("app.pid", "w", encoding="utf-8") as pid_file:
        pid_file.write(pid)


if __name__ == "__main__":
    write_pid_file()
    app.run(debug=False, use_debugger=False, use_reloader=False)  # nosec
