import statistics
class SleepAnalyzer:
    def __init__(self):
        pass
    
    def analyze_patterns(self, sleep_data):
        # Analyze sleep patterns from collected data
        heart_rates = [data['heart_rate'] for data in sleep_data]
        body_temperatures = [data['body_temperature'] for data in sleep_data]
        movements = [data['movement'] for data in sleep_data]
        
        analysis = {
            'avg_heart_rate': statistics.mean(heart_rates),
            'avg_body_temp': statistics.mean(body_temperatures),
            'total_movement': sum(movements),
            'sleep_quality_score': self._calculate_sleep_quality(heart_rates, movements)
        }
        return analysis
    
    def _calculate_sleep_quality(self, heart_rates, movements):
        # Simple quality score based on heart rate variability and movement
        avg_hr = statistics.mean(heart_rates) if heart_rates else 60
        avg_movement = statistics.mean(movements) if movements else 50
        
        # Lower movement and stable heart rate indicate better sleep
        score = max(0, min(100, 100 - abs(avg_hr - 60) * 0.5 - avg_movement * 0.2))
        return round(score, 2)