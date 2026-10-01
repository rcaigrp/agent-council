import unittest
from data_analyzer import analyze_sleep_pattern

class TestDataAnalyzer(unittest.TestCase):
    def test_analyze_sleep_pattern(self):
        # Mock data for testing
        sleep_data = {'duration': 8, 'quality_score': 7.5}
        result = analyze_sleep_pattern(sleep_data)
        self.assertEqual(result['quality'], 7.5)

if __name__ == '__main__':
    unittest.main()