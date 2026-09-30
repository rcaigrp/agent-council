class RecommendationEngine:
    def __init__(self):
        pass
    
    def generate_recommendations(self, analysis_result):
        recommendations = []
        
        if analysis_result['sleep_quality_score'] < 60:
            recommendations.append("Your sleep quality is low. Try to maintain a consistent sleep schedule.")
            recommendations.append("Reduce screen time before bed to improve sleep quality.")
        
        if analysis_result['avg_heart_rate'] > 70:
            recommendations.append("Consider relaxation techniques to lower your resting heart rate.")
        
        if analysis_result['total_movement'] > 200:
            recommendations.append("Excessive movement during sleep may indicate restlessness. Try a comfortable sleeping position.")
        
        return recommendations