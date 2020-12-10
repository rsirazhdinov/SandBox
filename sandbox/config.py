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
    user = os.getenv('SANDBOX_DB_SANDBOX_DB_PG_DB_USER','38ef6bbf-f9ce-4154-8eb5-cf1c9ceea057')
    password = os.getenv('SANDBOX_DB_SANDBOX_DB_PG_DB_PASSWORD','b5c5u2cbldnoj3vg182bfiqmy')
    host = os.getenv('SANDBOX_DB_SANDBOX_DB_PG_SERVICE_NAME','0700ngenie-infr-solut-dbp.ngenie.mtsit.com')
    port = os.getenv('SANDBOX_DB_SANDBOX_DB_PG_SERVICE_PORT', 5432)
    db_name = os.getenv('SANDBOX_DB_SANDBOX_DB_PG_DB_NAME','b4b7a530-dd26-4af9-ab38-0dccb91b16c7')
    SQLALCHEMY_DATABASE_URI = 'postgresql://{}:{}@{}:{}/{}'.format(user, password, host, port, db_name)
    SQLALCHEMY_TRACK_MODIFICATIONS = False