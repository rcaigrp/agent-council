import unittest
from models.goal import GoalsManager
from datetime import date

class TestGoalsManager(unittest.TestCase):
    def setUp(self):
        # Use an in-memory database for testing
        self.manager = GoalsManager(':memory:')

    def test_create_goal(self):
        goal_id = self.manager.create_goal(1, 'plastic', 5.0, date(2023, 12, 31))
        self.assertIsInstance(goal_id, int)
        
    def test_get_goals(self):
        # Create a goal first
        self.manager.create_goal(1, 'plastic', 5.0, date(2023, 12, 31))
        goals = self.manager.get_goals(1)
        self.assertEqual(len(goals), 1)
        
    def test_get_goals_empty(self):
        goals = self.manager.get_goals(999)  # Non-existent user
        self.assertEqual(len(goals), 0)

if __name__ == '__main__':
    unittest.main()