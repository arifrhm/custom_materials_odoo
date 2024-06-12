# -*- coding: utf-8 -*-
from odoo.tests.common import TransactionCase
from odoo.exceptions import ValidationError


class TestMaterial(TransactionCase):

    def setUp(self):
        super(TestMaterial, self).setUp()
        self.Material = self.env["custom.material"]
        self.Supplier = self.env["custom.supplier"]
        self.supplier = self.Supplier.create(
            {
                "name": "Test Supplier",
            }
        )

    def test_create_material(self):
        material = self.Material.create(
            {
                "code": "MAT001",
                "name": "Test Material",
                "type": "fabric",
                "buy_price": 150,
                "supplier_id": self.supplier.id,
            }
        )
        self.assertEqual(material.name, "Test Material")

    def test_buy_price_validation(self):
        with self.assertRaises(ValidationError):
            self.Material.create(
                {
                    "code": "MAT002",
                    "name": "Cheap Material",
                    "type": "jeans",
                    "buy_price": 50,  # Below 100
                    "supplier_id": self.supplier.id,
                }
            )

    def test_buy_price_below_100_validation(self):
        with self.assertRaises(ValidationError) as cm:
            self.Material.create(
                {
                    "code": "MAT003",
                    "name": "Very Cheap Material",
                    "type": "cotton",
                    "buy_price": 80,  # Below 100
                    "supplier_id": self.supplier.id,
                }
            )
        self.assertEqual(
            cm.exception.name, "Material buy price cannot be less than 100."
        )

    def test_buy_price_100_or_above_validation(self):
        try:
            self.Material.create(
                {
                    "code": "MAT004",
                    "name": "Reasonable Material",
                    "type": "fabric",
                    "buy_price": 100,  # Equal to 100
                    "supplier_id": self.supplier.id,
                }
            )
            self.Material.create(
                {
                    "code": "MAT005",
                    "name": "Expensive Material",
                    "type": "jeans",
                    "buy_price": 120,  # Above 100
                    "supplier_id": self.supplier.id,
                }
            )
        except ValidationError:
            self.fail(
                "Creating materials with buy price 100 "
                "or above should not raise a validation error."
            )
