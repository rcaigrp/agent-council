import pandas as pd
import numpy as np
from datetime import datetime, timedelta

class SleepQualityAnalyzer:
    def __init__(self):
        # Thresholds for movement detection (adjustable based on testing)
        self.movement_threshold = 0.1  # Movement magnitude threshold
        self.sleep_window_minutes = 30  # Minimum window for sleep period identification
        
    def analyze_sleep_periods(self, sensor_data):
        """
        Analyze sensor data to identify sleep periods
        
        Args:
            sensor_data (DataFrame): Sensor data with timestamp and movement columns
            
        Returns:
            list: List of dictionaries containing sleep period information
        """
        # Convert to DataFrame if it's a dict
        if isinstance(sensor_data, dict):
            df = pd.DataFrame(sensor_data)
        else:
            df = sensor_data.copy()
        
        # Calculate movement magnitude (assuming columns 'x', 'y', 'z' for accelerometer)
        df['movement_magnitude'] = np.sqrt(df['x']**2 + df['y']**2 + df['z']**2)
        
        # Identify sleep periods based on low movement
        sleep_mask = df['movement_magnitude'] < self.movement_threshold
        
        # Find continuous periods of low movement
        sleep_periods = []
        in_sleep = False
        sleep_start = None
        
        for idx, (timestamp, row) in enumerate(df.iterrows()):
            if not in_sleep and sleep_mask.iloc[idx]:
                # Start of a sleep period
                in_sleep = True
                sleep_start = timestamp
            elif in_sleep and not sleep_mask.iloc[idx]:
                # End of a sleep period
                in_sleep = False
                sleep_end = timestamp
                
                # Only consider periods that are long enough
                if (sleep_end - sleep_start).total_seconds() >= self.sleep_window_minutes * 60:
                    sleep_periods.append({
                        'start': sleep_start,
                        'end': sleep_end,
                        'duration_minutes': (sleep_end - sleep_start).total_seconds() / 60
                    })
        
        return sleep_periods
    
    def calculate_sleep_quality_metrics(self, sensor_data):
        """
        Calculate sleep quality metrics from sensor data
        
        Args:
            sensor_data (DataFrame): Sensor data with timestamp and movement columns
            
        Returns:
            dict: Dictionary containing sleep quality metrics
        """
        # Calculate movement statistics
        df = sensor_data.copy()
        df['movement_magnitude'] = np.sqrt(df['x']**2 + df['y']**2 + df['z']**2)
        
        total_duration = len(df) * 10  # Assuming 10 second intervals (adjust as needed)
        avg_movement = df['movement_magnitude'].mean()
        max_movement = df['movement_magnitude'].max()
        std_movement = df['movement_magnitude'].std()
        
        # Calculate sleep quality score (0-100)
        # Lower average movement = better sleep quality
        sleep_score = max(0, 100 - (avg_movement * 10))
        
        return {
            'sleep_score': round(sleep_score, 2),
            'average_movement': round(avg_movement, 2),
            'max_movement': round(max_movement, 2),
            'movement_std': round(std_movement, 2),
            'total_duration_minutes': total_duration / 60
        }
    
    def generate_sleep_report(self, sensor_data):
        """
        Generate comprehensive sleep report from sensor data
        
        Args:
            sensor_data (DataFrame): Sensor data with timestamp and movement columns
            
        Returns:
            dict: Complete sleep analysis report
        """
        sleep_periods = self.analyze_sleep_periods(sensor_data)
        metrics = self.calculate_sleep_quality_metrics(sensor_data)
        
        return {
            'sleep_periods': sleep_periods,
            'metrics': metrics,
            'total_sleep_periods': len(sleep_periods)
        }