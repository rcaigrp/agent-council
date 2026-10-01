#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Test suite for itinerary manager module.
"""
import pytest
from datetime import datetime, timedelta
from itinerary_manager import Activity, Itinerary

def test_activity_creation():
    activity = Activity(
        title="Museum Visit",
        start_time=datetime(2023, 6, 15, 10, 0),
        end_time=datetime(2023, 6, 15, 12, 0),
        location="Art Gallery"
    )
    assert activity.title == "Museum Visit"
    assert activity.start_time == datetime(2023, 6, 15, 10, 0)
    assert activity.end_time == datetime(2023, 6, 15, 12, 0)
    assert activity.location == "Art Gallery"

def test_activity_validation():
    # Valid activity
    valid = Activity("Visit", datetime(2023, 6, 15, 10, 0), datetime(2023, 6, 15, 12, 0))
    assert valid.validate() is True
    
    # Invalid: empty title
    invalid = Activity("", datetime(2023, 6, 15, 10, 0), datetime(2023, 6, 15, 12, 0))
    assert invalid.validate() is False
    
    # Invalid: start after end
    invalid = Activity("Visit", datetime(2023, 6, 15, 12, 0), datetime(2023, 6, 15, 10, 0))
    assert invalid.validate() is False

def test_itinerary_creation():
    itinerary = Itinerary("My Trip")
    assert itinerary.title == "My Trip"
    assert len(itinerary.activities) == 0
    
    # Test with activities
    activity = Activity("Visit", datetime(2023, 6, 15, 10, 0), datetime(2023, 6, 15, 12, 0))
    itinerary_with_activities = Itinerary("Trip with Activities", [activity])
    assert len(itinerary_with_activities.activities) == 1
    
    # Test serialization
    data = itinerary_with_activities.to_dict()
    restored = Itinerary.from_dict(data)
    assert restored.title == "Trip with Activities"
    assert len(restored.activities) == 1
    assert restored.activities[0].title == "Visit"

def test_itinerary_validation():
    # Valid itinerary
    activity = Activity("Visit", datetime(2023, 6, 15, 10, 0), datetime(2023, 6, 15, 12, 0))
    valid_itinerary = Itinerary("Valid Trip", [activity])
    assert valid_itinerary.validate() is True
    
    # Invalid: empty title
    invalid_itinerary = Itinerary("", [activity])
    assert invalid_itinerary.validate() is False
    
    # Invalid: activity with bad data
    invalid_activity = Activity("", datetime(2023, 6, 15, 10, 0), datetime(2023, 6, 15, 12, 0))
    invalid_itinerary = Itinerary("Trip with Bad Activity", [invalid_activity])
    assert invalid_itinerary.validate() is False
    
    # Invalid: overlapping activities
    act1 = Activity("Visit 1", datetime(2023, 6, 15, 10, 0), datetime(2023, 6, 15, 12, 0))
    act2 = Activity("Visit 2", datetime(2023, 6, 15, 11, 0), datetime(2023, 6, 15, 13, 0))
    overlapping_itinerary = Itinerary("Overlapping Activities", [act1, act2])
    # Note: validation doesn't check overlaps but we can detect them
    assert overlapping_itinerary.validate() is True  # Validation passes but overlaps exist
    
    # Test overlap detection
    overlaps = overlapping_itinerary.get_overlapping_activities()
    assert len(overlaps) == 1

def test_itinerary_operations():
    activity1 = Activity("Visit 1", datetime(2023, 6, 15, 10, 0), datetime(2023, 6, 15, 12, 0))
    activity2 = Activity("Visit 2", datetime(2023, 6, 15, 14, 0), datetime(2023, 6, 15, 16, 0))
    itinerary = Itinerary("My Trip", [activity1])
    
    # Add activity
    assert itinerary.add_activity(activity2) is True
    assert len(itinerary.activities) == 2
    
    # Remove activity
    assert itinerary.remove_activity(0) is True
    assert len(itinerary.activities) == 1
    assert itinerary.activities[0].title == "Visit 2"
    
    # Remove non-existent activity
    assert itinerary.remove_activity(5) is False