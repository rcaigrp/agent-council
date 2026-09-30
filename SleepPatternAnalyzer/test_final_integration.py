#!/usr/bin/env python3
import sys
import os
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from analysis import SleepAnalyzer
from recommendations import RecommendationEngine
from ui_components import SleepUI

# Test final integration
def test_complete_workflow():
    # Create sample data
    sample_data = {
        'accelerometer': [1, 2, 3, 4, 5],
        'gyroscope': [0.1, 0.2, 0.3, 0.4, 0.5]
    }
    
    # Test analysis
    analyzer = SleepAnalyzer()
    result = analyzer.analyze_sleep_data(sample_data)
    print(f'Sleep Analysis Result: {result}')
    
    # Test recommendations
    engine = RecommendationEngine()
    recommendations = engine.generate_recommendations(result)
    print(f'Recommendations: {recommendations}')
    
    # Test UI
    ui = SleepUI()
    ui_result = ui.show_sleep_analysis(result)
    print(ui_result)
    
    return True

if __name__ == '__main__':
    try:
        test_complete_workflow()
        print('SUCCESS: All components integrated correctly')
    except Exception as e:
        print(f'ERROR: {e}')
        sys.exit(1)