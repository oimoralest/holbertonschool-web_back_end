#!/usr/bin/env python3
""" Simple message of welcoming
Description:
    to start working models i18n and l10n
"""
from flask import Flask, render_template
from flask_babel import Babel


app = Flask(__name__)
babel = Babel(app)


class Config:
    """ config all objects to translate
    attribute:
        Languages allowed
        default local
        time zone
    """
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app.config.from_object(Config)


@app.route('/', strict_slashes=False)
def index():
    """ first index template to getting started translate
    Args:
        template rendering
    """
    return render_template('1-index.html')


if __name__ == '__main__':
    app.run('0.0.0.0', '5000')
