#!/usr/bin/env python3

import unittest
import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), '.'))

from recommendation_system import RecommendationSystem

class TestRecommendationSystem(unittest.TestCase):
    
    def setUp(self):
        self.recommendation_system = RecommendationSystem()
        
    def test_recommendation_generation(self):
        """
        Test that recommendations are generated correctly
        """
        preferences = {'budget': 'medium', 'interests': ['history', 'food']}
        location_data = {'city': 'Paris', 'country': 'France'}
        
        recommendations = self.recommendation_system.generate_recommendations(preferences, location_data)
        
        # Should return at least one recommendation
        self.assertIsInstance(recommendations, list)
        self.assertGreater(len(recommendations), 0)
        
    def test_user_preference_update(self):
        """
        Test updating user preferences
        """
        preferences = {'budget': 'high', 'interests': ['art', 'culture']}
        
        # Should not raise an exception
        self.recommendation_system.update_user_preferences(preferences)
        
if __name__ == '__main__':
    unittest.main()