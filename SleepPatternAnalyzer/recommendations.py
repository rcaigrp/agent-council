import pandas as pd
class RecommendationEngine:
    def __init__(self):
        self.tips = {
            'deep_sleep_deficit': 'Try to maintain 7-9 hours of sleep nightly to improve deep sleep duration.',
            'light_sleep_excess': 'Reduce screen time before bed and keep bedroom cool for better sleep quality.',
            'wake_time_consistency': 'Set a consistent bedtime and wake-up time, even on weekends.',
            'sleep_latency': 'Avoid caffeine after 2 PM and establish a relaxing pre-sleep routine.'
        }
    
    def generate_recommendations(self, sleep_data):
        recommendations = []
        if sleep_data['deep_sleep_percentage'] < 15:
            recommendations.append(self.tips['deep_sleep_deficit'])
        if sleep_data['light_sleep_percentage'] > 40:
            recommendations.append(self.tips['light_sleep_excess'])
        if sleep_data['sleep_latency'] > 30:
            recommendations.append(self.tips['sleep_latency'])
        return recommendations