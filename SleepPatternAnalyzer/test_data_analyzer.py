import unittest
from data_analyzer import DataAnalyzer

class TestDataAnalyzer(unittest.TestCase):
    def setUp(self):
        self.analyzer = DataAnalyzer()

    def test_detect_sleep_periods(self):
        # Mock data with proper datetime format
        mock_data = [
            {'timestamp': '2023-01-01T22:00:00', 'movement': 5},
            {'timestamp': '2023-01-01T22:05:00', 'movement': 3},
            {'timestamp': '2023-01-01T22:10:00', 'movement': 2},
            {'timestamp': '2023-01-01T22:15:00', 'movement': 1},
            {'timestamp': '2023-01-01T22:20:00', 'movement': 0}
        ]
        
        sleep_periods = self.analyzer.detect_sleep_periods(mock_data)
        self.assertEqual(len(sleep_periods), 1)
        
    def test_quality_metrics_calculation(self):
        # Mock data with proper datetime format
        mock_data = [
            {'timestamp': '2023-01-01T22:00:00', 'movement': 5},
            {'timestamp': '2023-01-01T22:05:00', 'movement': 3},
            {'timestamp': '2023-01-01T22:10:00', 'movement': 2},
            {'timestamp': '2023-01-01T22:15:00', 'movement': 1},
            {'timestamp': '2023-01-01T22:20:00', 'movement': 0}
        ]
        
        metrics = self.analyzer.calculate_quality_metrics(mock_data)
        self.assertIn('duration', metrics)
        self.assertIn('restlessness_index', metrics)
        self.assertIn('quality_score', metrics)

if __name__ == '__main__':
    unittest.main()