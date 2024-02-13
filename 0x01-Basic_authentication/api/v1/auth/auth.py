#!/usr/bin/env python3
'''
module for api authentication
'''
from flask import request
from typing import List, TypeVar

User = TypeVar('User')


class Auth:
    """
    class auth
    """
    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """ Method to require auth """
        return False

    def authorization_header(self, request=None) -> str:
        """ Method to get authorization header """
        return None

    def current_user(self, request=None) -> User:
        """ Method to get current user """
        return None
