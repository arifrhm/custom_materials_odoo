from odoo import models, fields


class Supplier(models.Model):
    _name = "custom.supplier"
    _description = "Supplier"

    name = fields.Char(string="Supplier Name", required=True)
