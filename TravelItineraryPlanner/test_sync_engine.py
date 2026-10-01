import pytest
from sync_engine import SyncEngine


def test_sync_engine_initialization():
    engine = SyncEngine()
    assert engine is not None
    

def test_data_sync():
    engine = SyncEngine()
    # Test basic sync functionality
    data = {'trip_id': '123', 'activities': []}
    engine.sync_data(data)
    assert len(engine.get_synced_data()) == 1
