from flask import Flask
from api.endpoints import app as api_app

# Create the main Flask application
app = Flask(__name__)

# Register the API blueprint
app.register_blueprint(api_app)

if __name__ == '__main__':
    app.run(debug=False, host='0.0.0.0', port=5000)
