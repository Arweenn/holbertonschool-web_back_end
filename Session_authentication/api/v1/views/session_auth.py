#!/usr/bin/env python3
"""
Route module for the API
"""
from os import getenv

from api.v1.views import app_views
from flask import Flask, abort, jsonify, request
from flask_cors import CORS

app = Flask(__name__)
app.config['JSONIFY_PRETTYPRINT_REGULAR'] = True
app.register_blueprint(app_views)
CORS(app, resources={r"/api/v1/*": {"origins": "*"}})
auth = None
AUTH_TYPE = getenv("AUTH_TYPE")

if AUTH_TYPE == "auth":
    from api.v1.auth.auth import Auth
    auth = Auth()
elif AUTH_TYPE == "basic_auth":
    from api.v1.auth.basic_auth import BasicAuth
    auth = BasicAuth()
elif AUTH_TYPE == "session_auth":
    from api.v1.auth.session_auth import SessionAuth
    auth = SessionAuth()


@app.errorhandler(401)
def unauthorized_error(error) -> str:
    """ Unauthorized handler
    """
    return jsonify({"error": "Unauthorized"}), 401


@app.errorhandler(403)
def forbidden_error(error) -> str:
    """ Forbidden handler
    """
    return jsonify({"error": "Forbidden"}), 403


@app.errorhandler(404)
def not_found(error) -> str:
    """ Not found handler
    """
    return jsonify({"error": "Not found"}), 404


@app.before_request
def before_request() -> str:
    """ Before Request Handler
    Requests Validation
    """
    if auth is None:
        return

    excluded_paths = ['/api/v1/status/',
                      '/api/v1/unauthorized/',
                      '/api/v1/forbidden/',
                      '/api/v1/auth_session/login/']

    if not auth.require_auth(request.path, excluded_paths):
        return

    if auth.authorization_header(request) is None \
            and auth.session_cookie(request) is None:
        abort(401)

    # if auth.current_user(request) is None:
    current_user = auth.current_user(request)
    if current_user is None:
        abort(403)

    request.current_user = current_user


if __name__ == "__main__":
    host = getenv("API_HOST", "0.0.0.0")
    port = getenv("API_PORT", "5000")
    app.run(host=host, port=port)


@app.errorhandler(404)
def not_found(error) -> str:
    """ Not found handler
    """
    return jsonify({"error": "Not found"}), 404


@app.errorhandler(401)
def unauthorized(error) -> str:
    """Error handler: Unauthorized"""
    return jsonify({"error": "Unauthorized"}), 401


@app.errorhandler(403)
def forbidden(error) -> str:
    """Error handler: Forbidden"""
    return jsonify({"error": "Forbidden"}), 403


@app.before_request
def before_request():
    """
        before request blueprint handler
    """
    unauthorized = [
        '/api/v1/status/',
        '/api/v1/unauthorized/',
        '/api/v1/forbidden/',
        '/api/v1/auth_session/login/',
        '/api/v1/auth_session/login/'
    ]
    if not auth:
        return
    if not auth.require_auth(request.path, unauthorized):
        return

    if (auth.authorization_header(request) is None
            and auth.session_cookie(request) is None):
        abort(401)

    elif auth.current_user(request) is None:
        abort(403)
    else:
        request.current_user = auth.current_user(request)

    if (auth.authorization_header(request) is None
            and auth.session_cookie(request) is None):
        abort(401)


if __name__ == "__main__":
    host = getenv("API_HOST", "0.0.0.0")
    port = getenv("API_PORT", "5000")
    app.run(host=host, port=port)
