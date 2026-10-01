from flask import Blueprint, request, jsonify
from models.goal import Goal
from models.waste_item import WasteItem
import json

bp = Blueprint('goals', __name__, url_prefix='/api/goals')

@bp.route('', methods=['POST'])
def create_goal():
    data = request.get_json()
    goal = Goal(
        user_id=data['user_id'],
        target_category=data['target_category'],
        target_amount=data['target_amount'],
        end_date=data.get('end_date')
    )
    saved_goal = Goal.save(goal)
    return jsonify({'id': saved_goal.id, 'message': 'Goal created successfully'}), 201

@bp.route('/user/<int:user_id>', methods=['GET'])
def get_user_goals(user_id):
    goals = Goal.get_by_user(user_id)
    return jsonify([{
        'id': g.id,
        'user_id': g.user_id,
        'target_category': g.target_category,
        'target_amount': g.target_amount,
        'start_date': g.start_date,
        'end_date': g.end_date,
        'status': g.status
    } for g in goals])

@bp.route('/<int:goal_id>', methods=['PUT'])
def update_goal(goal_id):
    data = request.get_json()
    goal = Goal(
        id=goal_id,
        user_id=data['user_id'],
        target_category=data['target_category'],
        target_amount=data['target_amount'],
        end_date=data.get('end_date'),
        status=data.get('status', 'active')
    )
    Goal.update(goal)
    return jsonify({'message': 'Goal updated successfully'}), 200