#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import api, fields, models, _
from odoo.exceptions import UserError, RedirectWarning, ValidationError
from odoo.osv.expression import get_unaccent_wrapper


class res_partner(models.Model):
    _description = "Partner registered turns"
    _inherit = 'res.partner'

    # Variables
    rubro = fields.Many2one('sales.rubro', string='Rubro')
    rubro_hijo = fields.Many2one('sales.rubro', string='Sub Rubro')