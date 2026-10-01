from flask import Flask, request, jsonify
from api.endpoints import todos_bp

app = Flask(__name__)
app.register_blueprint(todos_bp)

if __name__ == '__main__':
    app.run(debug=True)