import unittest
from recommendation_engine import generate_recommendations

class TestRecommendationEngine(unittest.TestCase):
    def test_generate_recommendations(self):
        # Test basic recommendation generation
        recommendations = generate_recommendations({'sleep_hours': 6, 'quality': 3.0})
        self.assertIsInstance(recommendations, list)
        
if __name__ == '__main__':
    unittest.main()