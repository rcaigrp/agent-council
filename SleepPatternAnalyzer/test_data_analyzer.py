# Test data analyzer module

import unittest
from data_analyzer import DataAnalyzer

class TestDataAnalyzer(unittest.TestCase):
    def test_analyze_sleep(self):
        analyzer = DataAnalyzer()
        result = analyzer.analyze_sleep([1, 2, 3, 4, 5])
        self.assertEqual(result['duration'], 5)
        self.assertEqual(result['restlessness_index'], 3.0)
        
    def test_analyze_empty_data(self):
        analyzer = DataAnalyzer()
        result = analyzer.analyze_sleep([])
        self.assertEqual(result['duration'], 0)
        self.assertEqual(result['restlessness_index'], 0)

if __name__ == '__main__':
    unittest.main()