"""
Data Collector Module

Collects sleep data from smartphone sensors.
"""

import random
from datetime import datetime, timedelta

class SensorDataCollector:
    """Simulates collection of sensor data from smartphone sensors."""
    
    def __init__(self):
        self.data = []
        
    def collect_accelerometer_data(self, duration_minutes=10):
        """Collect simulated accelerometer data."""
        data_points = []
        for i in range(duration_minutes * 60):  # 60 samples per minute
            timestamp = datetime.now() + timedelta(seconds=i)
            x = random.uniform(-1.0, 1.0)
            y = random.uniform(-1.0, 1.0)
            z = random.uniform(-1.0, 1.0)
            data_points.append({
                'timestamp': timestamp,
                'sensor': 'accelerometer',
                'x': x,
                'y': y,
                'z': z
            })
        return data_points
        
    def collect_gyroscope_data(self, duration_minutes=10):
        """Collect simulated gyroscope data."""
        data_points = []
        for i in range(duration_minutes * 60):  # 60 samples per minute
            timestamp = datetime.now() + timedelta(seconds=i)
            x = random.uniform(-5.0, 5.0)
            y = random.uniform(-5.0, 5.0)
            z = random.uniform(-5.0, 5.0)
            data_points.append({
                'timestamp': timestamp,
                'sensor': 'gyroscope',
                'x': x,
                'y': y,
                'z': z
            })
        return data_points
        
    def collect_microphone_data(self, duration_minutes=10):
        """Collect simulated microphone data."""
        data_points = []
        for i in range(duration_minutes * 60):  # 60 samples per minute
            timestamp = datetime.now() + timedelta(seconds=i)
            amplitude = random.uniform(0.0, 1.0)
            frequency = random.uniform(20.0, 20000.0)
            data_points.append({
                'timestamp': timestamp,
                'sensor': 'microphone',
                'amplitude': amplitude,
                'frequency': frequency
            })
        return data_points
        
    def collect_all_data(self, duration_minutes=10):
        """Collect all sensor data."""
        all_data = []
        all_data.extend(self.collect_accelerometer_data(duration_minutes))
        all_data.extend(self.collect_gyroscope_data(duration_minutes))
        all_data.extend(self.collect_microphone_data(duration_minutes))
        return all_data
