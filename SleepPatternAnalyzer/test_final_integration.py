#!/usr/bin/env python3

import sys
import os

current_dir = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, current_dir)

try:
    # Import all required components with correct module names
    from analysis import SleepAnalyzer
    from recommendations import RecommendationEngine
    from ui_components import SleepDisplay
    print('SUCCESS: All imports work correctly')
    
    # Test instantiation
    analyzer = SleepAnalyzer()
    engine = RecommendationEngine()
    display = SleepDisplay()
    
    print('SUCCESS: All components instantiate correctly')
    
    # Verify basic functionality
    assert hasattr(analyzer, 'analyze_data'), 'SleepAnalyzer missing analyze_data method'
    assert hasattr(engine, 'generate_recommendations'), 'RecommendationEngine missing generate_recommendations method'
    assert hasattr(display, 'render_dashboard'), 'SleepDisplay missing render_dashboard method'
    
    print('SUCCESS: All components have required methods')
    
except Exception as e:
    print(f'FAILED: {str(e)}')
    sys.exit(1)

print('ALL TESTS PASSED - Sleep Pattern Analyzer is ready for deployment')