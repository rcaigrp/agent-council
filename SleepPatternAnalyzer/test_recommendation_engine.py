import unittest
import sys
import os
sys.path.append(os.path.dirname(os.path.abspath(__file__)))
from recommendation_engine import SleepRecommendationEngine

class TestRecommendationEngine(unittest.TestCase):
    def setUp(self):
        self.engine = SleepRecommendationEngine()
    
    def test_short_duration_recommendation(self):
        sleep_data = {'sleep_duration': 6.0, 'sleep_efficiency': 90, 'sleep_latency': 20, 'schedule_consistency': 90}
        recommendations = self.engine.generate_recommendations(sleep_data)
        self.assertIn('Try to extend your sleep by 15-30 minutes each night', recommendations[0])
    
    def test_low_efficiency_recommendation(self):
        sleep_data = {'sleep_duration': 7.5, 'sleep_efficiency': 75, 'sleep_latency': 20, 'schedule_consistency': 90}
        recommendations = self.engine.generate_recommendations(sleep_data)
        self.assertIn('Improve sleep efficiency by minimizing nighttime awakenings', recommendations[0])
    
    def test_optimal_recommendation(self):
        sleep_data = {'sleep_duration': 8.0, 'sleep_efficiency': 90, 'sleep_latency': 15, 'schedule_consistency': 95}
        recommendations = self.engine.generate_recommendations(sleep_data)
        self.assertIn('Your sleep patterns are excellent! Keep up the good work with your current routine.', recommendations[0])

if __name__ == '__main__':
    unittest.main()