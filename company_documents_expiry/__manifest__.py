# -*- coding: utf-8 -*-

###################################################################################
{
    'name': ' Company Documents',
    'version': '14.0.1.0.0',
    'license': 'LGPL-3',
    'summary': """Manages Company Documents With Expiry Notifications.""",
    'description': """OH Addon: Manages Company Related Documents with Expiry Notifications.""",
    'category': 'Documents Modules',
    'author': 'samah kandil',
    'company': 'samah kandil',
    'maintainer': 'samah kandil',
    'website': "https://www.linkedin.com/in/samah-kandil-odoo/",
    'depends': ['base', 'contacts',],
    'data': [
        'security/ir.model.access.csv',
        'views/company_document_view.xml',
        'views/document_type_view.xml',
        'views/hr_document_template.xml',
    ],
    'installable': True,
    'auto_install': False,
    'application': False,
}
