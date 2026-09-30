import unittest
from sensor_data_collector import SensorDataCollector

class TestDataCollector(unittest.TestCase):
    def setUp(self):
        self.collector = SensorDataCollector()

    def test_collect_sleep_data(self):
        data = self.collector.collect_sleep_data()
        self.assertIn('timestamp', data)
        self.assertIn('heart_rate', data)
        self.assertIn('body_temperature', data)
        self.assertIn('movement', data)
        self.assertIn('light_level', data)

    def test_get_recent_data(self):
        # Collect some data
        for _ in range(5):
            self.collector.collect_sleep_data()
        
        recent_data = self.collector.get_recent_data(minutes=10)
        self.assertEqual(len(recent_data), 5)

if __name__ == '__main__':
    unittest.main()