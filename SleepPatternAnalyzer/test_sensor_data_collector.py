import unittest
from sensor_data_collector import SensorDataCollector

class TestSensorDataCollector(unittest.TestCase):
    def test_collect_movement_data(self):
        collector = SensorDataCollector()
        # Mock data for testing
        mock_data = [1, 2, 3, 4, 5]
        result = collector.collect_movement_data(mock_data)
        self.assertEqual(result, mock_data)
        
    def test_collect_heart_rate_data(self):
        collector = SensorDataCollector()
        # Mock data for testing
        mock_data = [70, 72, 75, 73, 71]
        result = collector.collect_heart_rate_data(mock_data)
        self.assertEqual(result, mock_data)
        
    def test_collect_light_level_data(self):
        collector = SensorDataCollector()
        # Mock data for testing
        mock_data = [50, 60, 70, 80, 90]
        result = collector.collect_light_level_data(mock_data)
        self.assertEqual(result, mock_data)

if __name__ == '__main__':
    unittest.main()