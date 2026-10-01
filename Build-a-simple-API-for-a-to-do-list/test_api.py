#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import unittest
import sys
import os
# Add project root to path for proper imports
project_root = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, project_root)

from api.app import app
from models.todo import Todo

class APITestCase(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()
        self.app_context = app.app_context()
        self.app_context.push()

    def tearDown(self):
        self.app_context.pop()

    def test_create_todo(self):
        response = self.app.post('/todos', 
                               json={'title': 'Test Todo', 'description': 'Test Description'})
        self.assertEqual(response.status_code, 201)
        data = response.get_json()
        self.assertEqual(data['title'], 'Test Todo')
        self.assertEqual(data['description'], 'Test Description')

    def test_get_todos(self):
        response = self.app.get('/todos')
        self.assertEqual(response.status_code, 200)
        data = response.get_json()
        self.assertIsInstance(data, list)

    def test_get_todo(self):
        # First create a todo
        create_response = self.app.post('/todos', 
                                      json={'title': 'Test Todo'})
        todo_id = create_response.get_json()['id']
        
        # Then get it
        response = self.app.get(f'/todos/{todo_id}')
        self.assertEqual(response.status_code, 200)
        data = response.get_json()
        self.assertEqual(data['title'], 'Test Todo')

    def test_update_todo(self):
        # Create a todo
        create_response = self.app.post('/todos', 
                                      json={'title': 'Test Todo'})
        todo_id = create_response.get_json()['id']
        
        # Update it
        response = self.app.put(f'/todos/{todo_id}', 
                              json={'title': 'Updated Title'})
        self.assertEqual(response.status_code, 200)
        data = response.get_json()
        self.assertEqual(data['title'], 'Updated Title')

    def test_delete_todo(self):
        # Create a todo
        create_response = self.app.post('/todos', 
                                      json={'title': 'Test Todo'})
        todo_id = create_response.get_json()['id']
        
        # Delete it
        response = self.app.delete(f'/todos/{todo_id}')
        self.assertEqual(response.status_code, 200)
        data = response.get_json()
        self.assertEqual(data['message'], 'Todo deleted successfully')


if __name__ == '__main__':
    unittest.main()