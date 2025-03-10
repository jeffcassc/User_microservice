from flask import Blueprint
from app.infrastructure.api.controllers.user_controller import (
    create_user, get_user, get_all_users, delete_user, update_user, login_user, validate_user
)

user_blueprint = Blueprint('user', __name__)

user_blueprint.route('/user', methods=['POST'])(create_user)
user_blueprint.route('/user/<int:user_id>', methods=['GET'])(get_user)
user_blueprint.route('/user', methods=['GET'])(get_all_users)
user_blueprint.route('/user/<int:user_id>', methods=['DELETE'])(delete_user)
user_blueprint.route('/user/<int:user_id>', methods=['PATCH'])(update_user)
user_blueprint.route('/user/login', methods=['POST'])(login_user)
user_blueprint.route('/user/validate', methods=['POST'])(validate_user)