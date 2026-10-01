import unittest
import sys
import os
sys.path.insert(0, os.path.dirname(__file__))
from models.recommendation_engine import RecommendationEngine

class TestRecommendationEngine(unittest.TestCase):
    def setUp(self):
        self.engine = RecommendationEngine()

    def test_generate_recommendations(self):
        waste_data = [{'category': 'plastic', 'amount': 5}, {'category': 'paper', 'amount': 3}]
        recommendations = self.engine.generate_recommendations(waste_data)
        self.assertIsInstance(recommendations, list)
        self.assertGreater(len(recommendations), 0)

if __name__ == '__main__':
    unittest.main()