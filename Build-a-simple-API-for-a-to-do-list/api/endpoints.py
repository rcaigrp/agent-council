#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from flask import Flask, request, jsonify
from models.todo import Todo
import uuid

class TodoAPI:
    def __init__(self):
        self.todos = {}

    def create_todo(self, title, description=""):
        todo_id = str(uuid.uuid4())
        self.todos[todo_id] = Todo(todo_id, title, description)
        return self.todos[todo_id]

    def get_todo(self, todo_id):
        return self.todos.get(todo_id)

    def update_todo(self, todo_id, title=None, description=None, completed=None):
        todo = self.get_todo(todo_id)
        if not todo:
            return None
        
        if title is not None:
            todo.title = title
        if description is not None:
            todo.description = description
        if completed is not None:
            todo.completed = completed
        
        return todo

    def delete_todo(self, todo_id):
        return self.todos.pop(todo_id, None)

    def get_all_todos(self):
        return list(self.todos.values())