#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Test cases for itinerary manager module
"""

import unittest
from itinerary_manager import ItineraryManager, Itinerary


class TestItineraryManager(unittest.TestCase):
    def setUp(self):
        self.manager = ItineraryManager()

    def test_create_itinerary(self):
        id1 = self.manager.create_itinerary("Summer Vacation", "2023-07-01", "2023-07-15", ["Paris", "Rome"])
        self.assertEqual(id1, "1")

    def test_get_itinerary(self):
        id1 = self.manager.create_itinerary("Summer Vacation", "2023-07-01", "2023-07-15")
        itinerary = self.manager.get_itinerary(id1)
        self.assertIsNotNone(itinerary)
        self.assertEqual(itinerary.title, "Summer Vacation")

    def test_update_itinerary(self):
        id1 = self.manager.create_itinerary("Summer Vacation", "2023-07-01", "2023-07-15")
        success = self.manager.update_itinerary(id1, title="Updated Summer Vacation")
        self.assertTrue(success)
        itinerary = self.manager.get_itinerary(id1)
        self.assertEqual(itinerary.title, "Updated Summer Vacation")

    def test_delete_itinerary(self):
        id1 = self.manager.create_itinerary("Summer Vacation", "2023-07-01", "2023-07-15")
        success = self.manager.delete_itinerary(id1)
        self.assertTrue(success)
        self.assertIsNone(self.manager.get_itinerary(id1))

    def test_list_itineraries(self):
        self.manager.create_itinerary("Summer Vacation", "2023-07-01", "2023-07-15")
        self.manager.create_itinerary("Winter Trip", "2023-12-01", "2023-12-15")
        itineraries = self.manager.list_itineraries()
        self.assertEqual(len(itineraries), 2)


if __name__ == "__main__":
    unittest.main()