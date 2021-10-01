import datetime

from odoo import fields, models

class EstateProperty(models.Model):
    _name = "estate.property"
    _description = "estate advertisement"

    name = fields.Char('名称', required=True, translate=True)
    description = fields.Text('描述')
    postcode = fields.Char('邮政编码')
    date_availability = fields.Date('可用日期', copy=False, default=fields.date.today()+datetime.timedelta(90))
    expected_price = fields.Float('预期价格', required=True)
    selling_price = fields.Float('售价', readonly=True, copy=False)
    bedrooms = fields.Integer('卧室数量', default=2)
    living_area = fields.Integer('生活区域')
    facedes = fields.Integer('外墙')
    garage = fields.Boolean('车库')
    garden = fields.Boolean('花园')
    garden_area = fields.Integer('花园区')
    garden_orientation = fields.Selection(
        [("North", 'North'),
         ("South", 'South'),
         ("East", 'East'),
         ("West", 'West')
        ],
         string = '花园方向'
    )
    state = fields.Selection(
        [
            ("New", '新建'),
            ("Offer Received", '收到报价'),
            ("Offer Accepted", '接受报价'),
            ("Sold", '出售'),
            ("Cancelled", '终止')
        ],
        string='状态',
        required=True,
        default="New"
    )
    active = fields.Boolean('活动', default=False)

