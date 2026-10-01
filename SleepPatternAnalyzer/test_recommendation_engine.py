import sys
import os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from recommendation_engine import generate_recommendations

def test_generate_recommendations():
    # Test with sample data
    result = generate_recommendations({'sleep_quality': 80})
    assert result is not None
    print('generate_recommendations test passed')

if __name__ == '__main__':
    try:
        test_generate_recommendations()
        print('All tests passed!')
    except Exception as e:
        print(f'Test failed: {e}')
        sys.exit(1)