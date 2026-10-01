from flask import Blueprint, request, jsonify
from models.waste_item import WasteItem
from models.sustainability_goal import SustainabilityGoal

api_bp = Blueprint('api', __name__)

# In-memory storage (would be replaced with database in production)
waste_items = []
goals = []

@api_bp.route('/waste', methods=['POST'])
def add_waste_item():
    data = request.get_json()
    waste_item = WasteItem(
        item_id=data['item_id'],
        name=data['name'],
        category=data['category'],
        weight=data['weight']
    )
    waste_items.append(waste_item)
    return jsonify({'message': 'Waste item added successfully'}), 201

@api_bp.route('/waste', methods=['GET'])
def get_waste_items():
    return jsonify([item.to_dict() for item in waste_items])

@api_bp.route('/goals', methods=['POST'])
def create_goal():
    data = request.get_json()
    goal = SustainabilityGoal(
        goal_id=data['goal_id'],
        description=data['description'],
        target_amount=data['target_amount'],
        unit=data['unit']
    )
    goals.append(goal)
    return jsonify({'message': 'Goal created successfully'}), 201

@api_bp.route('/goals', methods=['GET'])
def get_goals():
    return jsonify([goal.to_dict() for goal in goals])