import numpy as np
import pandas as pd
from scipy import signal

def detect_sleep_patterns(data):
    """
    Detect sleep patterns from accelerometer and gyroscope data
    
    Args:
        data (DataFrame): Sensor data with timestamp, x, y, z columns
    
    Returns:
        dict: Sleep quality metrics and patterns
    """
    # Normalize the data
    normalized_data = (data[['x', 'y', 'z']] - data[['x', 'y', 'z']].mean()) / data[['x', 'y', 'z']].std()
    
    # Calculate movement intensity
    intensity = np.sqrt(normalized_data['x']**2 + normalized_data['y']**2 + normalized_data['z']**2)
    
    # Detect sleep periods (low movement)
    threshold = 0.5
    sleep_periods = intensity < threshold
    
    # Calculate sleep quality metrics
    total_samples = len(intensity)
    sleep_duration = np.sum(sleep_periods) / 60  # minutes
    movement_intensity = np.mean(intensity[sleep_periods])
    
    return {
        'sleep_duration': sleep_duration,
        'avg_movement_intensity': movement_intensity,
        'sleep_quality_score': 100 - (movement_intensity * 10),
        'total_samples': total_samples
    }