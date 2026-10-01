import sys
import os
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from data_analyzer import analyze_sleep_pattern, calculate_sleep_quality

def test_analyze_sleep_pattern():
    result = analyze_sleep_pattern([1, 2, 3, 4, 5])
    assert result is not None
    print("analyze_sleep_pattern test passed")

def test_calculate_sleep_quality():
    result = calculate_sleep_quality(8, 10)
    assert result >= 0 and result <= 100
    print("calculate_sleep_quality test passed")

if __name__ == "__main__":
    test_analyze_sleep_pattern()
    test_calculate_sleep_quality()
    print("All tests passed!")