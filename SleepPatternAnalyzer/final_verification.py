# Final verification test
import sys
import os
import importlib

# Clear any cached modules
modules_to_clear = [k for k in sys.modules.keys() if 'analysis' in k or 'recommendations' in k or 'ui_components' in k]
for module in modules_to_clear:
    del sys.modules[module]

try:
    # Test imports directly
    import analysis
    import recommendations
    import ui_components
    
    # Test instantiation
    analyzer = analysis.SleepAnalyzer()
    engine = recommendations.RecommendationEngine()
    display = ui_components.SleepDisplay()
    
    print('SUCCESS: All modules imported and instantiated correctly')
    
    # Test basic functionality
    test_data = [{'timestamp': 0, 'x': 1.0, 'y': 2.0, 'z': 3.0}]
    result = analyzer.analyze_sleep_pattern(test_data)
    print(f'SUCCESS: Analysis completed with {len(result)} results')
    
    recommendations_list = engine.generate_recommendations(result)
    print(f'SUCCESS: Generated {len(recommendations_list)} recommendations')
    
    display.show_analytics(result, recommendations_list)
    print('SUCCESS: All components work together correctly')
    
except Exception as e:
    print(f'ERROR: {e}')
    import traceback
    traceback.print_exc()
    sys.exit(1)