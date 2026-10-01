import unittest
from recommendation_engine import RecommendationEngine

class TestRecommendationEngine(unittest.TestCase):
    def test_generate_recommendations(self):
        engine = RecommendationEngine()
        recommendations = engine.generate_recommendations({})
        self.assertIsNotNone(recommendations)

if __name__ == '__main__':
    unittest.main()