from app.infrastructure.database.db import db, UserModel
from app.domain.user import User

class UserRepository:
    def __init__(self):
        self.db = db

    def add_user(self, user: User):
        user_model = UserModel(name=user.name, email=user.email, password=user.password)
        self.db.session.add(user_model)
        self.db.session.commit()
        self.db.session.refresh(user_model)
        return User(id=user_model.id, name=user_model.name, email=user_model.email, password=user_model.password)

    def get_user_by_id(self, user_id: int):
        user_model = self.db.session.query(UserModel).filter(UserModel.id == user_id).first()
        if user_model:
            return User(id=user_model.id, name=user_model.name, email=user_model.email, password=user_model.password)
        return None

    def get_all_users(self):
        users = self.db.session.query(UserModel).all()
        return [User(id=user.id, name=user.name, email=user.email, password=user.password) for user in users]
    
    def delete_user(self, user_id: int):
        user_model = self.db.session.query(UserModel).filter(UserModel.id == user_id).first()
        if user_model:
            self.db.session.delete(user_model)
            self.db.session.commit()
            return True
        return False
    
    def update_user(self, user_id: int, name=None, email=None, password=None):
        user_model = self.db.session.query(UserModel).filter(UserModel.id == user_id).first()
        if user_model:
            if name:
                user_model.name = name
            if email:
                user_model.email = email
            if password:
                user_model.password = password
            self.db.session.commit()
            self.db.session.refresh(user_model)
            return User(id=user_model.id, name=user_model.name, email=user_model.email, password=user_model.password)
        return None