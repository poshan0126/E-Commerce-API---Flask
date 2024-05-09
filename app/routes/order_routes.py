from flask import Blueprint, jsonify, request
from ..models import dBase, Order, OrderItem
from ..schemas import OrderSchema

order_bp = Blueprint('order_bp', __name__)

# Endpoint to retrieve all orders
@order_bp.route('/orders', methods=['GET'])
def get_orders():
    orders = Order.query.all()
    if orders:
        return jsonify(OrderSchema().dump(orders)), 200
    else:
        return jsonify({"message": "No orders found"}), 404

# Endpoint to retrieve a specific order by ID
@order_bp.route('/orders/<int:id>', methods=['GET'])
def get_order(id):
    order = Order.query.get_or_404(id)
    return jsonify(OrderSchema().dump(order)), 200

# Endpoint to create a new order
@order_bp.route('/orders', methods=['POST'])
def create_order():
    data = request.json
    new_order = Order(order_date=data['order_date'], customer_id=data['customer_id'])
    dBase.session.add(new_order)
    dBase.session.commit()
    for item in data['items']:
        order_item = OrderItem(product_id=item['product_id'], quantity=item['quantity'], order_id=new_order.id)
        dBase.session.add(order_item)
    dBase.session.commit()
    return jsonify(OrderSchema().dump(new_order)), 200

# Endpoint to delete an order
@order_bp.route('/orders/<int:id>', methods=['DELETE'])
def delete_order(id):
    order = Order.query.get_or_404(id)
    dBase.session.delete(order)
    dBase.session.commit()
    return '', 204
