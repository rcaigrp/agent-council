from flask import Blueprint, jsonify
from models.recommendation_engine import RecommendationEngine

recommendation_bp = Blueprint('recommendation', __name__)
engine = RecommendationEngine()

@recommendation_bp.route('/recommendations/<user_id>', methods=['GET'])
def get_recommendations(user_id):
    # In a real app, this would fetch user's waste data from DB
    # For now, we'll simulate with sample data
    import pandas as pd
    sample_data = pd.DataFrame({
        'category': ['plastic', 'paper', 'organic'],
        'amount': [3, 2, 1]
    })
    
    recommendations = engine.generate_recommendations(sample_data)
    return jsonify({'recommendations': recommendations})