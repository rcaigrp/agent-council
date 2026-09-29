import json
import pytest
from api import create_app

@pytest.fixture
def client():
    app = create_app({'TESTING': True, 'SQLALCHEMY_DATABASE_URI': 'sqlite:///:memory:'})
    with app.test_client() as client:
        with app.app_context():
            app.db.create_all()
        yield client

def test_create_task(client):
    response = client.post('/tasks', json={'title': 'Test task'})
    assert response.status_code == 201
    data = response.get_json()
    assert data['title'] == 'Test task'
    assert data['completed'] is False

def test_get_tasks(client):
    client.post('/tasks', json={'title': 'Task 1'})
    response = client.get('/tasks')
    assert response.status_code == 200
    tasks = response.get_json()
    assert isinstance(tasks, list)
    assert len(tasks) == 1
    assert tasks[0]['title'] == 'Task 1'

def test_update_task(client):
    create_resp = client.post('/tasks', json={'title': 'Old'})
    task_id = create_resp.get_json()['id']
    resp = client.put(f'/tasks/{task_id}', json={'title': 'New', 'completed': True})
    assert resp.status_code == 200
    data = resp.get_json()
    assert data['title'] == 'New'
    assert data['completed'] is True

def test_delete_task(client):
    create_resp = client.post('/tasks', json={'title': 'To delete'})
    task_id = create_resp.get_json()['id']
    del_resp = client.delete(f'/tasks/{task_id}')
    assert del_resp.status_code == 204
    get_resp = client.get(f'/tasks/{task_id}')
    assert get_resp.status_code == 404
