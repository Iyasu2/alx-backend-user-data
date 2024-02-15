#!/usr/bin/env python3
'''
this is the module
'''
from api.v1.auth.auth import Auth
import base64
from typing import TypeVar
from models.user import User
import uuid


class SessionAuth(Auth):
    '''
    a class
    '''
    user_id_by_session_id = {}

    def create_session(self, user_id: str = None) -> str:
        """Creates a Session ID for a user_id"""
        if user_id is None or not isinstance(user_id, str):
            return None
        else:
            session_id = str(uuid.uuid4())
            self.user_id_by_session_id[session_id] = user_id
            return session_id