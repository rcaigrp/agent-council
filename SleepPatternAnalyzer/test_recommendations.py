import unittest
from recommendations import RecommendationEngine

class TestRecommendationEngine(unittest.TestCase):
    def test_generate_recommendations(self):
        engine = RecommendationEngine()
        sleep_data = {
            'deep_sleep_percentage': 10,
            'light_sleep_percentage': 45,
            'sleep_latency': 35
        }
        recommendations = engine.generate_recommendations(sleep_data)
        self.assertEqual(len(recommendations), 3)