"""
models.py
- Data classes for the sandbox application
"""

from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class ClientAttractedBy(db.Model):
    __tablename__ = 'client_attracted_by'
    id = db.Column(db.Integer, primary_key=True)
    value = db.Column(db.String(500))

class ProductSellBy(db.Model):
    __tablename__ = 'product_sell_by'
    id = db.Column(db.Integer, primary_key=True)
    value = db.Column(db.String(500))

class ProductProvidedBy(db.Model):
    __tablename__ = 'product_provided_by'
    id = db.Column(db.Integer, primary_key=True)
    value = db.Column(db.String(500))

class PaymentMadeFromTo(db.Model):
    __tablename__ = 'payment_made_from_to'
    id = db.Column(db.Integer, primary_key=True)
    value = db.Column(db.String(500))

# Размещение продукта
class ProductPlacement(db.Model):
    __tablename__ = 'product_placements'
    id = db.Column(db.Integer, primary_key=True)
    value = db.Column(db.String(500))

    def to_dict(self):
        return dict(id=self.id,
                    value=self.value)

# Типы тарификации
class TariffType(db.Model):
    __tablename__ = 'tariff_type'
    id = db.Column(db.Integer, primary_key=True)
    value = db.Column(db.String(500))

    def to_dict(self):
        return dict(id=self.id,
                    value=self.value)

# Типы партнеров
class PartnerType(db.Model):
    __tablename__ = 'partner_type'
    id = db.Column(db.Integer, primary_key=True)
    value = db.Column(db.String(500))

    def to_dict(self):
        return dict(id=self.id,
                    value=self.value)

class TypicalProcess(db.Model):
    __tablename__ = 'typical_process'
    id = db.Column(db.Integer, primary_key=True)
    value = db.Column(db.String(500))

class СalculationScheme(db.Model):
    __tablename__ = 'calculation_scheme'
    id = db.Column(db.Integer, primary_key=True)
    value = db.Column(db.String(500))

    def to_dict(self):
        return dict(id=self.id,
                    value=self.value)

association_table_calculation_scheme = db.Table('association_calculation_scheme', db.Model.metadata,
    db.Column('business_model_id', db.Integer, db.ForeignKey('business_model.id')),
    db.Column('calculation_scheme_id', db.Integer, db.ForeignKey('calculation_scheme.id')))

class BusinessModel(db.Model):
    __tablename__ = 'business_model'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(500))
    tag = db.Column(db.String(500))
    have_client = db.Column(db.Integer)
    client_attracted_by_id = db.Column(db.Integer, db.ForeignKey('client_attracted_by.id'), nullable=False, info={'verbose_name': 'Сторона, которая привлекает клиента'})
    product_sell_by_id = db.Column(db.Integer, db.ForeignKey('product_sell_by.id'), nullable=False, info={'verbose_name': 'Сторона, которая продаёт продукт'})
    product_provided_by_id = db.Column(db.Integer, db.ForeignKey('product_provided_by.id'), nullable=False, info={'verbose_name': 'Сторона, которая создаёт продукт'})
    payment_made_from_to_id = db.Column(db.Integer, db.ForeignKey('payment_made_from_to.id'), nullable=False, info={'verbose_name': 'Кто кому выплачивает вознаграждение за продажи/привлечение'})
    typical_process_id = db.Column(db.Integer, db.ForeignKey('typical_process.id'), nullable=False, info={'verbose_name': 'Типовой процесс'})
    calculation_scheme = db.relationship("СalculationScheme", secondary=association_table_calculation_scheme)

    def to_dict(self):
        return dict(  id=self.id,
                      name=self.name,
                      tag=self.tag,
                      have_client=self.have_client,
                      client_attracted_by_id=self.client_attracted_by_id,
                      product_sell_by_id=self.product_sell_by_id,
                      product_provided_by_id=self.product_provided_by_id,
                      payment_made_from_to_id=self.payment_made_from_to_id,
                      typical_process_id=self.typical_process_id,
                      calculation_scheme=[item.to_dict() for item in self.calculation_scheme])

association_table_product_placement = db.Table('association_product_placement', db.Model.metadata,
    db.Column('survey_id', db.Integer, db.ForeignKey('surveys.id')),
    db.Column('product_placements_id', db.Integer, db.ForeignKey('product_placements.id')))

association_table_tariff_type = db.Table('association_tariff_type', db.Model.metadata,
    db.Column('survey_id', db.Integer, db.ForeignKey('surveys.id')),
    db.Column('tariff_type_id', db.Integer, db.ForeignKey('tariff_type.id')))

association_table_partner_type = db.Table('association_partner_type', db.Model.metadata,
    db.Column('survey_id', db.Integer, db.ForeignKey('surveys.id')),
    db.Column('partner_type_id', db.Integer, db.ForeignKey('partner_type.id')))

class Survey(db.Model):
    __tablename__ = 'surveys'

    id = db.Column(db.Integer, primary_key=True)
    login = db.Column(db.String(100))
    is_active_partners = db.Column(db.Boolean, default=0, info={'verbose_name': 'Есть действующие партнеры'})
    is_third_side = db.Column(db.Boolean, default=False, info={'verbose_name': 'Есть третья сторона (клиент)'})
    product_name = db.Column(db.String(500), nullable=False, info={'verbose_name': 'Название партнеской программы/продукта'})
    number_partners = db.Column(db.String(500), nullable=False, info={'verbose_name': 'Предполагаемое количество участников на старте/через год'})
    product_placement = db.relationship("ProductPlacement", secondary=association_table_product_placement, info={'verbose_name': 'Предполагаемое размещение партнерской программы/продукта'})
    client_attracted_by_id = db.Column(db.Integer, db.ForeignKey('client_attracted_by.id'), nullable=False, info={'verbose_name': 'Сторона, которая привлекает клиента'})
    product_sell_by_id = db.Column(db.Integer, db.ForeignKey('product_sell_by.id'), nullable=False, info={'verbose_name': 'Сторона, которая продаёт продукт'})
    product_provided_by_id = db.Column(db.Integer, db.ForeignKey('product_provided_by.id'), nullable=False, info={'verbose_name': 'Сторона, которая создаёт продукт'})
    payment_made_from_to_id = db.Column(db.Integer, db.ForeignKey('payment_made_from_to.id'), nullable=False, info={'verbose_name': 'Кто кому выплачивает вознаграждение за продажи/привлечение'})
    tariff_type = db.relationship("TariffType", secondary=association_table_tariff_type, info={'verbose_name': 'Тип тарификации (вознаграждение между МТС и Партнером)'})
    partner_type = db.relationship("PartnerType", secondary=association_table_partner_type, info={'verbose_name': 'Кем является Партнер'})

    def business_model_to_dict(self):
       obj = BusinessModel.query.filter_by(have_client=self.is_third_side,
                                           client_attracted_by_id=self.client_attracted_by_id,
                                           product_sell_by_id=self.product_sell_by_id,
                                           product_provided_by_id=self.product_provided_by_id,
                                           payment_made_from_to_id=self.payment_made_from_to_id).first()

       if obj:
           return obj.to_dict()
       else:
           return dict(id=-1)

    def to_dict(self):
        return dict(id=self.id,
                  login=self.login,
                  is_third_side=self.is_third_side,
                  is_active_partners=self.is_active_partners,
                  product_name=self.product_name,
                  number_partners=self.number_partners,
                  product_placement=[item.to_dict() for item in self.product_placement],
                  client_attracted_by_id=self.client_attracted_by_id,
                  product_provided_by_id=self.product_provided_by_id,
                  payment_made_from_to_id=self.payment_made_from_to_id,
                  tariff_type=[item.to_dict() for item in self.tariff_type],
                  partner_type=[item.to_dict() for item in self.partner_type],
                  business_model=self.business_model_to_dict())


