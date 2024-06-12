from odoo.tests.common import HttpCase, tagged

@tagged("-at_install", "post_install")
class TestMaterialController(HttpCase):

    def setUp(self):
        super().setUp()
        # Authenticate as a user and retrieve CSRF token
        self.csrf_token = self.authenticate("admin", "admin")

    def test_create_material_100(self):
        headers = {'X-CSRF-Token': self.csrf_token}

        # Test creating material with price equal to 100
        payload = {
            "code": "M001",
            "name": "Test Material",
            "type": "Fabric",
            "buy_price": 100,
            "supplier": "Supplier Name",
        }
        response = self.url_open("/web/dataset/call_kw/custom.material/create",
                                 data=payload, headers=headers)
        self.assertEqual(response.status_code, 200)

    def test_create_material_above_100(self):
        headers = {'X-CSRF-Token': self.csrf_token}

        # Test creating material with price above 100
        payload = {
            "code": "M002",
            "name": "Test Material 2",
            "type": "Fabric",
            "buy_price": 150,
            "supplier": "Supplier Name",
        }
        response = self.url_open("/web/dataset/call_kw/custom.material/create",
                                 data=payload, headers=headers)
        self.assertEqual(response.status_code, 200)

    def test_create_material_below_100(self):
        headers = {'X-CSRF-Token': self.csrf_token}

        # Test creating material with price below 100
        payload = {
            "code": "M003",
            "name": "Test Material 3",
            "type": "Fabric",
            "buy_price": 50,
            "supplier": "Supplier Name",
        }
        response = self.url_open("/web/dataset/call_kw/custom.material/create",
                                 data=payload, headers=headers)
        self.assertEqual(response.status_code, 200)

    def test_delete_material(self):
        headers = {'X-CSRF-Token': self.csrf_token}

        # Test deleting material
        material_id = 1  # Replace with actual material ID
        url = "/web/dataset/call_kw/custom.material/delete/{}".\
            format(material_id)
        response = self.url_open(url, headers=headers)
        self.assertEqual(response.status_code, 200)

    def test_list_materials(self):
        headers = {'X-CSRF-Token': self.csrf_token}

        # Test listing materials
        response = self.url_open("/web/dataset/call_kw/custom.material/",
                                 headers=headers)
        self.assertEqual(response.status_code, 200)

    def test_update_material(self):
        headers = {'X-CSRF-Token': self.csrf_token}

        # Test updating material
        material_id = 1  # Replace with actual material ID
        url = "/web/dataset/call_kw/custom.material/update/{}".\
            format(material_id)
        payload = {"name": "Updated Test Material"}
        response = self.url_open(url, data=payload,
                                 headers=headers)
        self.assertEqual(response.status_code, 200)

    def authenticate(self, username, password):
        """Authenticate HTTP request with provided credentials."""
        login_response = self.url_open('/web/login')
        csrf_token = login_response.cookies.get('csrf_token')
        headers = {'X-CSRF-Token': csrf_token}
        payload = {
            'login': username,
            'password': password,
        }
        response = self.url_open('/web/login', data=payload, headers=headers)
        self.assertEqual(response.status_code, 200)
        return csrf_token
