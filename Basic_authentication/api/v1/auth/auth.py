#!/usr/bin/env python3
""" Module of Authentication
"""

from typing import List, TypeVar

from flask import request


class Auth:
    """ Class to manage the API authentication """

    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """ Method for validating if endpoint requires auth """
        if path is None or excluded_paths is None or excluded_paths == []:
            return True

        if not path.endswith('/'):
            path = path + '/'

        for excluded_path in excluded_paths:
            if (excluded_path.endswith('*') and
                    path.startswith(excluded_path[:-1])):
                return False
            if path == excluded_path:
                return False
        return True

    def authorization_header(self, request=None) -> str:
        """ Method that handles authorization header """
        if request is None or 'Authorization' not in request.headers:
            return None
        return request.headers['Authorization']

    def current_user(self, request=None) -> TypeVar('User'):
        """A public method current_user"""
        return None
