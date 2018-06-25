# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import api, fields, models
from odoo.exceptions import ValidationError

class sales_rublo(models.Model):
    _description = "Rubros"
    _name = 'sales.rubro'

    name = fields.Char('Nombre', translate=True )
    cod = fields.Char('Código', translate=True)
    desc = fields.Text('Descripción', translate=True)
    padre = fields.Many2one('sales.rubro', string='Rubro Padre')

