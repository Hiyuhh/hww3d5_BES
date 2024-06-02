from marshmallow import fields, validate
from schemas import ma


class ProductSchema(ma.Schema):
    id = fields.Integer(required=False)
    name = fields.String(required=True, validate=validate.Length(min=2, max=25))
    price = fields.Float(required=True, validate=validate.Range(min=0))

    class Meta:
        fields = ("id", "name", "price")

class ProductIdSchema(ma.Schema):
    id = fields.Integer(required=True)
    name = fields.String(required=False)
    price = fields.String(required=False)

product_schema = ProductSchema()
products_schema = ProductSchema(many=True)
