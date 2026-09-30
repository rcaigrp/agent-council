import unittest
from sensor_data_collector import SensorDataCollector
from sleep_analyzer import SleepAnalyzer
from recommendation_engine import RecommendationEngine

class TestSleepModules(unittest.TestCase):
    def test_sensor_data_collection(self):
        collector = SensorDataCollector()
        data = collector.collect_sleep_data()
        self.assertIn('heart_rate', data)
        self.assertIn('body_temperature', data)
        
    def test_sleep_analysis(self):
        analyzer = SleepAnalyzer()
        sample_data = [
            {'heart_rate': 60, 'body_temperature': 37.0, 'movement': 10, 'light_level': 50},
            {'heart_rate': 62, 'body_temperature': 36.8, 'movement': 15, 'light_level': 45}
        ]
        result = analyzer.analyze_patterns(sample_data)
        self.assertIn('avg_heart_rate', result)
        self.assertIn('sleep_quality_score', result)
        
    def test_recommendation_engine(self):
        engine = RecommendationEngine()
        analysis_result = {'sleep_quality_score': 50, 'avg_heart_rate': 75, 'total_movement': 250}
        recommendations = engine.generate_recommendations(analysis_result)
        self.assertIsInstance(recommendations, list)

if __name__ == '__main__':
    unittest.main()