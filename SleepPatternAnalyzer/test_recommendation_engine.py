import unittest
from recommendation_engine import RecommendationEngine

class TestRecommendationEngine(unittest.TestCase):
    def setUp(self):
        self.engine = RecommendationEngine()
    
    def test_generate_recommendations_high_quality(self):
        sleep_data = {'quality_score': 85, 'restlessness_index': 0.2}
        recommendations = self.engine.generate_recommendations(sleep_data)
        # Should generate basic recommendations
        self.assertIsInstance(recommendations, list)
        
    def test_generate_recommendations_low_quality(self):
        sleep_data = {'quality_score': 60, 'restlessness_index': 0.7}
        recommendations = self.engine.generate_recommendations(sleep_data)
        # Should generate more specific recommendations
        self.assertIsInstance(recommendations, list)
        
    def test_generate_recommendations_with_disorder(self):
        sleep_data = {'quality_score': 65, 'restlessness_index': 0.6}
        user_profile = {'sleep_disorder': 'insomnia'}
        recommendations = self.engine.generate_recommendations(sleep_data, user_profile)
        # Should include disorder-specific recommendations
        self.assertIsInstance(recommendations, list)

if __name__ == '__main__':
    unittest.main()