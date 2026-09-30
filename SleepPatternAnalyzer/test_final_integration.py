import sys
sys.path.append('/workspace/projects/SleepPatternAnalyzer')
from analysis import SleepAnalyzer
from recommendations import RecommendationEngine
from ui_components import SleepAnalyticsUI

def test_complete_workflow():
    # Test data simulating sensor readings
    test_data = [
        {'timestamp': '2023-10-01 22:00:00', 'x': 0.1, 'y': 0.2, 'z': 0.1},
        {'timestamp': '2023-10-01 22:01:00', 'x': 0.05, 'y': 0.1, 'z': 0.08},
        {'timestamp': '2023-10-01 23:30:00', 'x': 0.02, 'y': 0.03, 'z': 0.01}
    ]
    
    analyzer = SleepAnalyzer()
    metrics = analyzer.analyze_sleep_data(test_data)
    
    engine = RecommendationEngine()
    recommendations = engine.generate_recommendations(metrics)
    
    ui = SleepAnalyticsUI()
    ui.display_metrics(metrics)
    ui.display_recommendations(recommendations)
    
    print('Integration test passed successfully!')

if __name__ == '__main__':
    test_complete_workflow()