# -*- coding: utf-8 -*-
{
    'name': "booking_order_MUHAMMADRAFIADININGRAT_03092024",

    'summary': """
        Short (1 phrase/line) summary of the module's purpose, used as
        subtitle on modules listing or apps.openerp.com""",

    'description': """
        Long description of module's purpose
    """,

    'author': "My Company",
    'website': "http://www.yourcompany.com",

    
    'category': 'Administration',
    'version': '1.0',
    'application': True,

    # any module necessary for this one to work correctly
    'depends': ['base', 'sale', 'sale_management'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'data/sequences.xml', 

        'report/work_order_report.xml',

        'views/sale_order_views.xml',  
        'views/service_team_views.xml',   
        'views/work_order_views.xml',     
        'views/menus.xml',           
         
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}
