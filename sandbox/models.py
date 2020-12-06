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

class ProductPlacement(db.Model):
    __tablename__ = 'product_placements'
    id = db.Column(db.Integer, primary_key=True)
    value = db.Column(db.String(500))

class TariffType(db.Model):
    __tablename__ = 'tariff_type'
    id = db.Column(db.Integer, primary_key=True)
    value = db.Column(db.String(500))

class PartnerType(db.Model):
    __tablename__ = 'partner_type'
    id = db.Column(db.Integer, primary_key=True)
    value = db.Column(db.String(500))

class TypicalProcess(db.Model):
    __tablename__ = 'typical_process'
    id = db.Column(db.Integer, primary_key=True)
    value = db.Column(db.String(500))

class СalculationScheme(db.Model):
    __tablename__ = 'calculation_scheme'
    id = db.Column(db.Integer, primary_key=True)
    value = db.Column(db.String(500))

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


class Survey(db.Model):
    __tablename__ = 'surveys'

    id = db.Column(db.Integer, primary_key=True)
    login = db.Column(db.String(100))

    product_name = db.Column(db.String(500), nullable=False, info={'verbose_name': 'Название партнеской программы/продукта'})
    number_partners = db.Column(db.String(500), nullable=False, info={'verbose_name': 'Предполагаемое количество участников на старте/через год'})
    product_placement_id = db.Column(db.Integer, db.ForeignKey('product_placements.id'), nullable=False, info={'verbose_name': 'Предполагаемое размещение партнерской программы/продукта'})
    client_attracted_by_id = db.Column(db.Integer, db.ForeignKey('client_attracted_by.id'), nullable=False, info={'verbose_name': 'Сторона, которая привлекает клиента'})
    product_sell_by_id = db.Column(db.Integer, db.ForeignKey('product_sell_by.id'), nullable=False, info={'verbose_name': 'Сторона, которая продаёт продукт'})
    product_provided_by_id = db.Column(db.Integer, db.ForeignKey('product_provided_by.id'), nullable=False, info={'verbose_name': 'Сторона, которая создаёт продукт'})
    payment_made_from_to_id = db.Column(db.Integer, db.ForeignKey('payment_made_from_to.id'), nullable=False, info={'verbose_name': 'Кто кому выплачивает вознаграждение за продажи/привлечение'})
    tariff_type_id = db.Column(db.Integer, db.ForeignKey('tariff_type.id'), nullable=False, info={'verbose_name': 'Тип тарификации (вознаграждение между МТС и Партнером)'})
    partner_type_id = db.Column(db.Integer, db.ForeignKey('partner_type.id'), nullable=False, info={'verbose_name': 'Кем является Партнер'})

    def to_dict(self):
        return dict(id=self.id,
                  name=self.login,
                  product_name=self.product_name,
                  number_partners=self.number_partners,
                  product_placement_id=self.product_placement_id,
                  client_attracted_by_id=self.client_attracted_by_id,
                  product_provided_by_id=self.product_provided_by_id,
                  payment_made_from_to_id=self.payment_made_from_to_id,
                  tariff_type_id=self.tariff_type_id,
                  partner_type_id=self.partner_type_id)


