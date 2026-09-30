import unittest.mock as mock
import socket
import pytest
import sys
import os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

# Import directly from the module to avoid import issues
import network_scanner

# Test that functions exist and can be imported properly
class TestNetworkScanner:
    def test_imports(self):
        # This just verifies we can import the module
        assert hasattr(network_scanner, 'scan_port')
        assert hasattr(network_scanner, 'resolve_host')
        assert hasattr(network_scanner, 'scan_host')

    def test_scan_port_success(self):
        with mock.patch('socket.socket') as mock_socket:
            mock_sock = mock.Mock()
            mock_socket.return_value = mock_sock
            mock_sock.connect_ex.return_value = 0  # Success
            result = network_scanner.scan_port('127.0.0.1', 80, 1)
            assert result is True

    def test_scan_port_failure(self):
        with mock.patch('socket.socket') as mock_socket:
            mock_sock = mock.Mock()
            mock_socket.return_value = mock_sock
            mock_sock.connect_ex.return_value = 1  # Failure
            result = network_scanner.scan_port('127.0.0.1', 80, 1)
            assert result is False

    def test_scan_port_timeout(self):
        with mock.patch('socket.socket') as mock_socket:
            mock_sock = mock.Mock()
            mock_socket.return_value = mock_sock
            mock_sock.connect_ex.side_effect = socket.timeout()
            result = network_scanner.scan_port('127.0.0.1', 80, 1)
            assert result is False

    def test_resolve_host_success(self):
        with mock.patch('socket.getaddrinfo') as mock_getaddrinfo:
            mock_getaddrinfo.return_value = [(socket.AF_INET, socket.SOCK_STREAM, 6, '', ('192.168.1.1', 0))]
            result = network_scanner.resolve_host('example.com')
            assert result == '192.168.1.1'

    def test_resolve_host_failure(self):
        with mock.patch('socket.getaddrinfo') as mock_getaddrinfo:
            mock_getaddrinfo.side_effect = socket.gaierror('DNS resolution failed')
            # Test that the function raises the exception
            try:
                network_scanner.resolve_host('invalid.host')
                assert False, "Expected socket.gaierror to be raised"
            except socket.gaierror:
                pass  # Expected

    def test_scan_host_success(self):
        with mock.patch('network_scanner.resolve_host') as mock_resolve:
            mock_resolve.return_value = '127.0.0.1'
            with mock.patch('network_scanner.scan_port') as mock_scan:
                mock_scan.return_value = True
                result = network_scanner.scan_host('example.com', [80], 1)
                assert result == {'example.com': {'127.0.0.1': [80]}}

    def test_scan_host_failure(self):
        with mock.patch('network_scanner.resolve_host') as mock_resolve:
            mock_resolve.return_value = '127.0.0.1'
            with mock.patch('network_scanner.scan_port') as mock_scan:
                mock_scan.return_value = False
                result = network_scanner.scan_host('example.com', [80], 1)
                assert result == {'example.com': {'127.0.0.1': []}}

    def test_scan_host_dns_error(self):
        with mock.patch('network_scanner.resolve_host') as mock_resolve:
            mock_resolve.side_effect = socket.gaierror('DNS resolution failed')
            result = network_scanner.scan_host('invalid.host', [80], 1)
            assert result == {'invalid.host': {}}

    def test_scan_host_timeout(self):
        with mock.patch('network_scanner.resolve_host') as mock_resolve:
            mock_resolve.return_value = '127.0.0.1'
            with mock.patch('network_scanner.scan_port') as mock_scan:
                mock_scan.side_effect = socket.timeout()
                result = network_scanner.scan_host('example.com', [80], 1)
                assert result == {'example.com': {'127.0.0.1': []}}