import unittest
from recommendation_engine import generate_recommendations

class TestRecommendationEngine(unittest.TestCase):
    def test_generate_recommendations(self):
        # Test with sample data
        sleep_data = {'duration': 6, 'quality_score': 5.0}
        recommendations = generate_recommendations(sleep_data)
        self.assertIsInstance(recommendations, list)
        self.assertGreater(len(recommendations), 0)

if __name__ == '__main__':
    unittest.main()