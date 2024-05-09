from flask import Blueprint, jsonify, request
from app.models import dBase, Customer  
from app.schemas import CustomerSchema  

customer_bp = Blueprint('customer_bp', __name__)

# Endpoint to retrieve all customers
@customer_bp.route('/customers', methods=['GET'])
def get_customers():
    try:
        customers = Customer.query.all()
        if customers:
            return CustomerSchema().jsonify(customers)
        else:
            return jsonify({"message": "No customers found"}), 404
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Endpoint to retrieve a specific customer by ID
@customer_bp.route('/customers/<int:id>', methods=['GET'])
def get_customer(id):
    try:
        customer = Customer.query.get_or_404(id)
        return CustomerSchema.jsonify(customer)
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Endpoint to create a new customer
@customer_bp.route('/customers', methods=['POST'])
def create_customer():
    try:
        data = request.json
        new_customer = Customer(name=data['name'], email=data['email'], phone=data['phone'])
        dBase.session.add(new_customer)
        dBase.session.commit()
        return CustomerSchema.jsonify(new_customer)
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Endpoint to update an existing customer
@customer_bp.route('/customers/<int:id>', methods=['PUT'])
def update_customer(id):
    try:
        customer = Customer.query.get_or_404(id)
        data = request.json
        customer.name = data['name']
        customer.email = data['email']
        customer.phone = data['phone']
        dBase.session.commit()
        return CustomerSchema.jsonify(customer)
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Endpoint to delete a customer
@customer_bp.route('/customers/<int:id>', methods=['DELETE'])
def delete_customer(id):
    try:
        customer = Customer.query.get_or_404(id)
        dBase.session.delete(customer)
        dBase.session.commit()
        return '', 204
    except Exception as e:
        return jsonify({"error": str(e)}), 500
