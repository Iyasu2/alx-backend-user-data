#!/usr/bin/env python3
'''
this is a module
'''
from flask import Flask, jsonify, request, abort, make_response
from api.v1.views import app_views
from models.user import User
from os import getenv
from api.v1.app import auth
from typing import Tuple


@app_views.route('/auth_session/login', methods=['POST'], strict_slashes=False)
def login():
    '''
    a function
    '''
    email = request.form.get('email')
    if not email:
        return jsonify({"error": "email missing"}), 400

    password = request.form.get('password')
    if not password:
        return jsonify({"error": "password missing"}), 400

    users = User.search({'email': email})
    if not users:
        return jsonify({"error": "no user found for this email"}), 404

    for user in users:
        if user.is_valid_password(password):
            session_id = auth.create_session(user.id)
            response = make_response(user.to_json())
            response.set_cookie(getenv('SESSION_NAME'), session_id)
            return response

    return jsonify({"error": "wrong password"}), 401


@app_views.route(
        '/auth_session/logout',
        methods=['DELETE'],
        strict_slashes=False
        )
def logout() -> Tuple[str, int]:
    """Log out"""
    success = auth.destroy_session(request)
    if not success:
        abort(404)
    return jsonify({}), 200
