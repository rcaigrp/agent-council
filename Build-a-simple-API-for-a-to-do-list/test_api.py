import pytest
import sys
import os
sys.path.append(os.path.dirname(os.path.abspath(__file__)))
from api.app import app

@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_create_todo(client):
    response = client.post('/todos', json={'title': 'Test todo'})
    assert response.status_code == 201

def test_get_todos(client):
    response = client.get('/todos')
    assert response.status_code == 200

def test_get_todo(client):
    response = client.get('/todos/1')
    assert response.status_code == 200

def test_update_todo(client):
    response = client.put('/todos/1', json={'title': 'Updated todo'})
    assert response.status_code == 200

def test_delete_todo(client):
    response = client.delete('/todos/1')
    assert response.status_code == 200