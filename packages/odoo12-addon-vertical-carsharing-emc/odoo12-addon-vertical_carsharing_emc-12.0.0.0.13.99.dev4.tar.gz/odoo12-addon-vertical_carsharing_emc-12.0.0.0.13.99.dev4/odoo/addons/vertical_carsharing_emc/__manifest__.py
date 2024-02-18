# -*- coding: utf-8 -*-
{
    'name': "vertical_carsharing_emc",

    'summary': """
    Enhace EMC subscription request with carsharing logic""",

    'author': "Som Mobilitat",
    'website': "https://www.sommobilitat.coop",

    'category': 'vertical-carsharing',
    'version': '12.0.0.0.13',

    # any module necessary for this one to work correctly
    'depends': [
        'base',
        'vertical_carsharing',
        'easy_my_coop',
        'easy_my_coop_es',
        'easy_my_coop_api',
        'sm_partago_user',
        'sm_partago_user_rest_api'
    ],

    # always loaded
    'data': [
        'views/views_subscription_request.xml',
        'views/views_cs_registration_request.xml',
        'views/views_res_company.xml',
        'views/views_cron.xml'
    ],
    # only loaded in demonstration mode
    'demo': [],
}
