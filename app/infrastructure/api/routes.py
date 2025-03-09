from flask import Blueprint
from app.infrastructure.api.controllers.user_controller import create_user, get_user, get_all_users, delete_user,update_user

user_blueprint = Blueprint('user', __name__)

user_blueprint.route('/users', methods=['POST'])(create_user)
user_blueprint.route('/users/<int:user_id>', methods=['GET'])(get_user)
user_blueprint.route('/users', methods=['GET'])(get_all_users)
user_blueprint.route('/users/<int:user_id>', methods=['DELETE'])(delete_user)
user_blueprint.route('/users/<int:user_id>', methods=['PUT'])(update_user)