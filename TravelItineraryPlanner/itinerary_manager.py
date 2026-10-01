#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Core module for managing travel itineraries.
"""

import json
from datetime import datetime
from typing import Dict, List, Optional

class ItineraryManager:
    def __init__(self):
        self.itineraries = {}
        self.next_id = 1

    def create_itinerary(self, title: str, description: str, start_date: str, end_date: str) -> Dict:
        """
        Create a new itinerary.
        
        Args:
            title (str): The title of the itinerary
            description (str): Description of the trip
            start_date (str): Start date in YYYY-MM-DD format
            end_date (str): End date in YYYY-MM-DD format
        
        Returns:
            Dict: The created itinerary with ID
        """
        # Basic validation
        if not title or not description:
            raise ValueError("Title and description are required")
        
        try:
            datetime.strptime(start_date, "%Y-%m-%d")
            datetime.strptime(end_date, "%Y-%m-%d")
        except ValueError:
            raise ValueError("Date format must be YYYY-MM-DD")
        
        itinerary_id = self.next_id
        self.next_id += 1
        
        itinerary = {
            "id": itinerary_id,
            "title": title,
            "description": description,
            "start_date": start_date,
            "end_date": end_date,
            "created_at": datetime.now().isoformat(),
            "updated_at": datetime.now().isoformat(),
            "activities": [],
            "accommodations": []
        }
        
        self.itineraries[itinerary_id] = itinerary
        return itinerary
    
    def get_itinerary(self, itinerary_id: int) -> Optional[Dict]:
        """
        Retrieve an itinerary by ID.
        
        Args:
            itinerary_id (int): The ID of the itinerary to retrieve
        
        Returns:
            Optional[Dict]: The itinerary if found, None otherwise
        """
        return self.itineraries.get(itinerary_id)
    
    def update_itinerary(self, itinerary_id: int, **kwargs) -> Optional[Dict]:
        """
        Update an existing itinerary.
        
        Args:
            itinerary_id (int): The ID of the itinerary to update
            **kwargs: Fields to update
        
        Returns:
            Optional[Dict]: Updated itinerary if successful, None otherwise
        """
        if itinerary_id not in self.itineraries:
            return None
        
        itinerary = self.itineraries[itinerary_id]
        
        # Update fields that are provided
        for key, value in kwargs.items():
            if key in ["title", "description", "start_date", "end_date"]:
                itinerary[key] = value
        
        # Update timestamp
        itinerary["updated_at"] = datetime.now().isoformat()
        
        return itinerary
    
    def delete_itinerary(self, itinerary_id: int) -> bool:
        """
        Delete an itinerary by ID.
        
        Args:
            itinerary_id (int): The ID of the itinerary to delete
        
        Returns:
            bool: True if deletion was successful, False otherwise
        """
        if itinerary_id in self.itineraries:
            del self.itineraries[itinerary_id]
            return True
        return False
    
    def list_itineraries(self) -> List[Dict]:
        """
        Get a list of all itineraries.
        
        Returns:
            List[Dict]: List of all itineraries
        """
        return list(self.itineraries.values())