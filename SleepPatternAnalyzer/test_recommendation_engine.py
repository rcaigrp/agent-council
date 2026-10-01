import sys
import os
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from recommendation_engine import generate_recommendations

def test_generate_recommendations():
    result = generate_recommendations({'sleep_duration': 7, 'sleep_quality': 85})
    assert isinstance(result, list)
    print("generate_recommendations test passed")

if __name__ == "__main__":
    test_generate_recommendations()
    print("All tests passed!")