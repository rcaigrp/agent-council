# Recommendation engine module for sleep improvement suggestions

def generate_recommendations(sleep_data):
    '''Generate personalized recommendations based on sleep data'''
    # Dummy implementation for testing
    return {
        'recommendations': [
            'Maintain consistent sleep schedule',
            'Avoid screens 1 hour before bedtime',
            'Keep bedroom cool and dark'
        ],
        'score': sleep_data.get('quality_score', 85)
    }