import os

class Config:
    SECRET_KEY = '123'
    PORT = os.environ.get("PORT", default=3000)
    SQLALCHEMY_DATABASE_URI = os.environ.get("DATABASE_URL", default='postgresql://postgres:admin@localhost:5432/notes')
    SQLALCHEMY_COMMIT_ON_TEARDOWN = True
    SQLALCHEMY_TRACK_MODIFICATIONS = 'models_committed'

    @staticmethod
    def init_app(app):
        pass

class DevelopmentConfig(Config):
    DEBUG = True

class TestingConfig(Config):
    TESTING = True
    DEBUG = False

class ProductionConfig(Config):
    DEBUG = False

config = {
    'development': DevelopmentConfig,
    'testing': TestingConfig,
    'production': ProductionConfig,

    'default': DevelopmentConfig
}
