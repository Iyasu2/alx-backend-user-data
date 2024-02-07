#!/usr/bin/env python3
'''
this is a module
'''
import re
from typing import List


def filter_datum(
        fields: List[str],
        redaction: str,
        message: str,
        separator: str) -> str:
    '''
    this is a function
    '''
    pattern = separator.join(
            [f"{field}=.*?{separator}" for field in fields]
            )
    return re.sub(
            pattern,
            lambda match: match.group().replace(
                match.group().split('=')[1].rstrip(separator),
                redaction), message
            )
