import unittest
from data_analyzer import analyze_sleep_pattern, calculate_sleep_quality

class TestDataAnalyzer(unittest.TestCase):
    def test_analyze_sleep_pattern(self):
        # Test basic functionality
        result = analyze_sleep_pattern([7, 8, 6, 9])
        self.assertIsNotNone(result)
        
    def test_calculate_sleep_quality(self):
        # Test quality calculation
        quality = calculate_sleep_quality(8, 0.8)
        self.assertEqual(quality, 4.0)

if __name__ == '__main__':
    unittest.main()