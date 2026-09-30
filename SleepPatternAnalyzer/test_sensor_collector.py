# Test for Sensor Data Collector
import unittest
from sensor_data_collector import SensorDataCollector

class TestSensorDataCollector(unittest.TestCase):
    def setUp(self):
        self.collector = SensorDataCollector()
        
    def test_generate_mock_accelerometer_data(self):
        data = self.collector.generate_mock_accelerometer_data(10)  # 10 minutes
        self.assertEqual(len(data), 60)  # 10 minutes * 6 data points per minute
        
    def test_get_sleep_periods(self):
        # Create mock data with known sleep periods
        data = [
            {'timestamp': '2023-01-01T00:00:00', 'x': 0.05, 'y': 0.03, 'z': 0.02},
            {'timestamp': '2023-01-01T00:00:10', 'x': 0.01, 'y': 0.02, 'z': 0.01},
            {'timestamp': '2023-01-01T00:00:20', 'x': 0.03, 'y': 0.04, 'z': 0.05}
        ]
        
        sleep_periods = self.collector.get_sleep_periods(data)
        # Should detect one sleep period
        self.assertEqual(len(sleep_periods), 1)
        
        # Verify the first sleep period properties
        sleep_period = sleep_periods[0]
        self.assertEqual(sleep_period['start'], '2023-01-01T00:00:00')
        self.assertEqual(sleep_period['end'], '2023-01-01T00:00:10')

if __name__ == '__main__':
    unittest.main()