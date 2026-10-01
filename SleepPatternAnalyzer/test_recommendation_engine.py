import sys
import os
sys.path.append(os.path.dirname(os.path.abspath(__file__)))
from recommendation_engine import generate_recommendations

def test_generate_recommendations():
    # Test basic functionality
    recommendations = generate_recommendations({'sleep_quality': 85, 'duration': 7.5})
    assert isinstance(recommendations, list)
    assert len(recommendations) > 0  # Should return at least one recommendation
    print('test_generate_recommendations: PASSED')

if __name__ == '__main__':
    test_generate_recommendations()
    print('All tests passed!')