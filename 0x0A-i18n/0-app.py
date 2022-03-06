#!/usr/bin/env python3
""" Simple message of welcoming
Description:
    to start working models i18n and l10n
"""
from flask import Flask, render_template


app = Flask(__name__)


@app.route('/', strict_slashes=False)
def index():
    """ first index template to getting started translate
    Args:
        template rendering
    """
    return render_template('0-index.html')


if __name__ == '__main__':
    app.run()
