from odoo import fields, models

class Estate(models.Model):
    _name = "estate"
    _description = "estate advertisement"

    name = fields.Char('名称', required=True, translate=True)
    description = fields.Text('描述')
    postcode = fields.Char('postcode')
    date_availability = fields.Date('date_availability')
    expected_price = fields.Float('expected_price', required=True)
    selling_price = fields.Float('selling_price')
    bedrooms = fields.Integer('bedrooms')
    living_area = fields.Integer('living_area')
    facedes = fields.Integer('facedes')
    garage = fields.Boolean('garage')
    garden = fields.Boolean('garden')
    garden_area = fields.Integer('garden_area')
    garden_orientation = fields.Selection(
        [("North", 'North'),
         ("South", 'South'),
         ("East", 'East'),
         ("West", 'West')
        ],
         string = 'orientation'
    )

