# api/goals.py

from flask import Blueprint, request, jsonify
from models.goal import SustainabilityGoal

goals_bp = Blueprint('goals', __name__)

goal_data = {}

def get_goals_by_user(user_id):
    return [goal for goal in goal_data.values() if goal.user_id == user_id]

@goals_bp.route('/goals', methods=['POST'])
def create_goal():
    data = request.get_json()
    goal = SustainabilityGoal(
        user_id=data['user_id'],
        goal_type=data['goal_type'],
        target_amount=data['target_amount'],
        time_frame=data['time_frame']
    )
    goal_data[goal.user_id] = goal
    return jsonify({'message': 'Goal created successfully'}), 201

@goals_bp.route('/goals/<user_id>', methods=['GET'])
def get_goals(user_id):
    goals = get_goals_by_user(user_id)
    return jsonify([goal.to_dict() for goal in goals])

@goals_bp.route('/goals/<user_id>/<goal_type>/progress', methods=['PUT'])
def update_progress(user_id, goal_type):
    data = request.get_json()
    goal = goal_data.get(user_id)
    if goal and goal.goal_type == goal_type:
        progress = goal.update_progress(data['amount'])
        return jsonify({'current_progress': progress, 'completed': goal.is_completed()})
    return jsonify({'error': 'Goal not found'}), 404