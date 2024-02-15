#!/usr/bin/env python3
'''
this is the module
'''
from api.v1.auth.session_auth import SessionAuth
from os import getenv
from datetime import datetime, timedelta


class SessionExpAuth(SessionAuth):
    '''
    a class
    '''
    def __init__(self) -> None:
        self.session_duration = int(getenv("SESSION_DURATION", 0))

    def create_session(self, user_id=None):
        '''
        a function
        '''
        session_id = super().create_session(user_id)
        if session_id is None:
            return None
        self.user_id_by_session_id[session_id] = {
            'user_id': user_id,
            'created_at': datetime.now()
        }
        return session_id

    def user_id_for_session_id(self, session_id=None):
        '''
        a function
        '''
        if session_id is None:
            return None
        session_dict = self.user_id_by_session_id.get(session_id)
        if session_dict is None:
            return None
        user_id = session_dict.get('user_id')
        if self.session_duration <= 0:
            return user_id
        created_at = session_dict.get('created_at')
        if created_at is None:
            return None
        if datetime.now() > created_at + timedelta(seconds=self.session_duration):
            return None
        return user_id
