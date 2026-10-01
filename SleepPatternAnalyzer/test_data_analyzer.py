import sys
import os
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

def test_analyze_sleep_pattern():
    from data_analyzer import analyze_sleep_pattern
    # Test with sample data
    result = analyze_sleep_pattern([8, 7, 6, 9, 8])
    assert isinstance(result, dict)
    assert 'avg_duration' in result

def test_calculate_sleep_quality():
    from data_analyzer import calculate_sleep_quality
    # Test with sample data
    result = calculate_sleep_quality(8.0, 15, 5)
    assert isinstance(result, float)
    assert 0 <= result <= 100