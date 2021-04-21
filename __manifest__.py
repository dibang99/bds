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
        'product'
    ],
    'data': [
        'security/ir.model.access.csv',
        'views/product_views.xml',
        'views/product_template_views.xml'
    ],
    # 'qweb': ['static/src/xml/*.xml'],
    'installable': True,
    'application': True,
}
