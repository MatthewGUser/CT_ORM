from flask import Blueprint, request, jsonify
from connect_to_db import db
from models import Member

members_bp = Blueprint('members', __name__)

# Create a new member
@members_bp.route('/members', methods=['POST'])
def add_member():
    data = request.get_json()
    new_member = Member(name=data['name'], email=data['email'])
    db.session.add(new_member)
    db.session.commit()
    return jsonify({'message': 'Member added successfully!'}), 201

# Get a member by ID
@members_bp.route('/members/<int:id>', methods=['GET'])
def get_member(id):
    member = Member.query.get(id)
    if member:
        return jsonify({'id': member.id, 'name': member.name, 'email': member.email}), 200
    return jsonify({'error': 'Member not found'}), 404

# Update a member
@members_bp.route('/members/<int:id>', methods=['PUT'])
def update_member(id):
    data = request.get_json()
    member = Member.query.get(id)
    if member:
        member.name = data.get('name', member.name)
        member.email = data.get('email', member.email)
        db.session.commit()
        return jsonify({'message': 'Member updated successfully!'}), 200
    return jsonify({'error': 'Member not found'}), 404

# Delete a member
@members_bp.route('/members/<int:id>', methods=['DELETE'])
def delete_member(id):
    member = Member.query.get(id)
    if member:
        db.session.delete(member)
        db.session.commit()
        return jsonify({'message': 'Member deleted successfully!'}), 200
    return jsonify({'error': 'Member not found'}), 404
