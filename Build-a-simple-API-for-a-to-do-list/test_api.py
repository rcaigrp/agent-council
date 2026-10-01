import sys
import os
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

test_dir = os.path.dirname(os.path.abspath(__file__))

# Import the Flask app from the correct location
try:
    from api.app import app
    print("App imported successfully")
except ImportError as e:
    print(f"Failed to import app: {e}")
    sys.exit(1)

# Run tests
if __name__ == '__main__':
    print("Testing API endpoints...")
    with app.test_client() as client:
        # Test GET /todos
        response = client.get('/todos')
        print(f"GET /todos: {response.status_code}")
        
        # Test POST /todos
        response = client.post('/todos', json={'title': 'Test todo'})
        print(f"POST /todos: {response.status_code}")
        
        # Test GET /todos/1
        response = client.get('/todos/1')
        print(f"GET /todos/1: {response.status_code}")
        
        # Test PUT /todos/1
        response = client.put('/todos/1', json={'title': 'Updated todo'})
        print(f"PUT /todos/1: {response.status_code}")
        
        # Test DELETE /todos/1
        response = client.delete('/todos/1')
        print(f"DELETE /todos/1: {response.status_code}")
    print("All tests completed")