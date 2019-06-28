from config import config
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS

db = SQLAlchemy()

def create_app(config_name):
    app = Flask(__name__)
    app.config.from_object(config[config_name])
    config[config_name].init_app(app)

    CORS(app)
    db.init_app(app)

    from .notes import notes
    app.register_blueprint(notes, url_prefix='/notes')


    return app