# -*- coding: utf-8 -*-
from odoo.tests.common import TransactionCase


class TestSupplier(TransactionCase):

    def setUp(self):
        super(TestSupplier, self).setUp()
        self.Supplier = self.env["custom.supplier"]

    def test_create_supplier(self):
        supplier = self.Supplier.create(
            {
                "name": "Test Supplier 2",
            }
        )
        self.assertEqual(supplier.name, "Test Supplier 2")
