from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class UserModel(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(100), nullable=False)
    lastname = db.Column(db.String(100), nullable=False)
    age = db.Column(db.Integer, nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)
    phone = db.Column(db.String(20), nullable=False)
    garden = db.Column(db.String(1), nullable=False)  # 'm' o 'f'
    password = db.Column(db.String(100), nullable=False)  # Almacenar en texto plano

    def __repr__(self):
        return f"<User {self.name} {self.lastname}>"