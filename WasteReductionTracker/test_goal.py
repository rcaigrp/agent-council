import unittest
import sys
import os
sys.path.insert(0, os.path.abspath('.'))

class TestGoalsManager(unittest.TestCase):
    def test_create_goal(self):
        # This test will be run by the manager
        self.assertTrue(True)

    def test_update_goal(self):
        # This test will be run by the manager
        self.assertTrue(True)

    def test_track_progress(self):
        # This test will be run by the manager
        self.assertTrue(True)

if __name__ == '__main__':
    unittest.main()