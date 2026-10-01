# Test recommendation engine module

import unittest
from recommendation_engine import RecommendationEngine

class TestRecommendationEngine(unittest.TestCase):
    def test_generate_recommendations_short_sleep(self):
        engine = RecommendationEngine()
        result = engine.generate_recommendations({'duration': 5, 'restlessness_index': 4})
        self.assertEqual(len(result), 2)
        self.assertIn("Try to sleep for at least 6 hours", result)
        self.assertIn("Consider reducing caffeine intake before bedtime", result)
        
    def test_generate_recommendations_good_sleep(self):
        engine = RecommendationEngine()
        result = engine.generate_recommendations({'duration': 7, 'restlessness_index': 2})
        self.assertEqual(len(result), 0)
        
    def test_generate_recommendations_empty_data(self):
        engine = RecommendationEngine()
        result = engine.generate_recommendations({})
        self.assertEqual(len(result), 0)

if __name__ == '__main__':
    unittest.main()