import pandas as pd
class RecommendationEngine:
    def __init__(self):
        self.recommendations = {
            'sleep_duration': [
                'Try to maintain consistent sleep schedule with 7-9 hours nightly',
                'Avoid long daytime naps that may disrupt nighttime sleep'
            ],
            'sleep_quality': [
                'Keep bedroom cool (65-68°F) for optimal sleep temperature',
                'Limit screen time 1 hour before bedtime'
            ]
        }
    
    def generate_recommendations(self, sleep_data):
        # Calculate sleep efficiency
        total_sleep = sleep_data['total_sleep_minutes'].iloc[0] if not sleep_data.empty else 0
        sleep_efficiency = sleep_data['sleep_efficiency'].iloc[0] if not sleep_data.empty else 0
        
        recommendations = []
        
        # Duration-based recommendations
        if total_sleep < 420:  # Less than 7 hours
            recommendations.extend(self.recommendations['sleep_duration'])
        
        # Quality-based recommendations
        if sleep_efficiency < 85:
            recommendations.extend(self.recommendations['sleep_quality'])
        
        return recommendations