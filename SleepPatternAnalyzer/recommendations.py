# Sleep Recommendations Engine
import pandas as pd

class RecommendationEngine:
    def __init__(self):
        self.recommendations = {
            'sleep_duration': [
                "You're getting {duration} hours of sleep, which is {status}. Try to maintain 7-9 hours for optimal health.",
                "Your sleep duration is {status}. Consider adjusting your bedtime routine to improve consistency."
            ],
            'sleep_quality': [
                "Your sleep quality score is {score}/100. {feedback}",
                "Sleep efficiency of {efficiency}% indicates {quality} sleep patterns."
            ],
            'sleep_consistency': [
                "Your bedtime consistency is {consistency}. {tip}",
                "You're sleeping {hours} hours on average. Try to keep this consistent across weekdays and weekends."
            ]
        }

    def generate_recommendations(self, sleep_data):
        recommendations = []
        
        # Sleep duration analysis
        avg_duration = sleep_data['sleep_duration'].mean()
        if avg_duration < 6:
            status = "below recommended"
        elif avg_duration > 9:
            status = "above recommended"
        else:
            status = "within recommended range"
        
        recommendations.append({
            'type': 'sleep_duration',
            'message': self.recommendations['sleep_duration'][0].format(duration=round(avg_duration, 1), status=status)
        })
        
        # Sleep quality analysis
        avg_quality = sleep_data['quality_score'].mean()
        if avg_quality < 60:
            feedback = "This indicates poor sleep quality. Consider reducing screen time before bed and keeping your room cool and dark."
        elif avg_quality < 80:
            feedback = "Your sleep quality is moderate. Try to improve your sleep environment for better rest."
        else:
            feedback = "Great job maintaining high-quality sleep! Keep up the good work."
        
        recommendations.append({
            'type': 'sleep_quality',
            'message': self.recommendations['sleep_quality'][0].format(score=round(avg_quality, 1), feedback=feedback)
        })
        
        # Sleep consistency analysis
        consistency = sleep_data['consistency_score'].mean()
        if consistency < 70:
            tip = "Consider setting a regular bedtime and wake-up time to improve consistency."
        else:
            tip = "Excellent consistency! Your sleep schedule is well-established."
        
        recommendations.append({
            'type': 'sleep_consistency',
            'message': self.recommendations['sleep_consistency'][0].format(consistency=round(consistency, 1), tip=tip)
        })
        
        return recommendations