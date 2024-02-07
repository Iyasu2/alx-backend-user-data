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


def is_valid(hashed_password: bytes, password: str) -> bool:
    '''
    a function
    '''
    return bcrypt.checkpw(password.encode(), hashed_password)
