#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Test suite for sync engine module.
"""
import pytest
from datetime import datetime
from sync_engine import SyncEngine

def test_sync_engine_creation():
    engine = SyncEngine()
    assert len(engine.devices) == 0
    
    # Register device
    engine.register_device("device1")
    assert "device1" in engine.devices
    
    # Generate token
    token = engine.generate_sync_token("itinerary1")
    assert isinstance(token, str)
    assert len(token) == 16
    
    # Test sync with no previous data
    data = {
        'title': 'My Trip',
        'activities': [],
        'created_at': datetime.now().isoformat(),
        'updated_at': datetime.now().isoformat()
    }
    
    result = engine.sync_itinerary("itinerary1", "device1", data)
    assert result == data
    
    # Test sync with newer local version
    new_data = {
        'title': 'My Trip',
        'activities': [],
        'created_at': datetime.now().isoformat(),
        'updated_at': (datetime.now()).isoformat()
    }
    result = engine.sync_itinerary("itinerary1", "device2", new_data)
    assert result == new_data
    
    # Test sync with older local version
    old_data = {
        'title': 'My Trip',
        'activities': [],
        'created_at': datetime.now().isoformat(),
        'updated_at': (datetime.now()).isoformat()
    }
    result = engine.sync_itinerary("itinerary1", "device3", old_data)
    # Should return the newer version from storage
    assert result == new_data