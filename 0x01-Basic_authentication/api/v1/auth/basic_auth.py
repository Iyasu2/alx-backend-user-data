#!/usr/bin/env python3
'''
this is the module
'''
from api.v1.auth.auth import Auth
import base64


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

    def decode_base64_authorization_header(
            self,
            base64_authorization_header: str
            ) -> str:
        """ Method to decode the Base64 Authorization header """
        if base64_authorization_header is None:
            return None
        if type(base64_authorization_header) is not str:
            return None
        try:
            base64_bytes = base64_authorization_header.encode('utf-8')
            message_bytes = base64.b64decode(base64_bytes)
            return message_bytes.decode('utf-8')
        except Exception:
            return None

    def extract_user_credentials(
            self,
            decoded_base64_authorization_header: str
            ) -> (str, str):
        """ Method to extract the user credentials """
        if decoded_base64_authorization_header is None:
            return None, None
        if type(decoded_base64_authorization_header) is not str:
            return None, None
        if ':' not in decoded_base64_authorization_header:
            return None, None

        credentials = decoded_base64_authorization_header.split(':')
        return credentials[0], credentials[1]
