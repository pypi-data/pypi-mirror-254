# -*- coding: utf-8 -*-
{
    'name': "sm_partago_invoicing_rest_api",

    'summary': """
        Expose CS Invoice with REST API
    """,

    'description': """
        Expose CS Invoice with REST API
    """,

    'author': "Coopdevs Treball",
    'website': "https://git.coopdevs.org/coopdevs/odoo/odoo-addons/enhancements/enhancements-account-invoicing",

    'category': 'account',
    'version': '12.0.0.1.6',

    # any module necessary for this one to work correctly
    'depends': [
        'base',
        'account',
        'base_rest_base_structure',
        'sm_partago_invoicing'
    ],

    'data': [
        'views/views_res_config_settings.xml'
    ],

    'demo': [],
}
