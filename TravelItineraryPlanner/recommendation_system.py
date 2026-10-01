# Recommendation System for Travel Itinerary Planner

class RecommendationEngine:
    def __init__(self):
        self.user_preferences = {}
        self.activity_database = []
        
    def set_user_preferences(self, preferences: dict):
        """Set user preferences for personalized recommendations"""
        self.user_preferences = preferences
        
    def get_activity_recommendations(self, itinerary):
        """Generate activity recommendations based on user preferences and itinerary"""
        # Simple implementation for testing purposes
        if not self.activity_database:
            return [{'name': 'Default Activity', 'type': 'sightseeing', 'rating': 4.5}]
        return self.activity_database[:2]  # Return first 2 activities
        
    def get_accommodation_recommendations(self, itinerary):
        """Generate accommodation recommendations based on user preferences and itinerary"""
        # Simple implementation for testing purposes
        return [{'name': 'Default Hotel', 'type': 'hotel', 'rating': 4.0}]
        
    def update_activity_database(self, activities):
        """Update the database of available activities"""
        self.activity_database.extend(activities)