from flask import Blueprint, request, jsonify
from models.waste_item import WasteItem
from models.sustainability_goal import SustainabilityGoal
from database import Database

app = Blueprint('api', __name__)
db = Database()

@app.route('/waste_items', methods=['POST'])
def create_waste_item():
    data = request.get_json()
    name = data.get('name')
    category = data.get('category')
    weight = data.get('weight')
    date = data.get('date')
    
    if not WasteItem.validate_fields(name, category, weight):
        return jsonify({'error': 'Invalid waste item data'}), 400
    
    waste_item = WasteItem(0, name, category, weight, date)
    db.add_waste_item(waste_item)
    return jsonify({'message': 'Waste item created successfully'}), 201

@app.route('/waste_items', methods=['GET'])
def get_waste_items():
    items = db.get_waste_items()
    return jsonify(items), 200

@app.route('/goals', methods=['POST'])
def create_goal():
    data = request.get_json()
    description = data.get('description')
    target_date = data.get('target_date')
    
    if not SustainabilityGoal.validate_fields(description, target_date):
        return jsonify({'error': 'Invalid goal data'}), 400
    
    goal = SustainabilityGoal(0, description, target_date)
    db.add_sustainability_goal(goal)
    return jsonify({'message': 'Goal created successfully'}), 201

@app.route('/goals', methods=['GET'])
def get_goals():
    goals = db.get_sustainability_goals()
    return jsonify(goals), 200
