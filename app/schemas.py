from flask_marshmallow import Marshmallow
from marshmallow import fields
import sys

sys.path.append('D:/Desktop/E-Commerce-API-Mini-Project/app')
ma = Marshmallow()

class CustomerSchema(ma.Schema):
    id = fields.Int(dump_only=True)
    name = fields.String(required=True)
    email = fields.Email(required=True)
    phone = fields.String()


class ProductSchema(ma.Schema):
    id = fields.Int(dump_only=True)
    name = fields.String(required=True)
    price = fields.Float(required=True)

class OrderSchema(ma.Schema):
    id = fields.Int(dump_only=True)
    order_date = fields.DateTime()
    customer_id = fields.Int()
    products = fields.List(fields.Nested(ProductSchema))

class OrderItemSchema(ma.Schema):
    id = fields.Int(dump_only=True)
    product_id = fields.Int()
    quantity = fields.Int()
    order_id = fields.Int()
