from odoo import api, fields, models

class DailyMortality(models.Model):
    _name = 'piscigranja.daily.mortality'
    _description = 'Mortalidad Diaria'

    date = fields.Date(string='Fecha', default=fields.Date.context_today, required=True)
    batch_id = fields.Many2one('piscigranja.fish.batch', string='Lote', required=True)
    quantity = fields.Integer(string='Cantidad', required=True)
    cause = fields.Char(string='Causa')
    notes = fields.Text(string='Notas')
    company_id = fields.Many2one('res.company', string='Compañía', default=lambda self: self.env.company)

class HealthTreatment(models.Model):
    _name = 'piscigranja.health.treatment'
    _description = 'Tratamiento Sanitario'

    name = fields.Char(string='Nombre', required=True)
    batch_id = fields.Many2one('piscigranja.fish.batch', string='Lote', required=True)
    medication = fields.Char(string='Medicamento/Dosis')
    start_date = fields.Date(string='Inicio', required=True)
    end_date = fields.Date(string='Fin')
    notes = fields.Text(string='Notas')
    company_id = fields.Many2one('res.company', string='Compañía', default=lambda self: self.env.company)
