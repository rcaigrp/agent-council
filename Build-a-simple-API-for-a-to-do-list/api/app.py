#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from flask import Flask, request, jsonify
from endpoints import TodoAPI

app = Flask(__name__)
todo_api = TodoAPI()

@app.route('/todos', methods=['GET'])
def get_todos():
    todos = todo_api.get_all_todos()
    return jsonify([todo.to_dict() for todo in todos])

@app.route('/todos/<string:todo_id>', methods=['GET'])
def get_todo(todo_id):
    todo = todo_api.get_todo(todo_id)
    if not todo:
        return jsonify({'error': 'Todo not found'}), 404
    return jsonify(todo.to_dict())

@app.route('/todos', methods=['POST'])
def create_todo():
    data = request.get_json()
    title = data.get('title')
    description = data.get('description', '')
    
    if not title:
        return jsonify({'error': 'Title is required'}), 400
    
    todo = todo_api.create_todo(title, description)
    return jsonify(todo.to_dict()), 201

@app.route('/todos/<string:todo_id>', methods=['PUT'])
def update_todo(todo_id):
    data = request.get_json()
    title = data.get('title')
    description = data.get('description')
    completed = data.get('completed')
    
    todo = todo_api.update_todo(todo_id, title, description, completed)
    if not todo:
        return jsonify({'error': 'Todo not found'}), 404
    
    return jsonify(todo.to_dict())

@app.route('/todos/<string:todo_id>', methods=['DELETE'])
def delete_todo(todo_id):
    deleted = todo_api.delete_todo(todo_id)
    if not deleted:
        return jsonify({'error': 'Todo not found'}), 404
    
    return jsonify({'message': 'Todo deleted successfully'})

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)