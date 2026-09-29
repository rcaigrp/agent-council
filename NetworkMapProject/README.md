# Network Scan Script

This script performs a comprehensive network scan, gathering information about devices and their connectivity.

## Key Parameters

*   `--host`: The IP address or hostname to scan.
*   `--port`: The port range to scan (e.g., 80, 443, 22).
*   `--timeout`: The timeout value in seconds.
*   `--output`: The output file to store the scan results.

## Usage Example

```bash
python network_scanner.py --host 192.168.1.0/24 --port 22,80,443 --timeout 1
```

## Troubleshooting

[Link to Network Scanner Library Documentation]