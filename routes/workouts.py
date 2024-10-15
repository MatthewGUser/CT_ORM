from flask import Blueprint, request, jsonify
from connect_to_db import db
from models.workout_session import WorkoutSession
from datetime import datetime

workouts_bp = Blueprint('workouts_bp', __name__)

@workouts_bp.route('/workouts', methods=['POST'])
def schedule_workout():
    data = request.get_json()
    member_id = data.get('member_id')
    session_date = datetime.strptime(data.get('session_date'), '%Y-%m-%d %H:%M:%S')
    duration = data.get('duration')

    try:
        new_session = WorkoutSession(member_id=member_id, session_date=session_date, duration=duration)
        db.session.add(new_session)
        db.session.commit()
        return jsonify({'message': 'Workout session scheduled successfully!'}), 201
    except Exception as e:
        return jsonify({'error': str(e)}), 400

@workouts_bp.route('/workouts/<int:member_id>', methods=['GET'])
def get_workout_sessions(member_id):
    sessions = WorkoutSession.query.filter_by(member_id=member_id).all()
    if not sessions:
        return jsonify({'error': 'No workout sessions found for this member'}), 404

    result = [{'id': s.id, 'session_date': s.session_date, 'duration': s.duration} for s in sessions]
    return jsonify(result), 200
