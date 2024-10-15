from flask import Blueprint, request, jsonify
from connect_to_db import db
from models import WorkoutSession

workouts_bp = Blueprint('workouts', __name__)

# Create a new workout session
@workouts_bp.route('/workouts', methods=['POST'])
def add_workout():
    data = request.get_json()
    new_workout = WorkoutSession(
        member_id=data['member_id'],
        session_date=data['session_date'],
        duration=data['duration']
    )
    db.session.add(new_workout)
    db.session.commit()
    return jsonify({'message': 'Workout session added successfully!'}), 201

# Get all workout sessions for a member
@workouts_bp.route('/members/<int:member_id>/workouts', methods=['GET'])
def get_workouts(member_id):
    workouts = WorkoutSession.query.filter_by(member_id=member_id).all()
    if workouts:
        workout_list = [{'id': workout.id, 'session_date': workout.session_date, 'duration': workout.duration} for workout in workouts]
        return jsonify(workout_list), 200
    return jsonify({'error': 'No workouts found for this member'}), 404

# Update a workout session
@workouts_bp.route('/workouts/<int:id>', methods=['PUT'])
def update_workout(id):
    data = request.get_json()
    workout = WorkoutSession.query.get(id)
    if workout:
        workout.session_date = data.get('session_date', workout.session_date)
        workout.duration = data.get('duration', workout.duration)
        db.session.commit()
        return jsonify({'message': 'Workout session updated successfully!'}), 200
    return jsonify({'error': 'Workout session not found'}), 404

# Delete a workout session
@workouts_bp.route('/workouts/<int:id>', methods=['DELETE'])
def delete_workout(id):
    workout = WorkoutSession.query.get(id)
    if workout:
        db.session.delete(workout)
        db.session.commit()
        return jsonify({'message': 'Workout session deleted successfully!'}), 200
    return jsonify({'error': 'Workout session not found'}), 404
