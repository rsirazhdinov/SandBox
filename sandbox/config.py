"""
    config.py
    - settings for the flask application object
"""

class BaseConfig(object):
    DEBUG = True
    SECRET_KEY = 'secretkey'
    # SQLALCHEMY_DATABASE_URI = 'sqlite:///sandbox.db'
    SQLALCHEMY_DATABASE_URI = 'postgresql://postgres:postgres@localhost/postgres'

    SQLALCHEMY_TRACK_MODIFICATIONS = False