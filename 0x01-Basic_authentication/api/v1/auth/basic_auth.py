#!/usr/bin/env python3
'''
this is the module
'''
from api.v1.auth.auth import Auth


class BasicAuth(Auth):
    '''
    a class
    '''
    def extract_base64_authorization_header(
            self,
            authorization_header: str
            ) -> str:
        """ Method to extract the Base64 Authorization header """
        if authorization_header is None:
            return None

        if type(authorization_header) is not str:
            return None

        if not authorization_header.startswith('Basic '):
            return None

        return authorization_header.split(" ")[1]
