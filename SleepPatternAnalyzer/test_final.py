#!/usr/bin/env python3

import sys
import os

current_dir = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, current_dir)

try:
    from analysis import SleepAnalyzer
    from recommendations import RecommendationEngine
    print('SUCCESS: Core modules imported correctly')
    
    # Test basic instantiation
    analyzer = SleepAnalyzer()
    engine = RecommendationEngine()
    
    print('SUCCESS: Components created successfully')
    
except ImportError as e:
    print(f'FAILED: Import error - {str(e)}')
    sys.exit(1)
except Exception as e:
    print(f'FAILED: Runtime error - {str(e)}')
    sys.exit(1)

print('Integration test completed successfully')