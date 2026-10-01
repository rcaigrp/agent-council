from flask import Flask
from api.goals import goals_bp
from api.waste import waste_bp


def create_app():
    app = Flask(__name__)
    
    # Register blueprints
    app.register_blueprint(goals_bp, url_prefix='/api')
    app.register_blueprint(waste_bp, url_prefix='/api')
    
    return app