from odoo import fields, models


class VetPatient(models.Model):
    _name = 'vet.patient'
    _description = 'Veterinary Patient'

    name = fields.Char(required=True)
    owner_id = fields.Many2one('res.partner', string='Owner')
    species = fields.Char()
    breed = fields.Char()
    age = fields.Integer()
    medical_record_ids = fields.One2many(
        'vet.medical.record',
        'patient_id',
        string='Medical Records',
    )
