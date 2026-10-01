from flask import Flask, request, jsonify
from models.waste_data_model import WasteDataModel
from models.recommendation_engine import RecommendationEngine

app = Flask(__name__)
model = WasteDataModel()
engine = RecommendationEngine()

@app.route('/api/waste', methods=['POST'])
def add_waste_item():
    data = request.get_json()
    model.add_item(data)
    return jsonify({'status': 'success'})

@app.route('/api/recommendations', methods=['GET'])
def get_recommendations():
    waste_data = model.get_all_items()
    recommendations = engine.generate_recommendations(waste_data)
    return jsonify({'recommendations': recommendations})

if __name__ == '__main__':
    app.run(debug=True)