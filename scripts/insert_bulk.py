import sandbox.models as m

product_placements = m.ProductPlacement.__table__
op.bulk_insert(product_placements,
               [{'id': 1,
                 'value': 'Собственная витрина'},
                {'id': 2,
                 'value': 'На винтрине partners.mts.ru'},
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


calculation_scheme = m.СalculationScheme.__table__
op.bulk_insert(calculation_scheme,
               [{'id': 1,
                 'value': 'Revenue Sharing для каналов продаж'},
                {'id': 2,
                 'value': 'Лидогенерация IN'},
                {'id': 3,
                 'value': 'Продуктовый Revenue Sharing'},
                {'id': 4,
                 'value': 'Продуктовый Fix/Продуктовый Роялти'},
                {'id': 5,
                'value': 'Смешанная'},
                {'id': 6,
                'value': 'Правообладатель'},
                {'id': 7,
                'value': 'Лидогенерация OUT'},
                {'id': 8,
                'value': 'Контракт является поставщиком'},
                {'id': 9,
                'value': 'Аренда IN'},
                {'id': 10,
                'value': 'Контракт является потребителем'},
                {'id': 11,
                'value': 'Аренда OUT'},
                {'id': 12,
                'value': 'Виртуальные операторы MVNO'},
                {'id': 13,
                'value': 'Интерконнект'},
                {'id': 14,
                'value': 'Финтех'}])