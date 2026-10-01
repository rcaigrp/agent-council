import sys
import os
sys.path.append(os.path.dirname(os.path.abspath(__file__)))
from data_analyzer import analyze_sleep_pattern, calculate_sleep_quality

def test_analyze_sleep_pattern():
    # Test basic functionality
    result = analyze_sleep_pattern([1, 2, 3, 4, 5])
    assert result is not None
    assert 'duration' in result
    assert 'quality_score' in result
    print('test_analyze_sleep_pattern: PASSED')

def test_calculate_sleep_quality():
    # Test basic functionality with correct parameters
    quality = calculate_sleep_quality(8, 0.9)
    # Should return reasonable value based on implementation
    assert isinstance(quality, int)
    print('test_calculate_sleep_quality: PASSED')

if __name__ == '__main__':
    test_analyze_sleep_pattern()
    test_calculate_sleep_quality()
    print('All tests passed!')