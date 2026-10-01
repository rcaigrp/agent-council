import sys
import os
sys.path.append(os.path.dirname(os.path.abspath(__file__)))
from data_analyzer import analyze_sleep_pattern, calculate_sleep_quality

def test_analyze_sleep_pattern():
    # Test case 1: Normal sleep pattern
    sleep_data = [7, 8, 6, 9, 7]
    result = analyze_sleep_pattern(sleep_data)
    assert result == 'Normal'
    
    # Test case 2: Poor sleep pattern
    sleep_data = [4, 5, 3, 6, 4]
    result = analyze_sleep_pattern(sleep_data)
    assert result == 'Poor'
    
    print('All tests passed for data_analyzer!')

test_analyze_sleep_pattern()