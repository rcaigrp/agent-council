#!/usr/bin/env python3

import json
from typing import List, Dict, Any, Optional
from datetime import datetime, timedelta
from dataclasses import dataclass, asdict

@dataclass
class ActivityRecommendation:
    activity_type: str
    title: str
    description: str
    location: str
    estimated_duration: int  # in minutes
    price_range: str  # low/medium/high
    rating: float
    confidence_score: float = 0.0

@dataclass
class UserPreferences:
    interests: List[str]
    budget_range: str  # low/medium/high
    travel_style: str  # casual/adventurous/leisure
    accessibility_needs: List[str]  # wheelchair_access, hearing_aid, etc.

@dataclass
class RecommendationContext:
    user_preferences: UserPreferences
    current_itinerary: Dict[str, Any]
    destination_info: Dict[str, Any]
    time_frame: Dict[str, datetime]

class RecommendationEngine:
    def __init__(self):
        # Mock recommendation database - in real app this would be a proper DB
        self.recommendation_database = {
            "museums": [
                ActivityRecommendation(
                    activity_type="museum",
                    title="City History Museum",
                    description="Explore the rich cultural heritage of the city.",
                    location="Downtown",
                    estimated_duration=120,
                    price_range="medium",
                    rating=4.5
                )
            ],
            "restaurants": [
                ActivityRecommendation(
                    activity_type="restaurant",
                    title="Local Cuisine Experience",
                    description="Authentic dishes prepared by local chefs.",
                    location="Historic Quarter",
                    estimated_duration=90,
                    price_range="medium",
                    rating=4.7
                )
            ],
            "parks": [
                ActivityRecommendation(
                    activity_type="park",
                    title="Central Park",
                    description="Beautiful green space perfect for relaxation.",
                    location="City Center",
                    estimated_duration=180,
                    price_range="low",
                    rating=4.3
                )
            ],
            "shopping": [
                ActivityRecommendation(
                    activity_type="shopping",
                    title="Local Market",
                    description="Traditional market with local crafts and goods.",
                    location="Old Town",
                    estimated_duration=120,
                    price_range="low",
                    rating=4.6
                )
            ]
        }

    def generate_recommendations(self, context: RecommendationContext) -> List[ActivityRecommendation]:
        """
        Generate personalized activity recommendations based on user preferences and itinerary.
        
        Args:
            context: RecommendationContext containing user preferences, current itinerary,
                     destination info, and time frame
        
        Returns:
            List of recommended activities sorted by confidence score
        """
        # Get relevant recommendations based on interests
        recommendations = []
        
        # Match user interests with activity types
        for interest in context.user_preferences.interests:
            if interest in self.recommendation_database:
                recommendations.extend(self.recommendation_database[interest])
        
        # Filter by accessibility needs
        filtered_recommendations = []
        for rec in recommendations:
            if self._meets_accessibility_requirements(rec, context.user_preferences.accessibility_needs):
                filtered_recommendations.append(rec)
        
        # Apply confidence scoring based on preferences and existing activities
        scored_recommendations = []
        for rec in filtered_recommendations:
            confidence = self._calculate_confidence_score(rec, context)
            rec.confidence_score = confidence
            scored_recommendations.append(rec)
        
        # Sort by confidence score
        scored_recommendations.sort(key=lambda x: x.confidence_score, reverse=True)
        return scored_recommendations
    
    def _meets_accessibility_requirements(self, recommendation: ActivityRecommendation, accessibility_needs: List[str]) -> bool:
        """
        Check if a recommendation meets the user's accessibility needs.
        
        Args:
            recommendation: The activity to check
            accessibility_needs: User's accessibility requirements
        
        Returns:
            True if all requirements are met, False otherwise
        """
        # For simplicity, assume wheelchair access is required for this example
        if "wheelchair_access" in accessibility_needs:
            # In a real implementation, we'd check actual facility accessibility data
            return recommendation.location != "Downtown"  # Simplified test case
        return True
    
    def _calculate_confidence_score(self, recommendation: ActivityRecommendation, context: RecommendationContext) -> float:
        """
        Calculate confidence score for a recommendation based on various factors.
        
        Args:
            recommendation: The activity to score
            context: Current recommendation context
        
        Returns:
            Confidence score between 0.0 and 1.0
        """
        score = 0.0
        
        # Preference match (1 point)
        for interest in context.user_preferences.interests:
            if interest == recommendation.activity_type:
                score += 1.0
        
        # Budget compatibility (0.5 points)
        if self._budget_compatible(context.user_preferences.budget_range, recommendation.price_range):
            score += 0.5
        
        # Location relevance (0.5 points)
        if self._location_relevant(recommendation.location, context.destination_info.get("name", "")):
            score += 0.5
        
        # Time availability (0.5 points)
        if self._has_time_availability(context.current_itinerary, recommendation):
            score += 0.5
        
        # Rating factor (0.5 points)
        score += recommendation.rating / 10.0
        
        return min(score, 1.0)  # Cap at 1.0
    
    def _budget_compatible(self, user_budget: str, activity_price: str) -> bool:
        """
        Check if activity price is compatible with user's budget range.
        
        Args:
            user_budget: User's budget range (low/medium/high)
            activity_price: Activity's price range
        
        Returns:
            True if compatible, False otherwise
        """
        # Simplified logic - in practice this would be more nuanced
        if user_budget == "high":
            return activity_price in ["high", "medium", "low"]
        elif user_budget == "medium":
            return activity_price in ["medium", "low"]
        else:  # low
            return activity_price == "low"
    
    def _location_relevant(self, activity_location: str, destination_name: str) -> bool:
        """
        Check if activity location is relevant to current destination.
        
        Args:
            activity_location: Activity's location
            destination_name: Current destination name
        
        Returns:
            True if relevant, False otherwise
        """
        # Simplified - in real app would use geolocation or more detailed matching
        return activity_location.lower() in destination_name.lower() or destination_name.lower() in activity_location.lower()
    
    def _has_time_availability(self, itinerary: Dict[str, Any], recommendation: ActivityRecommendation) -> bool:
        """
        Check if there's time available in the current itinerary for this recommendation.
        
        Args:
            itinerary: Current itinerary data
            recommendation: Recommendation to check
        
        Returns:
            True if time is available, False otherwise
        """
        # Simplified - in real app would check against actual scheduled times
        return True  # For now assume availability

# Test function to demonstrate usage
if __name__ == "__main__":
    engine = RecommendationEngine()
    
    # Create a user preference profile
    preferences = UserPreferences(
        interests=["museums", "restaurants"],
        budget_range="medium",
        travel_style="leisure",
        accessibility_needs=[]
    )
    
    # Create sample itinerary context
    context = RecommendationContext(
        user_preferences=preferences,
        current_itinerary={"title": "Sample Trip", "activities": []},
        destination_info={"name": "City Center", "country": "USA"},
        time_frame={"start": datetime.now(), "end": datetime.now() + timedelta(days=3)}
    )
    
    # Generate recommendations
    recommendations = engine.generate_recommendations(context)
    print("Generated Recommendations:")
    for rec in recommendations:
        print(f"- {rec.title}: {rec.description} (Confidence: {rec.confidence_score:.2f})")