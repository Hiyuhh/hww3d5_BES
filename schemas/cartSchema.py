from marshmallow import fields
from schemas import ma


class CartSchema(ma.Schema):
    id = fields.Integer(required=False)
    customer_id = fields.Integer(required=True)
    products = fields.Nested('ProductIdSchema', required=True, many=True)

class CartQuantitySchema(ma.Schema):
    quantity = fields.Integer(required=True, default=1)

cart_schema = CartSchema()
cart_schemas = CartSchema(many=True)
cart_quantity_schema = CartQuantitySchema()