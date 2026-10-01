import sys
import os
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

def test_generate_recommendations():
    from recommendation_engine import generate_recommendations
    # Test with sample data
    recommendations = generate_recommendations({'sleep_duration': 6.5, 'deep_sleep': 1.2})
    assert isinstance(recommendations, list)
    assert len(recommendations) > 0