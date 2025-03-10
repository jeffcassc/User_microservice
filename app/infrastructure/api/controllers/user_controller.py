from flask import request, jsonify
from app.application.user_service import UserService
from app.infrastructure.database.user_repository import UserRepository

user_service = UserService(UserRepository())

def create_user():
    data = request.get_json()
    user = user_service.create_user(
        data['name'],
        data['lastname'],
        data['age'],
        data['email'],
        data['phone'],
        data['garden'],
        data['password']
    )
    return jsonify({
        'id': user.id,
        'name': user.name,
        'lastname': user.lastname,
        'age': user.age,
        'email': user.email,
        'phone': user.phone,
        'garden': user.garden
    }), 201

def get_user(user_id):
    user = user_service.get_user(user_id)
    if user:
        return jsonify({
            'id': user.id,
            'name': user.name,
            'lastname': user.lastname,
            'age': user.age,
            'email': user.email,
            'phone': user.phone,
            'garden': user.garden
        }), 200
    return jsonify({'error': 'User not found'}), 404

def get_all_users():
    users = user_service.get_all_users()
    return jsonify([{
        'id': user.id,
        'name': user.name,
        'lastname': user.lastname,
        'age': user.age,
        'email': user.email,
        'phone': user.phone,
        'garden': user.garden
    } for user in users]), 200

def delete_user(user_id):
    if user_service.delete_user(user_id):
        return jsonify({'message': 'User deleted successfully'}), 200
    return jsonify({'error': 'User not found'}), 404

def update_user(user_id):
    data = request.get_json()
    user = user_service.update_user(
        user_id,
        data.get('name'),
        data.get('lastname'),
        data.get('age'),
        data.get('email'),
        data.get('phone'),
        data.get('garden'),
        data.get('password')
    )
    if user:
        return jsonify({
            'id': user.id,
            'name': user.name,
            'lastname': user.lastname,
            'age': user.age,
            'email': user.email,
            'phone': user.phone,
            'garden': user.garden
        }), 200
    return jsonify({'error': 'User not found'}), 404

def login_user():
    data = request.get_json()
    user = user_service.login_user(data['email'], data['password'])
    if user:
        return jsonify({
            'id': user.id,
            'name': user.name,
            'lastname': user.lastname,
            'age': user.age,
            'email': user.email,
            'phone': user.phone,
            'garden': user.garden
        }), 200
    return jsonify({'error': 'Invalid credentials'}), 401

def validate_user():
    data = request.get_json()
    if user_service.validate_user(data['email']):
        return jsonify({'message': 'User exists'}), 200
    return jsonify({'error': 'User does not exist'}), 404