from flask import Flask
from siphon.resources.api import api
from siphon.resources.settings import DevConfig


def create_app(config=DevConfig):
    app = Flask(__name__)
    app.config.from_object(config)

    register_extensions(app)

    return app


def register_extensions(app):
    api.init_app(app)
