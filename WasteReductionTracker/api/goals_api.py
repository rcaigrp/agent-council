from flask import Flask, request, jsonify
from models.goal_manager import GoalsManager
from models.goal import SustainabilityGoal
from datetime import datetime, date

app = Flask(__name__)
goals_manager = GoalsManager()

def validate_goal_data(data):
    required_fields = ['user_id', 'title', 'target_amount', 'unit', 'deadline']
    for field in required_fields:
        if field not in data:
            return False, f"Missing required field: {field}"
    try:
        datetime.fromisoformat(data['deadline'])
    except ValueError:
        return False, "Invalid deadline format. Use ISO format (YYYY-MM-DD)"
    if not isinstance(data['target_amount'], (int, float)) or data['target_amount'] < 0:
        return False, "Target amount must be a non-negative number"
    return True, "Valid"

@app.route('/goals', methods=['POST'])
def create_goal():
    data = request.get_json()
    is_valid, message = validate_goal_data(data)
    if not is_valid:
        return jsonify({'error': message}), 400
    
    goal = SustainabilityGoal(
        goal_id=data['goal_id'] if 'goal_id' in data else str(datetime.now().timestamp()),
        user_id=data['user_id'],
        title=data['title'],
        target_amount=data['target_amount'],
        unit=data['unit'],
        deadline=datetime.fromisoformat(data['deadline'])
    )
    
    try:
        goals_manager.create_goal(goal)
        return jsonify({'message': 'Goal created successfully', 'goal': goal.to_dict()}), 201
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/goals/<goal_id>', methods=['GET'])
def get_goal(goal_id):
    goal = goals_manager.get_goal(goal_id)
    if not goal:
        return jsonify({'error': 'Goal not found'}), 404
    return jsonify({'goal': goal.to_dict()}), 200

@app.route('/goals/<goal_id>', methods=['PUT'])
def update_goal(goal_id):
    data = request.get_json()
    goal = goals_manager.get_goal(goal_id)
    if not goal:
        return jsonify({'error': 'Goal not found'}), 404
    
    # Update goal attributes
    goal.title = data.get('title', goal.title)
    goal.target_amount = data.get('target_amount', goal.target_amount)
    goal.unit = data.get('unit', goal.unit)
    goal.deadline = datetime.fromisoformat(data['deadline']) if 'deadline' in data else goal.deadline
    goal.updated_at = datetime.now()
    
    try:
        goals_manager.update_goal(goal)
        return jsonify({'message': 'Goal updated successfully', 'goal': goal.to_dict()}), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/goals/<goal_id>', methods=['DELETE'])
def delete_goal(goal_id):
    goals_manager.delete_goal(goal_id)
    return jsonify({'message': 'Goal deleted successfully'}), 200

if __name__ == '__main__':
    app.run(debug=True)