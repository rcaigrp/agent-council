from app.utils.scan_network import scan_network

def test_scan_returns_devices():
    devices = scan_network()
    assert isinstance(devices, list)
    assert len(devices) > 0
    for d in devices:
        assert isinstance(d, dict)
        assert 'ip' in d and 'hostname' in d