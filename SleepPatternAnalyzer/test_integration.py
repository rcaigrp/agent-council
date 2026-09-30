#!/usr/bin/env python3
"""
Integration tests for Sleep Pattern Analyzer
"""

import unittest
from sensor_data_collector import SensorDataCollector
from data_analyzer import DataAnalyzer
from recommendation_engine import RecommendationEngine


class TestSleepPatternAnalyzer(unittest.TestCase):
    def setUp(self):
        self.collector = SensorDataCollector()
        self.analyzer = DataAnalyzer()
        self.recommender = RecommendationEngine()

    def test_end_to_end_workflow(self):
        # Create sample data
        sample_data = [
            {'timestamp': '2023-01-01T22:00:00', 'acceleration_x': 0.1, 'acceleration_y': 0.2, 'acceleration_z': 0.3},
            {'timestamp': '2023-01-01T22:01:00', 'acceleration_x': 0.05, 'acceleration_y': 0.1, 'acceleration_z': 0.2},
            {'timestamp': '2023-01-01T22:02:00', 'acceleration_x': 0.02, 'acceleration_y': 0.05, 'acceleration_z': 0.1},
        ]
        
        # Process through the full pipeline
        processed_data = self.collector.process_data(sample_data)
        analysis_results = self.analyzer.analyze(processed_data)
        recommendations = self.recommender.generate(analysis_results)
        
        # Verify all components work together
        self.assertIsNotNone(analysis_results)
        self.assertIsNotNone(recommendations)
        self.assertIn('sleep_duration', analysis_results)
        self.assertIn('restlessness_index', analysis_results)
        self.assertIsInstance(recommendations, list)
        self.assertGreater(len(recommendations), 0)

    def test_data_collection_module(self):
        collector = SensorDataCollector()
        sample_data = [
            {'timestamp': '2023-01-01T22:00:00', 'acceleration_x': 0.1, 'acceleration_y': 0.2, 'acceleration_z': 0.3},
        ]
        result = collector.process_data(sample_data)
        self.assertIsNotNone(result)

    def test_analysis_module(self):
        analyzer = DataAnalyzer()
        sample_data = [
            {'timestamp': '2023-01-01T22:00:00', 'acceleration_x': 0.1, 'acceleration_y': 0.2, 'acceleration_z': 0.3},
            {'timestamp': '2023-01-01T22:01:00', 'acceleration_x': 0.05, 'acceleration_y': 0.1, 'acceleration_z': 0.2},
        ]
        result = analyzer.analyze(sample_data)
        self.assertIsNotNone(result)
        self.assertIn('sleep_duration', result)

    def test_recommendation_module(self):
        recommender = RecommendationEngine()
        sample_analysis = {
            'sleep_duration': 7.5,
            'restlessness_index': 0.2,
        }
        recommendations = recommender.generate(sample_analysis)
        self.assertIsInstance(recommendations, list)

if __name__ == '__main__':
    unittest.main()