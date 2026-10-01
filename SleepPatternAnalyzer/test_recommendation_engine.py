import unittest
from recommendation_engine import generate_recommendations

class TestRecommendationEngine(unittest.TestCase):
    def test_generate_recommendations(self):
        # Mock data for testing
        sleep_data = {'duration': 8, 'quality_score': 7.5}
        recommendations = generate_recommendations(sleep_data)
        self.assertIsInstance(recommendations, list)

if __name__ == '__main__':
    unittest.main()