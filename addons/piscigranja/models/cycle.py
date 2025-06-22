from odoo import api, fields, models

class FishBatch(models.Model):
    _name = 'piscigranja.fish.batch'
    _description = 'Lote de Peces'
    _inherit = ['mail.thread', 'mail.activity.mixin']

    name = fields.Char(string='Nombre del lote', required=True, tracking=True)
    species = fields.Char(string='Especie/Raza', required=True, tracking=True)
    start_date = fields.Date(string='Fecha de Siembra', required=True, tracking=True)
    quantity = fields.Integer(string='Cantidad Inicial', required=True, tracking=True)
    avg_weight = fields.Float(string='Peso Promedio Inicial (g)', tracking=True)
    company_id = fields.Many2one('res.company', string='Compañía', default=lambda self: self.env.company)
    active = fields.Boolean(default=True)

class FishTransfer(models.Model):
    _name = 'piscigranja.fish.transfer'
    _description = 'Transferencia de Peces'

    date = fields.Date(string='Fecha', default=fields.Date.context_today, required=True)
    batch_id = fields.Many2one('piscigranja.fish.batch', string='Lote', required=True)
    source_unit = fields.Char(string='Unidad Origen')
    dest_unit = fields.Char(string='Unidad Destino')
    quantity = fields.Integer(string='Cantidad', required=True)
    notes = fields.Text(string='Notas')
    company_id = fields.Many2one('res.company', string='Compañía', default=lambda self: self.env.company)

class FishHarvest(models.Model):
    _name = 'piscigranja.fish.harvest'
    _description = 'Cosecha de Peces'

    date = fields.Date(string='Fecha', default=fields.Date.context_today, required=True)
    batch_id = fields.Many2one('piscigranja.fish.batch', string='Lote', required=True)
    quantity = fields.Integer(string='Cantidad Cosechada', required=True)
    total_weight = fields.Float(string='Peso Total (kg)')
    destination = fields.Char(string='Destino')
    notes = fields.Text(string='Notas')
    company_id = fields.Many2one('res.company', string='Compañía', default=lambda self: self.env.company)
