import sys
import os
sys.path.append(os.path.dirname(os.path.abspath(__file__)))
from recommendation_engine import generate_recommendations

def test_generate_recommendations():
    # Test basic functionality
    result = generate_recommendations({'quality_score': 85})
    assert result is not None
    assert 'recommendations' in result

if __name__ == '__main__':
    test_generate_recommendations()
    print('All tests passed!')