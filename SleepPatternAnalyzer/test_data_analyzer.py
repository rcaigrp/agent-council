import unittest
from data_analyzer import DataAnalyzer

class TestDataAnalyzer(unittest.TestCase):
    def test_analyze_sleep_patterns(self):
        analyzer = DataAnalyzer()
        result = analyzer.analyze_sleep_patterns([])
        self.assertIsNotNone(result)

if __name__ == '__main__':
    unittest.main()