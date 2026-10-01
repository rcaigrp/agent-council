def generate_recommendations(analysis_results):
    '''Generate personalized sleep recommendations based on analysis results'''
    
    recommendations = []
    
    # Quality-based recommendations
    if analysis_results.get('sleep_quality') == 'poor':
        recommendations.extend([
            'Try to maintain consistent sleep schedule',
            'Avoid screens 1 hour before bedtime',
            'Keep bedroom temperature between 65-68°F'
        ])
    else:
        recommendations.extend([
            'Great job maintaining good sleep quality!',
            'Continue with your current sleep routine',
            'Consider keeping a sleep diary to track patterns'
        ])
    
    # Duration-based recommendations
    duration = analysis_results.get('sleep_duration', 0)
    if duration < 6:
        recommendations.append('Aim for 7-9 hours of sleep per night')
    elif duration > 9:
        recommendations.append('Consider reducing bedtime to avoid oversleeping')
    
    return recommendations