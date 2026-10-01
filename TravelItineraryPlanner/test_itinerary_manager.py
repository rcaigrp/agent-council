import pytest
from itinerary_manager import Trip, Activity, Location

def test_trip_creation():
    trip = Trip("Paris Trip", "2023-06-01", "2023-06-05")
    assert trip.name == "Paris Trip"
    assert trip.start_date == "2023-06-01"
    assert trip.end_date == "2023-06-05"


def test_activity_creation():
    location = Location("Eiffel Tower", "Paris, France")
    activity = Activity("Visit Eiffel Tower", "2023-06-02 10:00", "2023-06-02 12:00", location)
    assert activity.name == "Visit Eiffel Tower"
    assert activity.start_time == "2023-06-02 10:00"
    assert activity.end_time == "2023-06-02 12:00"
    assert activity.location.name == "Eiffel Tower"


def test_invalid_trip_dates():
    with pytest.raises(ValueError):
        Trip("Invalid Trip", "2023-06-05", "2023-06-01")  # End date before start date


def test_activity_overlapping():
    location = Location("Test Location", "Test City")
    activity1 = Activity("Activity 1", "2023-06-02 10:00", "2023-06-02 12:00", location)
    activity2 = Activity("Activity 2", "2023-06-02 11:00", "2023-06-02 13:00", location)
    # This should be handled by trip manager logic
