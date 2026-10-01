import sys
import os
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

test_data = {
    'user_preferences': {'interests': ['history', 'food']},
    'itinerary': {
        'destination': 'Paris',
        'dates': ['2023-06-01', '2023-06-05']
    }
}

# Test the recommendation engine
from recommendation_system import RecommendationEngine

engine = RecommendationEngine()
engine.set_user_preferences(test_data['user_preferences'])

# Test activity recommendations
activities = engine.get_activity_recommendations(test_data['itinerary'])
print(f'Activity recommendations: {activities}')

# Test accommodation recommendations
accommodations = engine.get_accommodation_recommendations(test_data['itinerary'])
print(f'Accommodation recommendations: {accommodations}')

print('Recommendation system test completed successfully')