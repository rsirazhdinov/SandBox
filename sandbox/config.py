import os
"""
    config.py
    - settings for the flask application object
"""

class BaseConfig(object):
    DEBUG = True
    SECRET_KEY = 'secretkey'
    # SQLALCHEMY_DATABASE_URI = 'sqlite:///sandbox.db'
    # SQLALCHEMY_DATABASE_URI = 'postgresql://postgres:postgres@localhost/postgres'
    user = os.environ['SANDBOX_DB_SANDBOX_DB_PG_DB_USER']
    password = os.environ['SANDBOX_DB_SANDBOX_DB_PG_DB_PASSWORD']
    host = os.environ['SANDBOX_DB_SANDBOX_DB_PG_SERVICE_NAME']
    port = os.environ['SANDBOX_DB_SANDBOX_DB_PG_SERVICE_PORT']
    db_name = os.environ['SANDBOX_DB_SANDBOX_DB_PG_DB_NAME']
    SQLALCHEMY_DATABASE_URI = 'postgresql://{}:{}@{}:{}/{}'.format(user, password, host, port, db_name)
    SQLALCHEMY_TRACK_MODIFICATIONS = False