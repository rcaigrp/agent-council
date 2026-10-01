import sys
import os
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

import unittest
from data_analyzer import DataAnalyzer

class TestDataAnalyzer(unittest.TestCase):
    def test_analyze_sleep_patterns(self):
        analyzer = DataAnalyzer()
        sleep_data = {'duration': 8, 'quality': 0.9}
        result = analyzer.analyze_sleep_patterns(sleep_data)
        self.assertIsNotNone(result)
        self.assertIsInstance(result, dict)

if __name__ == '__main__':
    unittest.main()