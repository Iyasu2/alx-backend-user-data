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
    return re.sub(separator.join(fields), redaction, message)
