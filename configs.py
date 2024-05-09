import os

class Config:
    # Other configurations
    SQLALCHEMY_DATABASE_URI = os.environ.get('mysql+mysqlconnector://<root>:<0715>@<host>:3306/<e_commerce_db>')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
