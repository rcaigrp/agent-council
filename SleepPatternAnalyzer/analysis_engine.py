import pandas as pd
import numpy as np
from datetime import datetime, timedelta

class SleepAnalysisEngine:
    def __init__(self):
        self.sleep_quality_threshold = 0.7
        
    def analyze_sleep_patterns(self, sensor_data):
        """Analyze sensor data to identify sleep patterns and calculate quality metrics."""
        # Convert to DataFrame if it's a dict
        if isinstance(sensor_data, dict):
            df = pd.DataFrame(sensor_data)
        else:
            df = sensor_data
        
        # Calculate movement intensity
        df['movement_intensity'] = np.sqrt(df['x_acceleration']**2 + df['y_acceleration']**2 + df['z_acceleration']**2)
        
        # Detect sleep periods based on low movement
        sleep_periods = self._detect_sleep_periods(df)
        
        # Calculate quality metrics
        quality_metrics = self._calculate_quality_metrics(df, sleep_periods)
        
        return {
            'sleep_periods': sleep_periods,
            'quality_metrics': quality_metrics
        }
    
    def _detect_sleep_periods(self, df):
        """Detect periods of sleep based on movement patterns."""
        # Simple threshold-based detection
        low_movement_threshold = 0.1
        df['is_low_movement'] = df['movement_intensity'] < low_movement_threshold
        
        # Group consecutive low movement periods
        df['group'] = (df['is_low_movement'] != df['is_low_movement'].shift()).cumsum()
        
        sleep_periods = []
        for group_id, group_data in df.groupby('group'):
            if group_data['is_low_movement'].all():
                start_time = group_data.index.min()
                end_time = group_data.index.max()
                duration = (end_time - start_time).total_seconds() / 60  # minutes
                sleep_periods.append({
                    'start': start_time,
                    'end': end_time,
                    'duration_minutes': duration
                })
        
        return sleep_periods
    
    def _calculate_quality_metrics(self, df, sleep_periods):
        """Calculate sleep quality metrics from the data."""
        if not sleep_periods:
            return {'average_duration': 0, 'quality_score': 0}
        
        # Calculate average sleep duration
        total_duration = sum(period['duration_minutes'] for period in sleep_periods)
        avg_duration = total_duration / len(sleep_periods) if sleep_periods else 0
        
        # Calculate movement during sleep (lower is better)
        avg_movement_during_sleep = df[df['movement_intensity'] < 0.1]['movement_intensity'].mean() if not df[df['movement_intensity'] < 0.1].empty else 0
        
        # Quality score: higher when less movement and longer durations
        quality_score = max(0, min(100, (1 - avg_movement_during_sleep) * 50 + avg_duration / 60 * 2))
        
        return {
            'average_duration': avg_duration,
            'quality_score': quality_score,
            'total_sleep_periods': len(sleep_periods)
        }