#!/usr/bin/env python3
'''
this is the module
'''
from api.v1.auth.session_exp_auth import SessionExpAuth
from models.user_session import UserSession


class SessionDBAuth(SessionExpAuth):
    '''
    this is a class
    '''
    def create_session(self, user_id=None):
        '''
        a function
        '''
        session_id = super().create_session(user_id)
        if session_id is None:
            return None
        user_session = UserSession(user_id=user_id, session_id=session_id)
        user_session.save()
        return session_id

    def user_id_for_session_id(self, session_id=None):
        '''
        a function
        '''
        user_session = UserSession.search({'session_id': session_id})
        if user_session:
            return user_session[0].user_id
        return None

    def destroy_session(self, request=None):
        '''
        a function
        '''
        session_id = self.session_cookie(request)
        if session_id is None:
            return False
        user_session = UserSession.search({'session_id': session_id})
        if user_session:
            user_session[0].remove()
            return True
        return False
