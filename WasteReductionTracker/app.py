#!/usr/bin/env python3
from flask import Flask
from api.waste import waste_bp
from api.goals import goals_bp
from models.recommendation import RecommendationEngine
import os

app = Flask(__name__)

# Register blueprints
app.register_blueprint(waste_bp)
app.register_blueprint(goals_bp)

@app.route('/')
def index():
    return 'Waste Reduction Tracker API is running!'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)