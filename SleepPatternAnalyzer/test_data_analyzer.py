import sys
import os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from data_analyzer import analyze_sleep_pattern, calculate_sleep_quality

def test_analyze_sleep_pattern():
    # Test with sample data
    result = analyze_sleep_pattern([1, 2, 3, 4, 5])
    assert result is not None
    assert 'duration' in result
    assert 'quality_score' in result
    print('analyze_sleep_pattern test passed')

def test_calculate_sleep_quality():
    # Test with sample data - passing numbers, not lists
    result = calculate_sleep_quality(7, 85, 0.3)
    assert result is not None
    assert isinstance(result, (int, float))
    print('calculate_sleep_quality test passed')

def main():
    test_analyze_sleep_pattern()
    test_calculate_sleep_quality()
    print('All tests passed!')

if __name__ == '__main__':
    main()