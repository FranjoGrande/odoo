# -*- coding: utf-8 -*-
from odoo import models, fields

class AccountMove(models.Model):
    _inherit = 'account.move'

    l10n_pe_edi_fga_response = fields.Text(
        string='FGA Response',
        copy=False,
        help='Raw response returned by the SUNAT FGA service when sending the document.'
    )
