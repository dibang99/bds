# -*- coding: utf-8 -*-
from odoo import api, fields, models, tools, _
from odoo.exceptions import UserError, ValidationError


class Property(models.Model):
    _name = "property"
    # _inherit = 'rem.project'
    _description = "My property model"

    name = fields.Char('Property Name', required=True)
    group = fields.Char('Property Group')
    price = fields.Float('Price Property (VND)', default=0)
    attribute = fields.Text('Property Attribute')
    description = fields.Text('Property Description')
    parcel_number = fields.Integer('Property parcel number')
    area = fields.Float('Property Area (m2)', required=True)
    # gender = fields.Selection([
    #     ('male', 'Male'),
    #     ('female', 'Female')
    # ], string='Gender', default='male')
    property_image = fields.Binary(
        "Property Image", attachment=True, help="Property Image")
    owner_id = fields.Many2one('res.partner', string='Owner')
    product_ids = fields.Many2many(comodel_name='product.product',
                                   string="Related Products",
                                   relation='property_product_rel',
                                   column1='col_property_id',
                                   column2='col_product_id')

    code = fields.Many2many('rem.project', string="Project")
