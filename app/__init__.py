from flask import Flask

from .routes import bp


def create_app(testing=False):
    app = Flask(__name__)
    app.config.update(TESTING=testing)
    app.register_blueprint(bp)
    return app
