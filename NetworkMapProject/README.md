# Network Scan Script

This script performs a comprehensive network scan, gathering information about devices and their connectivity.

## Key Parameters

*   `--host`: The IP address or hostname to scan.
*   `--port`: The port range to scan (e.g., 80, 443, 22).
*   `--timeout`: The timeout value in seconds.
*   `--output`: The output file to store the scan results.

## Usage Example

```bash
python network_scanner.py --host 192.168.1.0/24 --port 22 80 443 --timeout 1
```

To run tests:

```bash
python -m pytest test_scanner.py
```

## Features

- Comprehensive error handling for socket operations
- Detailed logging for debugging and progress tracking
- Input validation for ports and hosts
- Support for CIDR notation in host specification
- JSON output format for easy parsing

## Troubleshooting

If you see ResourceWarnings about unclosed sockets, ensure your Python version is 3.6+ and the code properly handles socket cleanup.

[Link to Network Scanner Library Documentation]