import pytest
import numpy as np
import pandas as pd
from analysis import detect_sleep_patterns

def test_detect_sleep_patterns():
    # Create mock data with clear sleep pattern
    data = pd.DataFrame({
        'timestamp': range(100),
        'x': [0.1] * 50 + [2.0] * 50,
        'y': [0.1] * 50 + [2.0] * 50,
        'z': [0.1] * 50 + [2.0] * 50
    })
    
    result = detect_sleep_patterns(data)
    
    assert result['sleep_duration'] > 0
    assert result['avg_movement_intensity'] < 1.0  # Should be low during sleep
    assert result['sleep_quality_score'] > 0
    assert result['total_samples'] == 100