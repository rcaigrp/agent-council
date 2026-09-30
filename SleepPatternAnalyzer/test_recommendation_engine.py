import unittest
from recommendation_engine import RecommendationEngine

class TestRecommendationEngine(unittest.TestCase):
    def setUp(self):
        self.engine = RecommendationEngine()
    
    def test_generate_recommendations_duration_short(self):
        sleep_data = {'duration': 5, 'restlessness_index': 0.3, 'quality_score': 75}
        recommendations = self.engine.generate_recommendations(sleep_data)
        self.assertIn('Try to maintain consistent sleep schedule (7-9 hours for adults)', recommendations)
    
    def test_generate_recommendations_restlessness_high(self):
        sleep_data = {'duration': 8, 'restlessness_index': 0.8, 'quality_score': 75}
        recommendations = self.engine.generate_recommendations(sleep_data)
        self.assertIn('Create a calming bedtime routine to reduce mental stimulation', recommendations)
    
    def test_generate_recommendations_quality_low(self):
        sleep_data = {'duration': 8, 'restlessness_index': 0.3, 'quality_score': 45}
        recommendations = self.engine.generate_recommendations(sleep_data)
        self.assertIn('Limit screen time 1 hour before bed', recommendations)

if __name__ == '__main__':
    unittest.main()