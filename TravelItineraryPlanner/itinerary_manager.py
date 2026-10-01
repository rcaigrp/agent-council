#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Core module for managing travel itineraries with validation and persistence.
"""
import json
from datetime import datetime, timedelta
from typing import List, Dict, Optional

class Activity:
    """Represents a single activity in an itinerary."""
    def __init__(self, title: str, start_time: datetime, end_time: datetime, location: str = ""):
        self.title = title
        self.start_time = start_time
        self.end_time = end_time
        self.location = location
        
    def to_dict(self) -> Dict:
        return {
            'title': self.title,
            'start_time': self.start_time.isoformat(),
            'end_time': self.end_time.isoformat(),
            'location': self.location
        }
        
    @classmethod
    def from_dict(cls, data: Dict) -> 'Activity':
        return cls(
            title=data['title'],
            start_time=datetime.fromisoformat(data['start_time']),
            end_time=datetime.fromisoformat(data['end_time']),
            location=data.get('location', '')
        )

    def validate(self) -> bool:
        """Validate activity data integrity."""
        if not self.title or len(self.title.strip()) == 0:
            return False
        if self.start_time >= self.end_time:
            return False
        return True

class Itinerary:
    """Represents a complete travel itinerary."""
    def __init__(self, title: str, activities: List[Activity] = None):
        self.title = title
        self.activities = activities or []
        self.created_at = datetime.now()
        self.updated_at = datetime.now()
        
    def add_activity(self, activity: Activity) -> bool:
        """Add an activity to the itinerary."""
        if not activity.validate():
            return False
        self.activities.append(activity)
        self.updated_at = datetime.now()
        return True
        
    def remove_activity(self, index: int) -> bool:
        """Remove an activity by index."""
        if 0 <= index < len(self.activities):
            self.activities.pop(index)
            self.updated_at = datetime.now()
            return True
        return False
        
    def to_dict(self) -> Dict:
        return {
            'title': self.title,
            'activities': [act.to_dict() for act in self.activities],
            'created_at': self.created_at.isoformat(),
            'updated_at': self.updated_at.isoformat()
        }
        
    @classmethod
    def from_dict(cls, data: Dict) -> 'Itinerary':
        activities = [Activity.from_dict(act_data) for act_data in data['activities']]
        itinerary = cls(data['title'], activities)
        itinerary.created_at = datetime.fromisoformat(data['created_at'])
        itinerary.updated_at = datetime.fromisoformat(data['updated_at'])
        return itinerary

    def validate(self) -> bool:
        """Validate itinerary data integrity."""
        if not self.title or len(self.title.strip()) == 0:
            return False
        for activity in self.activities:
            if not activity.validate():
                return False
        return True

    def get_overlapping_activities(self) -> List[tuple]:
        """Find overlapping activities based on time."""
        overlaps = []
        sorted_acts = sorted(self.activities, key=lambda x: x.start_time)
        for i in range(len(sorted_acts)):
            for j in range(i+1, len(sorted_acts)):
                a1, a2 = sorted_acts[i], sorted_acts[j]
                if a1.end_time > a2.start_time:
                    overlaps.append((a1, a2))
                else:
                    break
        return overlaps