#!/usr/bin/env python3
""" Simple message of welcoming
Description:
    to start working models i18n and l10n
"""
from flask_babel import Babel
from flask import (
    Flask,
    render_template,
    request,
    g
)
import pytz.exceptions


app = Flask(__name__)
babel = Babel(app)


users = {
    1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
    2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
    3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
    4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"},
}


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
    return render_template('6-index.html')


def get_user():
    """ Get user from mock db "users"
    Returns:
        [type]: [description]
    """
    user_id = request.args.get('login_as')
    if user_id:
        return users.get(int(user_id))


@app.before_request
def before_request():
    """ logged in user if is paased like args
    """
    user = get_user()
    if user:
        g.user = user
    else:
        g.user = None


@babel.localeselector
def get_locale():
    """ GET localization of my user
    Returns:
        the best languages apply to his/her zone
    """
    locale = request.args.get('locale')
    if locale:
        if locale in app.config['LANGUAGES']:
            return locale
    elif g.user and g.user.get('locale')\
            and g.user.get('locale') in app.config['LANGUAGES']:
        return g.user.get('locale')
    else:
        return request.accept_languages.best_match(app.config['LANGUAGES'])


@babel.timezoneselector
def get_timezone():
    """ to obtain correct user's time zone
    """
    if request.args.get('timezone'):
        tm_zone = request.args.get('timezone')
        try:
            return timezone(tm_zone).zone
        except pytz.exceptions.UnknownTimeZoneError:
            return None
    elif g.user and g.user.get('timezone'):
        try:
            return timezone(g.user.get('timezone')).zone
        except pytz.exceptions.UnknownTimeZoneError:
            return None
    else:
        return request.accept_languages.best_match(app.config['LANGUAGES'])


if __name__ == '__main__':
    app.run('0.0.0.0', '5000')
