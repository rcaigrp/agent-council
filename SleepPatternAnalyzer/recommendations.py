import pandas as pd
class RecommendationEngine:
    def __init__(self):
        self.recommendations = {
            'low_sleep_efficiency': 'Try to maintain consistent sleep schedule and avoid caffeine 6 hours before bedtime',
            'high_latency': 'Create a relaxing pre-sleep routine to help your body wind down',
            'low_deep_sleep': 'Keep bedroom temperature between 65-68°F for optimal deep sleep'
        }
    
    def generate_recommendations(self, sleep_metrics):
        recommendations = []
        if sleep_metrics['sleep_efficiency'] < 85:
            recommendations.append(self.recommendations['low_sleep_efficiency'])
        if sleep_metrics['sleep_latency'] > 30:
            recommendations.append(self.recommendations['high_latency'])
        if sleep_metrics['deep_sleep_percentage'] < 20:
            recommendations.append(self.recommendations['low_deep_sleep'])
        return recommendations