
"""
api.py
- provides the API endpoints for consuming and producing
  REST requests and responses
"""

import sys
from flask import Blueprint, jsonify, request, current_app

from .models import db, Survey, BusinessModel, ProductPlacement, TariffType, PartnerType

api = Blueprint('api', __name__)

MESSAGE = "Hello, world! </br> Python version: {}".format(sys.version)

@api.route("/")
def root():
    response = MESSAGE.encode("utf-8")
    return response

@api.route('/surveys', methods=('POST','GET'))
def create_survey():
    if request.method == 'GET':
        login = request.args['login']
        if login:
            qs = Survey.query.filter_by(login=login).all()
            return jsonify([q.to_dict() for q in qs]), 201
        else:
            return None
    elif request.method == 'POST':
        data = request.get_json()
        survey = Survey(login=data['login'],
                        is_active_partners=data.get('is_active_partners', None),
                        is_third_side=data.get('is_third_side', None),
                        product_name=data['product_name'],
                        number_partners=data['number_partners'],
                        client_attracted_by_id=data['client_attracted_by_id'],
                        product_sell_by_id=data['product_sell_by_id'],
                        product_provided_by_id=data['product_provided_by_id'],
                        payment_made_from_to_id=data['payment_made_from_to_id'])

        survey.product_placement.extend(ProductPlacement.query.filter(ProductPlacement.id.in_(data['product_placement'])).all())
        survey.tariff_type.extend(TariffType.query.filter(TariffType.id.in_(data['tariff_type'])).all())
        survey.partner_type.extend(PartnerType.query.filter(PartnerType.id.in_(data['partner_type'])).all())

        db.session.add(survey)
        db.session.commit()

    return jsonify(survey.to_dict()), 201


@api.route('/surveys/<int:id>', methods=('GET', 'PUT'))
def survey(id):
    survey = Survey.query.filter(Survey.id == id).first_or_404()
    if request.method == 'GET':
        return jsonify(survey.to_dict()), 201
    elif request.method == 'PUT':
        data = request.get_json()
        survey.is_active_partners = data.get('is_active_partners', False)
        survey.is_third_side = data.get('is_third_side', False)
        survey.product_name = data['product_name']
        survey.number_partners = data['number_partners']
        survey.client_attracted_by_id = data['client_attracted_by_id']
        survey.product_sell_by_id = data['product_sell_by_id']
        survey.product_provided_by_id = data['product_provided_by_id']
        survey.payment_made_from_to_id = data['payment_made_from_to_id']

        survey.product_placement[:] = []
        survey.tariff_type[:] = []
        survey.partner_type[:] = []
        survey.product_placement.extend(ProductPlacement.query.filter(ProductPlacement.id.in_(data['product_placement'])).all())
        survey.tariff_type.extend(TariffType.query.filter(TariffType.id.in_(data['tariff_type'])).all())
        survey.partner_type.extend(PartnerType.query.filter(PartnerType.id.in_(data['partner_type'])).all())

        db.session.commit()
        survey = Survey.query.filter(Survey.id == id).first_or_404()
        return jsonify(survey.to_dict()), 201
