def generate_recommendations(sleep_quality):
    '''Generate personalized sleep recommendations based on quality'''
    
    if sleep_quality == 'Poor':
        return [
            'Try to go to bed earlier',
            'Avoid screens 1 hour before bedtime',
            'Keep bedroom cool and dark',
            'Limit caffeine after 2 PM'
        ]
    elif sleep_quality == 'Normal':
        return [
            'Maintain consistent sleep schedule',
            'Try relaxation techniques before bed',
            'Create a calming bedtime routine'
        ]
    else:  # Good
        return [
            'Keep up the good work!',
            'Continue your healthy sleep habits',
            'Consider tracking your sleep to maintain quality'
        ]