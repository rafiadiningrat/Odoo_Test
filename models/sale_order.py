from odoo import api, fields, models
from datetime import *

class SaleOrder(models.Model):
    _inherit = 'sale.order'
        
    is_booking_order = fields.Boolean(string="Is Booking Order")
    service_team_id = fields.Many2one('service.team', string="Team")
    team_leader_id = fields.Many2one('res.users', string="Team Leader")
    team_member_ids = fields.Many2many('res.users', string="Team Members")
    booking_start = fields.Datetime(string="Booking Start")
    booking_end = fields.Datetime(string="Booking End")

    def check_team_availability(self):
        overlapping_wo = self.env['work.order'].search([
            ('service_team_id', '=', self.service_team_id.id),
            ('state', 'not in', ['cancelled']),
            ('planned_start', '<=', self.booking_end),
            ('planned_end', '>=', self.booking_start),
        ])
        if overlapping_wo:
            return False, f"Team already has work order during that period on SO{overlapping_wo.sale_order_id.name}"
        return True, "Team is available for booking"

    def action_check_availability(self):
        available, message = self.check_team_availability()
        return {
            'type': 'ir.actions.client',
            'tag': 'display_notification',
            'params': {
                'title': 'Availability Check',
                'message': message,
                'sticky': False,
            }
        }

    def action_confirm(self):
        available, message = self.check_team_availability()
        if not available:
            return {
                'type': 'ir.actions.client',
                'tag': 'display_notification',
                'params': {
                    'title': 'Error',
                    'message': message,
                    'sticky': False,
                }
            }
        work_order = self.env['work.order'].create({
            'booking_order_ref_id': self.id,
            'service_team_id': self.service_team_id.id,
            'team_leader_id': self.team_leader_id.id,
            'team_member_ids': [(6, 0, self.team_member_ids.ids)],
            'planned_start': self.booking_start,
            'planned_end': self.booking_end,
            'state': 'pending',
        })
        self.work_order_id = work_order.id
        return super(SaleOrder, self).action_confirm()