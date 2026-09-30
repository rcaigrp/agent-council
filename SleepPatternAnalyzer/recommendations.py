# Recommendation Engine Module

class RecommendationEngine:
    def __init__(self):
        self.recommendations = []
        
    def generate_recommendations(self, sleep_data):
        """
        Generate personalized recommendations for sleep improvement based on analysis results
        """
        recommendations = []
        
        # Base recommendations
        if sleep_data['sleep_duration'] < 7:
            recommendations.append("Try to get at least 7 hours of sleep per night")
        
        if sleep_data['quality_score'] < 80:
            recommendations.append("Improve your sleep environment for better quality")
        
        # Add more specific recommendations
        if sleep_data['deep_sleep'] < 1.5:
            recommendations.append("Consider relaxing activities before bedtime to improve deep sleep")
        
        if sleep_data['light_sleep'] > 5:
            recommendations.append("Try to reduce light sleep periods for more restful sleep")
        
        return recommendations