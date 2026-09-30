#!/usr/bin/env python3

class TestSleepAnalyzer:
    def test_sleep_analysis(self):
        # Import the actual implementation
        from analysis import SleepAnalyzer
        
        # Create a simple test data set
        test_data = [
            {'timestamp': 1609459200, 'x': 0.1, 'y': 0.2, 'z': 0.3},
            {'timestamp': 1609459260, 'x': 0.05, 'y': 0.1, 'z': 0.2},
            {'timestamp': 1609459320, 'x': 0.01, 'y': 0.02, 'z': 0.03}
        ]
        
        # Create analyzer instance
        analyzer = SleepAnalyzer()
        
        # Test analysis function
        result = analyzer.analyze(test_data)
        
        # Verify result is not None and has expected structure
        assert result is not None, "Analysis should return results"
        assert 'sleep_duration' in result, "Result should contain sleep duration"
        assert 'quality_score' in result, "Result should contain quality score"
        
        print('Sleep analysis test passed')
        
    def test_recommendations(self):
        from recommendations import RecommendationEngine
        
        # Test recommendation generation
        engine = RecommendationEngine()
        
        # Create mock sleep data
        sleep_data = {
            'sleep_duration': 7.5,
            'quality_score': 85,
            'deep_sleep': 2.0,
            'light_sleep': 4.0,
            'rem_sleep': 1.5
        }
        
        recommendations = engine.generate(sleep_data)
        
        assert recommendations is not None, "Recommendations should be generated"
        assert len(recommendations) > 0, "Should have at least one recommendation"
        
        print('Recommendation test passed')

if __name__ == '__main__':
    tester = TestSleepAnalyzer()
    tester.test_sleep_analysis()
    tester.test_recommendations()
    print('All tests passed!')