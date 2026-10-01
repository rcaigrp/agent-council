import unittest
from data_analyzer import analyze_sleep_pattern

class TestDataAnalyzer(unittest.TestCase):
    def test_analyze_sleep_pattern(self):
        # Test basic functionality
        result = analyze_sleep_pattern([])
        self.assertIsNotNone(result)

if __name__ == '__main__':
    unittest.main()