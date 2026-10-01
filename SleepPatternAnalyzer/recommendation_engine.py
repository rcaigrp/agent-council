# Recommendation engine module

class RecommendationEngine:
    def __init__(self):
        pass

    def generate_recommendations(self, sleep_data):
        # Generate personalized recommendations based on sleep data
        if not sleep_data:
            return []
        
        duration = sleep_data.get('duration', 0)
        restlessness = sleep_data.get('restlessness_index', 0)
        
        recommendations = []
        if duration < 6:
            recommendations.append("Try to sleep for at least 6 hours")
        if restlessness > 3:
            recommendations.append("Consider reducing caffeine intake before bedtime")
            
        return recommendations