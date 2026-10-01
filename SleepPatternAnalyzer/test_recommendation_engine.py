import sys
import os
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

import unittest
from recommendation_engine import RecommendationEngine

class TestRecommendationEngine(unittest.TestCase):
    def test_generate_recommendations(self):
        engine = RecommendationEngine()
        sleep_data = {'duration': 8, 'quality': 0.9}
        recommendations = engine.generate_recommendations(sleep_data)
        self.assertIsNotNone(recommendations)
        self.assertIsInstance(recommendations, list)

if __name__ == '__main__':
    unittest.main()