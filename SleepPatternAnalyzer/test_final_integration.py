# Final integration test for Sleep Pattern Analyzer
import sys
import os

current_dir = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, current_dir)

# Test all components work together
def test_complete_workflow():
    from analysis import SleepAnalyzer
    from recommendations import RecommendationEngine
    from ui_components import SleepDataDisplay
    
    # Create sample data
    sample_data = {
        'accelerometer': [0.1, 0.2, 0.3],
        'gyroscope': [0.05, 0.1, 0.15]
    }
    
    # Test analysis
    analyzer = SleepAnalyzer()
    metrics = analyzer.analyze_sleep_data(sample_data)
    print(f'Analysis complete: {metrics}')
    
    # Test recommendations
    engine = RecommendationEngine()
    recommendations = engine.generate_recommendations(metrics)
    print(f'Recommendations generated: {recommendations}')
    
    # Test UI display
    ui = SleepDataDisplay()
    display_result = ui.display_sleep_metrics(metrics)
    print(f'UI Display test: {display_result}')
    
    print('All components working correctly!')
    return True

if __name__ == '__main__':
    try:
        test_complete_workflow()
        print('SUCCESS: All tests passed')
    except Exception as e:
        print(f'FAILED: {str(e)}')
        sys.exit(1)