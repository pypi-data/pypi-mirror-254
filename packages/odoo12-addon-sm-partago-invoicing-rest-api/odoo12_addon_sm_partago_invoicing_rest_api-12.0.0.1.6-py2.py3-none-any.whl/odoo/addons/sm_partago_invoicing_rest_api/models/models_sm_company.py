# -*- coding: utf-8 -*-

from odoo import models, fields, api
from odoo.tools.translate import _


class sm_company(models.Model):
    """
    General config prepaid invoice (oneshot)
    """
    _inherit = 'res.company'

    cs_app_oneshot_account_journal_id = fields.Many2one(
        'account.journal',
        string=_("Account Journal (for account journal invoices generated from APP (oneshot))")
    )

    cs_app_oneshot_payment_mode_id = fields.Many2one(
        'account.payment.mode',
        string=_("Payment mode (for prepayment invoices generated from APP (oneshot))")
    )

    cs_app_oneshot_product_id = fields.Many2one(
        'product.product',
        string=_("Product (for prepayment invoices generated from APP(oneshot))")
    )
