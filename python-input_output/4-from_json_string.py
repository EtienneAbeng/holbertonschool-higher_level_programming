#!/usr/bin/python3
"""
    Function that convert JSON to objct
"""
import json


def from_json_string(my_str):
    """my_str:  the string to be converted"""
    return json.loads(my_str)
