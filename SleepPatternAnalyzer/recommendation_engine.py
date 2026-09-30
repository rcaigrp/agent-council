import datetime

class RecommendationEngine:
    def __init__(self):
        pass
    
    def generate_recommendations(self, sleep_data):
        recommendations = []
        
        # Extract key metrics from sleep data
        total_sleep_duration = sleep_data.get('total_sleep_duration', 0)
        restlessness_index = sleep_data.get('restlessness_index', 0)
        sleep_efficiency = sleep_data.get('sleep_efficiency', 0)
        
        # Generate recommendations based on sleep quality metrics
        if total_sleep_duration < 6:
            recommendations.append("You're getting less than 6 hours of sleep. Try to extend your sleep duration to at least 7-8 hours.")
        elif total_sleep_duration > 9:
            recommendations.append("You're sleeping more than 9 hours. Consider reducing sleep duration for better sleep quality.")
        
        if restlessness_index > 0.5:
            recommendations.append("High restlessness detected. Try to minimize movement during sleep by adjusting your sleep environment.")
        
        if sleep_efficiency < 85:
            recommendations.append("Low sleep efficiency. Aim for higher sleep efficiency by maintaining a consistent sleep schedule.")
        
        return recommendations