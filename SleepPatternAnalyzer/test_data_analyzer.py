import unittest
from data_analyzer import analyze_sleep_pattern, calculate_sleep_quality

class TestDataAnalyzer(unittest.TestCase):
    def test_analyze_sleep_pattern(self):
        # Test with sample data
        sleep_data = [7, 8, 6, 9, 7]
        result = analyze_sleep_pattern(sleep_data)
        self.assertIsNotNone(result)
        
    def test_calculate_sleep_quality(self):
        # Test quality calculation
        quality = calculate_sleep_quality(7.5, 8, 0.8)
        self.assertIsInstance(quality, float)

if __name__ == '__main__':
    unittest.main()