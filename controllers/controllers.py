# -*- coding: utf-8 -*-
# from odoo import http


# class BookingOrderMuhajirin(http.Controller):
#     @http.route('/booking_order__muhajirin/booking_order__muhajirin/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/booking_order__muhajirin/booking_order__muhajirin/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('booking_order__muhajirin.listing', {
#             'root': '/booking_order__muhajirin/booking_order__muhajirin',
#             'objects': http.request.env['booking_order__muhajirin.booking_order__muhajirin'].search([]),
#         })

#     @http.route('/booking_order__muhajirin/booking_order__muhajirin/objects/<model("booking_order__muhajirin.booking_order__muhajirin"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('booking_order__muhajirin.object', {
#             'object': obj
#         })
