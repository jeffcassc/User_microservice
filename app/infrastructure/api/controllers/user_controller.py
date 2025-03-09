from flask import request, jsonify
from app.application.user_service import UserService
from app.infrastructure.database.user_repository import UserRepository

user_service = UserService(UserRepository())

def create_user():
    data = request.get_json()
    user = user_service.create_user(data['name'], data['email'], data['password'])
    return jsonify({
        'id': user.id,
        'name': user.name,
        'email': user.email
    }), 201

def get_user(user_id):
    user = user_service.get_user(user_id)
    if user:
        return jsonify({
            'id': user.id,
            'name': user.name,
            'email': user.email
        }), 200
    return jsonify({'error': 'User not found'}), 404

def get_all_users():
    users = user_service.get_all_users()
    return jsonify([{
        'id': user.id,
        'name': user.name,
        'email': user.email
    } for user in users]), 200

def delete_user(user_id):
    if user_service.delete_user(user_id):
        return jsonify({'message': 'User deleted successfully'}), 200
    return jsonify({'error': 'User not found'}), 404

def update_user(user_id):
    data = request.get_json()
    user = user_service.update_user(user_id, data.get('name'), data.get('email'), data.get('password'))
    if user:
        return jsonify({
            'id': user.id,
            'name': user.name,
            'email': user.email
        }), 200
    return jsonify({'error': 'User not found'}), 404
