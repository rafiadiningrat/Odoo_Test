from odoo import api, fields, models
from datetime import *

class WorkOrder(models.Model):
    _name = 'work.order'
    _description = 'Work Order'

    name = fields.Char(string="WO Number", required=True, readonly=True, default=lambda self: self.env['ir.sequence'].next_by_code('work.order'))
    booking_order_ref_id = fields.Many2one('sale.order', string="Booking Order Reference", readonly=True)
    service_team_id = fields.Many2one('service.team', string="Team", required=True)
    team_leader_id = fields.Many2one('res.users', string="Team Leader", required=True)
    team_member_ids = fields.Many2many('res.users', string="Team Members")
    planned_start = fields.Datetime(string="Planned Start", required=True)
    planned_end = fields.Datetime(string="Planned End", required=True)
    date_start = fields.Datetime(string="Date Start", readonly=True)
    date_end = fields.Datetime(string="Date End", readonly=True)
    state = fields.Selection([
        ('pending', 'Pending'),
        ('in_progress', 'In Progress'),
        ('done', 'Done'),
        ('cancelled', 'Cancelled'),
    ], string="State", default='pending')
    notes = fields.Text(string="Notes")

    def action_start_work(self):
        self.write({
            'state': 'in_progress',
            'date_start': fields.Datetime.now(),
        })

    def action_end_work(self):
        self.write({
            'state': 'done',
            'date_end': fields.Datetime.now(),
        })

    def action_reset(self):
        self.write({
            'state': 'pending',
            'date_start': False,
        })

    def action_cancel(self):
        return {
            'name': 'Cancel Work Order',
            'type': 'ir.actions.act_window',
            'res_model': 'work.order.cancel.wizard',
            'view_mode': 'form',
            'target': 'new',
            'context': {'default_work_order_id': self.id}
        }
    