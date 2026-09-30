import pandas as pd
from datetime import datetime

class DataAnalyzer:
    def __init__(self):
        pass

    def detect_sleep_periods(self, sensor_data):
        # Convert timestamp strings to datetime objects
        for entry in sensor_data:
            entry['timestamp'] = datetime.fromisoformat(entry['timestamp'].replace('Z', '+00:00'))
        
        # Simple logic to group consecutive low movement periods as sleep
        sleep_periods = []
        current_period = None
        
        for entry in sensor_data:
            if entry['movement'] <= 2 and current_period is None:
                # Start new sleep period
                current_period = {'start': entry['timestamp'], 'end': entry['timestamp']}
            elif entry['movement'] <= 2 and current_period is not None:
                # Extend current sleep period
                current_period['end'] = entry['timestamp']
            elif entry['movement'] > 2 and current_period is not None:
                # End current sleep period
                sleep_periods.append(current_period)
                current_period = None
        
        # Add final period if still active
        if current_period:
            sleep_periods.append(current_period)
        
        return sleep_periods

    def calculate_quality_metrics(self, sensor_data):
        # Calculate duration in hours
        if len(sensor_data) < 2:
            duration = 0
        else:
            start_time = datetime.fromisoformat(sensor_data[0]['timestamp'].replace('Z', '+00:00'))
            end_time = datetime.fromisoformat(sensor_data[-1]['timestamp'].replace('Z', '+00:00'))
            duration = (end_time - start_time).total_seconds() / 3600
        
        # Calculate restlessness index (higher is more restless)
        movement_values = [entry['movement'] for entry in sensor_data]
        if len(movement_values) == 0:
            restlessness_index = 0
        else:
            avg_movement = sum(movement_values) / len(movement_values)
            # Normalize restlessness index between 0 and 1
            restlessness_index = min(avg_movement / 5.0, 1.0)
        
        # Simple quality score based on duration and restlessness
        if duration < 6:
            base_score = 30
        elif duration < 8:
            base_score = 70
        else:
            base_score = 90
        
        # Adjust for restlessness (lower is better)
        quality_score = max(0, base_score - (restlessness_index * 50))
        
        return {
            'duration': duration,
            'restlessness_index': restlessness_index,
            'quality_score': quality_score
        }