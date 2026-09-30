import sys
import os
sys.path.append(os.path.dirname(os.path.abspath(__file__)))
from recommendations import RecommendationEngine

class TestRecommendationEngine:
    def test_good_sleep(self):
        engine = RecommendationEngine()
        sleep_data = {'sleep_efficiency': 90, 'deep_sleep_duration': 45}
        recs = engine.generate_recommendations(sleep_data)
        assert len(recs) == 0
        
    def test_low_efficiency(self):
        engine = RecommendationEngine()
        sleep_data = {'sleep_efficiency': 75, 'deep_sleep_duration': 45}
        recs = engine.generate_recommendations(sleep_data)
        assert len(recs) >= 1
        
    def test_low_deep_sleep(self):
        engine = RecommendationEngine()
        sleep_data = {'sleep_efficiency': 90, 'deep_sleep_duration': 20}
        recs = engine.generate_recommendations(sleep_data)
        assert len(recs) >= 1
        
    def test_both_issues(self):
        engine = RecommendationEngine()
        sleep_data = {'sleep_efficiency': 75, 'deep_sleep_duration': 20}
        recs = engine.generate_recommendations(sleep_data)
        assert len(recs) >= 2
        
if __name__ == '__main__':
    test = TestRecommendationEngine()
    test.test_good_sleep()
    test.test_low_efficiency()
    test.test_low_deep_sleep()
    test.test_both_issues()
    print('All tests passed!')