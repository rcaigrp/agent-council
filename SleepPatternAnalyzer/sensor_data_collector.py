# Sleep Pattern Analyzer - Sensor Data Collector
import random
import time
from datetime import datetime, timedelta

class SensorDataCollector:
    def __init__(self):
        self.data = []
        
    def generate_mock_accelerometer_data(self, duration_minutes=60):
        """Generate mock accelerometer data for sleep tracking"""
        start_time = datetime.now()
        data_points = []
        
        # Generate data points every 10 seconds
        for i in range(0, duration_minutes * 60, 10):
            timestamp = start_time + timedelta(seconds=i)
            # Simulate movement data (x, y, z acceleration values)
            x = random.uniform(-1.0, 1.0)
            y = random.uniform(-1.0, 1.0)
            z = random.uniform(-1.0, 1.0)
            
            data_points.append({
                'timestamp': timestamp.isoformat(),
                'x': x,
                'y': y,
                'z': z
            })
        
        return data_points
    
    def get_sleep_periods(self, data):
        """Identify sleep periods from accelerometer data"""
        sleep_periods = []
        
        # Simple algorithm: detect periods with low movement activity
        threshold = 0.1  # Movement threshold
        
        # Check consecutive points for low movement
        i = 0
        while i < len(data) - 1:
            current_point = data[i]
            next_point = data[i + 1]
            
            # Calculate movement magnitude
            current_movement = abs(current_point['x']) + abs(current_point['y']) + abs(current_point['z'])
            next_movement = abs(next_point['x']) + abs(next_point['y']) + abs(next_point['z'])
            
            # If both points show low movement, consider it a sleep period
            if current_movement < threshold and next_movement < threshold:
                sleep_periods.append({
                    'start': current_point['timestamp'],
                    'end': next_point['timestamp'],
                    'duration_minutes': 10/60  # 10 seconds in minutes
                })
                
                # Skip ahead to avoid overlapping periods
                i += 2
            else:
                i += 1
        
        return sleep_periods