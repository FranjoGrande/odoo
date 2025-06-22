from odoo import api, fields, models

class WaterParameter(models.Model):
    _name = 'piscigranja.water.parameter'
    _description = 'Lectura de Parámetros de Agua'

    date = fields.Datetime(string='Fecha y Hora', default=fields.Datetime.now, required=True)
    batch_id = fields.Many2one('piscigranja.fish.batch', string='Lote')
    unit = fields.Char(string='Unidad')
    temperature = fields.Float(string='Temperatura (°C)')
    oxygen = fields.Float(string='Oxígeno Disuelto (mg/L)')
    ph = fields.Float(string='pH')
    notes = fields.Text(string='Notas')
    sensor_uid = fields.Char(string='ID Sensor')  # Placeholder for future IoT integration
    company_id = fields.Many2one('res.company', string='Compañía', default=lambda self: self.env.company)
