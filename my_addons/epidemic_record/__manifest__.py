{
    'name' : "疫情记录",

    'summary' : """
        疫情记录""",

    'description' : """
        疫情记录
    """,
    'depends' : [],

    'author' : "Orange",
    'website' : "todo",

    # for the full list
    'version' : '0.1',

    # always loaded
    'data' : [
        'views/epidemic_record_view.xml',
        'security/ir.model.access.csv'
    ],

    # application : 当前模块是独立模块
    'application' : True,
}