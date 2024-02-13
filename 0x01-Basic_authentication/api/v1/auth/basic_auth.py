#!/usr/bin/env python3
'''
this is the module
'''
from api.v1.auth.auth import Auth
import base64
from typing import TypeVar
from models.user import User


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

        credentials = decoded_base64_authorization_header.split(':', 1)
        return credentials[0], credentials[1]

    def user_object_from_credentials(
            self,
            user_email: str,
            user_pwd: str
            ) -> TypeVar('User'):
        """ Method to get the User instance based on email and password """
        if type(user_email) == str and type(user_pwd) == str:
            try:
                users = User.search({'email': user_email})
            except Exception:
                return None
            if len(users) <= 0:
                return None
            if users[0].is_valid_password(user_pwd):
                return users[0]
        return None

    def current_user(self, request=None) -> TypeVar('User'):
        """ Method to get the current User instance based on the request """
        if request is None:
            return None

        authorization_header = self.authorization_header(request)
        base64_authorization_header = \
            self.extract_base64_authorization_header(authorization_header)
        decoded_base64_authorization_header = \
            self.decode_base64_authorization_header(
                    base64_authorization_header
                    )
        user_email, user_pwd = \
            self.extract_user_credentials(
                    decoded_base64_authorization_header
                    )

        return self.user_object_from_credentials(user_email, user_pwd)
