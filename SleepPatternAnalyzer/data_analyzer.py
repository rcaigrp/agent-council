import statistics
from collections import defaultdict

class SleepDataAnalyzer:
    def __init__(self):
        pass

    def analyze_sleep_quality(self, data):
        if not data:
            return {'quality': 0, 'duration': 0}
        
        # Calculate sleep duration (assuming data is collected every minute)
        duration = len(data)
        
        # Calculate quality metrics
        heart_rates = [d['heart_rate'] for d in data]
        body_temperatures = [d['body_temperature'] for d in data]
        movements = [d['movement'] for d in data]
        
        avg_heart_rate = statistics.mean(heart_rates)
        avg_body_temp = statistics.mean(body_temperatures)
        avg_movement = statistics.mean(movements)
        
        # Simple quality score calculation
        heart_rate_score = max(0, 100 - abs(avg_heart_rate - 60))
        temp_score = max(0, 100 - abs(avg_body_temp - 37.0))
        movement_score = max(0, 100 - avg_movement)
        
        quality = (heart_rate_score + temp_score + movement_score) / 3
        
        return {
            'quality': round(quality, 2),
            'duration': duration,
            'avg_heart_rate': round(avg_heart_rate, 2),
            'avg_body_temp': round(avg_body_temp, 2),
            'avg_movement': round(avg_movement, 2)
        }