import pandas as pd
import numpy as np
from datetime import datetime, timedelta

class SleepDataAnalyzer:
    def __init__(self):
        self.sleep_threshold = 0.1  # Movement threshold for sleep detection
        
    def analyze_sleep_patterns(self, sensor_data):
        """
        Analyze sensor data to identify sleep patterns and calculate quality metrics
        
        Args:
            sensor_data (DataFrame): Sensor data with timestamp and movement columns
            
        Returns:
            dict: Sleep analysis results including periods, duration, and quality metrics
        """
        # Identify sleep periods based on low movement
        sleep_periods = self._detect_sleep_periods(sensor_data)
        
        # Calculate sleep quality metrics
        quality_metrics = self._calculate_quality_metrics(sensor_data, sleep_periods)
        
        return {
            'sleep_periods': sleep_periods,
            'quality_metrics': quality_metrics
        }
        
    def _detect_sleep_periods(self, sensor_data):
        """
        Detect periods of sleep based on movement patterns
        """
        # Group data by 5-minute intervals
        data_grouped = sensor_data.resample('5T').mean()
        
        # Identify periods where movement is below threshold
        sleep_mask = data_grouped['movement'] < self.sleep_threshold
        
        # Find consecutive periods of sleep
        sleep_periods = []
        in_sleep_period = False
        start_time = None
        
        for idx, is_sleep in enumerate(sleep_mask):
            if is_sleep and not in_sleep_period:
                # Start of sleep period
                in_sleep_period = True
                start_time = data_grouped.index[idx]
            elif not is_sleep and in_sleep_period:
                # End of sleep period
                in_sleep_period = False
                end_time = data_grouped.index[idx]
                sleep_periods.append({
                    'start': start_time,
                    'end': end_time,
                    'duration': (end_time - start_time).total_seconds() / 60  # minutes
                })
        
        return sleep_periods
        
    def _calculate_quality_metrics(self, sensor_data, sleep_periods):
        """
        Calculate sleep quality metrics from sensor data and sleep periods
        """
        if not sleep_periods:
            return {'duration': 0, 'restlessness': 0, 'movement_intensity': 0}
        
        # Total sleep duration
        total_duration = sum(period['duration'] for period in sleep_periods)
        
        # Calculate restlessness (high movement during sleep periods)
        restlessness_score = 0
        for period in sleep_periods:
            period_data = sensor_data[(sensor_data.index >= period['start']) & 
                                    (sensor_data.index <= period['end'])]
            avg_movement = period_data['movement'].mean()
            # Higher movement during sleep indicates restlessness
            restlessness_score += avg_movement
        
        # Average movement intensity across all data
        avg_movement_intensity = sensor_data['movement'].mean()
        
        return {
            'duration': total_duration,
            'restlessness': restlessness_score,
            'movement_intensity': avg_movement_intensity
        }