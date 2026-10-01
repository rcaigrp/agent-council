import sys
import os
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from recommendation_engine import generate_recommendations

def test_generate_recommendations():
    # Test with sample data
    sleep_quality = 75
    recommendations = generate_recommendations(sleep_quality)
    assert isinstance(recommendations, list)
    print('test_generate_recommendations passed')

if __name__ == '__main__':
    test_generate_recommendations()
    print('All tests passed!')