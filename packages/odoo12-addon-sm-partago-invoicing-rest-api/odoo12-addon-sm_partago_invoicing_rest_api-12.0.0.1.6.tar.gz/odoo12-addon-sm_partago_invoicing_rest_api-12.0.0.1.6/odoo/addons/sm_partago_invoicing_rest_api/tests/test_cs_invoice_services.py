import json
from odoo.tests import TransactionCase


class TestCsInvoiceServices(TransactionCase):

    def setUp(self):
        super(TestCsInvoiceServices, self).setUp()

        self.invoice_service = self.env['cs.invoice.service']

    def test_create_invoice_without_partner(self):

        self.assertEqual(True, False)
