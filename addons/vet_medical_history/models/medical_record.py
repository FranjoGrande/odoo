from odoo import fields, models


class VetMedicalRecord(models.Model):
    _name = 'vet.medical.record'
    _description = 'Veterinary Medical Record'

    patient_id = fields.Many2one('vet.patient', string='Patient', required=True)
    date = fields.Date(default=fields.Date.context_today)
    description = fields.Text()
    treatment = fields.Text()
