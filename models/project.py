# from datetime import timedelta
# from odoo import models, fields, api, exceptions, _


# class Project(models.Model):
#     _name = 'rem.project'
#     _description = "Project Real Estate"

#     code = fields.Char(string="Project code", required=True)
#     name = fields.Char(string="Project name", required=True)
#     investor = fields.Char(string="Investor", required=True)
#     location = fields.Text(string="Project location", required=True)
#     scale = fields.Text(string="Project scale")
#     area = fields.Float(string="Project area", required=True)
#     legal = fields.Text(string="Project legal")
#     status = fields.Char(string="Project status", required=True)
#     type = fields.Char(string="Project type", required=True)
#     construction_form = fields.Char(string="Construction form", required=True)
#     time_book_receipt = fields.Date(
#         string="Time of land allocation/book receipt", required=True)
#     price = fields.Float(string="Project selling price", required=True)
#     bank_support = fields.Float(string="Bank support")
#     discount = fields.Float(string="Discount")

#     payment_methods = fields.Char(string="Payment methods", required=True)

#     _sql_constraints = [
#         ('name_unique',
#          'UNIQUE(name)',
#          "The course title must be unique"),
#     ]
