import unittest
import sys
import os
sys.path.append(os.path.dirname(os.path.abspath(__file__)))
from recommendations import RecommendationEngine

class TestFinalRecommendationEngine(unittest.TestCase):
    def setUp(self):
        self.engine = RecommendationEngine()
    
    def test_recommendations_generated(self):
        # Create mock sleep data
        import pandas as pd
        data = {'total_sleep_minutes': [480], 'sleep_efficiency': [90]}
        sleep_data = pd.DataFrame(data)
        
        recommendations = self.engine.generate_recommendations(sleep_data)
        self.assertIsInstance(recommendations, list)
        self.assertGreater(len(recommendations), 0)
    
    def test_empty_data_handling(self):
        import pandas as pd
        sleep_data = pd.DataFrame()
        
        recommendations = self.engine.generate_recommendations(sleep_data)
        self.assertIsInstance(recommendations, list)