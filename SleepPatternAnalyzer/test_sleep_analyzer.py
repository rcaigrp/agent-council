import unittest
import pandas as pd
import numpy as np
from datetime import datetime, timedelta
from sleep_quality_analyzer import SleepQualityAnalyzer

class TestSleepQualityAnalyzer(unittest.TestCase):
    def setUp(self):
        self.analyzer = SleepQualityAnalyzer()
    
    def test_analyze_sleep_periods(self):
        # Create mock sensor data with clear sleep periods
        timestamps = [datetime(2023, 1, 1, 22, 0) + timedelta(minutes=i*10) for i in range(60)]
        
        # Simulate low movement during sleep (0.05) and high movement during awake time
        x = [0.05] * 30 + [0.8] * 30  # First 30 intervals are sleep, last 30 are awake
        y = [0.05] * 30 + [0.8] * 30
        z = [0.05] * 30 + [0.8] * 30
        
        df = pd.DataFrame({
            'timestamp': timestamps,
            'x': x,
            'y': y,
            'z': z
        })
        
        result = self.analyzer.analyze_sleep_periods(df)
        
        # Should find one sleep period
        self.assertEqual(len(result), 1)
        self.assertGreater(result[0]['duration_minutes'], 25)  # At least 25 minutes
    
    def test_calculate_sleep_quality_metrics(self):
        # Create mock sensor data
        timestamps = [datetime(2023, 1, 1, 22, 0) + timedelta(minutes=i*10) for i in range(60)]
        
        # Low movement data (better sleep)
        x = [0.05] * 60
        y = [0.05] * 60
        z = [0.05] * 60
        
        df = pd.DataFrame({
            'timestamp': timestamps,
            'x': x,
            'y': y,
            'z': z
        })
        
        result = self.analyzer.calculate_sleep_quality_metrics(df)
        
        # Should have high sleep score
        self.assertGreater(result['sleep_score'], 80)
        self.assertAlmostEqual(result['average_movement'], 0.05, places=2)
    
    def test_generate_sleep_report(self):
        # Create mock sensor data
        timestamps = [datetime(2023, 1, 1, 22, 0) + timedelta(minutes=i*10) for i in range(60)]
        
        # Low movement data (better sleep)
        x = [0.05] * 60
        y = [0.05] * 60
        z = [0.05] * 60
        
        df = pd.DataFrame({
            'timestamp': timestamps,
            'x': x,
            'y': y,
            'z': z
        })
        
        result = self.analyzer.generate_sleep_report(df)
        
        # Should have sleep report with correct structure
        self.assertIn('sleep_periods', result)
        self.assertIn('metrics', result)
        self.assertIn('total_sleep_periods', result)
        
if __name__ == '__main__':
    unittest.main()