import pytest

# Import the scan module using string path for reliable monkeypatching

def test_scan_network(monkeypatch):
    calls = []
    def mock_is_host_up(ip):
        calls.append(str(ip))
        return str(ip).endswith('.1') or str(ip).endswith('.2')
    # Patch the function via its import path
    monkeypatch.setattr('app.utils.scan.is_host_up', mock_is_host_up)
    import importlib
    scan_mod = importlib.import_module('app.utils.scan')
    result = scan_mod.scan_network('192.168.0.0/30')  # hosts .1 and .2
    assert result == ['192.168.0.1', '192.168.0.2']
    assert calls == ['192.168.0.1', '192.168.0.2']