"""empty message

Revision ID: 4ccc5ebeca8d
Revises: 
Create Date: 2020-12-10 11:45:34.814138

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '4ccc5ebeca8d'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('calculation_scheme',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('value', sa.String(length=500), nullable=True),
    sa.Column('tag', sa.String(length=500), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('client_attracted_by',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('value', sa.String(length=500), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('partner_type',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('value', sa.String(length=500), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('payment_made_from_to',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('value', sa.String(length=500), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('product_placements',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('value', sa.String(length=500), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('product_provided_by',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('value', sa.String(length=500), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('product_sell_by',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('value', sa.String(length=500), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('tariff_type',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('value', sa.String(length=500), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('typical_process',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('value', sa.String(length=500), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('business_model',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=500), nullable=True),
    sa.Column('tag', sa.String(length=500), nullable=True),
    sa.Column('have_client', sa.Integer(), nullable=True),
    sa.Column('client_attracted_by_id', sa.Integer(), nullable=False),
    sa.Column('product_sell_by_id', sa.Integer(), nullable=False),
    sa.Column('product_provided_by_id', sa.Integer(), nullable=False),
    sa.Column('payment_made_from_to_id', sa.Integer(), nullable=False),
    sa.Column('typical_process_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['client_attracted_by_id'], ['client_attracted_by.id'], ),
    sa.ForeignKeyConstraint(['payment_made_from_to_id'], ['payment_made_from_to.id'], ),
    sa.ForeignKeyConstraint(['product_provided_by_id'], ['product_provided_by.id'], ),
    sa.ForeignKeyConstraint(['product_sell_by_id'], ['product_sell_by.id'], ),
    sa.ForeignKeyConstraint(['typical_process_id'], ['typical_process.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('surveys',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('login', sa.String(length=100), nullable=True),
    sa.Column('is_active_partners', sa.Boolean(), nullable=True),
    sa.Column('is_third_side', sa.Integer(), nullable=True),
    sa.Column('product_name', sa.String(length=500), nullable=False),
    sa.Column('number_partners', sa.String(length=500), nullable=False),
    sa.Column('client_attracted_by_id', sa.Integer(), nullable=False),
    sa.Column('product_sell_by_id', sa.Integer(), nullable=False),
    sa.Column('product_provided_by_id', sa.Integer(), nullable=False),
    sa.Column('payment_made_from_to_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['client_attracted_by_id'], ['client_attracted_by.id'], ),
    sa.ForeignKeyConstraint(['payment_made_from_to_id'], ['payment_made_from_to.id'], ),
    sa.ForeignKeyConstraint(['product_provided_by_id'], ['product_provided_by.id'], ),
    sa.ForeignKeyConstraint(['product_sell_by_id'], ['product_sell_by.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    association_calculation_scheme=op.create_table('association_calculation_scheme',
    sa.Column('business_model_id', sa.Integer(), nullable=True),
    sa.Column('calculation_scheme_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['business_model_id'], ['business_model.id'], ),
    sa.ForeignKeyConstraint(['calculation_scheme_id'], ['calculation_scheme.id'], )
    )
    op.create_table('association_partner_type',
    sa.Column('survey_id', sa.Integer(), nullable=True),
    sa.Column('partner_type_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['partner_type_id'], ['partner_type.id'], ),
    sa.ForeignKeyConstraint(['survey_id'], ['surveys.id'], )
    )
    op.create_table('association_product_placement',
    sa.Column('survey_id', sa.Integer(), nullable=True),
    sa.Column('product_placements_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['product_placements_id'], ['product_placements.id'], ),
    sa.ForeignKeyConstraint(['survey_id'], ['surveys.id'], )
    )
    op.create_table('association_tariff_type',
    sa.Column('survey_id', sa.Integer(), nullable=True),
    sa.Column('tariff_type_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['survey_id'], ['surveys.id'], ),
    sa.ForeignKeyConstraint(['tariff_type_id'], ['tariff_type.id'], )
    )
    # ### end Alembic commands ###

    import sandbox.models as m

    product_placements = m.ProductPlacement.__table__
    op.bulk_insert(product_placements,
                   [{'id': 1,
                     'value': 'Собственная витрина'},
                    {'id': 2,
                     'value': 'На витрине partners.mts.ru'},
                    {'id': 3,
                     'value': 'Неизвестно'}])

    client_attracted_by = m.ClientAttractedBy.__table__
    op.bulk_insert(client_attracted_by,
                   [{'id': 1,
                     'value': 'МТС'},
                    {'id': 2,
                     'value': 'Партнер'},
                    {'id': 3,
                     'value': 'МТС и Партнер'},
                    {'id': 4,
                     'value': 'Третья сторона отсутсвует'}
                    ])

    product_sell_by = m.ProductSellBy.__table__
    op.bulk_insert(product_sell_by,
                   [{'id': 1,
                     'value': 'МТС'},
                    {'id': 2,
                     'value': 'Партнер'},
                    {'id': 3,
                     'value': 'МТС и Партнер'}
                    ])

    product_provided_by = m.ProductProvidedBy.__table__
    op.bulk_insert(product_provided_by,
                   [{'id': 1,
                     'value': 'Продукт МТС'},
                    {'id': 2,
                     'value': 'Продукт Партнера'},
                    {'id': 3,
                     'value': 'Продукт и МТС и Партнера'}
                    ])

    payment_made_from_to = m.PaymentMadeFromTo.__table__
    op.bulk_insert(payment_made_from_to,
                   [{'id': 1,
                     'value': 'МТС Партнеру'},
                    {'id': 2,
                     'value': 'Партнер платит МТС'},
                    {'id': 3,
                     'value': 'Взаиморасчеты между Партнером и МТС происходят с двух сторон'}
                    ])

    tariff_type = m.TariffType.__table__
    op.bulk_insert(tariff_type,
                   [{'id': 1,
                     'value': 'Предоплата'},
                    {'id': 2,
                     'value': 'Постоплата'},
                    {'id': 3,
                     'value': 'Разовые платежи'}
                    ])

    partner_type = m.PartnerType.__table__
    op.bulk_insert(partner_type,
                   [{'id': 1,
                     'value': 'Самозанятый'},
                    {'id': 2,
                     'value': 'ИП'},
                    {'id': 3,
                     'value': 'ЮЛ'},
                    {'id': 4,
                     'value': 'Сотрудник МТС'},
                    {'id': 5,
                     'value': 'Не важно'}])

    typical_process = m.TypicalProcess.__table__
    op.bulk_insert(typical_process,
                   [{'id': 1,
                     'value': 'Типовая схема'},
                    {'id': 2,
                     'value': 'Схема на согласовании'}])


    business_model = m.BusinessModel.__table__
    op.bulk_insert(business_model,
                   [{'id': 1,
                     'name': 'Партнер как канал привлечения  и канал продаж продукта МТС',
                     'tag': 'BrokerPartner',
                     'have_client': 1,
                     'client_attracted_by_id': 2,
                     'product_sell_by_id': 3,
                     'product_provided_by_id': 1,
                     'payment_made_from_to_id': 1,
                     'typical_process_id': 1,
                     },
                    {'id': 2,
                     'name': 'Партнер как канал привлечения, МТС как канал продаж продукта МТС',
                     'tag': 'PartnersClient',
                     'have_client': 1,
                     'client_attracted_by_id': 2,
                     'product_sell_by_id': 1,
                     'product_provided_by_id': 1,
                     'payment_made_from_to_id': 1,
                     'typical_process_id': 1,
                     },
                    {'id': 3,
                     'name': 'МТС как канал привлечения, Партнер как канал продаж продукта МТC',
                     'tag': 'MTSClientMTSProduct',
                     'have_client': 1,
                     'client_attracted_by_id': 1,
                     'product_sell_by_id': 1,
                     'product_provided_by_id': 2,
                     'payment_made_from_to_id': 1,
                     'typical_process_id': 2,
                     },
                    {'id': 4,
                     'name': 'МТС/Партнер как канал привлечения МТС как канал продаж продукта партнера ',
                     'tag': 'BrokerMTS',
                     'have_client': 1,
                     'client_attracted_by_id': 1,
                     'product_sell_by_id': 2,
                     'product_provided_by_id': 2,
                     'payment_made_from_to_id': 2,
                     'typical_process_id': 1,
                     },
                    {'id': 5,
                     'name': 'МТС как канал привлечения, Партнер как канал продаж продукта партнера',
                     'tag': 'MTSClientPartnersProduct',
                     'have_client': 0,
                     'client_attracted_by_id': 4,
                     'product_sell_by_id': 2,
                     'product_provided_by_id': 2,
                     'payment_made_from_to_id': 1,
                     'typical_process_id': 2,
                     },
                    {'id': 6,
                     'name': 'Партнер как поставщик',
                     'tag': 'PartnersProduct',
                     'have_client': 0,
                     'client_attracted_by_id': 4,
                     'product_sell_by_id': 1,
                     'product_provided_by_id': 1,
                     'payment_made_from_to_id': 2,
                     'typical_process_id': 2,
                     },
                    {'id': 7,
                     'name': 'МТС как поставщик',
                     'tag': 'MTSProduct',
                     'have_client': 0,
                     'client_attracted_by_id': 4,
                     'product_sell_by_id': 2,
                     'product_provided_by_id': 2,
                     'payment_made_from_to_id': 2,
                     'typical_process_id': 2,
                     },
                    {'id': 8,
                     'name': 'МТС/Партнер как канал привлечения Партнер как канал продаж собственного продукта, использующего продукт МТС',
                     'tag': 'PartnersSales',
                     'have_client': 1,
                     'client_attracted_by_id': 3,
                     'product_sell_by_id': 3,
                     'product_provided_by_id': 3,
                     'payment_made_from_to_id': 3,
                     'typical_process_id': 2,
                     },
                    {'id': 9,
                     'name': 'МТС как канал привлечения МТС как канал продаж собственного продукта, использующего продукт Партнера',
                     'tag': 'MTSSales',
                     'have_client': 1,
                     'client_attracted_by_id': 1,
                     'product_sell_by_id': 1,
                     'product_provided_by_id': 1,
                     'payment_made_from_to_id': 1,
                     'typical_process_id': 2,
                     }])
    calculation_scheme = m.СalculationScheme.__table__
    op.bulk_insert(calculation_scheme,
                   [{'id': 1,
                     'value': 'Revenue Sharing для каналов продаж',
                     'tag': 'RS'
                     },
                    {'id': 2,
                     'value': 'Лидогенерация IN',
                     'tag': 'LidoIn'
                     },
                    {'id': 3,
                     'value': 'Продуктовый Revenue Sharing',
                     'tag': 'ProductRS'
                     },
                    {'id': 4,
                     'value': 'Продуктовый Fix/Продуктовый Роялти',
                     'tag': 'ProductFix'},
                    {'id': 5,
                     'value': 'Смешанная',
                     'tag': 'Mixed'},
                    {'id': 6,
                     'value': 'Правообладатель',
                     'tag': 'Pravo'},
                    {'id': 7,
                     'value': 'Лидогенерация OUT',
                     'tag': 'LidoOut'},
                    {'id': 8,
                     'value': 'Контракт является поставщиком',
                     'tag': 'SupplierPartner'},
                    {'id': 9,
                     'value': 'Аренда IN',
                     'tag': 'RentIn'},
                    {'id': 10,
                     'value': 'Контракт является потребителем',
                     'tag': 'ConsumerPartner'},
                    {'id': 11,
                     'value': 'Аренда OUT',
                     'tag': 'RentOut'},
                    {'id': 12,
                     'value': 'Виртуальные операторы MVNO',
                     'tag': 'MVNO'},
                    {'id': 13,
                     'value': 'Интерконнект',
                     'tag': 'Interconnect'},
                    {'id': 14,
                     'value': 'Финтех',
                     'tag': 'Fintech'}])

    op.bulk_insert(association_calculation_scheme,
                   [{'business_model_id': 1,
                     'calculation_scheme_id': 1},
                    {'business_model_id': 2,
                     'calculation_scheme_id': 2},
                    {'business_model_id': 4,
                     'calculation_scheme_id': 3},
                    {'business_model_id': 4,
                     'calculation_scheme_id': 4},
                    {'business_model_id': 4,
                     'calculation_scheme_id': 5},
                    {'business_model_id': 4,
                     'calculation_scheme_id': 6},
                    {'business_model_id': 5,
                     'calculation_scheme_id': 7},
                    {'business_model_id': 6,
                     'calculation_scheme_id': 8},
                    {'business_model_id': 6,
                     'calculation_scheme_id': 9},
                    {'business_model_id': 7,
                     'calculation_scheme_id': 10},
                    {'business_model_id': 7,
                     'calculation_scheme_id': 11},
                    {'business_model_id': 8,
                     'calculation_scheme_id': 12}])



def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('association_tariff_type')
    op.drop_table('association_product_placement')
    op.drop_table('association_partner_type')
    op.drop_table('association_calculation_scheme')
    op.drop_table('surveys')
    op.drop_table('business_model')
    op.drop_table('typical_process')
    op.drop_table('tariff_type')
    op.drop_table('product_sell_by')
    op.drop_table('product_provided_by')
    op.drop_table('product_placements')
    op.drop_table('payment_made_from_to')
    op.drop_table('partner_type')
    op.drop_table('client_attracted_by')
    op.drop_table('calculation_scheme')
    # ### end Alembic commands ###
