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
    user = os.getenv('SANDBOX_DB_SANDBOX_DB_PG_DB_USER','4eddfa95-3999-4ed9-a1ef-6e40c0da040e')
    password = os.getenv('SANDBOX_DB_SANDBOX_DB_PG_DB_PASSWORD','bwv11kp5lru3dthm6j2cnwwmt')
    host = os.getenv('SANDBOX_DB_SANDBOX_DB_PG_SERVICE_NAME','0700ngenie-infr-solut-dbp.ngenie.mtsit.com')
    port = os.getenv('SANDBOX_DB_SANDBOX_DB_PG_SERVICE_PORT')
    db_name = os.getenv('SANDBOX_DB_SANDBOX_DB_PG_DB_NAME','1f3e7ed3-110f-4745-9f01-1f9ba1878ace')
    SQLALCHEMY_DATABASE_URI = 'postgresql://{}:{}@{}:{}/{}'.format(user, password, host, port, db_name)
    SQLALCHEMY_TRACK_MODIFICATIONS = False