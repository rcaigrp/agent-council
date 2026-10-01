import pytest
from sync_engine import SyncEngine

def test_sync_engine_initialization():
    engine = SyncEngine()
    assert hasattr(engine, 'devices')
    assert hasattr(engine, 'data_store')
    

def test_device_registration():
    engine = SyncEngine()
    engine.register_device('device_123')
    assert 'device_123' in engine.devices
    assert engine.devices['device_123']['last_sync'] == 0
    

def test_sync_with_conflict_resolution():
    engine = SyncEngine()
    engine.register_device('device_123')
    
    # Initial data
    initial_data = {
        'id': 'iti_001',
        'title': 'Trip to Paris',
        'last_modified': 1000
    }
    
    # Sync initial data
    result1 = engine.sync_itinerary('device_123', initial_data, 1000)
    assert result1['status'] == 'synced'
    
    # New data with conflict
    conflicting_data = {
        'id': 'iti_001',
        'title': 'Trip to Paris Updated',
        'last_modified': 1500
    }
    
    # Sync updated data
    result2 = engine.sync_itinerary('device_123', conflicting_data, 1500)
    assert result2['status'] == 'synced'
    assert result2['conflicts_resolved'] == 0  # No actual conflict in this test case
    

def test_unregistered_device_error():
    engine = SyncEngine()
    with pytest.raises(ValueError):
        engine.sync_itinerary('unregistered_device', {}, 1000)
        

def test_conflict_detection():
    engine = SyncEngine()
    engine.register_device('device_123')
    
    # Initial data
    initial_data = {
        'id': 'iti_001',
        'title': 'Trip to Paris',
        'last_modified': 1000
    }
    
    # Sync initial data
    engine.sync_itinerary('device_123', initial_data, 1000)
    
    # New data with older timestamp
    old_data = {
        'id': 'iti_001',
        'title': 'Trip to Paris Old',
        'last_modified': 500
    }
    
    conflicts = engine._detect_conflicts('device_123', old_data)
    assert len(conflicts) == 1