import sys
import os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from data_analyzer import analyze_sleep_pattern, calculate_sleep_quality

def test_analyze_sleep_pattern():
    # Test with sample data
    result = analyze_sleep_pattern([1, 2, 3, 4, 5])
    assert result is not None
    print('analyze_sleep_pattern test passed')

def test_calculate_sleep_quality():
    # Test with sample data including required sleep_efficiency as a list
    result = calculate_sleep_quality([1, 2, 3, 4, 5], [85])
    assert result is not None
    print('calculate_sleep_quality test passed')

if __name__ == '__main__':
    try:
        test_analyze_sleep_pattern()
        test_calculate_sleep_quality()
        print('All tests passed!')
    except Exception as e:
        print(f'Test failed: {e}')
        sys.exit(1)