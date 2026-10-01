import unittest
import sys
import os
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from api.app import app

class APITestCase(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()
        
    def test_health_check(self):
        response = self.app.get('/health')
        self.assertEqual(response.status_code, 200)

if __name__ == '__main__':
    unittest.main()