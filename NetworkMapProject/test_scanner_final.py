# Test file for network scanner
import pytest
from network_scanner import scan_port, resolve_host, scan_network

def test_scan_port():
    # Test with invalid port (should return None)
    result = scan_port('127.0.0.1', 99999)
    assert result is None

def test_resolve_host():
    # Test resolving localhost
    result = resolve_host('localhost')
    assert result == '127.0.0.1'

def test_scan_network():
    # Test scanning a small network range
    result = scan_network('127.0.0.1/30', [22, 80])
    assert isinstance(result, dict)
