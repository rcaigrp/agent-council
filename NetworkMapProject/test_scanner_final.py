import pytest
from unittest.mock import patch, MagicMock
import socket

def test_resolve_host_success():
    with patch('socket.gethostbyname') as mock_gethostbyname:
        mock_gethostbyname.return_value = '192.168.1.100'
        from network_scanner import resolve_host
        assert resolve_host('example.com') == '192.168.1.100'

def test_resolve_host_failure():
    with patch('socket.gethostbyname') as mock_gethostbyname:
        mock_gethostbyname.side_effect = socket.gaierror("Name or service not known")
        from network_scanner import resolve_host
        with pytest.raises(socket.gaierror):
            resolve_host('invalid.domain')

def test_scan_port_success():
    with patch('socket.socket') as mock_socket:
        mock_sock = MagicMock()
        mock_socket.return_value = mock_sock
        mock_sock.connect_ex.return_value = 0  # Connection successful
        from network_scanner import scan_port
        assert scan_port('192.168.1.1', 80, 1) == True

def test_scan_port_timeout():
    with patch('socket.socket') as mock_socket:
        mock_sock = MagicMock()
        mock_socket.return_value = mock_sock
        mock_sock.connect_ex.return_value = 11  # Connection timeout (EINPROGRESS)
        from network_scanner import scan_port
        assert scan_port('192.168.1.1', 80, 1) == False

def test_scan_port_failure():
    with patch('socket.socket') as mock_socket:
        mock_sock = MagicMock()
        mock_socket.return_value = mock_sock
        mock_sock.connect_ex.return_value = 1  # Connection failed (EACCES)
        from network_scanner import scan_port
        assert scan_port('192.168.1.1', 80, 1) == False