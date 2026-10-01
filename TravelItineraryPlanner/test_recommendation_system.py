import pytest
from recommendation_system import RecommendationSystem

def test_generate_recommendations():
    rec_sys = RecommendationSystem()
    
    user_prefs = {'preferred_country': 'Japan'}
    destinations = [
        type('Destination', (), {'name': 'Tokyo', 'country': 'Japan'}),
        type('Destination', (), {'name': 'Osaka', 'country': 'France'})
    ]
    
    recommendations = rec_sys.generate_recommendations(user_prefs, destinations)
    assert len(recommendations) == 1
    assert recommendations[0]['name'] == 'Explore Tokyo'


def test_get_recommendations():
    rec_sys = RecommendationSystem()
    
    # Test empty recommendations
    assert rec_sys.get_recommendations() == []