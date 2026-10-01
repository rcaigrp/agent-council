from flask import Blueprint, jsonify, request
from models.waste_analyzer import WasteAnalyzer

analytics_bp = Blueprint('analytics', __name__)

@analytics_bp.route('/waste/analytics', methods=['POST'])
def analyze_waste():
    try:
        data = request.get_json()
        waste_items = data.get('waste_items', [])
        
        analyzer = WasteAnalyzer()
        categorized = analyzer.categorize_waste(waste_items)
        patterns = analyzer.analyze_patterns(waste_items)
        
        return jsonify({
            'categorized': categorized,
            'patterns': patterns
        }), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500
