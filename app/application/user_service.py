from app.domain.user import User
from app.infrastructure.database.user_repository import UserRepository

class UserService:
    def __init__(self, user_repository: UserRepository):
        self.user_repository = user_repository

    def create_user(self, name, email, password):
        user = User(id=None, name=name, email=email, password=password)
        return self.user_repository.add_user(user)

    def get_user(self, user_id):
        return self.user_repository.get_user_by_id(user_id)

    def get_all_users(self):
        return self.user_repository.get_all_users()
    
    def delete_user(self, user_id):
        return self.user_repository.delete_user(user_id)

    def update_user(self, user_id, name=None, email=None, password=None):
        return self.user_repository.update_user(user_id, name, email, password)
