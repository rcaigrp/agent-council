import unittest
import pandas as pd
import numpy as np
from datetime import datetime, timedelta
from data_analyzer import SleepDataAnalyzer

class TestDataAnalyzer(unittest.TestCase):
    
    def setUp(self):
        self.analyzer = SleepDataAnalyzer()
        
    def test_sleep_detection_basic(self):
        # Create mock sensor data with clear sleep and awake periods
        timestamps = pd.date_range(start='2023-01-01', periods=100, freq='5T')
        # Low movement for sleep (0.05), high for awake (0.8)
        movements = [0.05] * 40 + [0.8] * 20 + [0.05] * 40
        
        data = pd.DataFrame({
            'timestamp': timestamps,
            'movement': movements
        })
        data.set_index('timestamp', inplace=True)
        
        result = self.analyzer.analyze_sleep_patterns(data)
        
        # Should detect 2 sleep periods
        self.assertEqual(len(result['sleep_periods']), 2)
        
    def test_quality_metrics_calculation(self):
        timestamps = pd.date_range(start='2023-01-01', periods=100, freq='5T')
        movements = [0.05] * 40 + [0.8] * 20 + [0.05] * 40
        
        data = pd.DataFrame({
            'timestamp': timestamps,
            'movement': movements
        })
        data.set_index('timestamp', inplace=True)
        
        result = self.analyzer.analyze_sleep_patterns(data)
        metrics = result['quality_metrics']
        
        # Check that all metrics are calculated
        self.assertIn('duration', metrics)
        self.assertIn('restlessness', metrics)
        self.assertIn('movement_intensity', metrics)
        
if __name__ == '__main__':
    unittest.main()