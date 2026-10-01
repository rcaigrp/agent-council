import sys
import os
sys.path.append(os.path.dirname(os.path.abspath(__file__)))
from recommendation_engine import generate_recommendations

def test_generate_recommendations():
    # Test case: Generate recommendations for poor sleep quality
    sleep_quality = 'Poor'
    recommendations = generate_recommendations(sleep_quality)
    assert len(recommendations) > 0
    
    # Test case: Generate recommendations for good sleep quality
    sleep_quality = 'Good'
    recommendations = generate_recommendations(sleep_quality)
    assert len(recommendations) > 0
    
    print('All tests passed for recommendation_engine!')

test_generate_recommendations()