# Usage Guide for NetworkMapProject

## Running the Application
```bash
# Build the image (ensure you are in the project directory)
docker build -t networkmap:latest .

# Start the container (exposes port 5000 on the host)
# Using host networking simplifies subnet discovery
docker run -d --network host -p 5000:5000 networkmap:latest
```

The map UI is available at `http://localhost:5000`.

## Environment Variables (optional)
| Variable | Description | Default |
|---|---|---|
| `SCAN_SUBNET` | Subnet CIDR to scan (e.g., `192.168.1.0/24`). | Auto‑detect from host interface |
| `SCAN_TIMEOUT` | Ping timeout in seconds. | `1` |

## Development Workflow
1. **Modify code** under `app/`.
2. **Rebuild** the Docker image.
3. **Restart** the container.
4. Run tests with:
```bash
docker run --rm -v $(pwd):/app -w /app networkmap:latest sh -c "pip install -r requirements.txt && pytest"
```

## Testing Locally (without Docker)
```bash
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
pytest
```

---
*Keep this guide up‑to‑date as the project evolves.*