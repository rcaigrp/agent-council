import sys
import os
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

def test_integration():
    try:
        from analysis import SleepAnalyzer
        from recommendations import RecommendationEngine
        from ui_components import SleepDisplay
        
        # Test full integration
        analyzer = SleepAnalyzer()
        recommender = RecommendationEngine()
        display = SleepDisplay()
        
        # Mock data
        sleep_data = [1, 2, 3, 4, 5]
        insights = ['get more sleep', 'avoid caffeine late']
        
        # Test methods
        result = display.render_dashboard(sleep_data)
        recommendations = recommender.generate_recommendations(insights)
        
        print('Integration test successful')
        print(f'Dashboard: {result}')
        print(f'Recommendations: {recommendations}')
        return True
    except Exception as e:
        print(f'Integration error: {e}')
        return False

if __name__ == '__main__':
    if test_integration():
        print('INTEGRATION TEST PASSED')
    else:
        print('INTEGRATION TEST FAILED')
        sys.exit(1)
