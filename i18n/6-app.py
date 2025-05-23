#!/usr/bin/env python3
"""
Flask app
"""
from flask import Flask, render_template, request, g
from flask_babel import Babel


class Config:
    """
    Config class
    """
    LANGUAGES = ['en', 'fr']


app = Flask(__name__)
app.url_map.strict_slashes = False
app.config.from_object(Config)

babel = Babel(app)
Babel.default_locale = 'en'
Babel.default_timezone = 'UTC'

users = {
    1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
    2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
    3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
    4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"},
}


@app.route('/', methods=['GET'])
def hello():
    """ GET /
    Return:
      - Render template
    """
    return render_template('6-index.html', user=g.user)


@babel.localeselector
def get_locale():
    """
    Get locale from request
    """
    locale = request.args.get('locale')
    if locale in Config.LANGUAGES:
        return locale
    user = request.args.get('login_as')
    if user:
        locale = get_user(user).get('locale')
        if locale in Config.LANGUAGES:
            return locale
    header = request.headers.get('locale')
    if header:
        return header
    return request.accept_languages.best_match(Config.LANGUAGES)


def get_user(user):
    """
    Get user from request
    """
    if user and int(user) in users:
        return users.get(int(user))


@app.before_request
def before_request():
    """
    Get user, if any
    """
    g.user = get_user(request.args.get('login_as'))


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")
