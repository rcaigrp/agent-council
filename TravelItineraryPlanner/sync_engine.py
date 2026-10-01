#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Synchronization engine for travel itineraries across devices.
"""
import hashlib
from datetime import datetime
from typing import Dict, List, Optional
from itertools import groupby

# In-memory storage (in production would use database)
storage = {}

class SyncEngine:
    """Handles synchronization of itineraries between devices."""
    
    def __init__(self):
        self.devices = set()
        self.sync_history = []
        
    def register_device(self, device_id: str):
        """Register a new device for sync operations."""
        self.devices.add(device_id)
        
    def generate_sync_token(self, itinerary_id: str) -> str:
        """Generate a sync token based on itinerary data and timestamp."""
        # In practice, this would be more complex with cryptographic signing
        data = f"{itinerary_id}_{datetime.now().timestamp()}"
        return hashlib.md5(data.encode()).hexdigest()[:16]
        
    def get_itinerary(self, itinerary_id: str) -> Optional[Dict]:
        """Retrieve itinerary from storage."""
        return storage.get(itinerary_id)
        
    def save_itinerary(self, itinerary_id: str, data: Dict):
        """Save itinerary to storage."""
        storage[itinerary_id] = data
        
    def sync_itinerary(self, itinerary_id: str, device_id: str, local_data: Dict) -> Dict:
        """Synchronize an itinerary across devices."""
        # Get current remote version
        remote_data = self.get_itinerary(itinerary_id)
        
        if not remote_data:
            # First sync - save local version
            self.save_itinerary(itinerary_id, local_data)
            return local_data
            
        # Conflict resolution logic
        local_timestamp = datetime.fromisoformat(local_data['updated_at'])
        remote_timestamp = datetime.fromisoformat(remote_data['updated_at'])
        
        if local_timestamp > remote_timestamp:
            # Local is newer - update remote
            self.save_itinerary(itinerary_id, local_data)
            return local_data
        elif remote_timestamp > local_timestamp:
            # Remote is newer - return remote
            return remote_data
        else:
            # Same timestamp - no conflict
            return remote_data
        
    def get_conflicts(self, itinerary_id: str) -> List[Dict]:
        """Identify potential conflicts in itinerary data."""
        # Simple implementation for demo purposes
        # In production would check for conflicting activity times, etc.
        return []