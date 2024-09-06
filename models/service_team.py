from odoo import api, fields, models

class ServiceTeam(models.Model):
    _name = 'service.team'
    _description = 'Service Team'

    name = fields.Char(string="Team Name", required=True)
    team_leader_id = fields.Many2one('res.users', string="Team Leader", required=True)
    team_member_ids = fields.Many2many('res.users', string="Team Members")
    
    