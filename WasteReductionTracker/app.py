from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

# In-memory data storage
waste_data = []
goals = {}

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/api/waste', methods=['POST'])
def add_waste():
    data = request.get_json()
    waste_data.append(data)
    return jsonify({'status': 'success'})

@app.route('/api/waste', methods=['GET'])
def get_waste():
    return jsonify(waste_data)

@app.route('/api/goals', methods=['POST'])
def set_goal():
    data = request.get_json()
    goals[data['user_id']] = data
    return jsonify({'status': 'success'})

@app.route('/api/goals/<user_id>', methods=['GET'])
def get_goal(user_id):
    return jsonify(goals.get(user_id, {}))

if __name__ == '__main__':
    app.run(debug=True)