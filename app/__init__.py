import os
import flask
import importlib

from eve import Eve
from eve.io.mongo.mongo import MongoJSONEncoder

resources = {}


def get_app(config=None):
    # default config
    app_config = flask.Config('.')
    app_config.from_object('app.settings')
    app_config.setdefault('DOMAIN', {})
    app_config.setdefault('SOURCES', {})

    if config:
        app_config.update(config)

    app = Eve(
        settings=app_config,
        json_encoder=MongoJSONEncoder,
    )

    for module_name in app.config.get('INSTALLED_APPS', []):
        app_module = importlib.import_module(module_name)
        try:
            app_module.init_app(app)
        except AttributeError:
            pass

    return app


def blueprint(blueprint, app, **kwargs):
    """Register flask blueprint.

    :param blueprint: blueprint instance
    :param app: flask app instance
    """
    blueprint.kwargs = kwargs
    prefix = app.api_prefix or None
    app.register_blueprint(blueprint, url_prefix=prefix, **kwargs)
