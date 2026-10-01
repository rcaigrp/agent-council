# Test file for data_analyzer.py
import sys
import os
sys.path.append(os.path.dirname(os.path.abspath(__file__)))
from data_analyzer import analyze_sleep_data

def test_analyze_sleep_data():
    # Mock sleep data
    sleep_data = [
        {'timestamp': 1, 'acceleration': 0.1},
        {'timestamp': 2, 'acceleration': 0.2},
        {'timestamp': 3, 'acceleration': 0.05}
    ]
    
    # Test basic functionality
    result = analyze_sleep_data(sleep_data)
    assert 'sleep_duration' in result
    assert 'restlessness_index' in result
    print('test_data_analyzer.py: PASSED')

if __name__ == '__main__':
    test_analyze_sleep_data()
