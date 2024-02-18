#!/usr/bin/env python
# -*- coding: utf-8 -*-

from os import path
from os import makedirs

from quart import Quart
from quart import render_template

from .api.command import command
from .api.instrument import instrument
from .api.sequence import sequence
from .api.state import state
from .home import home
from .settings import settings
from .db import init_app
from .token import init_token

__version__ = "0.0.3"


async def page_not_found(e):
    return await render_template("404_not_found.html"), 404


def create_app(test_config=None):
    """
    Create and configure an instance of the Quart
    application.
    """

    app = Quart(
        __name__,
        instance_relative_config=True,
    )
    app.config.from_mapping(
        SECRET_KEY="dev",
        MAX_CONTENT_LENGTH=16000000,
        DATABASE=path.join(
            app.instance_path,
            "minstrel.sqlite",
        ),
    )
    if test_config is None:
        app.config.from_pyfile(
            "config.py",
            silent=True,
        )
    else:
        app.config.update(test_config)
    try:
        makedirs(app.instance_path)
    except OSError:
        pass
    init_app(app)
    init_token(app)
    app.register_blueprint(command)
    app.register_blueprint(instrument)
    app.register_blueprint(state)
    app.register_blueprint(sequence)
    app.register_blueprint(home)
    app.register_blueprint(settings)
    app.register_error_handler(404, page_not_found)
    return app
