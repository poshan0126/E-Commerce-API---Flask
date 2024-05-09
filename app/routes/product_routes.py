from flask import Blueprint, jsonify, request
from sqlalchemy.exc import IntegrityError
from ..models import dBase, Product
from ..schemas import ProductSchema

product_bp = Blueprint('product_bp', __name__)

# Endpoint to retrieve all products
@product_bp.route('/products', methods=['GET'])
def get_products():
    try:
        products = Product.query.all()
        return ProductSchema().jsonify(products), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500

# Endpoint to retrieve a specific product by ID
@product_bp.route('/products/<int:id>', methods=['GET'])
def get_product(id):
    try:
        product = Product.query.get_or_404(id)
        return ProductSchema().jsonify(product), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500

# Endpoint to create a new product
@product_bp.route('/products', methods=['POST'])
def create_product():
    try:
        data = request.json
        new_product = Product(name=data['name'], price=data['price'])
        dBase.session.add(new_product)
        dBase.session.commit()
        return ProductSchema().jsonify(new_product), 201
    except KeyError as e:
        return jsonify({'error': f'Missing required field: {str(e)}'}), 400
    except IntegrityError:
        dBase.session.rollback()
        return jsonify({'error': 'Duplicate product name or invalid data'}), 400
    except Exception as e:
        return jsonify({'error': str(e)}), 500

# Endpoint to update an existing product
@product_bp.route('/products/<int:id>', methods=['PUT'])
def update_product(id):
    try:
        product = Product.query.get_or_404(id)
        data = request.json
        product.name = data['name']
        product.price = data['price']
        dBase.session.commit()
        return ProductSchema().jsonify(product), 200
    except KeyError as e:
        return jsonify({'error': f'Missing required field: {str(e)}'}), 400
    except IntegrityError:
        dBase.session.rollback()
        return jsonify({'error': 'Duplicate product name or invalid data'}), 400
    except Exception as e:
        return jsonify({'error': str(e)}), 500

# Endpoint to delete a product
@product_bp.route('/products/<int:id>', methods=['DELETE'])
def delete_product(id):
    try:
        product = Product.query.get_or_404(id)
        dBase.session.delete(product)
        dBase.session.commit()
        return '', 204
    except Exception as e:
        return jsonify({'error': str(e)}), 500
