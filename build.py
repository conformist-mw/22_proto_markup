import staticjinja


factory_data = {
    'factory_name': 'ООО Строй-Сервис-Монтаж',
    'factory_place': 'Место деятельности: Новосибирск',
    'factory_products': 'Продукция: ЖБИ, бетон',
    'factory_address': 'Адрес: Под часами, на том-же месте',
    'factory_phone': 'Телефон: 00-00-00'
}
comments_data = {
    'comment_time': 'вчера, в 12:50',
    'request_text': '''60шт. ПК от 72-15  до ПК 21-15,
                        Криводановка, с доставкой.''',
    'request_name': 'Алексей',
    'views_amount': '12'
}
index_data = {
    'page': 'index',
    'user': 'Леонид Федорович',
    'title': 'Главная | Поиск',
    'request': 'Свежие заявки',
    'comments': 4,
    'items': 3,
    'item_user_info': 'Кирилл, 29 лет, г.Барабинск',
    'item_comment': '''Бла-бла, мне помогло, все супер! Бла-бла, мне помогло,
                все супер! Бла-бла, мне помогло, все супер! Бла-бла,
                мне помогло, все супер! Бла-бла, мне помогло, все супер!''',
    'footer': True
}
requests_data = {
    'request': 'Заявки',
    'user': 'Леонид Федорович',
    'title': 'Заявки',
    'comments': 8,
    'footer': True,
}
personal_data = {
    'user': 'Леонид Федорович',
    'title': 'Личный кабинет',
    'footer': False
}
catalog_data = {
    'user': 'Леонид Федорович',
    'title': 'Каталог организаций',
    'items': 6,
    'footer': True,
}
companies_data = {
    'user': 'Леонид Федорович',
    'title': 'Каталог организаций',
    'items': 6,
    'footer': True
}
company_data = {
    'user': 'Леонид Федорович',
    'title': 'Информация о организации',
    'footer': True
}
index_data.update(comments_data)
requests_data.update(comments_data)
catalog_data.update(factory_data)
companies_data.update(factory_data)

site = staticjinja.make_site(outpath='static', contexts=[
                             ('index.html', index_data),
                             ('requests.html', requests_data),
                             ('catalog.html', catalog_data),
                             ('companies.html', companies_data),
                             ('personal.html', personal_data),
                             ('company.html', company_data)])
site.render()
