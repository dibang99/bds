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
        'views/property_views.xml',
        'views/project_views.xml',
    ],
    # 'qweb': ['static/src/xml/*.xml'],
    'installable': True,
    'application': True,
}
