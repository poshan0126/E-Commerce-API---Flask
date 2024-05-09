from flask_sqlalchemy import SQLAlchemy

# Initialize SQLAlchemy instance
dBase = SQLAlchemy()

class Customer(dBase.Model):
    id = dBase.Column(dBase.Integer, primary_key=True)
    name = dBase.Column(dBase.String(100), nullable=False)
    email = dBase.Column(dBase.String(100), unique=True, nullable=False)
    phone = dBase.Column(dBase.String(20))

class CustomerAccount(dBase.Model):
    id = dBase.Column(dBase.Integer, primary_key=True)
    username = dBase.Column(dBase.String(50), unique=True, nullable=False)
    password = dBase.Column(dBase.String(100), nullable=False)
    customer_id = dBase.Column(dBase.Integer, dBase.ForeignKey('customer.id'), nullable=False)
    customer = dBase.relationship('Customer', backref=dBase.backref('accounts', lazy=True))

class Product(dBase.Model):
    id = dBase.Column(dBase.Integer, primary_key=True)
    name = dBase.Column(dBase.String(100), nullable=False)
    price = dBase.Column(dBase.Float, nullable=False)

class Order(dBase.Model):
    id = dBase.Column(dBase.Integer, primary_key=True)
    order_date = dBase.Column(dBase.DateTime, nullable=False)
    customer_id = dBase.Column(dBase.Integer, dBase.ForeignKey('customer.id'), nullable=False)
    customer = dBase.relationship('Customer', backref=dBase.backref('orders', lazy=True))
    items = dBase.relationship('OrderItem', backref='order', lazy=True)

class OrderItem(dBase.Model):
    id = dBase.Column(dBase.Integer, primary_key=True)
    product_id = dBase.Column(dBase.Integer, dBase.ForeignKey('product.id'), nullable=False)
    quantity = dBase.Column(dBase.Integer, nullable=False)
    order_id = dBase.Column(dBase.Integer, dBase.ForeignKey('order.id'), nullable=False)
