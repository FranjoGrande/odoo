# -*- coding: utf-8 -*-
from odoo import models

class AccountEdiFormat(models.Model):
    _inherit = 'account.edi.format'

    def _is_compatible_with_journal(self, journal):
        self.ensure_one()
        if self.code != 'pe_edi_fga':
            return super()._is_compatible_with_journal(journal)
        return journal.country_code == 'PE' and journal.type == 'sale'
