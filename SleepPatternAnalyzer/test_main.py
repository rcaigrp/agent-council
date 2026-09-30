import unittest
from main import SleepDataCollector


class TestSleepDataCollector(unittest.TestCase):
    def setUp(self):
        self.collector = SleepDataCollector()
        
    def test_initialization(self):
        self.assertFalse(self.collector.is_recording)
        self.assertEqual(len(self.collector.data_buffer), 0)
        
    def test_start_recording(self):
        self.collector.start_recording()
        self.assertTrue(self.collector.is_recording)
        
    def test_stop_recording(self):
        self.collector.start_recording()
        self.collector.stop_recording()
        self.assertFalse(self.collector.is_recording)
        
    def test_collect_accelerometer_data(self):
        self.collector.start_recording()
        data_point = self.collector.collect_accelerometer_data(1, 2, 3)
        self.assertIsNotNone(data_point)
        self.assertEqual(data_point['sensor'], 'accelerometer')
        
    def test_collect_gyroscope_data(self):
        self.collector.start_recording()
        data_point = self.collector.collect_gyroscope_data(1, 2, 3)
        self.assertIsNotNone(data_point)
        self.assertEqual(data_point['sensor'], 'gyroscope')
        
    def test_get_data(self):
        self.collector.start_recording()
        self.collector.collect_accelerometer_data(1, 2, 3)
        self.collector.collect_gyroscope_data(4, 5, 6)
        data = self.collector.get_data()
        self.assertEqual(len(data), 2)

if __name__ == '__main__':
    unittest.main()