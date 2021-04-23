# -*- coding: utf-8 -*-
{
    'name': "Property",
    'summary': """Property model""",
    'description': """Managing property information""",
    'author': "Dibangsairoi",
    'website': "",
    'category': 'Uncategorized',
    'version': '0.1',
    'depends': [
        'product',
        'sale',
        'website',
        'website_form',
        'digest',
        'website_mail',
    ],
    'data': [
        'security/ir.model.access.csv',
        'views/product_views.xml',
        'views/product_template_views.xml',
        'views/sale_order_views.xml',
    ],
    # 'qweb': ['static/src/xml/*.xml'],
    'installable': True,
    'application': True,
}
