import os

class Config(object):
    """ Parent configuration class. """
    DEBUG = False
    CSRF_ENABLED = True
    SECRET = os.getenv('SECRET')
    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URL')

class DevelopmentConfig(Config):
    """ Configurations for development. """
    DEBUG = True

class TestingConfig(Config):
    """ Configurations for testing, with a seperate test database. """
    TESTING = True
    SQLALCHEMY_DATABASE_URI = 'postgresql://127.0.0.1/test_db'
    DEBUG = True

class StagingConfig(Config):
    """ Configuration for staging."""

class ProductionConfig(Config):
    """ Configuration for production. """
    DEBUG = False
    TESTING = False


app_config = {
    'development': DevelopmentConfig,
    'testing': TestingConfig,
    'staging': StagingConfig,
    'production': ProductionConfig,
}