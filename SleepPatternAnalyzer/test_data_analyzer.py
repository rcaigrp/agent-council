import unittest
from data_analyzer import SleepDataAnalyzer

class TestDataAnalyzer(unittest.TestCase):
    def setUp(self):
        self.analyzer = SleepDataAnalyzer()
    
    def test_detect_sleep_periods(self):
        # Test with sample sensor data
        sensor_data = [{'timestamp': '2023-10-01T22:00:00', 'movement': 0.1}]
        periods = self.analyzer.detect_sleep_periods(sensor_data)
        self.assertIsInstance(periods, list)
        
    def test_calculate_sleep_quality(self):
        sleep_periods = [{'start_time': '2023-10-01T22:00:00', 'end_time': '2023-10-02T06:00:00', 'duration_minutes': 480}]
        quality = self.analyzer.calculate_sleep_quality(sleep_periods)
        self.assertIn('total_sleep_duration', quality)
        self.assertIn('restlessness_index', quality)
        self.assertIn('quality_score', quality)

if __name__ == '__main__':
    unittest.main()