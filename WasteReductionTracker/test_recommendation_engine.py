import sys
sys.path.insert(0, '/workspace/projects/WasteReductionTracker')


def test_recommendation():
    print('Importing recommendation module...')
    from api.recommendations import generate_recommendations
    print('Recommendation module imported successfully')
    print('test_recommendation_engine.py: PASS')

test_recommendation()