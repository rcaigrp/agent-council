from datetime import datetime

class Location:
    def __init__(self, name, address):
        self.name = name
        self.address = address


class Activity:
    def __init__(self, name, start_time, end_time, location):
        self.name = name
        self.start_time = start_time
        self.end_time = end_time
        self.location = location


class Trip:
    def __init__(self, name, start_date, end_date):
        self.name = name
        self.start_date = start_date
        self.end_date = end_date
        
        # Validate dates
        if start_date > end_date:
            raise ValueError("End date must be after start date")
        
        # Store as datetime objects for easier comparison
        self.start_datetime = datetime.strptime(start_date, "%Y-%m-%d")
        self.end_datetime = datetime.strptime(end_date, "%Y-%m-%d")

    def add_activity(self, activity):
        # Validate that activity is within trip dates
        activity_start = datetime.strptime(activity.start_time, "%Y-%m-%d %H:%M")
        if not (self.start_datetime <= activity_start <= self.end_datetime):
            raise ValueError("Activity time must be within trip dates")
        
        # Store activities in a list
        if not hasattr(self, 'activities'):
            self.activities = []
        self.activities.append(activity)
