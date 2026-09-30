import sys
import os
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from analysis import SleepAnalyzer
from recommendations import RecommendationEngine
from ui_components import SleepDisplay

# Test that all modules can be imported correctly
try:
    analyzer = SleepAnalyzer()
    engine = RecommendationEngine()
    display = SleepDisplay()
    print('SUCCESS: All modules imported and instantiated correctly')
    
    # Test basic functionality
    test_data = [{'timestamp': 0, 'x': 1.0, 'y': 2.0, 'z': 3.0}]
    result = analyzer.analyze_sleep_pattern(test_data)
    print(f'SUCCESS: Analysis completed with {len(result)} results')
    
    recommendations = engine.generate_recommendations(result)
    print(f'SUCCESS: Generated {len(recommendations)} recommendations')
    
    display.show_analytics(result, recommendations)
    print('SUCCESS: All components work together correctly')
    
except Exception as e:
    print(f'ERROR: {e}')
    sys.exit(1)