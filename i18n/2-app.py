#!/usr/bin/env python3
"""
Basic Babel setup
"""

from flask import Flask, render_template, request
from flask_babel import Babel

app = Flask(__name__)
babel = Babel(app)


class Config(object):
    """
    Config class for Babel
    """
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app.config.from_object("1-app.Config")


@babel.localeselector
def get_locale():
    """
    Get the current locale
    """
    return request.accept_languages.best_match(app.config["LANGUAGES"])


@app.route("/")
def index():
    """
    render index.html template
    """
    return render_template("1-index.html")


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
