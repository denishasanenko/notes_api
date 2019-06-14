from config import config
from flask import Flask

def create_app(config_name):
    app = Flask(__name__)
    app.config.from_object(config[config_name])
    config[config_name].init_app(app)

    from .notes import notes
    app.register_blueprint(notes)


    return app