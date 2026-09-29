import pytest
from app.app import app as flask_app

@pytest.fixture
def client():
    with flask_app.test_client() as client:
        yield client

def test_index_status(client):
    response = client.get('/')
    assert response.status_code == 200
    assert b'Network Map Placeholder' in response.data
