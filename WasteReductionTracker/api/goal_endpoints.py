from flask import Blueprint, request, jsonify
from models.goal import Goal
from models.database import db

bp = Blueprint('goals', __name__, url_prefix='/goals')

@bp.route('/', methods=['POST'])
def create_goal():
    data = request.get_json()
    goal = Goal(
        id=None,
        user_id=data['user_id'],
        title=data['title'],
        target_amount=data['target_amount'],
        unit=data['unit'],
        deadline=data['deadline']
    )
    db.create_goal(goal)
    return jsonify({'message': 'Goal created successfully', 'goal': goal.to_dict()}), 201

@bp.route('/<int:goal_id>', methods=['GET'])
def get_goal(goal_id):
    goal = db.get_goal(goal_id)
    if not goal:
        return jsonify({'error': 'Goal not found'}), 404
    return jsonify(goal.to_dict()), 200

@bp.route('/<int:goal_id>', methods=['PUT'])
def update_goal(goal_id):
    data = request.get_json()
    goal = db.get_goal(goal_id)
    if not goal:
        return jsonify({'error': 'Goal not found'}), 404
    
    for field in ['title', 'target_amount', 'unit', 'deadline']:
        if field in data:
            setattr(goal, field, data[field])
    
    db.update_goal(goal)
    return jsonify({'message': 'Goal updated successfully', 'goal': goal.to_dict()}), 200

@bp.route('/<int:goal_id>', methods=['DELETE'])
def delete_goal(goal_id):
    success = db.delete_goal(goal_id)
    if not success:
        return jsonify({'error': 'Goal not found'}), 404
    return jsonify({'message': 'Goal deleted successfully'}), 200