# -*- coding: utf-8 -*-
# from odoo import http


# class Reportearmodulo(http.Controller):
#     @http.route('/reportearmodulo/reportearmodulo', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/reportearmodulo/reportearmodulo/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('reportearmodulo.listing', {
#             'root': '/reportearmodulo/reportearmodulo',
#             'objects': http.request.env['reportearmodulo.reportearmodulo'].search([]),
#         })

#     @http.route('/reportearmodulo/reportearmodulo/objects/<model("reportearmodulo.reportearmodulo"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('reportearmodulo.object', {
#             'object': obj
#         })

