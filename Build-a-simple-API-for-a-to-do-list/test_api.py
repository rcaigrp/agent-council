# Test file for the to-do list API
import pytest
from api.app import app

class TestTodoAPI:
    def setup_method(self):
        self.client = app.test_client()
        self.client.testing = True

    def test_create_todo(self):
        response = self.client.post('/todos', json={'title': 'Test Todo'})
        assert response.status_code == 201
        data = response.get_json()
        assert data['title'] == 'Test Todo'

    def test_get_todos(self):
        response = self.client.get('/todos')
        assert response.status_code == 200

    def test_get_todo_by_id(self):
        response = self.client.get('/todos/1')
        assert response.status_code == 200

    def test_update_todo(self):
        response = self.client.put('/todos/1', json={'title': 'Updated Todo'})
        assert response.status_code == 200

    def test_delete_todo(self):
        response = self.client.delete('/todos/1')
        assert response.status_code == 200