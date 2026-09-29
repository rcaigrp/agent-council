import flask
from flask import request, jsonify

app = flask.Flask("to_do_api")
app.config['APPLICATION_NAME'] = 'to_do_api'

@app.route('/', methods=['GET'])
def hello():
    return jsonify("Hello, To-Do API!")

@app.route('/tasks', methods=['GET'])
def get_tasks():
    # Placeholder for fetching tasks from a database or other source
    tasks = [
        {"id": 1, "description": "Buy groceries"},
        {"id": 2, "description": "Walk the dog"}
    ]
    return jsonify(tasks)

@app.route('/tasks', methods=['POST'])
def create_task():
    data = request.get_json()
    # Placeholder for saving a new task
    new_task = {
        "id": len(tasks) + 1,
        "description": data.get("description")
    }
    tasks.append(new_task)
    return jsonify(new_task), 201

if __name__ == '__main__':
    app.run(debug=True)