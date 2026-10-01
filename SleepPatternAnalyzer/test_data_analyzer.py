import sys
import os
sys.path.append(os.path.dirname(os.path.abspath(__file__)))
from data_analyzer import analyze_sleep_pattern, calculate_sleep_quality

def test_analyze_sleep_pattern():
    # Test basic functionality
    result = analyze_sleep_pattern([1, 2, 3, 4, 5])
    assert result is not None
    assert 'total_sleep' in result

def test_calculate_sleep_quality():
    # Test quality calculation with proper dict input
    result = calculate_sleep_quality({'quality_score': 85})
    assert result == 85

if __name__ == '__main__':
    test_analyze_sleep_pattern()
    test_calculate_sleep_quality()
    print('All tests passed!')