import sys
import os
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from data_analyzer import analyze_sleep_pattern, calculate_sleep_quality

def test_analyze_sleep_pattern():
    # Test with sample data
    sleep_data = [7, 8, 6, 9, 7]
    result = analyze_sleep_pattern(sleep_data)
    assert result is not None
    print('test_analyze_sleep_pattern passed')

def test_calculate_sleep_quality():
    # Test with sample data
    sleep_duration = 8
    quality = calculate_sleep_quality(sleep_duration)
    assert quality >= 0 and quality <= 100
    print('test_calculate_sleep_quality passed')

if __name__ == '__main__':
    test_analyze_sleep_pattern()
    test_calculate_sleep_quality()
    print('All tests passed!')