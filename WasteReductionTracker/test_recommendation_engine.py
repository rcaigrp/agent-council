# Test for recommendation engine

import sys
import os
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from recommendation_engine import RecommendationEngine

def test_recommendation():
    engine = RecommendationEngine()
    
    # Test with empty input
    result = engine.generate_recommendations()
    assert len(result) > 0, "Should return a default message for empty input"
    
    # Test with None input
    result = engine.generate_recommendations(None)
    assert len(result) > 0, "Should handle None input gracefully"
    
    # Test with normal data
    waste_data = ["plastic bag", "paper box"]
    result = engine.generate_recommendations(waste_data)
    assert len(result) > 0, "Should generate recommendations for valid input"
    
    print("All tests passed!")

if __name__ == "__main__":
    test_recommendation()