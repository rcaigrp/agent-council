import unittest
from flask import Flask
import requests

class TestFlaskApp(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.app = Flask(__name__)
        cls.app.config['TESTING'] = True
        cls.app.config['DEBUG'] = False
        cls.app.url_map.redirect_rules = None

    def test_get_todos(self):
        response = self.app.get('/todos')
        self.assertEqual(response.status_code, 200)
        # Add more assertions here based on the API's expected behavior

    def test_post_todo(self):
        # Implement tests for adding new todos
        pass

if __name__ == '__main__':
    unittest.main()