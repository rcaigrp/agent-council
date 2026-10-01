from flask import Blueprint, request, jsonify
from models.goal import GoalsManager

bp = Blueprint('goals', __name__)
goals_manager = GoalsManager()

@bp.route('/goals', methods=['POST'])
def create_goal():
    data = request.get_json()
    goal = goals_manager.create_goal(data)
    return jsonify(goal), 201

@bp.route('/goals/<int:goal_id>', methods=['GET'])
def get_goal(goal_id):
    goal = goals_manager.get_goal(goal_id)
    if not goal:
        return jsonify({'error': 'Goal not found'}), 404
    return jsonify(goal)

@bp.route('/goals/<int:goal_id>', methods=['PUT'])
def update_goal(goal_id):
    data = request.get_json()
    goal = goals_manager.update_goal(goal_id, data)
    if not goal:
        return jsonify({'error': 'Goal not found'}), 404
    return jsonify(goal)

@bp.route('/goals/<int:goal_id>', methods=['DELETE'])
def delete_goal(goal_id):
    success = goals_manager.delete_goal(goal_id)
    if not success:
        return jsonify({'error': 'Goal not found'}), 404
    return jsonify({'message': 'Goal deleted successfully'})