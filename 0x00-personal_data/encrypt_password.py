#!/usr/bin/env python3
'''
this is a module
'''
import bcrypt


def hash_password(password: str) -> bytes:
    '''
    hashing function
    '''
    salt = bcrypt.gensalt()
    hashed = bcrypt.hashpw(password.encode(), salt)
    return hashed
