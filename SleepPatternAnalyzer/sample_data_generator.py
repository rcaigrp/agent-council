import pandas as pd
import numpy as np
from datetime import datetime, timedelta
import random

def generate_sample_sleep_data(duration_minutes=120):
    """Generate sample sleep data for testing."""
    start_time = datetime.now()
    timestamps = [start_time + timedelta(minutes=i) for i in range(duration_minutes)]
    
    # Generate realistic sensor data
    # For sleep periods (first 60 minutes): low movement
    x_accel = []
    y_accel = []
    z_accel = []
    
    # First 60 minutes: low movement (sleep)
    for i in range(60):
        x_accel.append(random.uniform(-0.1, 0.1))
        y_accel.append(random.uniform(-0.1, 0.1))
        z_accel.append(random.uniform(-0.1, 0.1))
    
    # Next 60 minutes: higher movement (awake)
    for i in range(60):
        x_accel.append(random.uniform(0.5, 1.5))
        y_accel.append(random.uniform(0.5, 1.5))
        z_accel.append(random.uniform(0.5, 1.5))
    
    return {
        'timestamp': timestamps,
        'x_acceleration': x_accel,
        'y_acceleration': y_accel,
        'z_acceleration': z_accel
    }