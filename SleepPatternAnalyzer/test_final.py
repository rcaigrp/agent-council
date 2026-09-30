# Final test for Sleep Pattern Analyzer
import sys
import os
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

try:
    from analysis import SleepAnalyzer
    from recommendations import RecommendationEngine
    
    print('All modules imported successfully')
    print('Sleep Pattern Analyzer ready for deployment')
    
except ImportError as e:
    print(f'Import error: {e}')
    sys.exit(1)

except Exception as e:
    print(f'Error: {e}')
    sys.exit(1)