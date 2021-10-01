{
    'name': "房地产广告",
    'version': '1.0',
    'depends': ['base'],
    'author': "Orange",
    'category': 'Category',
    'description': """
        房地产广告
    """,
    # data files always loaded at installation
    'data': [
        'views\estate_property_views.xml',
        'security\ir.model.access.csv'
    ],
    # data files containing optionally loaded demonstration data
    'demo': [
    ],

    'application' : True,
}