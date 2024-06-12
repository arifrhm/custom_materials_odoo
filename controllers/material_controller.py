from odoo import http
from odoo.http import request


class MaterialController(http.Controller):

    @http.route(
            "/materials",
            type="json",
            auth="user"
            )
    def list_materials(self, **kwargs):
        materials = request.env["custom.material"].search([])
        return [
            {
                "id": material.id,
                "code": material.code,
                "name": material.name,
                "type": material.type,
                "buy_price": material.buy_price,
                "supplier": material.supplier_id.name,
            }
            for material in materials
        ]

    @http.route(
            "/materials/create",
            type="json",
            auth="user",
            methods=["POST"]
            )
    def create_material(self, **post):
        material = request.env["custom.material"].create(post)
        return {"id": material.id}

    @http.route(
        "/materials/update/<int:id>",
        type="json",
        auth="user",
        methods=["POST"]
    )
    def update_material(self, id, **post):
        material = request.env["custom.material"].browse(id)
        material.write(post)
        return {"id": material.id}

    @http.route(
        "/materials/delete/<int:id>",
        type="json",
        auth="user",
        methods=["POST"]
    )
    def delete_material(self, id):
        material = request.env["custom.material"].browse(id)
        material.unlink()
        return {"id": id}
