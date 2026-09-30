# Final tests for Sleep Pattern Analyzer
import unittest
import pandas as pd
import numpy as np
from analysis import SleepAnalyzer
from recommendations import RecommendationEngine

class TestSleepAnalysisFinal(unittest.TestCase):
    def setUp(self):
        self.analyzer = SleepAnalyzer()
        self.recommender = RecommendationEngine()
        
        # Sample data for testing
        self.sample_data = pd.DataFrame({
            'date': ['2023-01-01', '2023-01-02', '2023-01-03'],
            'sleep_duration': [7.5, 6.0, 8.5],
            'quality_score': [75, 50, 90],
            'consistency_score': [80, 60, 95]
        })
    
    def test_sleep_analysis(self):
        metrics = self.analyzer.analyze_sleep_data(self.sample_data)
        self.assertIn('avg_duration', metrics)
        self.assertIn('quality_score', metrics)
        self.assertIn('consistency_score', metrics)
        
    def test_recommendations_generation(self):
        recommendations = self.recommender.generate_recommendations(self.sample_data)
        self.assertIsInstance(recommendations, list)
        self.assertGreater(len(recommendations), 0)
        
        # Check that all recommendation types are present
        rec_types = [rec['type'] for rec in recommendations]
        self.assertIn('sleep_duration', rec_types)
        self.assertIn('sleep_quality', rec_types)
        self.assertIn('sleep_consistency', rec_types)

if __name__ == '__main__':
    unittest.main()