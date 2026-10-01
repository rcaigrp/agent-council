# Test file for recommendation_engine.py
import sys
import os
sys.path.append(os.path.dirname(os.path.abspath(__file__)))
from recommendation_engine import generate_recommendations

def test_generate_recommendations():
    # Mock analysis results
    analysis_results = {
        'sleep_duration': 7.5,
        'restlessness_index': 0.3,
        'sleep_quality': 'good'
    }
    
    # Test basic functionality
    recommendations = generate_recommendations(analysis_results)
    assert isinstance(recommendations, list)
    assert len(recommendations) > 0
    print('test_recommendation_engine.py: PASSED')

if __name__ == '__main__':
    test_generate_recommendations()
