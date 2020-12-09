"""
application.py
- creates a Flask app instance and registers the database object
"""

from flask import Flask
from flask_cors import CORS

def create_app(app_name='SANDBOX_API'):
  app = Flask(app_name)
  app.config.from_object('sandbox.config.BaseConfig')

  cors = CORS(app, resources={r"/api/*": {"origins": "*"}})
  # cors = CORS(app, resources={r"*": {"origins": "*"}})

  from sandbox.api import api
  app.register_blueprint(api, url_prefix="/api")
  # app.register_blueprint(api, url_prefix="")

  from sandbox.models import db
  db.init_app(app)

  return app