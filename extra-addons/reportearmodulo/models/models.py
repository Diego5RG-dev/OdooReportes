# -*- coding: utf-8 -*-

from odoo import models, fields, api


class SaleOrder(models.Model):
    _inherit = 'sale.order'
    horario = fields.Char(string='Horario',
                          default='Horario de almacen: Lunes a Viernes de 08:00 a 16:00')
#     _name = 'reportearmodulo.reportearmodulo'
#     _description = 'reportearmodulo.reportearmodulo'

#     name = fields.Char()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100

