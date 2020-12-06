
"""
api.py
- provides the API endpoints for consuming and producing
  REST requests and responses
"""

from datetime import datetime, timedelta
from functools import wraps

import jwt
from flask import Blueprint, jsonify, request, current_app

from .models import db, Survey

api = Blueprint('api', __name__)

@api.route('/surveys/', methods=('POST',))
# @token_required
def create_survey():
    data = request.get_json()
    survey = Survey(**data)
    db.session.add(survey)
    db.session.commit()
    return jsonify(survey.to_dict()), 201


