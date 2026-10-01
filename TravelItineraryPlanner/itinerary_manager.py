# Travel Itinerary Manager

class ItineraryManager:
    def __init__(self):
        self.itineraries = {}
        
    def create_itinerary(self, name, destination, start_date, end_date):
        itinerary_id = len(self.itineraries) + 1
        self.itineraries[itinerary_id] = {
            'name': name,
            'destination': destination,
            'start_date': start_date,
            'end_date': end_date,
            'activities': []
        }
        return itinerary_id
        
    def add_activity(self, itinerary_id, activity):
        if itinerary_id in self.itineraries:
            self.itineraries[itinerary_id]['activities'].append(activity)
            return True
        return False