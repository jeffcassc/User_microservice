import os

class Config:
    # Conexión a MySQL en XAMPP
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:@localhost/bank_users'
    SQLALCHEMY_TRACK_MODIFICATIONS = False