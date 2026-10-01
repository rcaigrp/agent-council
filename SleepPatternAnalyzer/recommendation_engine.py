# Sleep Recommendation Engine

class RecommendationEngine:
    def __init__(self):
        self.sleep_disorder_map = {
            'insomnia': ['avoid_caffeine', 'relaxation_techniques'],
            'sleep_apnea': ['sleep_position', 'consult_doctor'],
            'narcolepsy': ['scheduled_naps', 'medical_advice']
        }
    
    def generate_recommendations(self, sleep_data, user_profile=None):
        recommendations = []
        
        # Basic recommendations based on sleep quality
        if sleep_data.get('quality_score', 0) < 70:
            recommendations.append('Improve sleep environment')
            recommendations.append('Maintain consistent sleep schedule')
        
        if sleep_data.get('restlessness_index', 0) > 0.5:
            recommendations.append('Consider relaxation techniques')
        
        # Add personalized recommendations based on profile
        if user_profile and 'sleep_disorder' in user_profile:
            disorder_recs = self.sleep_disorder_map.get(user_profile['sleep_disorder'], [])
            recommendations.extend(disorder_recs)
            
        return recommendations