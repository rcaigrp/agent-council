import unittest
import sys
import os
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from recommendation_engine import RecommendationEngine

class TestRecommendationEngine(unittest.TestCase):
    def setUp(self):
        self.engine = RecommendationEngine()
    
    def test_recommendations_for_short_sleep(self):
        sleep_data = {
            'total_sleep_duration': 5,
            'restlessness_index': 0.3,
            'sleep_efficiency': 90
        }
        recommendations = self.engine.generate_recommendations(sleep_data)
        self.assertIn("You're getting less than 6 hours of sleep", recommendations[0])
    
    def test_recommendations_for_long_sleep(self):
        sleep_data = {
            'total_sleep_duration': 10,
            'restlessness_index': 0.2,
            'sleep_efficiency': 80
        }
        recommendations = self.engine.generate_recommendations(sleep_data)
        self.assertIn("You're sleeping more than 9 hours", recommendations[0])
    
    def test_recommendations_for_high_restlessness(self):
        sleep_data = {
            'total_sleep_duration': 7,
            'restlessness_index': 0.7,
            'sleep_efficiency': 85
        }
        recommendations = self.engine.generate_recommendations(sleep_data)
        self.assertIn("High restlessness detected", recommendations[0])
    
    def test_recommendations_for_low_efficiency(self):
        sleep_data = {
            'total_sleep_duration': 8,
            'restlessness_index': 0.4,
            'sleep_efficiency': 75
        }
        recommendations = self.engine.generate_recommendations(sleep_data)
        self.assertIn("Low sleep efficiency", recommendations[0])

if __name__ == '__main__':
    unittest.main()