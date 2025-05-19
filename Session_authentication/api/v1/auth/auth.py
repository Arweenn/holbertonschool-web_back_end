#!/usr/bin/env python3
""" Module of Authentication
"""
import os
from typing import List, TypeVar

from flask import request


class Auth:
    """ Class to manage the API authentication """

    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """ Method for requiring authentication """
        if path is None or excluded_paths is None or not len(excluded_paths):
            return True
        if path[-1] != '/':
            path += '/'
        if excluded_paths[-1] != '/':
            excluded_paths += '/'
        if path in excluded_paths:
            return False
        return True

    def authorization_header(self, request=None) -> str:
        """ Method that handles authorization header """
        if request is None:
            return None

        return request.headers.get("Authorization", None)

    def current_user(self, request=None) -> TypeVar('User'):
        """ Validates current user """
        return None

    def session_cookie(self, request=None):
        """Session cookie"""
        if request is None:
            return None
        session = os.getenv("SESSION_NAME")
        _my_session_id = request.cookies.get(session)
        return _my_session_id
