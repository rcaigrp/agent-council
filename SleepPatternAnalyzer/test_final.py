import sys
import os
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

def test_imports():
    try:
        from analysis import SleepAnalyzer
        from recommendations import RecommendationEngine
        from ui_components import SleepDisplay
        print('All imports successful')
        return True
    except ImportError as e:
        print(f'Import error: {e}')
        return False

def test_functionality():
    try:
        from analysis import SleepAnalyzer
        from recommendations import RecommendationEngine
        from ui_components import SleepDisplay
        
        # Test basic functionality
        analyzer = SleepAnalyzer()
        recommender = RecommendationEngine()
        display = SleepDisplay()
        
        print('All classes instantiated successfully')
        return True
    except Exception as e:
        print(f'Functionality error: {e}')
        return False

if __name__ == '__main__':
    success1 = test_imports()
    success2 = test_functionality()
    if success1 and success2:
        print('TEST PASSED')
    else:
        print('TEST FAILED')
        sys.exit(1)
