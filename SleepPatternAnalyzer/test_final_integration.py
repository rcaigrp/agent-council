import sys
import os
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

def test_analysis_module():
    try:
        from analysis import SleepAnalyzer
        print('✓ Analysis module imported successfully')
        return True
    except Exception as e:
        print(f'✗ Analysis module import failed: {e}')
        return False

def test_recommendations_module():
    try:
        from recommendations import RecommendationEngine
        print('✓ Recommendations module imported successfully')
        return True
    except Exception as e:
        print(f'✗ Recommendations module import failed: {e}')
        return False

def test_ui_components_module():
    try:
        from ui_components import SleepDashboard
        print('✓ UI Components module imported successfully')
        return True
    except Exception as e:
        print(f'✗ UI Components module import failed: {e}')
        return False

def main():
    print('Running final integration tests...')
    results = [
        test_analysis_module(),
        test_recommendations_module(),
        test_ui_components_module()
    ]
    if all(results):
        print('\n🎉 All modules working correctly!')
        return 0
    else:
        print('\n❌ Some modules failed')
        return 1

if __name__ == '__main__':
    sys.exit(main())