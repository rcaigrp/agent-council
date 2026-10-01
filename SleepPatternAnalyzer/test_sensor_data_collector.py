import unittest
from sensor_data_collector import SensorDataCollector

class TestSensorDataCollector(unittest.TestCase):
    def test_collect_data(self):
        collector = SensorDataCollector()
        data = collector.collect_data()
        self.assertIsNotNone(data)

if __name__ == '__main__':
    unittest.main()