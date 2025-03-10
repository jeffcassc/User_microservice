from app.infrastructure.database.db import db, UserModel
from app.domain.user import User

class UserRepository:
    def __init__(self):
        self.db = db

    def add_user(self, user: User):
        user_model = UserModel(
            name=user.name,
            lastname=user.lastname,
            age=user.age,
            email=user.email,
            phone=user.phone,
            garden=user.garden,
            password=user.password  # Almacenar en texto plano
        )
        self.db.session.add(user_model)
        self.db.session.commit()
        self.db.session.refresh(user_model)
        return User(
            id=user_model.id,
            name=user_model.name,
            lastname=user_model.lastname,
            age=user_model.age,
            email=user_model.email,
            phone=user_model.phone,
            garden=user_model.garden,
            password=user_model.password  # Recuperar en texto plano
        )

    def get_user_by_id(self, user_id: int):
        user_model = self.db.session.query(UserModel).filter(UserModel.id == user_id).first()
        if user_model:
            return User(
                id=user_model.id,
                name=user_model.name,
                lastname=user_model.lastname,
                age=user_model.age,
                email=user_model.email,
                phone=user_model.phone,
                garden=user_model.garden,
                password=user_model.password  # Recuperar en texto plano
            )
        return None

    def get_user_by_email(self, email: str):
        user_model = self.db.session.query(UserModel).filter(UserModel.email == email).first()
        if user_model:
            return User(
                id=user_model.id,
                name=user_model.name,
                lastname=user_model.lastname,
                age=user_model.age,
                email=user_model.email,
                phone=user_model.phone,
                garden=user_model.garden,
                password=user_model.password  # Recuperar en texto plano
            )
        return None

    def get_all_users(self):
        users = self.db.session.query(UserModel).all()
        return [User(
            id=user.id,
            name=user.name,
            lastname=user.lastname,
            age=user.age,
            email=user.email,
            phone=user.phone,
            garden=user.garden,
            password=user.password
        ) for user in users]
    
    def delete_user(self, user_id: int):
        user_model = self.db.session.query(UserModel).filter(UserModel.id == user_id).first()
        if user_model:
            self.db.session.delete(user_model)
            self.db.session.commit()
            return True
        return False
    
    def update_user(self, user_id: int, name=None, lastname=None, age=None, email=None, phone=None, garden=None, password=None):
        user_model = self.db.session.query(UserModel).filter(UserModel.id == user_id).first()
        if user_model:
            if name:
                user_model.name = name
            if lastname:
                user_model.lastname = lastname
            if age:
                user_model.age = age
            if email:
                user_model.email = email
            if phone:
                user_model.phone = phone
            if garden:
                user_model.garden = garden
            if password:
                user_model.password = password
            self.db.session.commit()
            self.db.session.refresh(user_model)
            return User(
                id=user_model.id,
                name=user_model.name,
                lastname=user_model.lastname,
                age=user_model.age,
                email=user_model.email,
                phone=user_model.phone,
                garden=user_model.garden,
                password=user_model.password
            )
        return None