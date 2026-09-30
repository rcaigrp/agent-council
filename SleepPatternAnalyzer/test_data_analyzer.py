import unittest
from data_analyzer import SleepDataAnalyzer

class TestDataAnalyzer(unittest.TestCase):
    def setUp(self):
        self.analyzer = SleepDataAnalyzer()

    def test_analyze_sleep_quality(self):
        # Mock data for testing
        mock_data = [
            {'heart_rate': 60, 'body_temperature': 37.0, 'movement': 10, 'light_level': 50},
            {'heart_rate': 62, 'body_temperature': 36.9, 'movement': 8, 'light_level': 45}
        ]
        
        result = self.analyzer.analyze_sleep_quality(mock_data)
        self.assertIn('quality', result)
        self.assertIn('duration', result)
        self.assertIn('avg_heart_rate', result)
        self.assertIn('avg_body_temp', result)
        self.assertIn('avg_movement', result)

if __name__ == '__main__':
    unittest.main()