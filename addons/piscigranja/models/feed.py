from odoo import api, fields, models

class DailyFeeding(models.Model):
    _name = 'piscigranja.daily.feeding'
    _description = 'Registro Diario de Alimentación'

    date = fields.Date(string='Fecha', default=fields.Date.context_today, required=True)
    batch_id = fields.Many2one('piscigranja.fish.batch', string='Lote', required=True)
    feed_type = fields.Char(string='Tipo de Alimento', required=True)
    amount_kg = fields.Float(string='Cantidad (kg)', required=True)
    leftovers = fields.Float(string='Sobrante (kg)')
    notes = fields.Text(string='Notas')
    company_id = fields.Many2one('res.company', string='Compañía', default=lambda self: self.env.company)
