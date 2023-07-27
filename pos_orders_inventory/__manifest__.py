# -*- coding: utf-8 -*-
{
    'name': "pos_orders_inventory",

    'summary': """
        """,

    'description': """

    """,

    "author": "Kayuulab SRL",
    "website": "http://www.kayuulab.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/16.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Inventory',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base', 'stock','point_of_sale','sync_one2many_kanban'],

    # always loaded
    'data': [
        'views/pos_orders_inventory_views.xml',
    ],
    'application': True,
    'images': ['static/description/icon.png'],

}