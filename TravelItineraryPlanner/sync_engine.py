import json
from datetime import datetime, timedelta

class ConflictError(Exception):
    pass

class SyncEngine:
    def __init__(self):
        self.data_store = {}

    def sync_itinerary(self, user_id, itinerary_data):
        if user_id not in self.data_store:
            self.data_store[user_id] = {}
        
        existing_itinerary = self.data_store[user_id].get('itinerary')
        if existing_itinerary:
            # Simple conflict resolution: merge non-overlapping activities
            updated_activities = []
            for new_activity in itinerary_data.get('activities', []):
                conflicts = self._find_conflicts(existing_itinerary, new_activity)
                if not conflicts:
                    updated_activities.append(new_activity)
                else:
                    # For this version, we'll just skip conflicting activities
                    pass
            
            # Merge the non-conflicting activities
            merged_activities = existing_itinerary.get('activities', []) + updated_activities
            self.data_store[user_id]['itinerary'] = {
                'title': itinerary_data['title'],
                'activities': merged_activities,
                'destinations': itinerary_data.get('destinations', [])
            }
        else:
            self.data_store[user_id]['itinerary'] = itinerary_data
        
        return self.data_store[user_id]['itinerary']

    def _find_conflicts(self, existing_itinerary, new_activity):
        conflicts = []
        for existing_activity in existing_itinerary.get('activities', []):
            if self._times_overlap(existing_activity['time_range'], new_activity['time_range']):
                conflicts.append(existing_activity)
        return conflicts

    def _times_overlap(self, time_range1, time_range2):
        start1 = datetime.fromisoformat(time_range1[0])
        end1 = datetime.fromisoformat(time_range1[1])
        start2 = datetime.fromisoformat(time_range2[0])
        end2 = datetime.fromisoformat(time_range2[1])
        
        return (start1 <= start2 <= end1) or (start2 <= start1 <= end2)

    def get_itinerary(self, user_id):
        return self.data_store.get(user_id, {}).get('itinerary', {})