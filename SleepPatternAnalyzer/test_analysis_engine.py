import unittest
import pandas as pd
import numpy as np
from datetime import datetime, timedelta
from analysis_engine import SleepAnalysisEngine

class TestSleepAnalysisEngine(unittest.TestCase):
    def setUp(self):
        self.engine = SleepAnalysisEngine()
        
    def test_analyze_sleep_patterns_with_sample_data(self):
        # Create sample data with clear sleep periods
        start_time = datetime.now()
        timestamps = [start_time + timedelta(minutes=i) for i in range(100)]
        
        # Simulate movement data where first 40 minutes are low movement (sleep)
        x_accel = [0.05] * 40 + [0.8] * 60
        y_accel = [0.03] * 40 + [0.9] * 60
        z_accel = [0.02] * 40 + [1.0] * 60
        
        data = {
            'timestamp': timestamps,
            'x_acceleration': x_accel,
            'y_acceleration': y_accel,
            'z_acceleration': z_accel
        }
        
        result = self.engine.analyze_sleep_patterns(data)
        
        # Check that we found at least one sleep period
        self.assertGreater(len(result['sleep_periods']), 0)
        
        # Check quality metrics exist
        self.assertIn('average_duration', result['quality_metrics'])
        self.assertIn('quality_score', result['quality_metrics'])
        
    def test_empty_data_handling(self):
        # Test with empty data
        result = self.engine.analyze_sleep_patterns([])
        
        self.assertEqual(result['sleep_periods'], [])
        self.assertEqual(result['quality_metrics']['average_duration'], 0)
        self.assertEqual(result['quality_metrics']['quality_score'], 0)

if __name__ == '__main__':
    unittest.main()