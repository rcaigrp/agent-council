# Architecture Details

## Components
- **Flask Application** (`app/app.py`)
  - Serves API endpoints:
    - `GET /devices` – returns JSON list of discovered devices.
    - `GET /device/<ip>` – returns detailed info for a single device.
  - Serves static HTML/JS for the UI.

- **Network Scanner** (`app/utils/scan.py`)
  - Uses `ping3` to ping IPs in the target subnet.
  - Executes scans concurrently with `ThreadPoolExecutor` for speed.
  - Returns a list of live hosts with basic metadata (IP, latency).

- **Frontend** (`templates/index.html`, `static/js/map.js`)
  - Leaflet.js renders a map centered on the host network.
  - On load, fetches `/devices` and places markers.
  - Clicking a marker shows a popup with device details.

## Docker Image
- **Base Image**: `python:3.11-slim`
- **Dependencies** installed via `requirements.txt` (Flask, ping3, etc.)
- **Expose Port**: `5000`
- **Entry point**: `python -m app.app`

## Data Flow
1. Container starts, Flask app initializes.
2. Frontend loads and requests `/devices`.
3. Flask handler triggers `scan_network()` which runs the scanner.
4. Results are returned as JSON, UI updates map.

## Extensibility
- Add additional device info collectors (e.g., SNMP) by extending `app/utils/scan.py`.
- Swap Leaflet for another mapping library without changing backend API.
