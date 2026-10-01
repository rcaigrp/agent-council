import unittest
from recommendation_engine import generate_recommendations

class TestRecommendationEngine(unittest.TestCase):
    def test_generate_recommendations(self):
        # Test basic functionality
        result = generate_recommendations({})
        self.assertIsNotNone(result)

if __name__ == '__main__':
    unittest.main()