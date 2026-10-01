import sys
sys.path.insert(0, '/workspace/projects/WasteReductionTracker')


def test_goal():
    print('Importing goals module...')
    from api.goals import GoalsManager
    print('GoalsManager imported successfully')
    print('test_goal.py: PASS')

test_goal()