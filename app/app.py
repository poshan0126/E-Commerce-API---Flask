# app.py

import os
from flask import Flask
from .models import dBase
from flask_migrate import Migrate

from dotenv import load_dotenv
load_dotenv()

def create_app():
    app = Flask(__name__)

    # Configuration
    app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URI')
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
   

    # Initialize Flask SQLAlchemy
    from app.models import dBase
    
    dBase.init_app(app)
    migrate = Migrate(app, dBase)
    

    # Import and register blueprints
    from app.routes.customer_routes import customer_bp
    from app.routes.product_routes import product_bp
    from app.routes.order_routes import order_bp

    app.register_blueprint(customer_bp)
    app.register_blueprint(product_bp)
    app.register_blueprint(order_bp)

    return app

